import json
import os
import sys

# Improved mapping with more comprehensive Django field choices
def map_field_type(frappe_type):
    mapping = {
        "Data": "models.CharField(max_length=255, blank=True, null=True)",
        "Link": "models.ForeignKey('{options}', on_delete=models.SET_NULL, blank=True, null=True)",
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
    }
    return mapping.get(frappe_type, "models.TextField(blank=True, null=True)")

def migrate_doctype(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    doctype_name = data['name']
    fields = data.get('fields', [])

    model_code = f"class {doctype_name}(BaseDocument):\n"
    for field in fields:
        if field.get('fieldtype') in ['Section Break', 'Column Break', 'Tab Break', 'HTML', 'Button']:
            continue

        fieldname = field['fieldname']
        frappe_type = field['fieldtype']
        options = field.get('options', '')
        label = field.get('label', fieldname)

        if frappe_type == 'Link':
            # Handle self-references and known types
            target = options if options != doctype_name else 'self'
            model_code += f"    {fieldname} = models.ForeignKey('{target}', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='{label}')\n"
        elif frappe_type == 'Select':
            choices = options.split('\n') if options else []
            choice_tuples = [(c.strip(), c.strip()) for c in choices if c.strip()]
            model_code += f"    {fieldname} = models.CharField(max_length=255, choices={choice_tuples}, blank=True, null=True, verbose_name='{label}')\n"
        else:
            django_field = map_field_type(frappe_type)
            model_code += f"    {fieldname} = {django_field.replace(')', f', verbose_name=\"{label}\")')}\n"

    return model_code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python migrate_doctypes.py <path_to_doctype_json>")
    else:
        print(migrate_doctype(sys.argv[1]))
