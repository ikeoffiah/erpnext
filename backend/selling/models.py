from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class Quotation(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('SAL-QTN-.YYYY.-', 'SAL-QTN-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    quotation_to = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quotation To')
    party_name = models.TextField(blank=True, null=True, verbose_name="Party")
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    valid_till = models.DateField(blank=True, null=True, verbose_name="Valid Till")
    order_type = models.CharField(max_length=255, choices=[('Sales', 'Sales'), ('Maintenance', 'Maintenance'), ('Shopping Cart', 'Shopping Cart')], blank=True, null=True, verbose_name='Order Type')
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    shipping_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address')
    shipping_address = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
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
    taxes_and_charges = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Taxes and Charges")
    other_charges_calculation = models.TextField(blank=True, null=True, verbose_name="Taxes and Charges Calculation")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    coupon_code = models.ForeignKey('erp_core.CouponCode', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Coupon Code')
    referral_sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Referral Sales Partner')
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
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    payment_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Schedule")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Term Details")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    order_lost_reason = models.TextField(blank=True, null=True, verbose_name="Detailed Reason")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Replied', 'Replied'), ('Partially Ordered', 'Partially Ordered'), ('Ordered', 'Ordered'), ('Lost', 'Lost'), ('Cancelled', 'Cancelled'), ('Expired', 'Expired')], blank=True, null=True, verbose_name='Status')
    enq_det = models.TextField(blank=True, null=True, verbose_name="Opportunity Item")
    supplier_quotation = models.ForeignKey('erp_core.SupplierQuotation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Quotation')
    opportunity = models.ForeignKey('erp_core.Opportunity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity')
    lost_reasons = models.TextField(blank=True, null=True, verbose_name="Lost Reasons")
    packed_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Bundle Items")
    competitors = models.TextField(blank=True, null=True, verbose_name="Competitors")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address Name')
    company_address_display = models.TextField(blank=True, null=True, verbose_name="Company Address")
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    company_contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Contact Person')
    has_unit_price_items = models.BooleanField(default=False, verbose_name="Has Unit Price Items")
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'

class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class Customer(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('CUST-.YYYY.-', 'CUST-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    gender = models.ForeignKey('erp_core.Gender', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gender')
    customer_type = models.CharField(max_length=255, choices=[('Company', 'Company'), ('Individual', 'Individual'), ('Partnership', 'Partnership')], blank=True, null=True, verbose_name='Customer Type')
    default_bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Company Bank Account')
    lead_name = models.ForeignKey('erp_core.Lead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Lead')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    account_manager = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Manager')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax ID")
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    is_internal_customer = models.BooleanField(default=False, verbose_name="Is Internal Customer")
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    companies = models.JSONField(default=list, blank=True, null=True, verbose_name="Allowed To Transact With")
    default_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Billing Currency')
    default_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Price List')
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    customer_primary_contact = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Primary Contact')
    mobile_no = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    email_id = models.TextField(blank=True, null=True, verbose_name="Email Id")
    customer_primary_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Primary Address')
    primary_address = models.TextField(blank=True, null=True, verbose_name="Primary Address")
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    payment_terms = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payment Terms Template')
    customer_details = models.TextField(blank=True, null=True, verbose_name="Customer Details")
    market_segment = models.ForeignKey('erp_core.MarketSegment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Market Segment')
    industry = models.ForeignKey('erp_core.IndustryType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Industry')
    is_frozen = models.BooleanField(default=False, verbose_name="Is Frozen")
    loyalty_program = models.ForeignKey('erp_core.LoyaltyProgram', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Loyalty Program')
    loyalty_program_tier = models.CharField(max_length=255, blank=True, null=True, verbose_name="Loyalty Program Tier")
    default_sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    default_commission_rate = models.FloatField(default=0.0, verbose_name="Commission Rate")
    sales_team = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Team")
    customer_pos_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer POS ID")
    credit_limits = models.JSONField(default=list, blank=True, null=True, verbose_name="Credit Limit")
    so_required = models.BooleanField(default=False, verbose_name="Allow Sales Invoice Creation Without Sales Order")
    dn_required = models.BooleanField(default=False, verbose_name="Allow Sales Invoice Creation Without Delivery Note")
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    opportunity_name = models.ForeignKey('erp_core.Opportunity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity')
    portal_users = models.JSONField(default=list, blank=True, null=True, verbose_name="Customer Portal Users")
    prospect_name = models.ForeignKey('erp_core.Prospect', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Prospect')
    first_name = models.TextField(blank=True, null=True, verbose_name="First Name")
    last_name = models.TextField(blank=True, null=True, verbose_name="Last Name")
    supplier_numbers = models.JSONField(default=list, blank=True, null=True, verbose_name="Supplier Numbers")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SalesOrderItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    customer_item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Item Code")
    ensure_delivery_based_on_produced_serial_no = models.BooleanField(default=False, verbose_name="Ensure Delivery Based on Produced Serial No")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Delivery Date")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty as per Stock UOM")
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    base_price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate (Company Currency)")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")
    discount_percentage = models.TextField(blank=True, null=True, verbose_name="Discount (%) on Price List Rate with Margin")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    base_rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin (Company Currency)")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Basic Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="Supplier delivers to Customer")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Warehouse (Optional)')
    prevdoc_docname = models.ForeignKey('erp_core.Quotation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quotation')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand Name')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    billed_amt = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billed Amt")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    gross_profit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Gross Profit")
    blanket_order = models.ForeignKey('erp_core.BlanketOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Blanket Order')
    blanket_order_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Blanket Order Rate")
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty (Warehouse)")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    work_order_qty = models.FloatField(default=0.0, verbose_name="Work Order Qty")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    planned_qty = models.FloatField(default=0.0, verbose_name="Planned Quantity")
    produced_qty = models.FloatField(default=0.0, verbose_name="Produced Quantity")
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Sales Order Date")
    additional_notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")
    against_blanket_order = models.BooleanField(default=False, verbose_name="Against Blanket Order")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    grant_commission = models.BooleanField(default=False, verbose_name="Grant Commission")
    picked_qty = models.FloatField(default=0.0, verbose_name="Picked Qty (in Stock UOM)")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    quotation_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="quotation_item")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    reserve_stock = models.BooleanField(default=False, verbose_name="Reserve Stock")
    stock_reserved_qty = models.FloatField(default=0.0, verbose_name="Stock Reserved Qty (in Stock UOM)")
    production_plan_qty = models.FloatField(default=0.0, verbose_name="Production Plan Qty")
    is_stock_item = models.BooleanField(default=False, verbose_name="Is Stock Item")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    company_total_stock = models.FloatField(default=0.0, verbose_name="Qty (Company)")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    subcontracted_qty = models.FloatField(default=0.0, verbose_name="Subcontracted Quantity")
    fg_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good')
    fg_item_qty = models.FloatField(default=0.0, verbose_name="Finished Good Qty")
    requested_qty = models.FloatField(default=0.0, verbose_name="Requested Qty")

class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = '__all__'

class SalesOrderItemViewSet(viewsets.ModelViewSet):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemSerializer

class InstallationNoteItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    qty = models.FloatField(default=0.0, verbose_name="Installed Qty")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    prevdoc_detail_docname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Against Document Detail No")
    prevdoc_docname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Against Document No")
    prevdoc_doctype = models.CharField(max_length=255, blank=True, null=True, verbose_name="Document Type")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')

class InstallationNoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallationNoteItem
        fields = '__all__'

class InstallationNoteItemViewSet(viewsets.ModelViewSet):
    queryset = InstallationNoteItem.objects.all()
    serializer_class = InstallationNoteItemSerializer

class SalesTeam(BaseDocument):
    sales_person = models.ForeignKey('erp_core.SalesPerson', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Person')
    contact_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact No.")
    allocated_percentage = models.FloatField(default=0.0, verbose_name="Contribution (%)")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Contribution to Net Total")
    commission_rate = models.CharField(max_length=255, blank=True, null=True, verbose_name="Commission Rate")
    incentives = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Incentives")

class SalesTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTeam
        fields = '__all__'

class SalesTeamViewSet(viewsets.ModelViewSet):
    queryset = SalesTeam.objects.all()
    serializer_class = SalesTeamSerializer

class SupplierNumberAtCustomer(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    supplier_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Number")

class SupplierNumberAtCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierNumberAtCustomer
        fields = '__all__'

class SupplierNumberAtCustomerViewSet(viewsets.ModelViewSet):
    queryset = SupplierNumberAtCustomer.objects.all()
    serializer_class = SupplierNumberAtCustomerSerializer

class InstallationNote(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-INS-.YYYY.-', 'MAT-INS-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    inst_date = models.DateField(blank=True, null=True, verbose_name="Installation Date")
    inst_time = models.TextField(blank=True, null=True, verbose_name="Installation Time")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')

class InstallationNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallationNote
        fields = '__all__'

class InstallationNoteViewSet(viewsets.ModelViewSet):
    queryset = InstallationNote.objects.all()
    serializer_class = InstallationNoteSerializer

class ProductBundle(BaseDocument):
    new_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Item')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class ProductBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBundle
        fields = '__all__'

class ProductBundleViewSet(viewsets.ModelViewSet):
    queryset = ProductBundle.objects.all()
    serializer_class = ProductBundleSerializer

class ProductBundleItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    rate = models.FloatField(default=0.0, verbose_name="Rate")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class ProductBundleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBundleItem
        fields = '__all__'

class ProductBundleItemViewSet(viewsets.ModelViewSet):
    queryset = ProductBundleItem.objects.all()
    serializer_class = ProductBundleItemSerializer

class PartySpecificItem(BaseDocument):
    party_type = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Supplier', 'Supplier')], blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party Name")
    restrict_based_on = models.CharField(max_length=255, choices=[('Item', 'Item'), ('Item Group', 'Item Group'), ('Brand', 'Brand')], blank=True, null=True, verbose_name='Restrict Items Based On')
    based_on_value = models.TextField(blank=True, null=True, verbose_name="Based On Value")

class PartySpecificItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartySpecificItem
        fields = '__all__'

class PartySpecificItemViewSet(viewsets.ModelViewSet):
    queryset = PartySpecificItem.objects.all()
    serializer_class = PartySpecificItemSerializer

class SalesOrder(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('SAL-ORD-.YYYY.-', 'SAL-ORD-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    order_type = models.CharField(max_length=255, choices=[('Sales', 'Sales'), ('Maintenance', 'Maintenance'), ('Shopping Cart', 'Shopping Cart')], blank=True, null=True, verbose_name='Order Type')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Delivery Date")
    po_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Purchase Order")
    po_date = models.DateField(blank=True, null=True, verbose_name="Customer's Purchase Order Date")
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax Id")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    company_address_display = models.TextField(blank=True, null=True, verbose_name="Company Address")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address Name')
    shipping_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address Name')
    shipping_address = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Source Warehouse')
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
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
    taxes_and_charges = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Taxes and Charges")
    other_charges_calculation = models.TextField(blank=True, null=True, verbose_name="Taxes and Charges Calculation")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    loyalty_points = models.IntegerField(default=0, verbose_name="Loyalty Points")
    loyalty_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Loyalty Amount")
    coupon_code = models.ForeignKey('erp_core.CouponCode', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Coupon Code')
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Additional Discount On')
    base_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount")
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
    advance_paid = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Advance Paid")
    packed_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Packed Items")
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    payment_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Schedule")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions Details")
    inter_company_order_reference = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Order Reference')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    party_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Account Currency')
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('On Hold', 'On Hold'), ('To Pay', 'To Pay'), ('To Deliver and Bill', 'To Deliver and Bill'), ('To Bill', 'To Bill'), ('To Deliver', 'To Deliver'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    delivery_status = models.CharField(max_length=255, choices=[('Not Delivered', 'Not Delivered'), ('Fully Delivered', 'Fully Delivered'), ('Partly Delivered', 'Partly Delivered'), ('Closed', 'Closed'), ('Not Applicable', 'Not Applicable')], blank=True, null=True, verbose_name='Delivery Status')
    per_delivered = models.TextField(blank=True, null=True, verbose_name="%  Delivered")
    per_billed = models.TextField(blank=True, null=True, verbose_name="% Amount Billed")
    billing_status = models.CharField(max_length=255, choices=[('Not Billed', 'Not Billed'), ('Fully Billed', 'Fully Billed'), ('Partly Billed', 'Partly Billed'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Billing Status')
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    commission_rate = models.FloatField(default=0.0, verbose_name="Commission Rate")
    total_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Commission")
    sales_team = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Team")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    contact_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone")
    skip_delivery_note = models.BooleanField(default=False, verbose_name="Skip Delivery Note")
    is_internal_customer = models.BooleanField(default=False, verbose_name="Is Internal Customer")
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    dispatch_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Address Name')
    dispatch_address = models.TextField(blank=True, null=True, verbose_name="Dispatch Address")
    amount_eligible_for_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount Eligible for Commission")
    per_picked = models.TextField(blank=True, null=True, verbose_name="% Picked")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    reserve_stock = models.BooleanField(default=False, verbose_name="Reserve Stock")
    advance_payment_status = models.CharField(max_length=255, choices=[('Not Requested', 'Not Requested'), ('Requested', 'Requested'), ('Partially Paid', 'Partially Paid'), ('Fully Paid', 'Fully Paid')], blank=True, null=True, verbose_name='Advance Payment Status')
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    company_contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Contact Person')
    has_unit_price_items = models.BooleanField(default=False, verbose_name="Has Unit Price Items")
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    transaction_time = models.TextField(blank=True, null=True, verbose_name="Time")
    ignore_default_payment_terms_template = models.BooleanField(default=False, verbose_name="Ignore Default Payment Terms Template")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'

class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

class IndustryType(BaseDocument):
    industry = models.CharField(max_length=255, blank=True, null=True, verbose_name="Industry")

class IndustryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryType
        fields = '__all__'

class IndustryTypeViewSet(viewsets.ModelViewSet):
    queryset = IndustryType.objects.all()
    serializer_class = IndustryTypeSerializer

class DeliveryScheduleItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Stock Qty")
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Delivery Date")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')

class DeliveryScheduleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryScheduleItem
        fields = '__all__'

class DeliveryScheduleItemViewSet(viewsets.ModelViewSet):
    queryset = DeliveryScheduleItem.objects.all()
    serializer_class = DeliveryScheduleItemSerializer

class SMSCenter(BaseDocument):
    send_to = models.CharField(max_length=255, choices=[('All Contact', 'All Contact'), ('All Customer Contact', 'All Customer Contact'), ('All Supplier Contact', 'All Supplier Contact'), ('All Sales Partner Contact', 'All Sales Partner Contact'), ('All Lead (Open)', 'All Lead (Open)'), ('All Employee (Active)', 'All Employee (Active)'), ('All Sales Person', 'All Sales Person')], blank=True, null=True, verbose_name='Send To')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    branch = models.ForeignKey('erp_core.Branch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Branch')
    receiver_list = models.TextField(blank=True, null=True, verbose_name="Receiver List")
    message = models.TextField(blank=True, null=True, verbose_name="Message")
    total_characters = models.IntegerField(default=0, verbose_name="Total Characters")
    total_messages = models.IntegerField(default=0, verbose_name="Total Message(s)")

class SMSCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSCenter
        fields = '__all__'

class SMSCenterViewSet(viewsets.ModelViewSet):
    queryset = SMSCenter.objects.all()
    serializer_class = SMSCenterSerializer

class SellingSettings(BaseDocument):
    cust_master_name = models.CharField(max_length=255, choices=[('Customer Name', 'Customer Name'), ('Naming Series', 'Naming Series'), ('Auto Name', 'Auto Name')], blank=True, null=True, verbose_name='Customer Naming By')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Territory')
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Price List')
    so_required = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Sales Order required to create Sales Invoice/Delivery Note?')
    dn_required = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Delivery Note required to create Sales Invoice?')
    sales_update_frequency = models.CharField(max_length=255, choices=[('Monthly', 'Monthly'), ('Each Transaction', 'Each Transaction'), ('Daily', 'Daily')], blank=True, null=True, verbose_name='How often should sales data be updated in Company/Project?')
    maintain_same_sales_rate = models.BooleanField(default=False, verbose_name="Maintain same rate throughout sales cycle")
    editable_price_list_rate = models.BooleanField(default=False, verbose_name="Allow editing Price List rate in transactions")
    allow_multiple_items = models.BooleanField(default=False, verbose_name="Allow same Item to be added multiple times in a transaction")
    allow_against_multiple_purchase_orders = models.BooleanField(default=False, verbose_name="Allow multiple Sales Orders against a customer's Purchase Order")
    validate_selling_price = models.BooleanField(default=False, verbose_name="Validate selling price for Item against purchase or valuation rate")
    hide_tax_id = models.BooleanField(default=False, verbose_name="Hide Customer's Tax ID from sales transactions")
    maintain_same_rate_action = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn')], blank=True, null=True, verbose_name='Action if same rate is not maintained throughout sales cycle')
    role_to_override_stop_action = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role allowed to override stop action')
    editable_bundle_item_rates = models.BooleanField(default=False, verbose_name="Calculate Product Bundle price based on child Item's rates")
    enable_discount_accounting = models.BooleanField(default=False, verbose_name="Enable discount accounting for selling")
    allow_sales_order_creation_for_expired_quotation = models.BooleanField(default=False, verbose_name="Allow Sales Order creation for expired Quotation")
    dont_reserve_sales_order_qty_on_sales_return = models.BooleanField(default=False, verbose_name="Don't reserve Sales Order qty on sales return")
    allow_negative_rates_for_items = models.BooleanField(default=False, verbose_name="Allow negative rates for Items")
    blanket_order_allowance = models.FloatField(default=0.0, verbose_name="Blanket Order Allowance (%)")
    enable_cutoff_date_on_bulk_delivery_note_creation = models.BooleanField(default=False, verbose_name="Enable cut-off date on creating bulk Delivery Notes")
    allow_zero_qty_in_sales_order = models.BooleanField(default=False, verbose_name="Allow Sales Order with zero quantity")
    allow_zero_qty_in_quotation = models.BooleanField(default=False, verbose_name="Allow Quotation with zero quantity")
    allow_delivery_of_overproduced_qty = models.BooleanField(default=False, verbose_name="Allow delivery of overproduced quantity")
    fallback_to_default_price_list = models.BooleanField(default=False, verbose_name="Use prices from Default Price List as fallback")
    use_legacy_js_reactivity = models.BooleanField(default=False, verbose_name="Use Legacy (Client side) Reactivity")
    set_zero_rate_for_expired_batch = models.BooleanField(default=False, verbose_name="Set incoming rate as zero for expired Batch")
    enable_tracking_sales_commissions = models.BooleanField(default=False, verbose_name="Enable tracking sales commissions")
    enable_utm = models.BooleanField(default=False, verbose_name="Enable UTM")
    deliver_secondary_items = models.BooleanField(default=False, verbose_name="Deliver secondary Items")
    naming_series_details = models.TextField(blank=True, null=True, verbose_name="Naming Series options")

class SellingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingSettings
        fields = '__all__'

class SellingSettingsViewSet(viewsets.ModelViewSet):
    queryset = SellingSettings.objects.all()
    serializer_class = SellingSettingsSerializer

class SalesPartnerType(BaseDocument):
    sales_partner_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Partner Type")

class SalesPartnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPartnerType
        fields = '__all__'

class SalesPartnerTypeViewSet(viewsets.ModelViewSet):
    queryset = SalesPartnerType.objects.all()
    serializer_class = SalesPartnerTypeSerializer

class CustomerCreditLimit(BaseDocument):
    credit_limit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Limit")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    bypass_credit_limit_check = models.BooleanField(default=False, verbose_name="Bypass Credit Limit Check at Sales Order")

class CustomerCreditLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCreditLimit
        fields = '__all__'

class CustomerCreditLimitViewSet(viewsets.ModelViewSet):
    queryset = CustomerCreditLimit.objects.all()
    serializer_class = CustomerCreditLimitSerializer

class QuotationItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    customer_item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Item Code")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty as per Stock UOM")
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    base_price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate (Company Currency)")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")
    discount_percentage = models.TextField(blank=True, null=True, verbose_name="Discount (%) on Price List Rate with Margin")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    base_rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin (Company Currency)")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty (Warehouse)")
    prevdoc_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Doctype')
    prevdoc_docname = models.TextField(blank=True, null=True, verbose_name="Against Docname")
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    additional_notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")
    blanket_order = models.ForeignKey('erp_core.BlanketOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Blanket Order')
    blanket_order_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Blanket Order Rate")
    against_blanket_order = models.BooleanField(default=False, verbose_name="Against Blanket Order")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    gross_profit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Gross Profit")
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    is_alternative = models.BooleanField(default=False, verbose_name="Is Alternative")
    has_alternative_item = models.BooleanField(default=False, verbose_name="Has Alternative Item")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    company_total_stock = models.FloatField(default=0.0, verbose_name="Qty (Company)")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")

class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItem
        fields = '__all__'

class QuotationItemViewSet(viewsets.ModelViewSet):
    queryset = QuotationItem.objects.all()
    serializer_class = QuotationItemSerializer
