from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class DepreciationSchedule(BaseDocument):
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Schedule Date")
    depreciation_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Depreciation Amount")
    accumulated_depreciation_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Accumulated Depreciation Amount")
    journal_entry = models.ForeignKey('erp_core.JournalEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Journal Entry')
    shift = models.ForeignKey('erp_core.AssetShiftFactor', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shift')

class DepreciationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepreciationSchedule
        fields = '__all__'

class DepreciationScheduleViewSet(viewsets.ModelViewSet):
    queryset = DepreciationSchedule.objects.all()
    serializer_class = DepreciationScheduleSerializer

class AssetMovement(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    purpose = models.CharField(max_length=255, choices=[('Issue', 'Issue'), ('Receipt', 'Receipt'), ('Transfer', 'Transfer'), ('Transfer and Issue', 'Transfer and Issue')], blank=True, null=True, verbose_name='Purpose')
    transaction_date = models.DateTimeField(blank=True, null=True, verbose_name="Transaction Date")
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Document Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Document Name")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    assets = models.JSONField(default=list, blank=True, null=True, verbose_name="Assets")

class AssetMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMovement
        fields = '__all__'

class AssetMovementViewSet(viewsets.ModelViewSet):
    queryset = AssetMovement.objects.all()
    serializer_class = AssetMovementSerializer

class AssetCapitalizationAssetItem(BaseDocument):
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    asset_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Asset Name")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    asset_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Asset Value")
    fixed_asset_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fixed Asset Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    current_asset_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Current Asset Value")

class AssetCapitalizationAssetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCapitalizationAssetItem
        fields = '__all__'

class AssetCapitalizationAssetItemViewSet(viewsets.ModelViewSet):
    queryset = AssetCapitalizationAssetItem.objects.all()
    serializer_class = AssetCapitalizationAssetItemSerializer

class AssetCapitalization(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    target_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Item Code')
    target_asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Asset')
    target_asset_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Asset Name")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    naming_series = models.CharField(max_length=255, choices=[('ACC-ASC-.YYYY.-', 'ACC-ASC-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    stock_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Stock Items")
    asset_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Assets")
    stock_items_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Consumed Stock Total Value")
    asset_items_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Consumed Asset Total Value")
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    service_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Services")
    service_items_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Service Expense Total Amount")
    total_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Value")
    target_incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Target Incoming Rate")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    target_fixed_asset_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Fixed Asset Account')

class AssetCapitalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCapitalization
        fields = '__all__'

class AssetCapitalizationViewSet(viewsets.ModelViewSet):
    queryset = AssetCapitalization.objects.all()
    serializer_class = AssetCapitalizationSerializer

class LinkedLocation(BaseDocument):
    location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Location')

class LinkedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedLocation
        fields = '__all__'

class LinkedLocationViewSet(viewsets.ModelViewSet):
    queryset = LinkedLocation.objects.all()
    serializer_class = LinkedLocationSerializer

class AssetCapitalizationStockItem(BaseDocument):
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    stock_qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    actual_qty = models.FloatField(default=0.0, verbose_name="Actual Qty in Warehouse")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    purchase_receipt_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Receipt Item")

class AssetCapitalizationStockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCapitalizationStockItem
        fields = '__all__'

class AssetCapitalizationStockItemViewSet(viewsets.ModelViewSet):
    queryset = AssetCapitalizationStockItem.objects.all()
    serializer_class = AssetCapitalizationStockItemSerializer

class Asset(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ACC-ASS-.YYYY.-', 'ACC-ASS-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    asset_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Asset Name")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    asset_category = models.ForeignKey('erp_core.AssetCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Category')
    asset_owner = models.CharField(max_length=255, choices=[('Company', 'Company'), ('Supplier', 'Supplier'), ('Customer', 'Customer')], blank=True, null=True, verbose_name='Asset Owner')
    asset_owner_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Owner Company')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Location')
    custodian = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Custodian')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Purchase Date")
    disposal_date = models.DateField(blank=True, null=True, verbose_name="Disposal Date")
    journal_entry_for_scrap = models.ForeignKey('erp_core.JournalEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Journal Entry for Scrap')
    available_for_use_date = models.DateField(blank=True, null=True, verbose_name="Available for Use Date")
    calculate_depreciation = models.BooleanField(default=False, verbose_name="Calculate Depreciation")
    opening_accumulated_depreciation = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Opening Accumulated Depreciation")
    finance_books = models.JSONField(default=list, blank=True, null=True, verbose_name="Finance Books")
    depreciation_method = models.CharField(max_length=255, choices=[('Straight Line', 'Straight Line'), ('Double Declining Balance', 'Double Declining Balance'), ('Written Down Value', 'Written Down Value'), ('Manual', 'Manual')], blank=True, null=True, verbose_name='Depreciation Method')
    value_after_depreciation = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Value After Depreciation")
    total_number_of_depreciations = models.IntegerField(default=0, verbose_name="Total Number of Depreciations")
    frequency_of_depreciation = models.IntegerField(default=0, verbose_name="Frequency of Depreciation (Months)")
    next_depreciation_date = models.DateField(blank=True, null=True, verbose_name="Next Depreciation Date")
    policy_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Policy number")
    insurer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Insurer")
    insured_value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Insured value")
    insurance_start_date = models.DateField(blank=True, null=True, verbose_name="Insurance Start Date")
    insurance_end_date = models.DateField(blank=True, null=True, verbose_name="Insurance End Date")
    comprehensive_insurance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Comprehensive Insurance")
    maintenance_required = models.BooleanField(default=False, verbose_name="Maintenance Required")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Cancelled', 'Cancelled'), ('Partially Depreciated', 'Partially Depreciated'), ('Fully Depreciated', 'Fully Depreciated'), ('Sold', 'Sold'), ('Scrapped', 'Scrapped'), ('In Maintenance', 'In Maintenance'), ('Out of Order', 'Out of Order'), ('Issue', 'Issue'), ('Receipt', 'Receipt'), ('Capitalized', 'Capitalized'), ('Work In Progress', 'Work In Progress')], blank=True, null=True, verbose_name='Status')
    booked_fixed_asset = models.BooleanField(default=False, verbose_name="Booked Fixed Asset")
    purchase_receipt = models.ForeignKey('erp_core.PurchaseReceipt', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Receipt')
    purchase_invoice = models.ForeignKey('erp_core.PurchaseInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Invoice')
    default_finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Finance Book')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    split_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Split From')
    asset_quantity = models.IntegerField(default=0, verbose_name="Asset Quantity")
    depr_entry_posting_status = models.CharField(max_length=255, choices=[('Successful', 'Successful'), ('Failed', 'Failed')], blank=True, null=True, verbose_name='Depreciation Entry Posting Status')
    is_fully_depreciated = models.BooleanField(default=False, verbose_name="Is Fully Depreciated")
    total_asset_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Asset Cost")
    additional_asset_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Asset Cost")
    purchase_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Purchase Amount")
    opening_number_of_booked_depreciations = models.IntegerField(default=0, verbose_name="Opening Number of Booked Depreciations")
    purchase_receipt_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Receipt Item")
    purchase_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Invoice Item")
    net_purchase_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Purchase Amount")
    asset_type = models.CharField(max_length=255, choices=[('Existing Asset', 'Existing Asset'), ('Composite Asset', 'Composite Asset'), ('Composite Component', 'Composite Component')], blank=True, null=True, verbose_name='Asset Type')
    item_name = models.TextField(blank=True, null=True, verbose_name="Item Name")

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetCategory(BaseDocument):
    asset_category_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Asset Category Name")
    finance_books = models.JSONField(default=list, blank=True, null=True, verbose_name="Finance Books")
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    enable_cwip_accounting = models.BooleanField(default=False, verbose_name="Enable Capital Work in Progress Accounting")
    non_depreciable_category = models.BooleanField(default=False, verbose_name="Non Depreciable Category")

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'

class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

class AssetMovementItem(BaseDocument):
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    asset_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Asset Name")
    source_location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Location')
    target_location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Location')
    from_employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Employee')
    to_employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To Employee')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class AssetMovementItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMovementItem
        fields = '__all__'

class AssetMovementItemViewSet(viewsets.ModelViewSet):
    queryset = AssetMovementItem.objects.all()
    serializer_class = AssetMovementItemSerializer

class AssetCategoryAccount(BaseDocument):
    company_name = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    fixed_asset_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fixed Asset Account')
    accumulated_depreciation_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accumulated Depreciation Account')
    depreciation_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Depreciation Expense Account')
    capital_work_in_progress_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Capital Work In Progress Account')

class AssetCategoryAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategoryAccount
        fields = '__all__'

class AssetCategoryAccountViewSet(viewsets.ModelViewSet):
    queryset = AssetCategoryAccount.objects.all()
    serializer_class = AssetCategoryAccountSerializer

class AssetMaintenance(BaseDocument):
    asset_name = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Name')
    asset_category = models.TextField(blank=True, null=True, verbose_name="Asset Category")
    item_code = models.TextField(blank=True, null=True, verbose_name="Item Code")
    item_name = models.TextField(blank=True, null=True, verbose_name="Item Name")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    maintenance_team = models.ForeignKey('erp_core.AssetMaintenanceTeam', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Maintenance Team')
    maintenance_manager = models.CharField(max_length=255, blank=True, null=True, verbose_name="Maintenance Manager")
    maintenance_manager_name = models.TextField(blank=True, null=True, verbose_name="Maintenance Manager Name")
    asset_maintenance_tasks = models.JSONField(default=list, blank=True, null=True, verbose_name="Maintenance Tasks")

class AssetMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaintenance
        fields = '__all__'

class AssetMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = AssetMaintenance.objects.all()
    serializer_class = AssetMaintenanceSerializer

class AssetRepair(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ACC-ASR-.YYYY.-', 'ACC-ASR-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    failure_date = models.DateTimeField(blank=True, null=True, verbose_name="Failure Date")
    completion_date = models.DateTimeField(blank=True, null=True, verbose_name="Completion Date")
    repair_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Repair Status')
    description = models.TextField(blank=True, null=True, verbose_name="Error Description")
    actions_performed = models.TextField(blank=True, null=True, verbose_name="Actions performed")
    downtime = models.CharField(max_length=255, blank=True, null=True, verbose_name="Downtime")
    repair_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Repair Cost")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    asset_name = models.TextField(blank=True, null=True, verbose_name="Asset Name")
    capitalize_repair_cost = models.BooleanField(default=False, verbose_name="Capitalize Repair Cost")
    stock_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Stock Items")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    total_repair_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Repair Cost")
    increase_in_asset_life = models.IntegerField(default=0, verbose_name="Increase In Asset Life(Months)")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="Repair Purchase Invoices")
    consumed_items_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Consumed Items Cost")

class AssetRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetRepair
        fields = '__all__'

class AssetRepairViewSet(viewsets.ModelViewSet):
    queryset = AssetRepair.objects.all()
    serializer_class = AssetRepairSerializer

class AssetDepreciationSchedule(BaseDocument):
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    naming_series = models.CharField(max_length=255, choices=[('ACC-ADS-.YYYY.-', 'ACC-ADS-.YYYY.-')], blank=True, null=True, verbose_name='Naming Series')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    depreciation_method = models.CharField(max_length=255, choices=[('Straight Line', 'Straight Line'), ('Double Declining Balance', 'Double Declining Balance'), ('Written Down Value', 'Written Down Value'), ('Manual', 'Manual')], blank=True, null=True, verbose_name='Depreciation Method')
    rate_of_depreciation = models.TextField(blank=True, null=True, verbose_name="Rate of Depreciation")
    total_number_of_depreciations = models.IntegerField(default=0, verbose_name="Total Number of Depreciations")
    depreciation_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Depreciation Schedule")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    frequency_of_depreciation = models.IntegerField(default=0, verbose_name="Frequency of Depreciation (Months)")
    expected_value_after_useful_life = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Expected Value After Useful Life")
    finance_book_id = models.IntegerField(default=0, verbose_name="Finance Book Id")
    opening_accumulated_depreciation = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Opening Accumulated Depreciation")
    opening_number_of_booked_depreciations = models.IntegerField(default=0, verbose_name="Opening Number of Booked Depreciations")
    daily_prorata_based = models.BooleanField(default=False, verbose_name="Depreciate based on daily pro-rata")
    shift_based = models.BooleanField(default=False, verbose_name="Depreciate based on shifts")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    value_after_depreciation = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Value After Depreciation")
    net_purchase_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Purchase Amount")

class AssetDepreciationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetDepreciationSchedule
        fields = '__all__'

class AssetDepreciationScheduleViewSet(viewsets.ModelViewSet):
    queryset = AssetDepreciationSchedule.objects.all()
    serializer_class = AssetDepreciationScheduleSerializer

class AssetFinanceBook(BaseDocument):
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    depreciation_method = models.CharField(max_length=255, choices=[('Straight Line', 'Straight Line'), ('Double Declining Balance', 'Double Declining Balance'), ('Written Down Value', 'Written Down Value'), ('Manual', 'Manual')], blank=True, null=True, verbose_name='Depreciation Method')
    total_number_of_depreciations = models.IntegerField(default=0, verbose_name="Total Number of Depreciations")
    frequency_of_depreciation = models.IntegerField(default=0, verbose_name="Frequency of Depreciation (Months)")
    depreciation_start_date = models.DateField(blank=True, null=True, verbose_name="Depreciation Posting Date")
    expected_value_after_useful_life = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Salvage Value")
    value_after_depreciation = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Value After Depreciation")
    rate_of_depreciation = models.TextField(blank=True, null=True, verbose_name="Rate of Depreciation (%)")
    salvage_value_percentage = models.TextField(blank=True, null=True, verbose_name="Salvage Value Percentage")
    daily_prorata_based = models.BooleanField(default=False, verbose_name="Depreciate based on daily pro-rata")
    shift_based = models.BooleanField(default=False, verbose_name="Depreciate based on shifts")
    total_number_of_booked_depreciations = models.IntegerField(default=0, verbose_name="Total Number of Booked Depreciations ")
    increase_in_asset_life = models.IntegerField(default=0, verbose_name="Increase In Asset Life (Months)")

class AssetFinanceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetFinanceBook
        fields = '__all__'

class AssetFinanceBookViewSet(viewsets.ModelViewSet):
    queryset = AssetFinanceBook.objects.all()
    serializer_class = AssetFinanceBookSerializer

class AssetShiftFactor(BaseDocument):
    shift_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shift Name")
    shift_factor = models.FloatField(default=0.0, verbose_name="Shift Factor")
    default = models.BooleanField(default=False, verbose_name="Default")

class AssetShiftFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetShiftFactor
        fields = '__all__'

class AssetShiftFactorViewSet(viewsets.ModelViewSet):
    queryset = AssetShiftFactor.objects.all()
    serializer_class = AssetShiftFactorSerializer

class Location(BaseDocument):
    location_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Location Name")
    parent_location = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Location')
    is_container = models.BooleanField(default=False, verbose_name="Is Container")
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    latitude = models.FloatField(default=0.0, verbose_name="Latitude")
    longitude = models.FloatField(default=0.0, verbose_name="Longitude")
    area = models.FloatField(default=0.0, verbose_name="Area")
    area_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Area UOM')
    location = models.TextField(blank=True, null=True, verbose_name="Location")
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="Old Parent")

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AssetMaintenanceTeam(BaseDocument):
    maintenance_team_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Maintenance Team Name")
    maintenance_manager = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Maintenance Manager')
    maintenance_manager_name = models.TextField(blank=True, null=True, verbose_name="Maintenance Manager Name")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    maintenance_team_members = models.JSONField(default=list, blank=True, null=True, verbose_name="Maintenance Team Members")

class AssetMaintenanceTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaintenanceTeam
        fields = '__all__'

class AssetMaintenanceTeamViewSet(viewsets.ModelViewSet):
    queryset = AssetMaintenanceTeam.objects.all()
    serializer_class = AssetMaintenanceTeamSerializer

class AssetMaintenanceLog(BaseDocument):
    asset_maintenance = models.ForeignKey('erp_core.AssetMaintenance', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Maintenance')
    naming_series = models.CharField(max_length=255, choices=[('ACC-AML-.YYYY.-', 'ACC-AML-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    asset_name = models.TextField(blank=True, null=True, verbose_name="Asset Name")
    item_code = models.TextField(blank=True, null=True, verbose_name="Item Code")
    item_name = models.TextField(blank=True, null=True, verbose_name="Item Name")
    task = models.ForeignKey('erp_core.AssetMaintenanceTask', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Task')
    maintenance_type = models.TextField(blank=True, null=True, verbose_name="Maintenance Type")
    periodicity = models.CharField(max_length=255, blank=True, null=True, verbose_name="Periodicity")
    assign_to_name = models.TextField(blank=True, null=True, verbose_name="Assign To")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    completion_date = models.DateField(blank=True, null=True, verbose_name="Completion Date")
    maintenance_status = models.CharField(max_length=255, choices=[('Planned', 'Planned'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue')], blank=True, null=True, verbose_name='Maintenance Status')
    has_certificate = models.BooleanField(default=False, verbose_name="Has Certificate ")
    certificate_attachement = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Certificate")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    actions_performed = models.TextField(blank=True, null=True, verbose_name="Actions performed")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    task_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Task Name")
    task_assignee_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Task Assignee Email")

class AssetMaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaintenanceLog
        fields = '__all__'

class AssetMaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = AssetMaintenanceLog.objects.all()
    serializer_class = AssetMaintenanceLogSerializer

class AssetCapitalizationServiceItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')

class AssetCapitalizationServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCapitalizationServiceItem
        fields = '__all__'

class AssetCapitalizationServiceItemViewSet(viewsets.ModelViewSet):
    queryset = AssetCapitalizationServiceItem.objects.all()
    serializer_class = AssetCapitalizationServiceItemSerializer

class AssetRepairConsumedItem(BaseDocument):
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    consumed_quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name="Consumed Quantity")
    total_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Value")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')

class AssetRepairConsumedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetRepairConsumedItem
        fields = '__all__'

class AssetRepairConsumedItemViewSet(viewsets.ModelViewSet):
    queryset = AssetRepairConsumedItem.objects.all()
    serializer_class = AssetRepairConsumedItemSerializer

class AssetShiftAllocation(BaseDocument):
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    depreciation_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Depreciation Schedule")
    naming_series = models.CharField(max_length=255, choices=[('ACC-ASA-.YYYY.-', 'ACC-ASA-.YYYY.-')], blank=True, null=True, verbose_name='Naming Series')

class AssetShiftAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetShiftAllocation
        fields = '__all__'

class AssetShiftAllocationViewSet(viewsets.ModelViewSet):
    queryset = AssetShiftAllocation.objects.all()
    serializer_class = AssetShiftAllocationSerializer

class MaintenanceTeamMember(BaseDocument):
    team_member = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Team Member')
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    maintenance_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Maintenance Role')

class MaintenanceTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceTeamMember
        fields = '__all__'

class MaintenanceTeamMemberViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTeamMember.objects.all()
    serializer_class = MaintenanceTeamMemberSerializer

class AssetMaintenanceTask(BaseDocument):
    maintenance_task = models.CharField(max_length=255, blank=True, null=True, verbose_name="Maintenance Task")
    maintenance_type = models.CharField(max_length=255, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Calibration', 'Calibration')], blank=True, null=True, verbose_name='Maintenance Type')
    maintenance_status = models.CharField(max_length=255, choices=[('Planned', 'Planned'), ('Overdue', 'Overdue'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Maintenance Status')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    periodicity = models.CharField(max_length=255, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-yearly', 'Half-yearly'), ('Yearly', 'Yearly'), ('2 Yearly', '2 Yearly'), ('3 Yearly', '3 Yearly')], blank=True, null=True, verbose_name='Periodicity')
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    certificate_required = models.BooleanField(default=False, verbose_name="Certificate Required")
    assign_to = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Assign To')
    assign_to_name = models.TextField(blank=True, null=True, verbose_name="Assign to Name")
    next_due_date = models.DateField(blank=True, null=True, verbose_name="Next Due Date")
    last_completion_date = models.DateField(blank=True, null=True, verbose_name="Last Completion Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class AssetMaintenanceTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaintenanceTask
        fields = '__all__'

class AssetMaintenanceTaskViewSet(viewsets.ModelViewSet):
    queryset = AssetMaintenanceTask.objects.all()
    serializer_class = AssetMaintenanceTaskSerializer

class AssetRepairPurchaseInvoice(BaseDocument):
    purchase_invoice = models.ForeignKey('erp_core.PurchaseInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Invoice')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    repair_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Repair Cost")

class AssetRepairPurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetRepairPurchaseInvoice
        fields = '__all__'

class AssetRepairPurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = AssetRepairPurchaseInvoice.objects.all()
    serializer_class = AssetRepairPurchaseInvoiceSerializer

class AssetActivity(BaseDocument):
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    subject = models.TextField(blank=True, null=True, verbose_name="Subject")
    date = models.DateTimeField(blank=True, null=True, verbose_name="Date")
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')

class AssetActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetActivity
        fields = '__all__'

class AssetActivityViewSet(viewsets.ModelViewSet):
    queryset = AssetActivity.objects.all()
    serializer_class = AssetActivitySerializer

class AssetValueAdjustment(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    asset_category = models.TextField(blank=True, null=True, verbose_name="Asset Category")
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    journal_entry = models.ForeignKey('erp_core.JournalEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Journal Entry')
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    current_asset_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Current Asset Value")
    new_asset_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="New Asset Value")
    difference_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference Amount")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    difference_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Difference Account')

class AssetValueAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetValueAdjustment
        fields = '__all__'

class AssetValueAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = AssetValueAdjustment.objects.all()
    serializer_class = AssetValueAdjustmentSerializer
