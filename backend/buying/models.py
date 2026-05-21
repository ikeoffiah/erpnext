from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class PurchaseOrder(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('PUR-ORD-.YYYY.-', 'PUR-ORD-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    order_confirmation_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Order Confirmation No")
    order_confirmation_date = models.DateField(blank=True, null=True, verbose_name="Order Confirmation Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    customer_contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Contact')
    customer_contact_display = models.TextField(blank=True, null=True, verbose_name="Customer Contact")
    customer_contact_mobile = models.TextField(blank=True, null=True, verbose_name="Customer Mobile No")
    customer_contact_email = models.TextField(blank=True, null=True, verbose_name="Customer Contact Email")
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Contact')
    address_display = models.TextField(blank=True, null=True, verbose_name="Supplier Address Details")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact Name")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Contact Mobile No")
    contact_email = models.TextField(blank=True, null=True, verbose_name="Contact Email")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address Details")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Target Warehouse')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    supplier_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Warehouse')
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Purchase Order Pricing Rule")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total (Company Currency)")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total")
    total_net_weight = models.FloatField(default=0.0, verbose_name="Total Net Weight")
    taxes_and_charges = models.ForeignKey('erp_core.PurchaseTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Taxes and Charges Template')
    shipping_rule = models.ForeignKey('erp_core.ShippingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Rule')
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
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    advance_paid = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Advance Paid (Company Currency)")
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    payment_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Schedule")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('On Hold', 'On Hold'), ('To Receive and Bill', 'To Receive and Bill'), ('To Bill', 'To Bill'), ('To Receive', 'To Receive'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed'), ('Delivered', 'Delivered')], blank=True, null=True, verbose_name='Status')
    ref_sq = models.ForeignKey('erp_core.SupplierQuotation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Quotation')
    party_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Account Currency')
    inter_company_order_reference = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Order Reference')
    per_received = models.TextField(blank=True, null=True, verbose_name="% Received")
    per_billed = models.TextField(blank=True, null=True, verbose_name="% Billed")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Print Language")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    set_reserve_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Reserve Warehouse')
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address Details")
    is_internal_supplier = models.BooleanField(default=False, verbose_name="Is Internal Supplier")
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    set_from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set From Warehouse')
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    advance_payment_status = models.CharField(max_length=255, choices=[('Not Initiated', 'Not Initiated'), ('Initiated', 'Initiated'), ('Partially Paid', 'Partially Paid'), ('Fully Paid', 'Fully Paid')], blank=True, null=True, verbose_name='Advance Payment Status')
    has_unit_price_items = models.BooleanField(default=False, verbose_name="Has Unit Price Items")
    dispatch_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Address')
    dispatch_address_display = models.TextField(blank=True, null=True, verbose_name="Dispatch Address Details")
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    mps = models.ForeignKey('erp_core.MasterProductionSchedule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='MPS')
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    transaction_time = models.TextField(blank=True, null=True, verbose_name="Time")

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class SupplierQuotationItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    supplier_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Part Number")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    lead_time_days = models.IntegerField(default=0, verbose_name="Supplier Lead Time (days)")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    discount_percentage = models.TextField(blank=True, null=True, verbose_name="Discount on Price List Rate (%)")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty as per Stock UOM")
    base_price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate (Company Currency)")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    prevdoc_doctype = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Document Type")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    request_for_quotation = models.ForeignKey('erp_core.RequestforQuotation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Request for Quotation')
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    request_for_quotation_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Request for Quotation Item")
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    expected_delivery_date = models.DateField(blank=True, null=True, verbose_name="Expected Delivery Date")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")

class SupplierQuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierQuotationItem
        fields = '__all__'

class SupplierQuotationItemViewSet(viewsets.ModelViewSet):
    queryset = SupplierQuotationItem.objects.all()
    serializer_class = SupplierQuotationItemSerializer

class BuyingSettings(BaseDocument):
    supp_master_name = models.CharField(max_length=255, choices=[('Supplier Name', 'Supplier Name'), ('Naming Series', 'Naming Series'), ('Auto Name', 'Auto Name')], blank=True, null=True, verbose_name='Supplier Naming By')
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Supplier Group')
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Buying Price List')
    po_required = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Purchase Order required for Purchase Invoice & Receipt creation?')
    pr_required = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Purchase Receipt required for Purchase Invoice creation?')
    maintain_same_rate = models.BooleanField(default=False, verbose_name="Maintain same rate throughout the purchase  cycle")
    allow_multiple_items = models.BooleanField(default=False, verbose_name="Allow Item to be added multiple times in a transaction")
    backflush_raw_materials_of_subcontract_based_on = models.CharField(max_length=255, choices=[('BOM', 'BOM'), ('Material Transferred for Subcontract', 'Material Transferred for Subcontract')], blank=True, null=True, verbose_name='Backflush raw materials of subcontract based on')
    over_transfer_allowance = models.FloatField(default=0.0, verbose_name="Over Transfer Allowance (%)")
    maintain_same_rate_action = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn')], blank=True, null=True, verbose_name='Action if same rate is not maintained')
    role_to_override_stop_action = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role allowed to override stop action')
    bill_for_rejected_quantity_in_purchase_invoice = models.BooleanField(default=False, verbose_name="Bill for rejected quantity in Purchase Invoice")
    disable_last_purchase_rate = models.BooleanField(default=False, verbose_name="Disable last purchase rate")
    show_pay_button = models.BooleanField(default=False, verbose_name="Show pay button in Purchase Order portal")
    set_landed_cost_based_on_purchase_invoice_rate = models.BooleanField(default=False, verbose_name="Set Landed Cost Based on Purchase Invoice Rate")
    use_transaction_date_exchange_rate = models.BooleanField(default=False, verbose_name="Use Transaction Date Exchange Rate")
    blanket_order_allowance = models.FloatField(default=0.0, verbose_name="Blanket Order Allowance (%)")
    auto_create_subcontracting_order = models.BooleanField(default=False, verbose_name="Auto create Subcontracting Order")
    auto_create_purchase_receipt = models.BooleanField(default=False, verbose_name="Auto create Purchase Receipt")
    project_update_frequency = models.CharField(max_length=255, choices=[('Each Transaction', 'Each Transaction'), ('Manual', 'Manual')], blank=True, null=True, verbose_name='How often should project be updated of Total Purchase Cost ?')
    allow_zero_qty_in_purchase_order = models.BooleanField(default=False, verbose_name="Allow Purchase Order with Zero Quantity")
    allow_zero_qty_in_request_for_quotation = models.BooleanField(default=False, verbose_name="Allow Request for Quotation with Zero Quantity")
    allow_zero_qty_in_supplier_quotation = models.BooleanField(default=False, verbose_name="Allow Supplier Quotation with Zero Quantity")
    set_valuation_rate_for_rejected_materials = models.BooleanField(default=False, verbose_name="Set valuation rate for rejected Materials")
    fixed_email = models.ForeignKey('erp_core.EmailAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fixed Outgoing Email Account')
    validate_consumed_qty = models.BooleanField(default=False, verbose_name="Validate consumed quantity (as per BOM)")
    allow_negative_rates_for_items = models.BooleanField(default=False, verbose_name="Allow negative rates for Items")
    naming_series_details = models.TextField(blank=True, null=True, verbose_name="Naming Series options")

class BuyingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingSettings
        fields = '__all__'

class BuyingSettingsViewSet(viewsets.ModelViewSet):
    queryset = BuyingSettings.objects.all()
    serializer_class = BuyingSettingsSerializer

class RequestforQuotationSupplier(BaseDocument):
    send_email = models.BooleanField(default=False, verbose_name="Send Email")
    email_sent = models.BooleanField(default=False, verbose_name="Email Sent")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    contact = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact')
    quote_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Received', 'Received')], blank=True, null=True, verbose_name='Quote Status')
    supplier_name = models.TextField(blank=True, null=True, verbose_name="Supplier Name")
    email_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email ID")

class RequestforQuotationSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestforQuotationSupplier
        fields = '__all__'

class RequestforQuotationSupplierViewSet(viewsets.ModelViewSet):
    queryset = RequestforQuotationSupplier.objects.all()
    serializer_class = RequestforQuotationSupplierSerializer

class SupplierScorecardCriteria(BaseDocument):
    criteria_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Criteria Name")
    max_score = models.FloatField(default=0.0, verbose_name="Max Score")
    formula = models.TextField(blank=True, null=True, verbose_name="Criteria Formula")
    weight = models.TextField(blank=True, null=True, verbose_name="Criteria Weight")

class SupplierScorecardCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardCriteria
        fields = '__all__'

class SupplierScorecardCriteriaViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardCriteria.objects.all()
    serializer_class = SupplierScorecardCriteriaSerializer

class SupplierScorecardStanding(BaseDocument):
    standing_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Standing Name")
    standing_color = models.CharField(max_length=255, choices=[('Blue', 'Blue'), ('Purple', 'Purple'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Red', 'Red')], blank=True, null=True, verbose_name='Color')
    min_grade = models.TextField(blank=True, null=True, verbose_name="Min Grade")
    max_grade = models.TextField(blank=True, null=True, verbose_name="Max Grade")
    warn_rfqs = models.BooleanField(default=False, verbose_name="Warn RFQs")
    warn_pos = models.BooleanField(default=False, verbose_name="Warn Purchase Orders")
    prevent_rfqs = models.BooleanField(default=False, verbose_name="Prevent RFQs")
    prevent_pos = models.BooleanField(default=False, verbose_name="Prevent Purchase Orders")
    notify_supplier = models.BooleanField(default=False, verbose_name="Notify Supplier")
    notify_employee = models.BooleanField(default=False, verbose_name="Notify Other")
    employee_link = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Other')

class SupplierScorecardStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardStanding
        fields = '__all__'

class SupplierScorecardStandingViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardStanding.objects.all()
    serializer_class = SupplierScorecardStandingSerializer

class SupplierQuotation(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('PUR-SQTN-.YYYY.-', 'PUR-SQTN-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Detail")
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
    base_grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total (Company Currency)")
    base_rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment (Company Currency")
    base_in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words (Company Currency)")
    base_rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total (Company Currency)")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms Template')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Print Language")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Stopped', 'Stopped'), ('Cancelled', 'Cancelled'), ('Expired', 'Expired')], blank=True, null=True, verbose_name='Status')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    opportunity = models.ForeignKey('erp_core.Opportunity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity')
    valid_till = models.DateField(blank=True, null=True, verbose_name="Valid Till")
    quotation_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Quotation Number")
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address Details")
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address Details")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    has_unit_price_items = models.BooleanField(default=False, verbose_name="Has Unit Price Items")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")

class SupplierQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierQuotation
        fields = '__all__'

class SupplierQuotationViewSet(viewsets.ModelViewSet):
    queryset = SupplierQuotation.objects.all()
    serializer_class = SupplierQuotationSerializer

class PurchaseOrderItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    supplier_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Part Number")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    expected_delivery_date = models.DateField(blank=True, null=True, verbose_name="Expected Delivery Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    discount_percentage = models.TextField(blank=True, null=True, verbose_name="Discount on Price List Rate (%)")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    last_purchase_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Last Purchase Rate")
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
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    supplier_quotation = models.ForeignKey('erp_core.SupplierQuotation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Quotation')
    supplier_quotation_item = models.ForeignKey('erp_core.SupplierQuotationItem', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Quotation Item')
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="To be Delivered to Customer")
    blanket_order = models.ForeignKey('erp_core.BlanketOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Blanket Order')
    blanket_order_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Blanket Order Rate")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM')
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty in Stock UOM")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    billed_amt = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billed Amount")
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    against_blanket_order = models.BooleanField(default=False, verbose_name="Against Blanket Order")
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    actual_qty = models.FloatField(default=0.0, verbose_name="Available Qty at Target Warehouse")
    company_total_stock = models.FloatField(default=0.0, verbose_name="Available Qty at Company")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")
    base_rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin (Company Currency)")
    production_plan = models.ForeignKey('erp_core.ProductionPlan', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Production Plan')
    production_plan_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan Item")
    production_plan_sub_assembly_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan Sub Assembly Item")
    product_bundle = models.ForeignKey('erp_core.ProductBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Product Bundle')
    sales_order_packed_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Packed Item")
    fg_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good')
    fg_item_qty = models.FloatField(default=0.0, verbose_name="Finished Good Qty")
    from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Warehouse')
    wip_composite_asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP Composite Asset')
    job_card = models.ForeignKey('erp_core.JobCard', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Card')
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    subcontracted_qty = models.FloatField(default=0.0, verbose_name="Subcontracted Quantity")

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

class SupplierScorecard(BaseDocument):
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_score = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Score")
    indicator_color = models.CharField(max_length=255, blank=True, null=True, verbose_name="Indicator Color")
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name="Status")
    period = models.CharField(max_length=255, choices=[('Per Week', 'Per Week'), ('Per Month', 'Per Month'), ('Per Year', 'Per Year')], blank=True, null=True, verbose_name='Evaluation Period')
    weighting_function = models.TextField(blank=True, null=True, verbose_name="Weighting Function")
    standings = models.JSONField(default=list, blank=True, null=True, verbose_name="Scoring Standings")
    criteria = models.JSONField(default=list, blank=True, null=True, verbose_name="Scoring Criteria")
    warn_rfqs = models.BooleanField(default=False, verbose_name="Warn for new Request for Quotations")
    warn_pos = models.BooleanField(default=False, verbose_name="Warn for new Purchase Orders")
    prevent_rfqs = models.BooleanField(default=False, verbose_name="Prevent RFQs")
    prevent_pos = models.BooleanField(default=False, verbose_name="Prevent POs")
    notify_supplier = models.BooleanField(default=False, verbose_name="Notify Supplier")
    notify_employee = models.BooleanField(default=False, verbose_name="Notify Employee")
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')

class SupplierScorecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecard
        fields = '__all__'

class SupplierScorecardViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecard.objects.all()
    serializer_class = SupplierScorecardSerializer

class SupplierScorecardPeriod(BaseDocument):
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    naming_series = models.CharField(max_length=255, choices=[('PU-SSP-.YYYY.-', 'PU-SSP-.YYYY.-')], blank=True, null=True, verbose_name='Naming Series')
    total_score = models.TextField(blank=True, null=True, verbose_name="Period Score")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    criteria = models.JSONField(default=list, blank=True, null=True, verbose_name="Criteria")
    variables = models.JSONField(default=list, blank=True, null=True, verbose_name="Variables")
    scorecard = models.ForeignKey('erp_core.SupplierScorecard', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Scorecard Setup')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class SupplierScorecardPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardPeriod
        fields = '__all__'

class SupplierScorecardPeriodViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardPeriod.objects.all()
    serializer_class = SupplierScorecardPeriodSerializer

class PurchaseReceiptItemSupplied(BaseDocument):
    main_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    rm_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Raw Material Item Code')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    required_qty = models.FloatField(default=0.0, verbose_name="Available Qty For Consumption")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Qty to Be Consumed")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Uom')
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    current_stock = models.FloatField(default=0.0, verbose_name="Current Stock")
    reference_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Name")
    bom_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Detail No")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')

class PurchaseReceiptItemSuppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseReceiptItemSupplied
        fields = '__all__'

class PurchaseReceiptItemSuppliedViewSet(viewsets.ModelViewSet):
    queryset = PurchaseReceiptItemSupplied.objects.all()
    serializer_class = PurchaseReceiptItemSuppliedSerializer

class SupplierScorecardScoringStanding(BaseDocument):
    standing_name = models.ForeignKey('erp_core.SupplierScorecardStanding', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Standing Name')
    standing_color = models.CharField(max_length=255, choices=[('Blue', 'Blue'), ('Purple', 'Purple'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Red', 'Red')], blank=True, null=True, verbose_name='Color')
    min_grade = models.TextField(blank=True, null=True, verbose_name="Min Grade")
    max_grade = models.TextField(blank=True, null=True, verbose_name="Max Grade")
    warn_rfqs = models.BooleanField(default=False, verbose_name="Warn RFQs")
    warn_pos = models.BooleanField(default=False, verbose_name="Warn Purchase Orders")
    prevent_rfqs = models.BooleanField(default=False, verbose_name="Prevent RFQs")
    prevent_pos = models.BooleanField(default=False, verbose_name="Prevent Purchase Orders")
    notify_supplier = models.BooleanField(default=False, verbose_name="Notify Supplier")
    notify_employee = models.BooleanField(default=False, verbose_name="Notify Employee")
    employee_link = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee ')

class SupplierScorecardScoringStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardScoringStanding
        fields = '__all__'

class SupplierScorecardScoringStandingViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardScoringStanding.objects.all()
    serializer_class = SupplierScorecardScoringStandingSerializer

class RequestforQuotation(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('PUR-RFQ-.YYYY.-', 'PUR-RFQ-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    vendor = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    suppliers = models.JSONField(default=list, blank=True, null=True, verbose_name="Suppliers")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    email_template = models.ForeignKey('erp_core.EmailTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Email Template')
    message_for_supplier = models.TextField(blank=True, null=True, verbose_name="Message for Supplier")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    opportunity = models.ForeignKey('erp_core.Opportunity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required Date")
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    send_attached_files = models.BooleanField(default=False, verbose_name="Send Attached Files")
    send_document_print = models.BooleanField(default=False, verbose_name="Send Document Print")
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address Details")
    has_unit_price_items = models.BooleanField(default=False, verbose_name="Has Unit Price Items")
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")
    mfs_html = models.TextField(blank=True, null=True, verbose_name="Message for Supplier")
    use_html = models.BooleanField(default=False, verbose_name="Use HTML")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Shipping Address')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address Details")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

class RequestforQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestforQuotation
        fields = '__all__'

class RequestforQuotationViewSet(viewsets.ModelViewSet):
    queryset = RequestforQuotation.objects.all()
    serializer_class = RequestforQuotationSerializer

class SupplierScorecardScoringVariable(BaseDocument):
    variable_label = models.ForeignKey('erp_core.SupplierScorecardVariable', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Variable Name')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    value = models.FloatField(default=0.0, verbose_name="Value")
    param_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parameter Name")
    path = models.CharField(max_length=255, blank=True, null=True, verbose_name="Path")

class SupplierScorecardScoringVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardScoringVariable
        fields = '__all__'

class SupplierScorecardScoringVariableViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardScoringVariable.objects.all()
    serializer_class = SupplierScorecardScoringVariableSerializer

class RequestforQuotationItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    supplier_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Part No")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required Date")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    project_name = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty as per Stock UOM")

class RequestforQuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestforQuotationItem
        fields = '__all__'

class RequestforQuotationItemViewSet(viewsets.ModelViewSet):
    queryset = RequestforQuotationItem.objects.all()
    serializer_class = RequestforQuotationItemSerializer

class CustomerNumberAtSupplier(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    customer_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Number")

class CustomerNumberAtSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerNumberAtSupplier
        fields = '__all__'

class CustomerNumberAtSupplierViewSet(viewsets.ModelViewSet):
    queryset = CustomerNumberAtSupplier.objects.all()
    serializer_class = CustomerNumberAtSupplierSerializer

class SupplierScorecardScoringCriteria(BaseDocument):
    criteria_name = models.ForeignKey('erp_core.SupplierScorecardCriteria', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Criteria Name')
    score = models.TextField(blank=True, null=True, verbose_name="Score")
    weight = models.TextField(blank=True, null=True, verbose_name="Criteria Weight")
    max_score = models.FloatField(default=0.0, verbose_name="Max Score")
    formula = models.TextField(blank=True, null=True, verbose_name="Criteria Formula")

class SupplierScorecardScoringCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardScoringCriteria
        fields = '__all__'

class SupplierScorecardScoringCriteriaViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardScoringCriteria.objects.all()
    serializer_class = SupplierScorecardScoringCriteriaSerializer

class SupplierScorecardVariable(BaseDocument):
    variable_label = models.CharField(max_length=255, blank=True, null=True, verbose_name="Variable Name")
    is_custom = models.BooleanField(default=False, verbose_name="Custom?")
    param_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parameter Name")
    path = models.CharField(max_length=255, blank=True, null=True, verbose_name="Path")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class SupplierScorecardVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierScorecardVariable
        fields = '__all__'

class SupplierScorecardVariableViewSet(viewsets.ModelViewSet):
    queryset = SupplierScorecardVariable.objects.all()
    serializer_class = SupplierScorecardVariableSerializer

class Supplier(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('SUP-.YYYY.-', 'SUP-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')
    default_bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Company Bank Account')
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax ID")
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    is_transporter = models.BooleanField(default=False, verbose_name="Is Transporter")
    is_internal_supplier = models.BooleanField(default=False, verbose_name="Is Internal Supplier")
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')
    supplier_type = models.CharField(max_length=255, choices=[('Company', 'Company'), ('Individual', 'Individual'), ('Partnership', 'Partnership')], blank=True, null=True, verbose_name='Supplier Type')
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    warn_rfqs = models.BooleanField(default=False, verbose_name="Warn RFQs")
    warn_pos = models.BooleanField(default=False, verbose_name="Warn POs")
    prevent_rfqs = models.BooleanField(default=False, verbose_name="Prevent RFQs")
    prevent_pos = models.BooleanField(default=False, verbose_name="Prevent POs")
    companies = models.JSONField(default=list, blank=True, null=True, verbose_name="Allowed To Transact With")
    default_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Billing Currency')
    default_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    payment_terms = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payment Terms Template')
    on_hold = models.BooleanField(default=False, verbose_name="Block Supplier")
    hold_type = models.CharField(max_length=255, choices=[('All', 'All'), ('Invoices', 'Invoices'), ('Payments', 'Payments')], blank=True, null=True, verbose_name='Hold Type')
    release_date = models.DateField(blank=True, null=True, verbose_name="Release Date")
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    supplier_details = models.TextField(blank=True, null=True, verbose_name="Supplier Details")
    is_frozen = models.BooleanField(default=False, verbose_name="Is Frozen")
    allow_purchase_invoice_creation_without_purchase_order = models.BooleanField(default=False, verbose_name="Allow Purchase Invoice Creation Without Purchase Order")
    allow_purchase_invoice_creation_without_purchase_receipt = models.BooleanField(default=False, verbose_name="Allow Purchase Invoice Creation Without Purchase Receipt")
    supplier_primary_contact = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Primary Contact')
    mobile_no = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    email_id = models.TextField(blank=True, null=True, verbose_name="Email Id")
    primary_address = models.TextField(blank=True, null=True, verbose_name="Primary Address")
    supplier_primary_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Primary Address')
    portal_users = models.JSONField(default=list, blank=True, null=True, verbose_name="Supplier Portal Users")
    customer_numbers = models.JSONField(default=list, blank=True, null=True, verbose_name="Customer Numbers")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')
    gender = models.ForeignKey('erp_core.Gender', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gender')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
