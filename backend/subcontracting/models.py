from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class SubcontractingInwardOrderReceivedItem(BaseDocument):
    main_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    rm_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Raw Material Item Code')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    bom_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Detail No")
    reference_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Name")
    required_qty = models.FloatField(default=0.0, verbose_name="Required Qty")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Consumed Qty")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    work_order_qty = models.FloatField(default=0.0, verbose_name="Work Order Qty")
    is_customer_provided_item = models.BooleanField(default=False, verbose_name="Is Customer Provided Item")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    billed_qty = models.FloatField(default=0.0, verbose_name="Billed Qty")
    is_additional_item = models.BooleanField(default=False, verbose_name="Is Additional Item")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")

class SubcontractingInwardOrderReceivedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingInwardOrderReceivedItem
        fields = '__all__'

class SubcontractingInwardOrderReceivedItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingInwardOrderReceivedItem.objects.all()
    serializer_class = SubcontractingInwardOrderReceivedItemSerializer

class SubcontractingOrderItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    expected_delivery_date = models.DateField(blank=True, null=True, verbose_name="Expected Delivery Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM')
    include_exploded_items = models.BooleanField(default=False, verbose_name="Include Exploded Items")
    service_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Service Cost Per Qty")
    additional_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Cost Per Qty")
    rm_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Material Cost Per Qty")
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    job_card = models.ForeignKey('erp_core.JobCard', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Card')
    subcontracting_conversion_factor = models.FloatField(default=0.0, verbose_name="Subcontracting Conversion Factor")
    production_plan_sub_assembly_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan Sub Assembly Item")

class SubcontractingOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingOrderItem
        fields = '__all__'

class SubcontractingOrderItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingOrderItem.objects.all()
    serializer_class = SubcontractingOrderItemSerializer

class SubcontractingReceipt(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('MAT-SCR-.YYYY.-', 'MAT-SCR-.YYYY.-'), ('MAT-SCR-RET-.YYYY.-', 'MAT-SCR-RET-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Worker Name")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Job Worker Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.TextField(blank=True, null=True, verbose_name="Contact Email")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Shipping Address')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accepted Warehouse')
    rejected_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Warehouse')
    supplier_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker Warehouse')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    supplied_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Consumed Items")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    bill_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bill No")
    bill_date = models.DateField(blank=True, null=True, verbose_name="Bill Date")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Completed', 'Completed'), ('Return', 'Return'), ('Return Issued', 'Return Issued'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    range = models.CharField(max_length=255, blank=True, null=True, verbose_name="Range")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Print Language")
    instructions = models.TextField(blank=True, null=True, verbose_name="Instructions")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    transporter_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Transporter Name")
    lr_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Vehicle Number")
    lr_date = models.DateField(blank=True, null=True, verbose_name="Vehicle Date")
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address")
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    is_return = models.BooleanField(default=False, verbose_name="Is Return")
    return_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against Subcontracting Receipt')
    per_returned = models.TextField(blank=True, null=True, verbose_name="% Returned")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    distribute_additional_costs_based_on = models.CharField(max_length=255, choices=[('Qty', 'Qty'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Distribute Additional Costs Based On ')
    additional_costs = models.JSONField(default=list, blank=True, null=True, verbose_name="Additional Costs")
    total_additional_costs = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Additional Costs")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    supplier_delivery_note = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Worker Delivery Note")

class SubcontractingReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingReceipt
        fields = '__all__'

class SubcontractingReceiptViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingReceipt.objects.all()
    serializer_class = SubcontractingReceiptSerializer

class SubcontractingInwardOrder(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('SCI-ORD-.YYYY.-', 'SCI-ORD-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Sales Order')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    service_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Service Items")
    received_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Required Items")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Ongoing', 'Ongoing'), ('Produced', 'Produced'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    per_delivered = models.TextField(blank=True, null=True, verbose_name="% Delivered")
    per_produced = models.TextField(blank=True, null=True, verbose_name="% Produced")
    per_process_loss = models.TextField(blank=True, null=True, verbose_name="% Process Loss")
    set_delivery_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Delivery Warehouse')
    customer_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Warehouse')
    per_returned = models.TextField(blank=True, null=True, verbose_name="% Returned")
    per_raw_material_returned = models.TextField(blank=True, null=True, verbose_name="% Raw Material Returned")
    per_raw_material_received = models.TextField(blank=True, null=True, verbose_name="% Raw Material Received")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Currency')
    secondary_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Secondary Items")

class SubcontractingInwardOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingInwardOrder
        fields = '__all__'

class SubcontractingInwardOrderViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingInwardOrder.objects.all()
    serializer_class = SubcontractingInwardOrderSerializer

class SubcontractingInwardOrderItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM')
    include_exploded_items = models.BooleanField(default=False, verbose_name="Include Exploded Items")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    subcontracting_conversion_factor = models.FloatField(default=0.0, verbose_name="Subcontracting Conversion Factor")
    produced_qty = models.FloatField(default=0.0, verbose_name="Produced Qty")
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")
    delivery_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Warehouse')

class SubcontractingInwardOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingInwardOrderItem
        fields = '__all__'

class SubcontractingInwardOrderItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingInwardOrderItem.objects.all()
    serializer_class = SubcontractingInwardOrderItemSerializer

class SubcontractingOrderServiceItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    fg_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good Item')
    fg_item_qty = models.FloatField(default=0.0, verbose_name="Finished Good Item Quantity")
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")

class SubcontractingOrderServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingOrderServiceItem
        fields = '__all__'

class SubcontractingOrderServiceItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingOrderServiceItem.objects.all()
    serializer_class = SubcontractingOrderServiceItemSerializer

class SubcontractingBOM(BaseDocument):
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    finished_good = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good')
    finished_good_qty = models.FloatField(default=0.0, verbose_name="Finished Good Qty")
    finished_good_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good BOM')
    service_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Service Item')
    service_item_qty = models.FloatField(default=0.0, verbose_name="Service Item Qty")
    service_item_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Service Item UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    finished_good_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good UOM')

class SubcontractingBOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingBOM
        fields = '__all__'

class SubcontractingBOMViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingBOM.objects.all()
    serializer_class = SubcontractingBOMSerializer

class SubcontractingInwardOrderSecondaryItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    reference_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Name")
    produced_qty = models.FloatField(default=0.0, verbose_name="Produced Qty")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    fg_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good Item Code')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    type = models.CharField(max_length=255, choices=[('Co-Product', 'Co-Product'), ('By-Product', 'By-Product'), ('Scrap', 'Scrap'), ('Additional Finished Good', 'Additional Finished Good')], blank=True, null=True, verbose_name='Type')

class SubcontractingInwardOrderSecondaryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingInwardOrderSecondaryItem
        fields = '__all__'

class SubcontractingInwardOrderSecondaryItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingInwardOrderSecondaryItem.objects.all()
    serializer_class = SubcontractingInwardOrderSecondaryItemSerializer

class SubcontractingOrder(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('SC-ORD-.YYYY.-', 'SC-ORD-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Purchase Order')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Worker Name")
    supplier_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker Warehouse')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Date")
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Job Worker Address Details")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker Contact')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact Name")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Contact Mobile No")
    contact_email = models.TextField(blank=True, null=True, verbose_name="Contact Email")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Shipping Address')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address Details")
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address Details")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Target Warehouse')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    service_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Service Items")
    set_reserve_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Reserve Warehouse')
    supplied_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Supplied Items")
    additional_costs = models.JSONField(default=list, blank=True, null=True, verbose_name="Additional Costs")
    total_additional_costs = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Additional Costs")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Partially Received', 'Partially Received'), ('Completed', 'Completed'), ('Material Transferred', 'Material Transferred'), ('Partial Material Transferred', 'Partial Material Transferred'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    per_received = models.TextField(blank=True, null=True, verbose_name="% Received")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    distribute_additional_costs_based_on = models.CharField(max_length=255, choices=[('Qty', 'Qty'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Distribute Additional Costs Based On ')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    supplier_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Worker Currency')
    reserve_stock = models.BooleanField(default=False, verbose_name="Reserve Stock")
    production_plan = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan")

class SubcontractingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingOrder
        fields = '__all__'

class SubcontractingOrderViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingOrder.objects.all()
    serializer_class = SubcontractingOrderSerializer

class SubcontractingReceiptSuppliedItem(BaseDocument):
    main_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    rm_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Raw Material Item Code')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    required_qty = models.FloatField(default=0.0, verbose_name="Required Qty")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Consumed Qty")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    current_stock = models.FloatField(default=0.0, verbose_name="Current Stock")
    reference_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Name")
    bom_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Detail No")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    subcontracting_order = models.ForeignKey('erp_core.SubcontractingOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Order')
    available_qty_for_consumption = models.FloatField(default=0.0, verbose_name="Available Qty For Consumption")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial / Batch Bundle')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')

class SubcontractingReceiptSuppliedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingReceiptSuppliedItem
        fields = '__all__'

class SubcontractingReceiptSuppliedItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingReceiptSuppliedItem.objects.all()
    serializer_class = SubcontractingReceiptSuppliedItemSerializer

class SubcontractingInwardOrderServiceItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    fg_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good Item')
    fg_item_qty = models.FloatField(default=0.0, verbose_name="Finished Good Item Quantity")
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class SubcontractingInwardOrderServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingInwardOrderServiceItem
        fields = '__all__'

class SubcontractingInwardOrderServiceItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingInwardOrderServiceItem.objects.all()
    serializer_class = SubcontractingInwardOrderServiceItemSerializer

class SubcontractingReceiptItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    received_qty = models.FloatField(default=0.0, verbose_name="Qty (As per BOM)")
    qty = models.FloatField(default=0.0, verbose_name="Accepted Qty")
    rejected_qty = models.FloatField(default=0.0, verbose_name="Rejected Qty")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    rm_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Material Cost Per Qty")
    service_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Service Cost Per Qty")
    additional_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Cost Per Qty")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accepted Warehouse')
    rejected_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Warehouse')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    subcontracting_order = models.ForeignKey('erp_core.SubcontractingOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Order')
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    rejected_serial_no = models.TextField(blank=True, null=True, verbose_name="Rejected Serial No")
    subcontracting_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subcontracting Order Item")
    bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    rm_supp_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Materials Supplied Cost")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    subcontracting_receipt_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subcontracting Receipt Item")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    rejected_serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Serial and Batch Bundle')
    reference_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Name")
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    include_exploded_items = models.BooleanField(default=False, verbose_name="Include Exploded Items")
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    job_card = models.ForeignKey('erp_core.JobCard', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Job Card')
    landed_cost_voucher_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Landed Cost Voucher Amount")
    service_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Service Expense Account')
    type = models.CharField(max_length=255, choices=[('Co-Product', 'Co-Product'), ('By-Product', 'By-Product'), ('Scrap', 'Scrap'), ('Additional Finished Good', 'Additional Finished Good')], blank=True, null=True, verbose_name='Type')
    secondary_items_cost_per_qty = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Secondary Items Cost Per Qty")
    is_legacy_scrap_item = models.BooleanField(default=False, verbose_name="Is Legacy Scrap Item")
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")

class SubcontractingReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingReceiptItem
        fields = '__all__'

class SubcontractingReceiptItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingReceiptItem.objects.all()
    serializer_class = SubcontractingReceiptItemSerializer

class SubcontractingOrderSuppliedItem(BaseDocument):
    main_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    rm_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Raw Material Item Code')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    reserve_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reserve Warehouse')
    bom_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Detail No")
    reference_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Name")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    required_qty = models.FloatField(default=0.0, verbose_name="Required Qty")
    supplied_qty = models.FloatField(default=0.0, verbose_name="Supplied Qty")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Consumed Qty")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty")
    total_supplied_qty = models.FloatField(default=0.0, verbose_name="Total Supplied Qty")
    stock_reserved_qty = models.FloatField(default=0.0, verbose_name="Reserved Qty")

class SubcontractingOrderSuppliedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractingOrderSuppliedItem
        fields = '__all__'

class SubcontractingOrderSuppliedItemViewSet(viewsets.ModelViewSet):
    queryset = SubcontractingOrderSuppliedItem.objects.all()
    serializer_class = SubcontractingOrderSuppliedItemSerializer
