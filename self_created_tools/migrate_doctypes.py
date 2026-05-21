import json
import os
import sys

# Map of Doctype to App Label
doctype_app_map = {}

def build_doctype_map(erpnext_path):
    for module in os.listdir(erpnext_path):
        module_path = os.path.join(erpnext_path, module)
        if not os.path.isdir(module_path): continue
        doctype_dir = os.path.join(module_path, 'doctype')
        if os.path.exists(doctype_dir):
            for dt in os.listdir(doctype_dir):
                doctype_app_map[dt.replace(" ", "")] = module.lower()

def map_field_type(frappe_type):
    mapping = {
        "Data": "models.CharField(max_length=255, blank=True, null=True)",
        "Link": "models.ForeignKey('{target}', on_delete=models.SET_NULL, blank=True, null=True)",
        "Select": "models.CharField(max_length=255, choices={choices}, blank=True, null=True)",
        "Check": "models.BooleanField(default=False)",
        "Text": "models.TextField(blank=True, null=True)",
        "Text Editor": "models.TextField(blank=True, null=True)",
        "Date": "models.DateField(blank=True, null=True)",
        "Datetime": "models.DateTimeField(blank=True, null=True)",
        "Float": "models.FloatField(default=0.0)",
        "Int": "models.IntegerField(default=0)",
        "Currency": "models.DecimalField(max_digits=18, decimal_places=6, default=0.0)",
        "Long Text": "models.TextField(blank=True, null=True)",
        "Small Text": "models.TextField(blank=True, null=True)",
        "Attach": "models.FileField(upload_to='uploads/', blank=True, null=True)",
        "Attach Image": "models.ImageField(upload_to='uploads/', blank=True, null=True)",
        "Code": "models.TextField(blank=True, null=True)",
        "Table": "models.JSONField(default=list, blank=True, null=True)",
    }
    return mapping.get(frappe_type, "models.TextField(blank=True, null=True)")

def migrate_module(module_path, backend_root):
    module_name = os.path.basename(module_path).lower()
    app_path = os.path.join(backend_root, module_name)
    os.makedirs(os.path.join(app_path, 'migrations'), exist_ok=True)
    with open(os.path.join(app_path, '__init__.py'), 'w') as f: pass
    with open(os.path.join(app_path, 'migrations', '__init__.py'), 'w') as f: pass

    models_file = open(os.path.join(app_path, 'models.py'), 'w')
    models_file.write("from django.db import models\nfrom erp_core.models import BaseDocument\nfrom rest_framework import serializers, viewsets\n\n")

    doctype_dir = os.path.join(module_path, 'doctype')
    if not os.path.exists(doctype_dir):
        return

    for dt in os.listdir(doctype_dir):
        dt_path = os.path.join(doctype_dir, dt, dt + '.json')
        if os.path.exists(dt_path):
            try:
                with open(dt_path, 'r') as f:
                    data = json.load(f)

                dt_name = data['name'].replace(" ", "")
                models_file.write(f"class {dt_name}(BaseDocument):\n")

                fields = data.get('fields', [])
                for field in fields:
                    if field.get('fieldtype') in ['Section Break', 'Column Break', 'Tab Break', 'HTML', 'Button']:
                        continue

                    fieldname = field['fieldname']
                    frappe_type = field['fieldtype']
                    options = field.get('options', '')
                    label = field.get('label', fieldname)

                    if frappe_type == 'Link':
                        target_dt = options.replace(" ", "")
                        if target_dt == dt_name:
                            target = 'self'
                        else:
                            target_app = doctype_app_map.get(target_dt, 'erp_core')
                            target = f"{target_app}.{target_dt}"

                        models_file.write(f"    {fieldname} = models.ForeignKey('{target}', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='{label}')\n")
                    elif frappe_type == 'Select':
                        choices = options.split('\n') if options else []
                        choice_tuples = [(c.strip(), c.strip()) for c in choices if c.strip()]
                        models_file.write(f"    {fieldname} = models.CharField(max_length=255, choices={choice_tuples}, blank=True, null=True, verbose_name='{label}')\n")
                    else:
                        django_field = map_field_type(frappe_type)
                        models_file.write(f"    {fieldname} = {django_field.replace(')', f', verbose_name=\"{label}\")')}\n")

                models_file.write("\n")
                models_file.write(f"class {dt_name}Serializer(serializers.ModelSerializer):\n    class Meta:\n        model = {dt_name}\n        fields = '__all__'\n\n")
                models_file.write(f"class {dt_name}ViewSet(viewsets.ModelViewSet):\n    queryset = {dt_name}.objects.all()\n    serializer_class = {dt_name}Serializer\n\n")

            except Exception as e:
                print(f"Error migrating {dt}: {e}")

    models_file.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python migrate_doctypes.py <erpnext_root> <backend_root>")
    else:
        erpnext_root = sys.argv[1]
        backend_root = sys.argv[2]
        build_doctype_map(erpnext_root)
        for module in os.listdir(erpnext_root):
            module_path = os.path.join(erpnext_root, module)
            if os.path.isdir(module_path) and os.path.exists(os.path.join(module_path, 'doctype')):
                migrate_module(module_path, backend_root)
