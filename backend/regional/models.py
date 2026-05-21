from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class ImportSupplierInvoice(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')
    tax_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Account')
    zip_file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Zip File")
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name="Status")
    invoice_series = models.CharField(max_length=255, choices=[('ACC-PINV-.YYYY.-', 'ACC-PINV-.YYYY.-')], blank=True, null=True, verbose_name='Invoice Series')
    default_buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Buying Price List')

class ImportSupplierInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportSupplierInvoice
        fields = '__all__'

class ImportSupplierInvoiceViewSet(viewsets.ModelViewSet):
    queryset = ImportSupplierInvoice.objects.all()
    serializer_class = ImportSupplierInvoiceSerializer

class UAEVATSettings(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    uae_vat_accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="UAE VAT Accounts")

class UAEVATSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAEVATSettings
        fields = '__all__'

class UAEVATSettingsViewSet(viewsets.ModelViewSet):
    queryset = UAEVATSettings.objects.all()
    serializer_class = UAEVATSettingsSerializer

class SouthAfricaVATSettings(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    vat_accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="VAT Accounts")

class SouthAfricaVATSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SouthAfricaVATSettings
        fields = '__all__'

class SouthAfricaVATSettingsViewSet(viewsets.ModelViewSet):
    queryset = SouthAfricaVATSettings.objects.all()
    serializer_class = SouthAfricaVATSettingsSerializer

class LowerDeductionCertificate(BaseDocument):
    certificate_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Certificate No")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    pan_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="PAN No")
    valid_upto = models.DateField(blank=True, null=True, verbose_name="Valid Up To")
    rate = models.TextField(blank=True, null=True, verbose_name="Rate Of TDS As Per Certificate")
    certificate_limit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Certificate Limit")
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fiscal Year')
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class LowerDeductionCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowerDeductionCertificate
        fields = '__all__'

class LowerDeductionCertificateViewSet(viewsets.ModelViewSet):
    queryset = LowerDeductionCertificate.objects.all()
    serializer_class = LowerDeductionCertificateSerializer

class UAEVATAccount(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')

class UAEVATAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAEVATAccount
        fields = '__all__'

class UAEVATAccountViewSet(viewsets.ModelViewSet):
    queryset = UAEVATAccount.objects.all()
    serializer_class = UAEVATAccountSerializer
