from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class PackingSlip(BaseDocument):
    delivery_note = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Note')
    naming_series = models.CharField(max_length=255, choices=[('MAT-PAC-.YYYY.-', 'MAT-PAC-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    from_case_no = models.IntegerField(default=0, verbose_name="From Package No.")
    to_case_no = models.IntegerField(default=0, verbose_name="To Package No.")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    net_weight_pkg = models.FloatField(default=0.0, verbose_name="Net Weight")
    net_weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Net Weight UOM')
    gross_weight_pkg = models.FloatField(default=0.0, verbose_name="Gross Weight")
    gross_weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gross Weight UOM')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class PackingSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingSlip
        fields = '__all__'

class PackingSlipViewSet(viewsets.ModelViewSet):
    queryset = PackingSlip.objects.all()
    serializer_class = PackingSlipSerializer

class StockEntryType(BaseDocument):
    purpose = models.CharField(max_length=255, choices=[('Material Issue', 'Material Issue'), ('Material Receipt', 'Material Receipt'), ('Material Transfer', 'Material Transfer'), ('Material Transfer for Manufacture', 'Material Transfer for Manufacture'), ('Material Consumption for Manufacture', 'Material Consumption for Manufacture'), ('Manufacture', 'Manufacture'), ('Repack', 'Repack'), ('Send to Subcontractor', 'Send to Subcontractor'), ('Disassemble', 'Disassemble'), ('Receive from Customer', 'Receive from Customer'), ('Return Raw Material to Customer', 'Return Raw Material to Customer'), ('Subcontracting Delivery', 'Subcontracting Delivery'), ('Subcontracting Return', 'Subcontracting Return')], blank=True, null=True, verbose_name='Purpose')
    add_to_transit = models.BooleanField(default=False, verbose_name="Add to Transit")
    is_standard = models.BooleanField(default=False, verbose_name="Is Standard")

class StockEntryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntryType
        fields = '__all__'

class StockEntryTypeViewSet(viewsets.ModelViewSet):
    queryset = StockEntryType.objects.all()
    serializer_class = StockEntryTypeSerializer

class PickListItem(BaseDocument):
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    picked_qty = models.FloatField(default=0.0, verbose_name="Picked Qty (in Stock UOM)")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty (in Stock UOM)")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    item_group = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Group")
    product_bundle_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Product Bundle Item")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    stock_reserved_qty = models.FloatField(default=0.0, verbose_name="Stock Reserved Qty (in Stock UOM)")
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty (in Stock UOM)")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty (Warehouse)")
    company_total_stock = models.FloatField(default=0.0, verbose_name="Qty (Company)")

class PickListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickListItem
        fields = '__all__'

class PickListItemViewSet(viewsets.ModelViewSet):
    queryset = PickListItem.objects.all()
    serializer_class = PickListItemSerializer

class DeliveryTrip(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-DT-.YYYY.-', 'MAT-DT-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    email_notification_sent = models.BooleanField(default=False, verbose_name="Initial Email Notification Sent")
    driver = models.ForeignKey('erp_core.Driver', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Driver')
    driver_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Driver Name")
    total_distance = models.FloatField(default=0.0, verbose_name="Total Estimated Distance")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Distance UOM')
    vehicle = models.ForeignKey('erp_core.Vehicle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Vehicle')
    departure_time = models.DateTimeField(blank=True, null=True, verbose_name="Departure Time")
    delivery_stops = models.JSONField(default=list, blank=True, null=True, verbose_name="Delivery Stop")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Scheduled', 'Scheduled'), ('In Transit', 'In Transit'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    driver_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Driver Address')
    driver_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Driver Email")
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')

class DeliveryTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTrip
        fields = '__all__'

class DeliveryTripViewSet(viewsets.ModelViewSet):
    queryset = DeliveryTrip.objects.all()
    serializer_class = DeliveryTripSerializer

class ItemVariantSettings(BaseDocument):
    do_not_update_variants = models.BooleanField(default=False, verbose_name="Do not update variants on save")
    allow_rename_attribute_value = models.BooleanField(default=False, verbose_name="Allow Rename Attribute Value")
    fields = models.JSONField(default=list, blank=True, null=True, verbose_name="Fields")
    allow_different_uom = models.BooleanField(default=False, verbose_name="Allow Variant UOM to be different from Template UOM")

class ItemVariantSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariantSettings
        fields = '__all__'

class ItemVariantSettingsViewSet(viewsets.ModelViewSet):
    queryset = ItemVariantSettings.objects.all()
    serializer_class = ItemVariantSettingsSerializer

class UOMCategory(BaseDocument):
    category_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Category Name")

class UOMCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMCategory
        fields = '__all__'

class UOMCategoryViewSet(viewsets.ModelViewSet):
    queryset = UOMCategory.objects.all()
    serializer_class = UOMCategorySerializer

class ShipmentDeliveryNote(BaseDocument):
    delivery_note = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Note')
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Value")

class ShipmentDeliveryNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentDeliveryNote
        fields = '__all__'

class ShipmentDeliveryNoteViewSet(viewsets.ModelViewSet):
    queryset = ShipmentDeliveryNote.objects.all()
    serializer_class = ShipmentDeliveryNoteSerializer

class ItemSupplier(BaseDocument):
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Part Number")

class ItemSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSupplier
        fields = '__all__'

class ItemSupplierViewSet(viewsets.ModelViewSet):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer

class ItemDefault(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    default_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Warehouse')
    default_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Price List')
    buying_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Buying Cost Center')
    default_supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Supplier')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Expense Account')
    selling_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Selling Cost Center')
    income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Income Account')
    default_discount_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Discount Account')
    default_provisional_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Provisional Account (Service)')
    deferred_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Deferred Expense Account')
    deferred_revenue_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Deferred Revenue Account')
    default_cogs_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default COGS Account')
    purchase_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Expense Account')
    purchase_expense_contra_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Expense Contra Account')
    default_inventory_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Inventory Account')
    inventory_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inventory Account Currency')

class ItemDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDefault
        fields = '__all__'

class ItemDefaultViewSet(viewsets.ModelViewSet):
    queryset = ItemDefault.objects.all()
    serializer_class = ItemDefaultSerializer

class DeliveryStop(BaseDocument):
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Address Name')
    locked = models.BooleanField(default=False, verbose_name="Locked")
    customer_address = models.TextField(blank=True, null=True, verbose_name="Customer Address")
    visited = models.BooleanField(default=False, verbose_name="Visited")
    delivery_note = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Note')
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    contact = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Name')
    email_sent_to = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email sent to")
    customer_contact = models.TextField(blank=True, null=True, verbose_name="Customer Contact")
    distance = models.FloatField(default=0.0, verbose_name="Distance")
    estimated_arrival = models.DateTimeField(blank=True, null=True, verbose_name="Estimated Arrival")
    lat = models.FloatField(default=0.0, verbose_name="Latitude")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    lng = models.FloatField(default=0.0, verbose_name="Longitude")
    details = models.TextField(blank=True, null=True, verbose_name="Details")

class DeliveryStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStop
        fields = '__all__'

class DeliveryStopViewSet(viewsets.ModelViewSet):
    queryset = DeliveryStop.objects.all()
    serializer_class = DeliveryStopSerializer

class VariantField(BaseDocument):
    field_name = models.TextField(blank=True, null=True, verbose_name="Field Name")

class VariantFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantField
        fields = '__all__'

class VariantFieldViewSet(viewsets.ModelViewSet):
    queryset = VariantField.objects.all()
    serializer_class = VariantFieldSerializer

class StockClosingBalance(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    posting_datetime = models.DateTimeField(blank=True, null=True, verbose_name="Posting Datetime")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty Change")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    stock_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Balance Stock Value")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    stock_value_difference = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Change in Stock Value")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    stock_closing_entry = models.ForeignKey('erp_core.StockClosingEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Closing Entry')
    inventory_dimension_key = models.TextField(blank=True, null=True, verbose_name="Inventory Dimension key")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    fifo_queue = models.TextField(blank=True, null=True, verbose_name="FIFO Queue")

class StockClosingBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockClosingBalance
        fields = '__all__'

class StockClosingBalanceViewSet(viewsets.ModelViewSet):
    queryset = StockClosingBalance.objects.all()
    serializer_class = StockClosingBalanceSerializer

class PriceList(BaseDocument):
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    price_list_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Price List Name")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    buying = models.BooleanField(default=False, verbose_name="Buying")
    selling = models.BooleanField(default=False, verbose_name="Selling")
    price_not_uom_dependent = models.BooleanField(default=False, verbose_name="Price Not UOM Dependent")
    countries = models.JSONField(default=list, blank=True, null=True, verbose_name="Applicable for Countries")

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'

class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

class PurchaseReceiptItem(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    supplier_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Part Number")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Quantity")
    qty = models.FloatField(default=0.0, verbose_name="Accepted Quantity")
    rejected_qty = models.FloatField(default=0.0, verbose_name="Rejected Quantity")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    retain_sample = models.BooleanField(default=False, verbose_name="Retain Sample")
    sample_quantity = models.IntegerField(default=0, verbose_name="Sample Quantity")
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    discount_percentage = models.TextField(blank=True, null=True, verbose_name="Discount on Price List Rate (%)")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    base_price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate (Company Currency)")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accepted Warehouse')
    rejected_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Warehouse')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    stock_qty = models.FloatField(default=0.0, verbose_name="Accepted Qty in Stock UOM")
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    billed_amt = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billed Amt")
    landed_cost_voucher_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Landed Cost Voucher Amount")
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    rm_supp_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Materials Supplied Cost")
    item_tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Item Tax Amount Included in Value")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    asset_location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Location')
    asset_category = models.ForeignKey('erp_core.AssetCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Category')
    from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Warehouse')
    purchase_receipt_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Receipt Item")
    putaway_rule = models.ForeignKey('erp_core.PutawayRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Putaway Rule')
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty in Stock UOM")
    received_stock_qty = models.FloatField(default=0.0, verbose_name="Received Qty in Stock UOM")
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    delivery_note_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delivery Note Item")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")
    base_rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin (Company Currency)")
    purchase_invoice = models.ForeignKey('erp_core.PurchaseInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Invoice')
    purchase_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Invoice Item")
    product_bundle = models.ForeignKey('erp_core.ProductBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Product Bundle')
    provisional_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Provisional Expense Account')
    has_item_scanned = models.BooleanField(default=False, verbose_name="Has Item Scanned")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    rejected_serial_no = models.TextField(blank=True, null=True, verbose_name="Rejected Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    rejected_serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Serial and Batch Bundle')
    wip_composite_asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP Composite Asset')
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    subcontracting_receipt_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subcontracting Receipt Item")
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    return_qty_from_rejected_warehouse = models.BooleanField(default=False, verbose_name="Return Qty from Rejected Warehouse")
    sales_incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Sales Incoming Rate")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    amount_difference_with_purchase_invoice = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount Difference with Purchase Invoice")

class PurchaseReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseReceiptItem
        fields = '__all__'

class PurchaseReceiptItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseReceiptItem.objects.all()
    serializer_class = PurchaseReceiptItemSerializer

class PackingSlipItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    net_weight = models.FloatField(default=0.0, verbose_name="Net Weight")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    dn_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delivery Note Item")
    pi_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delivery Note Packed Item")

class PackingSlipItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingSlipItem
        fields = '__all__'

class PackingSlipItemViewSet(viewsets.ModelViewSet):
    queryset = PackingSlipItem.objects.all()
    serializer_class = PackingSlipItemSerializer

class ItemCustomerDetail(BaseDocument):
    customer_name = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Name')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    ref_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ref Code")

class ItemCustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCustomerDetail
        fields = '__all__'

class ItemCustomerDetailViewSet(viewsets.ModelViewSet):
    queryset = ItemCustomerDetail.objects.all()
    serializer_class = ItemCustomerDetailSerializer

class ShipmentParcel(BaseDocument):
    length = models.FloatField(default=0.0, verbose_name="Length (cm)")
    width = models.FloatField(default=0.0, verbose_name="Width (cm)")
    height = models.FloatField(default=0.0, verbose_name="Height (cm)")
    weight = models.FloatField(default=0.0, verbose_name="Weight (kg)")
    count = models.IntegerField(default=0, verbose_name="Count")

class ShipmentParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentParcel
        fields = '__all__'

class ShipmentParcelViewSet(viewsets.ModelViewSet):
    queryset = ShipmentParcel.objects.all()
    serializer_class = ShipmentParcelSerializer

class SerialandBatchEntry(BaseDocument):
    serial_no = models.ForeignKey('erp_core.SerialNo', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial No')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    incoming_rate = models.FloatField(default=0.0, verbose_name="Valuation Rate")
    outgoing_rate = models.FloatField(default=0.0, verbose_name="Outgoing Rate")
    stock_value_difference = models.FloatField(default=0.0, verbose_name="Change in Stock Value")
    is_outward = models.BooleanField(default=False, verbose_name="Is Outward")
    stock_queue = models.TextField(blank=True, null=True, verbose_name="FIFO Stock Queue (qty, rate)")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    reference_for_reservation = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference for Reservation")
    posting_datetime = models.DateTimeField(blank=True, null=True, verbose_name="Posting Datetime")
    voucher_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Type")
    voucher_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher No")
    voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail No")
    type_of_transaction = models.CharField(max_length=255, blank=True, null=True, verbose_name="Type of Transaction")
    is_cancelled = models.BooleanField(default=False, verbose_name="Is Cancelled")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')

class SerialandBatchEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialandBatchEntry
        fields = '__all__'

class SerialandBatchEntryViewSet(viewsets.ModelViewSet):
    queryset = SerialandBatchEntry.objects.all()
    serializer_class = SerialandBatchEntrySerializer

class PickList(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    parent_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    work_order = models.ForeignKey('erp_core.WorkOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Work Order')
    locations = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Locations")
    for_qty = models.FloatField(default=0.0, verbose_name="Qty of Finished Goods Item")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    purpose = models.CharField(max_length=255, choices=[('Material Transfer for Manufacture', 'Material Transfer for Manufacture'), ('Material Transfer', 'Material Transfer'), ('Delivery', 'Delivery')], blank=True, null=True, verbose_name='Purpose')
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    naming_series = models.CharField(max_length=255, choices=[('STO-PICK-.YYYY.-', 'STO-PICK-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    group_same_items = models.BooleanField(default=False, verbose_name="Group Same Items")
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    scan_mode = models.BooleanField(default=False, verbose_name="Scan Mode")
    prompt_qty = models.BooleanField(default=False, verbose_name="Prompt Qty")
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Partly Delivered', 'Partly Delivered'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    consider_rejected_warehouses = models.BooleanField(default=False, verbose_name="Consider Rejected Warehouses")
    pick_manually = models.BooleanField(default=False, verbose_name="Pick Manually")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    delivery_status = models.CharField(max_length=255, choices=[('Not Delivered', 'Not Delivered'), ('Fully Delivered', 'Fully Delivered'), ('Partly Delivered', 'Partly Delivered')], blank=True, null=True, verbose_name='Delivery Status')
    per_delivered = models.TextField(blank=True, null=True, verbose_name="% Delivered")

class PickListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickList
        fields = '__all__'

class PickListViewSet(viewsets.ModelViewSet):
    queryset = PickList.objects.all()
    serializer_class = PickListSerializer

class LandedCostVoucher(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-LCV-.YYYY.-', 'MAT-LCV-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    purchase_receipts = models.JSONField(default=list, blank=True, null=True, verbose_name="Vouchers")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Receipt Items")
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Landed Cost")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Landed Cost (Company Currency)")
    distribute_charges_based_on = models.CharField(max_length=255, choices=[('Qty', 'Qty'), ('Amount', 'Amount'), ('Distribute Manually', 'Distribute Manually')], blank=True, null=True, verbose_name='Distribute Charges Based On')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    vendor_invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="Vendor Invoices")
    total_vendor_invoices_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Vendor Invoices Cost (Company Currency)")

class LandedCostVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandedCostVoucher
        fields = '__all__'

class LandedCostVoucherViewSet(viewsets.ModelViewSet):
    queryset = LandedCostVoucher.objects.all()
    serializer_class = LandedCostVoucherSerializer

class UOMConversionDetail(BaseDocument):
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")

class UOMConversionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMConversionDetail
        fields = '__all__'

class UOMConversionDetailViewSet(viewsets.ModelViewSet):
    queryset = UOMConversionDetail.objects.all()
    serializer_class = UOMConversionDetailSerializer

class Manufacturer(BaseDocument):
    short_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Short Name")
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')
    logo = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Logo")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class StockSettings(BaseDocument):
    item_naming_by = models.CharField(max_length=255, choices=[('Item Code', 'Item Code'), ('Naming Series', 'Naming Series')], blank=True, null=True, verbose_name='Item Naming By')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Item Group')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Stock UOM')
    default_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Warehouse')
    sample_retention_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sample Retention Warehouse')
    valuation_method = models.CharField(max_length=255, choices=[('FIFO', 'FIFO'), ('Moving Average', 'Moving Average'), ('LIFO', 'LIFO')], blank=True, null=True, verbose_name='Default Valuation Method')
    over_delivery_receipt_allowance = models.FloatField(default=0.0, verbose_name="Over Delivery/Receipt Allowance (%)")
    action_if_quality_inspection_is_not_submitted = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn')], blank=True, null=True, verbose_name='Action If Quality Inspection Is Not Submitted')
    show_barcode_field = models.BooleanField(default=False, verbose_name="Show Barcode Field in Stock Transactions")
    clean_description_html = models.BooleanField(default=False, verbose_name="Convert Item Description to Clean HTML in Transactions")
    auto_insert_price_list_rate_if_missing = models.BooleanField(default=False, verbose_name="Auto Insert Item Price If Missing")
    allow_negative_stock = models.BooleanField(default=False, verbose_name="Allow Negative Stock")
    auto_indent = models.BooleanField(default=False, verbose_name="Raise Material Request When Stock Reaches Re-order Level")
    reorder_email_notify = models.BooleanField(default=False, verbose_name="Notify by Email on Creation of Automatic Material Request")
    stock_frozen_upto = models.DateField(blank=True, null=True, verbose_name="Stock Frozen Up To")
    stock_frozen_upto_days = models.IntegerField(default=0, verbose_name="Freeze Stocks Older Than (Days)")
    stock_auth_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role Allowed to Edit Frozen Stock')
    use_naming_series = models.BooleanField(default=False, verbose_name="Have Default Naming Series for Batch ID?")
    naming_series_prefix = models.CharField(max_length=255, blank=True, null=True, verbose_name="Naming Series Prefix")
    role_allowed_to_create_edit_back_dated_transactions = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role Allowed to Create/Edit Back-dated Transactions')
    disable_serial_no_and_batch_selector = models.BooleanField(default=False, verbose_name="Disable Serial No And Batch Selector")
    role_allowed_to_over_deliver_receive = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role Allowed to Over Deliver/Receive')
    action_if_quality_inspection_is_rejected = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn')], blank=True, null=True, verbose_name='Action If Quality Inspection Is Rejected')
    mr_qty_allowance = models.FloatField(default=0.0, verbose_name="Over Transfer Allowance")
    update_existing_price_list_rate = models.BooleanField(default=False, verbose_name="Update Existing Price List Rate")
    enable_stock_reservation = models.BooleanField(default=False, verbose_name="Enable Stock Reservation")
    allow_partial_reservation = models.BooleanField(default=False, verbose_name="Allow Partial Reservation")
    pick_serial_and_batch_based_on = models.CharField(max_length=255, choices=[('FIFO', 'FIFO'), ('LIFO', 'LIFO'), ('Expiry', 'Expiry')], blank=True, null=True, verbose_name='Pick Serial / Batch Based On')
    auto_create_serial_and_batch_bundle_for_outward = models.BooleanField(default=False, verbose_name="Auto Create Serial and Batch Bundle For Outward")
    auto_reserve_serial_and_batch = models.BooleanField(default=False, verbose_name="Auto Reserve Serial and Batch Nos")
    allow_to_edit_stock_uom_qty_for_sales = models.BooleanField(default=False, verbose_name="Allow to Edit Stock UOM Qty for Sales Documents")
    allow_to_edit_stock_uom_qty_for_purchase = models.BooleanField(default=False, verbose_name="Allow to Edit Stock UOM Qty for Purchase Documents")
    auto_reserve_stock_for_sales_order_on_purchase = models.BooleanField(default=False, verbose_name="Auto Reserve Stock for Sales Order on Purchase")
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial / Batch Fields")
    do_not_update_serial_batch_on_creation_of_auto_bundle = models.BooleanField(default=False, verbose_name="Do Not Update Serial / Batch on Creation of Auto Bundle")
    allow_internal_transfer_at_arms_length_price = models.BooleanField(default=False, verbose_name="Allow Internal Transfers at Arm's Length Price")
    do_not_use_batchwise_valuation = models.BooleanField(default=False, verbose_name="Do Not Use Batch-wise Valuation")
    over_picking_allowance = models.TextField(blank=True, null=True, verbose_name="Over Picking Allowance")
    allow_existing_serial_no = models.BooleanField(default=False, verbose_name="Allow existing Serial No to be Manufactured/Received again")
    auto_reserve_stock = models.BooleanField(default=False, verbose_name="Auto Reserve Stock")
    set_serial_and_batch_bundle_naming_based_on_naming_series = models.BooleanField(default=False, verbose_name="Set Serial and Batch Bundle Naming Based on Naming Series")
    allow_uom_with_conversion_rate_defined_in_item = models.BooleanField(default=False, verbose_name="Allow UOM with Conversion Rate Defined in Item")
    allow_to_make_quality_inspection_after_purchase_or_delivery = models.BooleanField(default=False, verbose_name="Allow to Make Quality Inspection after Purchase / Delivery")
    update_price_list_based_on = models.CharField(max_length=255, choices=[('Rate', 'Rate'), ('Price List Rate', 'Price List Rate')], blank=True, null=True, verbose_name='Update Price List Based On')
    validate_material_transfer_warehouses = models.BooleanField(default=False, verbose_name="Validate Material Transfer Warehouses")
    allow_negative_stock_for_batch = models.BooleanField(default=False, verbose_name="Allow Negative Stock for Batch")
    enable_serial_and_batch_no_for_item = models.BooleanField(default=False, verbose_name="Activate Serial / Batch No for Item")

class StockSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSettings
        fields = '__all__'

class StockSettingsViewSet(viewsets.ModelViewSet):
    queryset = StockSettings.objects.all()
    serializer_class = StockSettingsSerializer

class ItemVariant(BaseDocument):
    item_attribute = models.ForeignKey('erp_core.ItemAttribute', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Attribute')
    item_attribute_value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Attribute Value")

class ItemVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariant
        fields = '__all__'

class ItemVariantViewSet(viewsets.ModelViewSet):
    queryset = ItemVariant.objects.all()
    serializer_class = ItemVariantSerializer

class ItemBarcode(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    barcode_type = models.CharField(max_length=255, choices=[('EAN', 'EAN'), ('UPC-A', 'UPC-A'), ('CODE-39', 'CODE-39'), ('EAN-13', 'EAN-13'), ('EAN-8', 'EAN-8'), ('GS1', 'GS1'), ('GTIN', 'GTIN'), ('GTIN-14', 'GTIN-14'), ('ISBN', 'ISBN'), ('ISBN-10', 'ISBN-10'), ('ISBN-13', 'ISBN-13'), ('ISSN', 'ISSN'), ('JAN', 'JAN'), ('PZN', 'PZN'), ('UPC', 'UPC')], blank=True, null=True, verbose_name='Barcode Type')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class ItemBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBarcode
        fields = '__all__'

class ItemBarcodeViewSet(viewsets.ModelViewSet):
    queryset = ItemBarcode.objects.all()
    serializer_class = ItemBarcodeSerializer

class Warehouse(BaseDocument):
    warehouse_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Warehouse Name")
    is_group = models.BooleanField(default=False, verbose_name="Is Group Warehouse")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    email_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email Address")
    phone_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone No")
    mobile_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    address_line_1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address Line 1")
    address_line_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address Line 2")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="City")
    state = models.CharField(max_length=255, blank=True, null=True, verbose_name="State/Province")
    pin = models.CharField(max_length=255, blank=True, null=True, verbose_name="PIN")
    parent_warehouse = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Warehouse')
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Old Parent')
    warehouse_type = models.ForeignKey('erp_core.WarehouseType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse Type')
    default_in_transit_warehouse = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default In-Transit Warehouse')
    is_rejected_warehouse = models.BooleanField(default=False, verbose_name="Is Rejected Warehouse")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class QualityInspectionParameterGroup(BaseDocument):
    group_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parameter Group Name")

class QualityInspectionParameterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspectionParameterGroup
        fields = '__all__'

class QualityInspectionParameterGroupViewSet(viewsets.ModelViewSet):
    queryset = QualityInspectionParameterGroup.objects.all()
    serializer_class = QualityInspectionParameterGroupSerializer

class ItemAlternative(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    alternative_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Alternative Item Code')
    two_way = models.BooleanField(default=False, verbose_name="Two-way")
    item_name = models.TextField(blank=True, null=True, verbose_name="Item Name")
    alternative_item_name = models.TextField(blank=True, null=True, verbose_name="Alternative Item Name")

class ItemAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAlternative
        fields = '__all__'

class ItemAlternativeViewSet(viewsets.ModelViewSet):
    queryset = ItemAlternative.objects.all()
    serializer_class = ItemAlternativeSerializer

class MaterialRequestItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    stock_qty = models.FloatField(default=0.0, verbose_name="Stock Qty")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    lead_time_date = models.DateField(blank=True, null=True, verbose_name="Lead Time Date")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    production_plan = models.ForeignKey('erp_core.ProductionPlan', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Production Plan')
    material_request_plan_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Plan Item")
    min_order_qty = models.FloatField(default=0.0, verbose_name="Min Order Qty")
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    actual_qty = models.FloatField(default=0.0, verbose_name="Actual Qty")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Completed Qty")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    job_card_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Card Item")
    wip_composite_asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP Composite Asset')
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    reorder_level = models.FloatField(default=0.0, verbose_name="Reorder Level")
    reorder_qty = models.FloatField(default=0.0, verbose_name="Reorder Qty")
    projected_on_hand = models.FloatField(default=0.0, verbose_name="Projected On Hand")
    picked_qty = models.FloatField(default=0.0, verbose_name="Picked Qty")
    packed_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Packed Item")

class MaterialRequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequestItem
        fields = '__all__'

class MaterialRequestItemViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequestItem.objects.all()
    serializer_class = MaterialRequestItemSerializer

class StockClosingEntry(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('CBAL-.#####', 'CBAL-.#####')], blank=True, null=True, verbose_name='Naming Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Queued', 'Queued'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class StockClosingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockClosingEntry
        fields = '__all__'

class StockClosingEntryViewSet(viewsets.ModelViewSet):
    queryset = StockClosingEntry.objects.all()
    serializer_class = StockClosingEntrySerializer

class WarehouseType(BaseDocument):
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class WarehouseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseType
        fields = '__all__'

class WarehouseTypeViewSet(viewsets.ModelViewSet):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer

class Batch(BaseDocument):
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    batch_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Batch ID")
    item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    parent_batch = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Batch')
    manufacturing_date = models.DateField(blank=True, null=True, verbose_name="Manufacturing Date")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Expiry Date")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Document Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Source Document Name")
    description = models.TextField(blank=True, null=True, verbose_name="Batch Description")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    batch_qty = models.FloatField(default=0.0, verbose_name="Batch Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch UOM')
    qty_to_produce = models.FloatField(default=0.0, verbose_name="Qty To Produce")
    produced_qty = models.FloatField(default=0.0, verbose_name="Produced Qty")
    use_batchwise_valuation = models.BooleanField(default=False, verbose_name="Use Batch-wise Valuation")

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class ItemWebsiteSpecification(BaseDocument):
    label = models.CharField(max_length=255, blank=True, null=True, verbose_name="Label")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class ItemWebsiteSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemWebsiteSpecification
        fields = '__all__'

class ItemWebsiteSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ItemWebsiteSpecification.objects.all()
    serializer_class = ItemWebsiteSpecificationSerializer

class InventoryDimension(BaseDocument):
    reference_document = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Document')
    dimension_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dimension Name")
    document_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Apply to Document')
    istable = models.BooleanField(default=False, verbose_name=" Is Child Table")
    condition = models.TextField(blank=True, null=True, verbose_name="Conditional Rule")
    apply_to_all_doctypes = models.BooleanField(default=False, verbose_name="Apply to All Inventory Documents")
    target_fieldname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Target Fieldname (Stock Ledger Entry)")
    source_fieldname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Source Fieldname")
    type_of_transaction = models.CharField(max_length=255, choices=[('Inward', 'Inward'), ('Outward', 'Outward'), ('Both', 'Both')], blank=True, null=True, verbose_name='Type of Transaction')
    fetch_from_parent = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Fetch Value From')
    mandatory_depends_on = models.TextField(blank=True, null=True, verbose_name="Mandatory Depends On")
    reqd = models.BooleanField(default=False, verbose_name="Mandatory")
    validate_negative_stock = models.BooleanField(default=False, verbose_name="Validate Negative Stock")

class InventoryDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryDimension
        fields = '__all__'

class InventoryDimensionViewSet(viewsets.ModelViewSet):
    queryset = InventoryDimension.objects.all()
    serializer_class = InventoryDimensionSerializer

class PackedItem(BaseDocument):
    parent_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Item')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Warehouse')
    target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To Warehouse (Optional)')
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    actual_qty = models.FloatField(default=0.0, verbose_name="Actual Qty")
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    prevdoc_doctype = models.CharField(max_length=255, blank=True, null=True, verbose_name="Prevdoc DocType")
    parent_detail_docname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parent Detail docname")
    actual_batch_qty = models.FloatField(default=0.0, verbose_name="Actual Batch Quantity")
    incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Incoming Rate")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")
    picked_qty = models.FloatField(default=0.0, verbose_name="Picked Qty")
    packed_qty = models.FloatField(default=0.0, verbose_name="Packed Qty")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="Supplier delivers to Customer")
    requested_qty = models.FloatField(default=0.0, verbose_name="Requested Qty")
    reserve_stock = models.BooleanField(default=False, verbose_name="Reserve Stock")

class PackedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackedItem
        fields = '__all__'

class PackedItemViewSet(viewsets.ModelViewSet):
    queryset = PackedItem.objects.all()
    serializer_class = PackedItemSerializer

class PutawayRule(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    capacity = models.FloatField(default=0.0, verbose_name="Capacity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    priority = models.IntegerField(default=0, verbose_name="Priority")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    disable = models.BooleanField(default=False, verbose_name="Disable")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    stock_capacity = models.FloatField(default=0.0, verbose_name="Capacity in Stock UOM")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")

class PutawayRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PutawayRule
        fields = '__all__'

class PutawayRuleViewSet(viewsets.ModelViewSet):
    queryset = PutawayRule.objects.all()
    serializer_class = PutawayRuleSerializer

class StockReservationEntry(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    voucher_type = models.CharField(max_length=255, choices=[('Sales Order', 'Sales Order'), ('Work Order', 'Work Order'), ('Subcontracting Inward Order', 'Subcontracting Inward Order'), ('Production Plan', 'Production Plan'), ('Subcontracting Order', 'Subcontracting Order')], blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail No")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    reserved_qty = models.FloatField(default=0.0, verbose_name="Reserved Qty")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Partially Reserved', 'Partially Reserved'), ('Reserved', 'Reserved'), ('Partially Delivered', 'Partially Delivered'), ('Partially Used', 'Partially Used'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    available_qty = models.FloatField(default=0.0, verbose_name="Available Qty to Reserve")
    voucher_qty = models.FloatField(default=0.0, verbose_name="Voucher Qty")
    has_serial_no = models.BooleanField(default=False, verbose_name="Has Serial No")
    has_batch_no = models.BooleanField(default=False, verbose_name="Has Batch No")
    sb_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="sb_entries")
    reservation_based_on = models.CharField(max_length=255, choices=[('Qty', 'Qty'), ('Serial and Batch', 'Serial and Batch')], blank=True, null=True, verbose_name='Reservation Based On')
    from_voucher_type = models.CharField(max_length=255, choices=[('Pick List', 'Pick List'), ('Purchase Receipt', 'Purchase Receipt'), ('Stock Entry', 'Stock Entry'), ('Work Order', 'Work Order'), ('Production Plan', 'Production Plan'), ('Subcontracting Inward Order', 'Subcontracting Inward Order')], blank=True, null=True, verbose_name='From Voucher Type')
    from_voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="From Voucher Detail No")
    from_voucher_no = models.TextField(blank=True, null=True, verbose_name="From Voucher No")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Consumed Qty")
    transferred_qty = models.FloatField(default=0.0, verbose_name="Transferred Qty")

class StockReservationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockReservationEntry
        fields = '__all__'

class StockReservationEntryViewSet(viewsets.ModelViewSet):
    queryset = StockReservationEntry.objects.all()
    serializer_class = StockReservationEntrySerializer

class ItemQualityInspectionParameter(BaseDocument):
    specification = models.ForeignKey('erp_core.QualityInspectionParameter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parameter')
    value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Acceptance Criteria Value")
    acceptance_formula = models.TextField(blank=True, null=True, verbose_name="Acceptance Criteria Formula")
    formula_based_criteria = models.BooleanField(default=False, verbose_name="Formula Based Criteria")
    min_value = models.FloatField(default=0.0, verbose_name="Minimum Value")
    max_value = models.FloatField(default=0.0, verbose_name="Maximum Value")
    numeric = models.BooleanField(default=False, verbose_name="Numeric")
    parameter_group = models.ForeignKey('erp_core.QualityInspectionParameterGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parameter Group')

class ItemQualityInspectionParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemQualityInspectionParameter
        fields = '__all__'

class ItemQualityInspectionParameterViewSet(viewsets.ModelViewSet):
    queryset = ItemQualityInspectionParameter.objects.all()
    serializer_class = ItemQualityInspectionParameterSerializer

class LandedCostVendorInvoice(BaseDocument):
    vendor_invoice = models.ForeignKey('erp_core.PurchaseInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Vendor Invoice')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")

class LandedCostVendorInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandedCostVendorInvoice
        fields = '__all__'

class LandedCostVendorInvoiceViewSet(viewsets.ModelViewSet):
    queryset = LandedCostVendorInvoice.objects.all()
    serializer_class = LandedCostVendorInvoiceSerializer

class ItemVariantAttribute(BaseDocument):
    variant_of = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Variant Of')
    attribute = models.ForeignKey('erp_core.ItemAttribute', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Attribute')
    attribute_value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Attribute Value")
    numeric_values = models.BooleanField(default=False, verbose_name="Numeric Values")
    from_range = models.FloatField(default=0.0, verbose_name="From Range")
    increment = models.FloatField(default=0.0, verbose_name="Increment")
    to_range = models.FloatField(default=0.0, verbose_name="To Range")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class ItemVariantAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariantAttribute
        fields = '__all__'

class ItemVariantAttributeViewSet(viewsets.ModelViewSet):
    queryset = ItemVariantAttribute.objects.all()
    serializer_class = ItemVariantAttributeSerializer

class PurchaseReceipt(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('MAT-PRE-.YYYY.-', 'MAT-PRE-.YYYY.-'), ('MAT-PR-RET-.YYYY.-', 'MAT-PR-RET-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    supplier_delivery_note = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Delivery Note")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    is_return = models.BooleanField(default=False, verbose_name="Is Return")
    return_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against Purchase Receipt')
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.TextField(blank=True, null=True, verbose_name="Contact Email")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address Template')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accepted Warehouse')
    rejected_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Warehouse')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    supplier_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Warehouse')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Detail")
    supplied_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Consumed Items")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total (Company Currency)")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total")
    total_net_weight = models.FloatField(default=0.0, verbose_name="Total Net Weight")
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    shipping_rule = models.ForeignKey('erp_core.ShippingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Rule')
    taxes_and_charges = models.ForeignKey('erp_core.PurchaseTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Taxes and Charges Template')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Purchase Taxes and Charges")
    other_charges_calculation = models.TextField(blank=True, null=True, verbose_name="Taxes and Charges Calculation")
    base_taxes_and_charges_added = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Taxes and Charges Added (Company Currency)")
    base_taxes_and_charges_deducted = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Taxes and Charges Deducted (Company Currency)")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    taxes_and_charges_added = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Taxes and Charges Added")
    taxes_and_charges_deducted = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Taxes and Charges Deducted")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Additional Discount On')
    base_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount (Company Currency)")
    additional_discount_percentage = models.FloatField(default=0.0, verbose_name="Additional Discount Percentage")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount")
    base_grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    base_rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    base_in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    base_rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Partly Billed', 'Partly Billed'), ('To Bill', 'To Bill'), ('Completed', 'Completed'), ('Return', 'Return'), ('Return Issued', 'Return Issued'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    range = models.CharField(max_length=255, blank=True, null=True, verbose_name="Range")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    per_billed = models.TextField(blank=True, null=True, verbose_name="% Amount Billed")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Print Language")
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    instructions = models.TextField(blank=True, null=True, verbose_name="Instructions")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    transporter_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Transporter Name")
    lr_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Vehicle Number")
    lr_date = models.DateField(blank=True, null=True, verbose_name="Vehicle Date")
    is_internal_supplier = models.BooleanField(default=False, verbose_name="Is Internal Supplier")
    inter_company_reference = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Reference')
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address")
    apply_putaway_rule = models.BooleanField(default=False, verbose_name="Apply Putaway Rule")
    per_returned = models.TextField(blank=True, null=True, verbose_name="% Returned")
    set_from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set From Warehouse')
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    subcontracting_receipt = models.ForeignKey('erp_core.SubcontractingReceipt', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Receipt')
    dispatch_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Address Template')
    dispatch_address_display = models.TextField(blank=True, null=True, verbose_name="Dispatch Address")
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")

class PurchaseReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseReceipt
        fields = '__all__'

class PurchaseReceiptViewSet(viewsets.ModelViewSet):
    queryset = PurchaseReceipt.objects.all()
    serializer_class = PurchaseReceiptSerializer

class QuickStockBalance(BaseDocument):
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Barcode")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    item_description = models.TextField(blank=True, null=True, verbose_name="Item Description")
    qty = models.FloatField(default=0.0, verbose_name="Available Quantity")
    value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Stock Value")
    image = models.TextField(blank=True, null=True, verbose_name="Image View")
    date = models.DateField(blank=True, null=True, verbose_name="Date")

class QuickStockBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickStockBalance
        fields = '__all__'

class QuickStockBalanceViewSet(viewsets.ModelViewSet):
    queryset = QuickStockBalance.objects.all()
    serializer_class = QuickStockBalanceSerializer

class ItemTax(BaseDocument):
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    maximum_net_rate = models.FloatField(default=0.0, verbose_name="Maximum Net Rate")
    minimum_net_rate = models.FloatField(default=0.0, verbose_name="Minimum Net Rate")

class ItemTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTax
        fields = '__all__'

class ItemTaxViewSet(viewsets.ModelViewSet):
    queryset = ItemTax.objects.all()
    serializer_class = ItemTaxSerializer

class StockEntry(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-STE-.YYYY.-', 'MAT-STE-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    stock_entry_type = models.ForeignKey('erp_core.StockEntryType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Entry Type')
    outgoing_stock_entry = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Entry (Outward GIT)')
    source_stock_entry = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Stock Entry (Manufacture)')
    purpose = models.CharField(max_length=255, choices=[('Material Issue', 'Material Issue'), ('Material Receipt', 'Material Receipt'), ('Material Transfer', 'Material Transfer'), ('Material Transfer for Manufacture', 'Material Transfer for Manufacture'), ('Material Consumption for Manufacture', 'Material Consumption for Manufacture'), ('Manufacture', 'Manufacture'), ('Repack', 'Repack'), ('Send to Subcontractor', 'Send to Subcontractor'), ('Disassemble', 'Disassemble'), ('Receive from Customer', 'Receive from Customer'), ('Return Raw Material to Customer', 'Return Raw Material to Customer'), ('Subcontracting Delivery', 'Subcontracting Delivery'), ('Subcontracting Return', 'Subcontracting Return')], blank=True, null=True, verbose_name='Purpose')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    work_order = models.ForeignKey('erp_core.WorkOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Work Order')
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    subcontracting_order = models.ForeignKey('erp_core.SubcontractingOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Order')
    delivery_note_no = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Note No')
    sales_invoice_no = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Invoice No')
    purchase_receipt_no = models.ForeignKey('erp_core.PurchaseReceipt', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Receipt No')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    inspection_required = models.BooleanField(default=False, verbose_name="Inspection Required")
    from_bom = models.BooleanField(default=False, verbose_name="From BOM")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    fg_completed_qty = models.FloatField(default=0.0, verbose_name="Finished Good Quantity ")
    use_multi_level_bom = models.BooleanField(default=False, verbose_name="Use Multi-Level BOM")
    from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Source Warehouse')
    source_warehouse_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse Address Link')
    source_address_display = models.TextField(blank=True, null=True, verbose_name="Source Warehouse Address")
    to_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Target Warehouse')
    target_warehouse_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse Address Link')
    target_address_display = models.TextField(blank=True, null=True, verbose_name="Target Warehouse Address")
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    total_incoming_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Incoming Value (Receipt)")
    total_outgoing_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Outgoing Value (Consumption)")
    value_difference = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Value Difference (Incoming - Outgoing)")
    additional_costs = models.JSONField(default=list, blank=True, null=True, verbose_name="Additional Costs")
    total_additional_costs = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Additional Costs")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    per_transferred = models.TextField(blank=True, null=True, verbose_name="Per Transferred")
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Amount")
    job_card = models.ForeignKey('erp_core.JobCard', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Card')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    credit_note = models.ForeignKey('erp_core.JournalEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Credit Note')
    pick_list = models.ForeignKey('erp_core.PickList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pick List')
    add_to_transit = models.BooleanField(default=False, verbose_name="Add to Transit")
    apply_putaway_rule = models.BooleanField(default=False, verbose_name="Apply Putaway Rule")
    is_return = models.BooleanField(default=False, verbose_name="Is Return")
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")
    process_loss_percentage = models.TextField(blank=True, null=True, verbose_name="% Process Loss")
    asset_repair = models.ForeignKey('erp_core.AssetRepair', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Repair')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    is_additional_transfer_entry = models.BooleanField(default=False, verbose_name="Is Additional Transfer Entry")
    subcontracting_inward_order = models.ForeignKey('erp_core.SubcontractingInwardOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Inward Order')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')

class StockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntry
        fields = '__all__'

class StockEntryViewSet(viewsets.ModelViewSet):
    queryset = StockEntry.objects.all()
    serializer_class = StockEntrySerializer

class DeliveryNote(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-DN-.YYYY.-', 'MAT-DN-.YYYY.-'), ('MAT-DN-RET-.YYYY.-', 'MAT-DN-RET-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    is_return = models.BooleanField(default=False, verbose_name="Is Return")
    issue_credit_note = models.BooleanField(default=False, verbose_name="Issue Credit Note")
    return_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against Delivery Note')
    po_no = models.TextField(blank=True, null=True, verbose_name="Customer's Purchase Order No")
    po_date = models.DateField(blank=True, null=True, verbose_name="Customer's Purchase Order Date")
    shipping_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address')
    shipping_address = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Billing Address Name')
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax Id")
    address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address Name')
    company_address_display = models.TextField(blank=True, null=True, verbose_name="Company Address")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Source Warehouse')
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Delivery Note Item")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Detail")
    packed_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Packed Items")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total (Company Currency)")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total")
    total_net_weight = models.FloatField(default=0.0, verbose_name="Total Net Weight")
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    shipping_rule = models.ForeignKey('erp_core.ShippingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Rule')
    taxes_and_charges = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Taxes and Charges")
    other_charges_calculation = models.TextField(blank=True, null=True, verbose_name="Taxes and Charges Calculation")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Additional Discount On')
    base_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount (Company Currency)")
    additional_discount_percentage = models.FloatField(default=0.0, verbose_name="Additional Discount Percentage")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount")
    base_grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    base_rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    base_rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    base_in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions Details")
    transporter = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Transporter')
    driver = models.ForeignKey('erp_core.Driver', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Driver')
    lr_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Transport Receipt No")
    vehicle_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Vehicle No")
    transporter_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Transporter Name")
    driver_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Driver Name")
    lr_date = models.DateField(blank=True, null=True, verbose_name="Transport Receipt Date")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    per_billed = models.TextField(blank=True, null=True, verbose_name="% Amount Billed")
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    print_without_amount = models.BooleanField(default=False, verbose_name="Print Without Amount")
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('To Bill', 'To Bill'), ('Partially Billed', 'Partially Billed'), ('Completed', 'Completed'), ('Return', 'Return'), ('Return Issued', 'Return Issued'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    per_installed = models.TextField(blank=True, null=True, verbose_name="% Installed")
    installation_status = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Installation Status')
    excise_page = models.CharField(max_length=255, blank=True, null=True, verbose_name="Excise Page Number")
    instructions = models.TextField(blank=True, null=True, verbose_name="Instructions")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    commission_rate = models.FloatField(default=0.0, verbose_name="Commission Rate (%)")
    total_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Commission")
    sales_team = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Team")
    is_internal_customer = models.BooleanField(default=False, verbose_name="Is Internal Customer")
    inter_company_reference = models.ForeignKey('erp_core.PurchaseReceipt', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Reference')
    per_returned = models.TextField(blank=True, null=True, verbose_name="% Returned")
    set_target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Target Warehouse')
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    dispatch_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Address Name')
    dispatch_address = models.TextField(blank=True, null=True, verbose_name="Dispatch Address")
    amount_eligible_for_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount Eligible for Commission")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    delivery_trip = models.ForeignKey('erp_core.DeliveryTrip', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Trip')
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    company_contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Contact Person')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

class DeliveryNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryNote
        fields = '__all__'

class DeliveryNoteViewSet(viewsets.ModelViewSet):
    queryset = DeliveryNote.objects.all()
    serializer_class = DeliveryNoteSerializer

class StockRepostingSettings(BaseDocument):
    start_time = models.TextField(blank=True, null=True, verbose_name="Start Time")
    end_time = models.TextField(blank=True, null=True, verbose_name="End Time")
    limits_dont_apply_on = models.CharField(max_length=255, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], blank=True, null=True, verbose_name='Limits don't apply on')
    limit_reposting_timeslot = models.BooleanField(default=False, verbose_name="Limit timeslot for Stock Reposting")
    item_based_reposting = models.BooleanField(default=False, verbose_name="Use Item based reposting")
    notify_reposting_error_to_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Notify Reposting Error to Role')
    enable_parallel_reposting = models.BooleanField(default=False, verbose_name="Enable Parallel Reposting")
    no_of_parallel_reposting = models.IntegerField(default=0, verbose_name="No of Parallel Reposting (Per Item)")
    enable_separate_reposting_for_gl = models.BooleanField(default=False, verbose_name="Enable Separate Reposting for GL")
    do_not_fetch_incoming_rate_from_serial_no = models.BooleanField(default=False, verbose_name="Do not fetch incoming rate from Serial No")

class StockRepostingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRepostingSettings
        fields = '__all__'

class StockRepostingSettingsViewSet(viewsets.ModelViewSet):
    queryset = StockRepostingSettings.objects.all()
    serializer_class = StockRepostingSettingsSerializer

class QualityInspectionReading(BaseDocument):
    specification = models.ForeignKey('erp_core.QualityInspectionParameter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parameter')
    value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Acceptance Criteria Value")
    reading_1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 1")
    reading_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 2")
    reading_3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 3")
    reading_4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 4")
    reading_5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 5")
    reading_6 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 6")
    reading_7 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 7")
    reading_8 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 8")
    reading_9 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 9")
    reading_10 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading 10")
    status = models.CharField(max_length=255, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], blank=True, null=True, verbose_name='Status')
    acceptance_formula = models.TextField(blank=True, null=True, verbose_name="Acceptance Criteria Formula")
    formula_based_criteria = models.BooleanField(default=False, verbose_name="Formula Based Criteria")
    min_value = models.FloatField(default=0.0, verbose_name="Minimum Value")
    max_value = models.FloatField(default=0.0, verbose_name="Maximum Value")
    reading_value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reading Value")
    manual_inspection = models.BooleanField(default=False, verbose_name="Manual Inspection")
    numeric = models.BooleanField(default=False, verbose_name="Numeric")
    parameter_group = models.ForeignKey('erp_core.QualityInspectionParameterGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parameter Group')

class QualityInspectionReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspectionReading
        fields = '__all__'

class QualityInspectionReadingViewSet(viewsets.ModelViewSet):
    queryset = QualityInspectionReading.objects.all()
    serializer_class = QualityInspectionReadingSerializer

class StockLedgerEntry(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Batch No")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail No")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty Change")
    incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Incoming Rate")
    outgoing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outgoing Rate")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    qty_after_transaction = models.FloatField(default=0.0, verbose_name="Qty After Transaction")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    stock_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Balance Stock Value")
    stock_value_difference = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Change in Stock Value")
    stock_queue = models.TextField(blank=True, null=True, verbose_name="FIFO Stock Queue (qty, rate)")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    fiscal_year = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fiscal Year")
    is_cancelled = models.BooleanField(default=False, verbose_name="Is Cancelled")
    to_rename = models.BooleanField(default=False, verbose_name="To Rename")
    dependant_sle_voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dependant SLE Voucher Detail No")
    recalculate_rate = models.BooleanField(default=False, verbose_name="Recalculate Incoming/Outgoing Rate")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    has_batch_no = models.BooleanField(default=False, verbose_name="Has Batch No")
    has_serial_no = models.BooleanField(default=False, verbose_name="Has Serial No")
    is_adjustment_entry = models.BooleanField(default=False, verbose_name="Is Adjustment Entry")
    auto_created_serial_and_batch_bundle = models.BooleanField(default=False, verbose_name="Auto Created Serial and Batch Bundle")
    posting_datetime = models.DateTimeField(blank=True, null=True, verbose_name="Posting Datetime")

class StockLedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockLedgerEntry
        fields = '__all__'

class StockLedgerEntryViewSet(viewsets.ModelViewSet):
    queryset = StockLedgerEntry.objects.all()
    serializer_class = StockLedgerEntrySerializer

class StockEntryDetail(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    s_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    t_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    basic_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Basic Rate (as per Stock UOM)")
    basic_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Basic Amount")
    additional_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Cost")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    transfer_qty = models.FloatField(default=0.0, verbose_name="Qty as per Stock UOM")
    retain_sample = models.BooleanField(default=False, verbose_name="Retain Sample")
    sample_quantity = models.IntegerField(default=0, verbose_name="Sample Quantity")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Difference Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    actual_qty = models.FloatField(default=0.0, verbose_name="Actual Qty (at source/target)")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.ForeignKey('erp_core.MaterialRequestItem', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request Item')
    original_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Original Item')
    subcontracted_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracted Item')
    against_stock_entry = models.ForeignKey('erp_core.StockEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Stock Entry')
    ste_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Stock Entry Child")
    transferred_qty = models.FloatField(default=0.0, verbose_name="Transferred Qty")
    item_group = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Group")
    reference_purchase_receipt = models.ForeignKey('erp_core.PurchaseReceipt', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Purchase Receipt')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    po_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="PO Supplied Item")
    sco_rm_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="SCO Supplied Item")
    set_basic_rate_manually = models.BooleanField(default=False, verbose_name="Set Basic Rate Manually")
    putaway_rule = models.ForeignKey('erp_core.PutawayRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Putaway Rule')
    is_finished_item = models.BooleanField(default=False, verbose_name="Is Finished Item")
    job_card_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Card Item")
    has_item_scanned = models.BooleanField(default=False, verbose_name="Has Item Scanned")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    landed_cost_voucher_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Landed Cost Voucher Amount")
    customer_provided_item_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Customer Provided Item Cost")
    scio_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="SCIO Detail")
    against_fg = models.ForeignKey('erp_core.SubcontractingInwardOrderItem', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Finished Good')
    type = models.CharField(max_length=255, choices=[('Co-Product', 'Co-Product'), ('By-Product', 'By-Product'), ('Scrap', 'Scrap'), ('Additional Finished Good', 'Additional Finished Good')], blank=True, null=True, verbose_name='Type')
    bom_secondary_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Secondary Item")
    is_legacy_scrap_item = models.BooleanField(default=False, verbose_name="Is Legacy Scrap Item")

class StockEntryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntryDetail
        fields = '__all__'

class StockEntryDetailViewSet(viewsets.ModelViewSet):
    queryset = StockEntryDetail.objects.all()
    serializer_class = StockEntryDetailSerializer

class QualityInspection(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-QA-.YYYY.-', 'MAT-QA-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    report_date = models.DateField(blank=True, null=True, verbose_name="Report Date")
    inspection_type = models.CharField(max_length=255, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('In Process', 'In Process')], blank=True, null=True, verbose_name='Inspection Type')
    reference_type = models.CharField(max_length=255, choices=[('Purchase Receipt', 'Purchase Receipt'), ('Purchase Invoice', 'Purchase Invoice'), ('Subcontracting Receipt', 'Subcontracting Receipt'), ('Delivery Note', 'Delivery Note'), ('Sales Invoice', 'Sales Invoice'), ('Stock Entry', 'Stock Entry'), ('Job Card', 'Job Card')], blank=True, null=True, verbose_name='Reference Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_serial_no = models.ForeignKey('erp_core.SerialNo', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Serial No')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    sample_size = models.FloatField(default=0.0, verbose_name="Sample Size")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    inspected_by = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inspected By')
    verified_by = models.CharField(max_length=255, blank=True, null=True, verbose_name="Verified By")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    quality_inspection_template = models.ForeignKey('erp_core.QualityInspectionTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection Template')
    readings = models.JSONField(default=list, blank=True, null=True, verbose_name="Readings")
    status = models.CharField(max_length=255, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    manual_inspection = models.BooleanField(default=False, verbose_name="Manual Inspection")
    child_row_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Child Row Reference")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')

class QualityInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspection
        fields = '__all__'

class QualityInspectionViewSet(viewsets.ModelViewSet):
    queryset = QualityInspection.objects.all()
    serializer_class = QualityInspectionSerializer

class PriceListCountry(BaseDocument):
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')

class PriceListCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListCountry
        fields = '__all__'

class PriceListCountryViewSet(viewsets.ModelViewSet):
    queryset = PriceListCountry.objects.all()
    serializer_class = PriceListCountrySerializer

class ItemManufacturer(BaseDocument):
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    is_default = models.BooleanField(default=False, verbose_name="Is Default")

class ItemManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemManufacturer
        fields = '__all__'

class ItemManufacturerViewSet(viewsets.ModelViewSet):
    queryset = ItemManufacturer.objects.all()
    serializer_class = ItemManufacturerSerializer

class SerialNo(BaseDocument):
    serial_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Serial No")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    asset_status = models.CharField(max_length=255, choices=[('Issue', 'Issue'), ('Receipt', 'Receipt'), ('Transfer', 'Transfer')], blank=True, null=True, verbose_name='Asset Status')
    location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Location')
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    maintenance_status = models.CharField(max_length=255, choices=[('Under Warranty', 'Under Warranty'), ('Out of Warranty', 'Out of Warranty'), ('Under AMC', 'Under AMC'), ('Out of AMC', 'Out of AMC')], blank=True, null=True, verbose_name='Maintenance Status')
    warranty_period = models.IntegerField(default=0, verbose_name="Warranty Period (Days)")
    warranty_expiry_date = models.DateField(blank=True, null=True, verbose_name="Warranty Expiry Date")
    amc_expiry_date = models.DateField(blank=True, null=True, verbose_name="AMC Expiry Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    work_order = models.ForeignKey('erp_core.WorkOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Work Order')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    purchase_rate = models.FloatField(default=0.0, verbose_name="Incoming Rate")
    status = models.CharField(max_length=255, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Consumed', 'Consumed'), ('Delivered', 'Delivered'), ('Expired', 'Expired')], blank=True, null=True, verbose_name='Status')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Document Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Source Document Name")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")

class SerialNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNo
        fields = '__all__'

class SerialNoViewSet(viewsets.ModelViewSet):
    queryset = SerialNo.objects.all()
    serializer_class = SerialNoSerializer

class MaterialRequest(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-MR-.YYYY.-', 'MAT-MR-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    material_request_type = models.CharField(max_length=255, choices=[('Purchase', 'Purchase'), ('Material Transfer', 'Material Transfer'), ('Material Issue', 'Material Issue'), ('Manufacture', 'Manufacture'), ('Subcontracting', 'Subcontracting'), ('Customer Provided', 'Customer Provided')], blank=True, null=True, verbose_name='Purpose')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Transaction Date")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Stopped', 'Stopped'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending'), ('Partially Ordered', 'Partially Ordered'), ('Partially Received', 'Partially Received'), ('Ordered', 'Ordered'), ('Issued', 'Issued'), ('Transferred', 'Transferred'), ('Received', 'Received')], blank=True, null=True, verbose_name='Status')
    per_ordered = models.TextField(blank=True, null=True, verbose_name="% Ordered")
    per_received = models.TextField(blank=True, null=True, verbose_name="% Received")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions Content")
    job_card = models.ForeignKey('erp_core.JobCard', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Card')
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Target Warehouse')
    set_from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Source Warehouse')
    transfer_status = models.CharField(max_length=255, choices=[('Not Started', 'Not Started'), ('In Transit', 'In Transit'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Transfer Status')
    work_order = models.ForeignKey('erp_core.WorkOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Work Order')
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    auto_created_via_reorder = models.BooleanField(default=False, verbose_name="Auto Created (Reorder)")

class MaterialRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequest
        fields = '__all__'

class MaterialRequestViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequest.objects.all()
    serializer_class = MaterialRequestSerializer

class QualityInspectionTemplate(BaseDocument):
    quality_inspection_template_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Quality Inspection Template Name")
    item_quality_inspection_parameter = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Quality Inspection Parameter")

class QualityInspectionTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspectionTemplate
        fields = '__all__'

class QualityInspectionTemplateViewSet(viewsets.ModelViewSet):
    queryset = QualityInspectionTemplate.objects.all()
    serializer_class = QualityInspectionTemplateSerializer

class DeliverySettings(BaseDocument):
    dispatch_template = models.ForeignKey('erp_core.EmailTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Notification Template')
    dispatch_attachment = models.ForeignKey('erp_core.PrintFormat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Notification Attachment')
    send_with_attachment = models.BooleanField(default=False, verbose_name="Send with Attachment")
    stop_delay = models.IntegerField(default=0, verbose_name="Delay between Delivery Stops")

class DeliverySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySettings
        fields = '__all__'

class DeliverySettingsViewSet(viewsets.ModelViewSet):
    queryset = DeliverySettings.objects.all()
    serializer_class = DeliverySettingsSerializer

class SerialandBatchBundle(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    has_serial_no = models.BooleanField(default=False, verbose_name="Has Serial No")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    has_batch_no = models.BooleanField(default=False, verbose_name="Has Batch No")
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    is_cancelled = models.BooleanField(default=False, verbose_name="Is Cancelled")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    avg_rate = models.FloatField(default=0.0, verbose_name="Avg Rate")
    total_amount = models.FloatField(default=0.0, verbose_name="Total Amount")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Qty")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    type_of_transaction = models.CharField(max_length=255, choices=[('Inward', 'Inward'), ('Outward', 'Outward'), ('Maintenance', 'Maintenance'), ('Asset Repair', 'Asset Repair')], blank=True, null=True, verbose_name='Type of Transaction')
    is_rejected = models.BooleanField(default=False, verbose_name="Is Rejected")
    voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail No")
    entries = models.JSONField(default=list, blank=True, null=True, verbose_name="entries")
    returned_against = models.CharField(max_length=255, blank=True, null=True, verbose_name="Returned Against")
    naming_series = models.CharField(max_length=255, choices=[('SABB-.########', 'SABB-.########')], blank=True, null=True, verbose_name='Naming Series')
    is_packed = models.BooleanField(default=False, verbose_name="Is Packed")
    posting_datetime = models.DateTimeField(blank=True, null=True, verbose_name="Posting Datetime")

class SerialandBatchBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialandBatchBundle
        fields = '__all__'

class SerialandBatchBundleViewSet(viewsets.ModelViewSet):
    queryset = SerialandBatchBundle.objects.all()
    serializer_class = SerialandBatchBundleSerializer

class LandedCostItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    receipt_document_type = models.CharField(max_length=255, choices=[('Purchase Invoice', 'Purchase Invoice'), ('Purchase Receipt', 'Purchase Receipt'), ('Stock Entry', 'Stock Entry'), ('Subcontracting Receipt', 'Subcontracting Receipt')], blank=True, null=True, verbose_name='Receipt Document Type')
    receipt_document = models.TextField(blank=True, null=True, verbose_name="Receipt Document")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    applicable_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Applicable Charges")
    purchase_receipt_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Receipt Item")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    stock_entry_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Stock Entry Item")

class LandedCostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandedCostItem
        fields = '__all__'

class LandedCostItemViewSet(viewsets.ModelViewSet):
    queryset = LandedCostItem.objects.all()
    serializer_class = LandedCostItemSerializer

class ItemPrice(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    packing_unit = models.IntegerField(default=0, verbose_name="Packing Unit")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    item_description = models.TextField(blank=True, null=True, verbose_name="Item Description")
    price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    buying = models.BooleanField(default=False, verbose_name="Buying")
    selling = models.BooleanField(default=False, verbose_name="Selling")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    lead_time_days = models.IntegerField(default=0, verbose_name="Lead Time in days")
    valid_upto = models.DateField(blank=True, null=True, verbose_name="Valid Up To")
    note = models.TextField(blank=True, null=True, verbose_name="Note")
    reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')

class ItemPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPrice
        fields = '__all__'

class ItemPriceViewSet(viewsets.ModelViewSet):
    queryset = ItemPrice.objects.all()
    serializer_class = ItemPriceSerializer

class Item(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('STO-ITEM-.YYYY.-', 'STO-ITEM-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Code")
    variant_of = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Variant Of')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Unit of Measure')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    is_stock_item = models.BooleanField(default=False, verbose_name="Maintain Stock")
    include_item_in_manufacturing = models.BooleanField(default=False, verbose_name="Include Item In Manufacturing")
    opening_stock = models.FloatField(default=0.0, verbose_name="Opening Stock")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    standard_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Standard Selling Rate")
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    asset_category = models.ForeignKey('erp_core.AssetCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Category')
    asset_naming_series = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Asset Naming Series')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    barcodes = models.JSONField(default=list, blank=True, null=True, verbose_name="Barcodes")
    shelf_life_in_days = models.IntegerField(default=0, verbose_name="Shelf Life In Days")
    end_of_life = models.DateField(blank=True, null=True, verbose_name="End of Life")
    default_material_request_type = models.CharField(max_length=255, choices=[('Purchase', 'Purchase'), ('Material Transfer', 'Material Transfer'), ('Material Issue', 'Material Issue'), ('Manufacture', 'Manufacture'), ('Customer Provided', 'Customer Provided')], blank=True, null=True, verbose_name='Default Material Request Type')
    valuation_method = models.CharField(max_length=255, choices=[('FIFO', 'FIFO'), ('Moving Average', 'Moving Average'), ('LIFO', 'LIFO')], blank=True, null=True, verbose_name='Valuation Method')
    warranty_period = models.CharField(max_length=255, blank=True, null=True, verbose_name="Warranty Period (in days)")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    reorder_levels = models.JSONField(default=list, blank=True, null=True, verbose_name="Reorder level based on Warehouse")
    uoms = models.JSONField(default=list, blank=True, null=True, verbose_name="uoms")
    has_batch_no = models.BooleanField(default=False, verbose_name="Has Batch No")
    create_new_batch = models.BooleanField(default=False, verbose_name="Automatically Create New Batch")
    batch_number_series = models.CharField(max_length=255, blank=True, null=True, verbose_name="Batch Number Series")
    has_expiry_date = models.BooleanField(default=False, verbose_name="Has Expiry Date")
    retain_sample = models.BooleanField(default=False, verbose_name="Retain Sample")
    sample_quantity = models.IntegerField(default=0, verbose_name="Max Sample Quantity")
    has_serial_no = models.BooleanField(default=False, verbose_name="Has Serial No")
    serial_no_series = models.CharField(max_length=255, blank=True, null=True, verbose_name="Serial Number Series")
    has_variants = models.BooleanField(default=False, verbose_name="Has Variants")
    variant_based_on = models.CharField(max_length=255, choices=[('Item Attribute', 'Item Attribute'), ('Manufacturer', 'Manufacturer')], blank=True, null=True, verbose_name='Variant Based On')
    attributes = models.JSONField(default=list, blank=True, null=True, verbose_name="Variant Attributes")
    item_defaults = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Defaults")
    is_purchase_item = models.BooleanField(default=False, verbose_name="Allow Purchase")
    purchase_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Purchase Unit of Measure')
    min_order_qty = models.FloatField(default=0.0, verbose_name="Minimum Order Qty")
    safety_stock = models.FloatField(default=0.0, verbose_name="Safety Stock")
    lead_time_days = models.IntegerField(default=0, verbose_name="Lead Time in days")
    last_purchase_rate = models.FloatField(default=0.0, verbose_name="Last Purchase Rate")
    is_customer_provided_item = models.BooleanField(default=False, verbose_name="Is Customer Provided Item")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="Delivered by Supplier (Drop Ship)")
    supplier_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Supplier")
    country_of_origin = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country of Origin')
    customs_tariff_number = models.ForeignKey('erp_core.CustomsTariffNumber', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customs Tariff Number')
    sales_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Sales Unit of Measure')
    is_sales_item = models.BooleanField(default=False, verbose_name="Allow Sales")
    max_discount = models.FloatField(default=0.0, verbose_name="Max Discount (%)")
    enable_deferred_revenue = models.BooleanField(default=False, verbose_name="Enable Deferred Revenue")
    no_of_months = models.IntegerField(default=0, verbose_name="No of Months (Revenue)")
    enable_deferred_expense = models.BooleanField(default=False, verbose_name="Enable Deferred Expense")
    no_of_months_exp = models.IntegerField(default=0, verbose_name="No of Months (Expense)")
    customer_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Customer Items")
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Taxes")
    inspection_required_before_purchase = models.BooleanField(default=False, verbose_name="Inspection Required before Purchase")
    inspection_required_before_delivery = models.BooleanField(default=False, verbose_name="Inspection Required before Delivery")
    quality_inspection_template = models.ForeignKey('erp_core.QualityInspectionTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection Template')
    default_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default BOM')
    is_sub_contracted_item = models.BooleanField(default=False, verbose_name="Is Subcontracted Item")
    customer_code = models.TextField(blank=True, null=True, verbose_name="Customer Code")
    total_projected_qty = models.FloatField(default=0.0, verbose_name="Total Projected Qty")
    over_delivery_receipt_allowance = models.FloatField(default=0.0, verbose_name="Over Delivery/Receipt Allowance (%)")
    over_billing_allowance = models.FloatField(default=0.0, verbose_name="Over Billing Allowance (%)")
    auto_create_assets = models.BooleanField(default=False, verbose_name="Auto create assets on purchase")
    default_item_manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Item Manufacturer')
    default_manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Default Manufacturer Part No")
    grant_commission = models.BooleanField(default=False, verbose_name="Grant Commission")
    is_grouped_asset = models.BooleanField(default=False, verbose_name="Create Grouped Asset")
    allow_negative_stock = models.BooleanField(default=False, verbose_name="Allow Negative Stock")
    production_capacity = models.IntegerField(default=0, verbose_name="Production Capacity")
    purchase_tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Tax Withholding Category')
    sales_tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Tax Withholding Category')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemReorder(BaseDocument):
    warehouse_group = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Check Availability in Warehouse')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Request for')
    warehouse_reorder_level = models.FloatField(default=0.0, verbose_name="Re-order Level")
    warehouse_reorder_qty = models.FloatField(default=0.0, verbose_name="Re-order Qty")
    material_request_type = models.CharField(max_length=255, choices=[('Purchase', 'Purchase'), ('Transfer', 'Transfer'), ('Material Issue', 'Material Issue'), ('Manufacture', 'Manufacture')], blank=True, null=True, verbose_name='Material Request Type')

class ItemReorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReorder
        fields = '__all__'

class ItemReorderViewSet(viewsets.ModelViewSet):
    queryset = ItemReorder.objects.all()
    serializer_class = ItemReorderSerializer

class ItemAttributeValue(BaseDocument):
    attribute_value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Attribute Value")
    abbr = models.CharField(max_length=255, blank=True, null=True, verbose_name="Abbreviation")

class ItemAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAttributeValue
        fields = '__all__'

class ItemAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ItemAttributeValue.objects.all()
    serializer_class = ItemAttributeValueSerializer

class Shipment(BaseDocument):
    heading_pickup_from = models.TextField(blank=True, null=True, verbose_name="Pickup from")
    pickup_from_type = models.CharField(max_length=255, choices=[('Company', 'Company'), ('Customer', 'Customer'), ('Supplier', 'Supplier')], blank=True, null=True, verbose_name='Pickup from')
    pickup_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    pickup_customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    pickup_supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    pickup = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pickup From")
    pickup_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Address')
    pickup_address = models.TextField(blank=True, null=True, verbose_name="pickup_address")
    pickup_contact_name = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact')
    pickup_contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    pickup_contact = models.TextField(blank=True, null=True, verbose_name="pickup_contact")
    heading_delivery_to = models.TextField(blank=True, null=True, verbose_name="Delivery to")
    delivery_to_type = models.CharField(max_length=255, choices=[('Company', 'Company'), ('Customer', 'Customer'), ('Supplier', 'Supplier')], blank=True, null=True, verbose_name='Delivery to')
    delivery_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    delivery_customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    delivery_supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    delivery_to = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delivery To")
    delivery_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Address')
    delivery_address = models.TextField(blank=True, null=True, verbose_name="delivery_address")
    delivery_contact_name = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact')
    delivery_contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    delivery_contact = models.TextField(blank=True, null=True, verbose_name="delivery_contact")
    shipment_parcel = models.JSONField(default=list, blank=True, null=True, verbose_name="Shipment Parcel")
    parcel_template = models.ForeignKey('erp_core.ShipmentParcelTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parcel Template')
    pallets = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Pallets')
    value_of_goods = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Value of Goods")
    pickup_date = models.DateField(blank=True, null=True, verbose_name="Pickup Date")
    pickup_from = models.TextField(blank=True, null=True, verbose_name="Pickup from")
    pickup_to = models.TextField(blank=True, null=True, verbose_name="Pickup to")
    shipment_type = models.CharField(max_length=255, choices=[('Goods', 'Goods'), ('Documents', 'Documents')], blank=True, null=True, verbose_name='Shipment Type')
    pickup_type = models.CharField(max_length=255, choices=[('Pickup', 'Pickup'), ('Self delivery', 'Self delivery')], blank=True, null=True, verbose_name='Pickup Type')
    description_of_content = models.TextField(blank=True, null=True, verbose_name="Description of Content")
    service_provider = models.CharField(max_length=255, blank=True, null=True, verbose_name="Service Provider")
    shipment_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shipment ID")
    shipment_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Shipment Amount")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    tracking_url = models.TextField(blank=True, null=True, verbose_name="Tracking URL")
    carrier = models.CharField(max_length=255, blank=True, null=True, verbose_name="Carrier")
    carrier_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Carrier Service")
    awb_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="AWB Number")
    tracking_status = models.CharField(max_length=255, choices=[('In Progress', 'In Progress'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Lost', 'Lost')], blank=True, null=True, verbose_name='Tracking Status')
    tracking_status_info = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tracking Status Info")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    shipment_delivery_note = models.JSONField(default=list, blank=True, null=True, verbose_name="Shipment Delivery Note")
    pickup_contact_person = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pickup Contact Person')
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight (kg)")

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class ShipmentParcelTemplate(BaseDocument):
    length = models.FloatField(default=0.0, verbose_name="Length (cm)")
    width = models.FloatField(default=0.0, verbose_name="Width (cm)")
    height = models.FloatField(default=0.0, verbose_name="Height (cm)")
    weight = models.FloatField(default=0.0, verbose_name="Weight (kg)")
    parcel_template_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parcel Template Name")

class ShipmentParcelTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentParcelTemplate
        fields = '__all__'

class ShipmentParcelTemplateViewSet(viewsets.ModelViewSet):
    queryset = ShipmentParcelTemplate.objects.all()
    serializer_class = ShipmentParcelTemplateSerializer

class LandedCostPurchaseReceipt(BaseDocument):
    receipt_document_type = models.CharField(max_length=255, choices=[('Purchase Invoice', 'Purchase Invoice'), ('Purchase Receipt', 'Purchase Receipt'), ('Stock Entry', 'Stock Entry'), ('Subcontracting Receipt', 'Subcontracting Receipt')], blank=True, null=True, verbose_name='Receipt Document Type')
    receipt_document = models.TextField(blank=True, null=True, verbose_name="Receipt Document")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")

class LandedCostPurchaseReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandedCostPurchaseReceipt
        fields = '__all__'

class LandedCostPurchaseReceiptViewSet(viewsets.ModelViewSet):
    queryset = LandedCostPurchaseReceipt.objects.all()
    serializer_class = LandedCostPurchaseReceiptSerializer

class StockReconciliation(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-RECO-.YYYY.-', 'MAT-RECO-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    purpose = models.CharField(max_length=255, choices=[('Opening Stock', 'Opening Stock'), ('Stock Reconciliation', 'Stock Reconciliation')], blank=True, null=True, verbose_name='Purpose')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Difference Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    difference_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference Amount")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    scan_mode = models.BooleanField(default=False, verbose_name="Scan Mode")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Warehouse')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")

class StockReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockReconciliation
        fields = '__all__'

class StockReconciliationViewSet(viewsets.ModelViewSet):
    queryset = StockReconciliation.objects.all()
    serializer_class = StockReconciliationSerializer

class RepostItemValuation(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Skipped', 'Skipped'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    error_log = models.TextField(blank=True, null=True, verbose_name="Error Log")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    based_on = models.CharField(max_length=255, choices=[('Transaction', 'Transaction'), ('Item and Warehouse', 'Item and Warehouse')], blank=True, null=True, verbose_name='Based On')
    allow_negative_stock = models.BooleanField(default=False, verbose_name="Allow Negative Stock")
    via_landed_cost_voucher = models.BooleanField(default=False, verbose_name="Via Landed Cost Voucher")
    allow_zero_rate = models.BooleanField(default=False, verbose_name="Allow Zero Rate")
    items_to_be_repost = models.TextField(blank=True, null=True, verbose_name="Items to Be Repost")
    current_index = models.IntegerField(default=0, verbose_name="Current Index")
    gl_reposting_index = models.IntegerField(default=0, verbose_name="GL reposting index")
    total_reposting_count = models.IntegerField(default=0, verbose_name="No of Items to Repost")
    recreate_stock_ledgers = models.BooleanField(default=False, verbose_name="Recreate Stock Ledgers")
    reposting_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reposting Reference")
    repost_only_accounting_ledgers = models.BooleanField(default=False, verbose_name="Repost Only Accounting Ledgers")
    total_vouchers = models.IntegerField(default=0, verbose_name="Total Ledgers")
    vouchers_posted = models.IntegerField(default=0, verbose_name="Ledgers Posted")
    reposting_data_file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Reposting Data File")

class RepostItemValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostItemValuation
        fields = '__all__'

class RepostItemValuationViewSet(viewsets.ModelViewSet):
    queryset = RepostItemValuation.objects.all()
    serializer_class = RepostItemValuationSerializer

class QualityInspectionParameter(BaseDocument):
    parameter = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parameter")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    parameter_group = models.ForeignKey('erp_core.QualityInspectionParameterGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parameter Group')

class QualityInspectionParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspectionParameter
        fields = '__all__'

class QualityInspectionParameterViewSet(viewsets.ModelViewSet):
    queryset = QualityInspectionParameter.objects.all()
    serializer_class = QualityInspectionParameterSerializer

class ItemAttribute(BaseDocument):
    attribute_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Attribute Name")
    numeric_values = models.BooleanField(default=False, verbose_name="Numeric Values")
    from_range = models.FloatField(default=0.0, verbose_name="From Range")
    increment = models.FloatField(default=0.0, verbose_name="Increment")
    to_range = models.FloatField(default=0.0, verbose_name="To Range")
    item_attribute_values = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Attribute Values")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class ItemAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAttribute
        fields = '__all__'

class ItemAttributeViewSet(viewsets.ModelViewSet):
    queryset = ItemAttribute.objects.all()
    serializer_class = ItemAttributeSerializer

class DeliveryNoteItem(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    customer_item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Item Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty in Stock UOM")
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    base_price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate (Company Currency)")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")
    discount_percentage = models.FloatField(default=0.0, verbose_name="Discount (%) on Price List Rate with Margin")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    base_rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin (Company Currency)")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty (Warehouse)")
    actual_batch_qty = models.FloatField(default=0.0, verbose_name="Available Batch Qty at From Warehouse")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand Name')
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    against_sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Sales Order')
    against_sales_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Sales Invoice')
    so_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Against Sales Order Item")
    si_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Against Sales Invoice Item")
    installed_qty = models.FloatField(default=0.0, verbose_name="Installed Qty")
    billed_amt = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billed Amt")
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    dn_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Against Delivery Note Item")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty in Stock UOM")
    incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Incoming Rate")
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    grant_commission = models.BooleanField(default=False, verbose_name="Grant Commission")
    pick_list_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pick List Item")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    has_item_scanned = models.BooleanField(default=False, verbose_name="Has Item Scanned")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    packed_qty = models.FloatField(default=0.0, verbose_name="Packed Qty")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    company_total_stock = models.FloatField(default=0.0, verbose_name="Qty (Company)")
    against_pick_list = models.ForeignKey('erp_core.PickList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Pick List')

class DeliveryNoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryNoteItem
        fields = '__all__'

class DeliveryNoteItemViewSet(viewsets.ModelViewSet):
    queryset = DeliveryNoteItem.objects.all()
    serializer_class = DeliveryNoteItemSerializer

class CustomsTariffNumber(BaseDocument):
    tariff_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tariff Number")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")

class CustomsTariffNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomsTariffNumber
        fields = '__all__'

class CustomsTariffNumberViewSet(viewsets.ModelViewSet):
    queryset = CustomsTariffNumber.objects.all()
    serializer_class = CustomsTariffNumberSerializer

class Bin(BaseDocument):
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    reserved_qty = models.FloatField(default=0.0, verbose_name="Reserved Qty")
    actual_qty = models.FloatField(default=0.0, verbose_name="Actual Qty")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")
    indented_qty = models.FloatField(default=0.0, verbose_name="Requested Qty")
    planned_qty = models.FloatField(default=0.0, verbose_name="Planned Qty")
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    reserved_qty_for_production = models.FloatField(default=0.0, verbose_name="Reserved Qty for Production")
    reserved_qty_for_sub_contract = models.FloatField(default=0.0, verbose_name="Reserved Qty for Subcontract")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    valuation_rate = models.FloatField(default=0.0, verbose_name="Valuation Rate")
    stock_value = models.FloatField(default=0.0, verbose_name="Stock Value")
    reserved_qty_for_production_plan = models.FloatField(default=0.0, verbose_name="Reserved Qty for Production Plan")
    reserved_stock = models.FloatField(default=0.0, verbose_name="Reserved Stock")

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = '__all__'

class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer

class LandedCostTaxesandCharges(BaseDocument):
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    has_corrective_cost = models.BooleanField(default=False, verbose_name="Has Corrective Cost")
    has_operating_cost = models.BooleanField(default=False, verbose_name="Has Operating Cost")

class LandedCostTaxesandChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandedCostTaxesandCharges
        fields = '__all__'

class LandedCostTaxesandChargesViewSet(viewsets.ModelViewSet):
    queryset = LandedCostTaxesandCharges.objects.all()
    serializer_class = LandedCostTaxesandChargesSerializer

class StockReconciliationItem(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    current_qty = models.FloatField(default=0.0, verbose_name="Current Qty")
    current_serial_no = models.TextField(blank=True, null=True, verbose_name="Current Serial No")
    current_valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Current Valuation Rate")
    current_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Current Amount")
    quantity_difference = models.TextField(blank=True, null=True, verbose_name="Quantity Difference")
    amount_difference = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount Difference")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    has_item_scanned = models.CharField(max_length=255, blank=True, null=True, verbose_name="Has Item Scanned")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial / Batch Bundle')
    current_serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Current Serial / Batch Bundle')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    reconcile_all_serial_batch = models.BooleanField(default=False, verbose_name="Reconcile All Serial Nos / Batches")

class StockReconciliationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockReconciliationItem
        fields = '__all__'

class StockReconciliationItemViewSet(viewsets.ModelViewSet):
    queryset = StockReconciliationItem.objects.all()
    serializer_class = StockReconciliationItemSerializer

class ItemLeadTime(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    buffer_time = models.IntegerField(default=0, verbose_name="Buffer Time")
    no_of_shift = models.IntegerField(default=0, verbose_name="No of Shift")
    manufacturing_time_in_mins = models.IntegerField(default=0, verbose_name="Manufacturing Time")
    total_workstation_time = models.IntegerField(default=0, verbose_name="Total Workstation Time (In Hours)")
    daily_yield = models.TextField(blank=True, null=True, verbose_name="Daily Yield (%)")
    capacity_per_day = models.IntegerField(default=0, verbose_name="Capacity")
    no_of_units_produced = models.IntegerField(default=0, verbose_name="No of Units Produced")
    purchase_time = models.IntegerField(default=0, verbose_name="Purchase Time")
    shift_time_in_hours = models.IntegerField(default=0, verbose_name="Shift Time (In Hours)")
    no_of_workstations = models.IntegerField(default=0, verbose_name="No of Workstations")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')

class ItemLeadTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLeadTime
        fields = '__all__'

class ItemLeadTimeViewSet(viewsets.ModelViewSet):
    queryset = ItemLeadTime.objects.all()
    serializer_class = ItemLeadTimeSerializer
