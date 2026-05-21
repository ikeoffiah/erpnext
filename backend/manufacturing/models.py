from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class BOMOperation(BaseDocument):
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    workstation = models.ForeignKey('erp_core.Workstation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    hour_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Hour Rate")
    time_in_mins = models.FloatField(default=0.0, verbose_name="Operation Time")
    fixed_time = models.BooleanField(default=False, verbose_name="Fixed Time")
    operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Operating Cost")
    base_hour_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Hour Rate(Company Currency)")
    base_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Operating Cost(Company Currency)")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    batch_size = models.IntegerField(default=0, verbose_name="Batch Size")
    sequence_id = models.IntegerField(default=0, verbose_name="Sequence ID")
    cost_per_unit = models.FloatField(default=0.0, verbose_name="Cost Per Unit")
    base_cost_per_unit = models.FloatField(default=0.0, verbose_name="Base Cost Per Unit")
    set_cost_based_on_bom_qty = models.BooleanField(default=False, verbose_name="Set Operating Cost Based On BOM Quantity")
    workstation_type = models.ForeignKey('erp_core.WorkstationType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation Type')
    finished_good = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='FG / Semi FG Item')
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    finished_good_qty = models.FloatField(default=0.0, verbose_name="Qty to Produce")
    is_final_finished_good = models.BooleanField(default=False, verbose_name="Is Final Finished Good")
    wip_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP Warehouse')
    fg_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Goods Warehouse')
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    skip_material_transfer = models.BooleanField(default=False, verbose_name=" Skip Material Transfer")
    backflush_from_wip_warehouse = models.BooleanField(default=False, verbose_name="Backflush Materials From WIP Warehouse")
    quality_inspection_required = models.BooleanField(default=False, verbose_name="Quality Inspection Required")

class BOMOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMOperation
        fields = '__all__'

class BOMOperationViewSet(viewsets.ModelViewSet):
    queryset = BOMOperation.objects.all()
    serializer_class = BOMOperationSerializer

class JobCardOperation(BaseDocument):
    status = models.CharField(max_length=255, choices=[('Complete', 'Complete'), ('Pause', 'Pause'), ('Pending', 'Pending'), ('Work In Progress', 'Work In Progress')], blank=True, null=True, verbose_name='Status')
    completed_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Completed Time")
    sub_operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    completed_qty = models.FloatField(default=0.0, verbose_name="Completed Qty")

class JobCardOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCardOperation
        fields = '__all__'

class JobCardOperationViewSet(viewsets.ModelViewSet):
    queryset = JobCardOperation.objects.all()
    serializer_class = JobCardOperationSerializer

class ProductionPlan(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MFG-PP-.YYYY.-', 'MFG-PP-.YYYY.-')], blank=True, null=True, verbose_name='Naming Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    get_items_from = models.CharField(max_length=255, choices=[('Sales Order', 'Sales Order'), ('Material Request', 'Material Request')], blank=True, null=True, verbose_name='Get Items From')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    sales_orders = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Orders")
    material_requests = models.JSONField(default=list, blank=True, null=True, verbose_name="Material Requests")
    po_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Assembly Items")
    include_non_stock_items = models.BooleanField(default=False, verbose_name="Include Non Stock Items")
    include_subcontracted_items = models.BooleanField(default=False, verbose_name="Include Subcontracted Items")
    ignore_existing_ordered_qty = models.BooleanField(default=False, verbose_name="Consider Projected Qty in Calculation (RM)")
    mr_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Raw Materials")
    total_planned_qty = models.FloatField(default=0.0, verbose_name="Total Planned Qty")
    total_produced_qty = models.FloatField(default=0.0, verbose_name="Total Produced Qty")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Not Started', 'Not Started'), ('In Process', 'In Process'), ('Completed', 'Completed'), ('Closed', 'Closed'), ('Cancelled', 'Cancelled'), ('Material Requested', 'Material Requested')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    for_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Warehouse')
    warehouses = models.TextField(blank=True, null=True, verbose_name="Warehouses")
    sales_order_status = models.CharField(max_length=255, choices=[('To Deliver and Bill', 'To Deliver and Bill'), ('To Bill', 'To Bill'), ('To Deliver', 'To Deliver')], blank=True, null=True, verbose_name='Sales Order Status')
    include_safety_stock = models.BooleanField(default=False, verbose_name="Include Safety Stock in Required Qty Calculation")
    combine_items = models.BooleanField(default=False, verbose_name="Consolidate Sales Order Items")
    prod_plan_references = models.JSONField(default=list, blank=True, null=True, verbose_name="Production Plan Item Reference")
    sub_assembly_items = models.JSONField(default=list, blank=True, null=True, verbose_name="sub_assembly_items")
    from_delivery_date = models.DateField(blank=True, null=True, verbose_name="From Delivery Date")
    to_delivery_date = models.DateField(blank=True, null=True, verbose_name="To Delivery Date")
    combine_sub_items = models.BooleanField(default=False, verbose_name="Consolidate Sub Assembly Items")
    skip_available_sub_assembly_item = models.BooleanField(default=False, verbose_name="Consider Projected Qty in Calculation")
    sub_assembly_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sub Assembly Warehouse')
    consider_minimum_order_qty = models.BooleanField(default=False, verbose_name="Consider Minimum Order Qty")
    reserve_stock = models.BooleanField(default=False, verbose_name="Reserve Stock")

class ProductionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlan
        fields = '__all__'

class ProductionPlanViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlan.objects.all()
    serializer_class = ProductionPlanSerializer

class ProductionPlanItem(BaseDocument):
    include_exploded_items = models.BooleanField(default=False, verbose_name="Include Exploded Items")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    planned_qty = models.FloatField(default=0.0, verbose_name="Planned Qty")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Goods Warehouse')
    planned_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Planned Start Date")
    pending_qty = models.FloatField(default=0.0, verbose_name="Pending Qty")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")
    produced_qty = models.FloatField(default=0.0, verbose_name="Produced Qty")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="material_request_item")
    product_bundle_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Product Bundle Item')
    item_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Reference")
    temporary_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="temporary name")

class ProductionPlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlanItem
        fields = '__all__'

class ProductionPlanItemViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlanItem.objects.all()
    serializer_class = ProductionPlanItemSerializer

class JobCardScheduledTime(BaseDocument):
    from_time = models.DateTimeField(blank=True, null=True, verbose_name="From Time")
    to_time = models.DateTimeField(blank=True, null=True, verbose_name="To Time")
    time_in_mins = models.FloatField(default=0.0, verbose_name="Time (In Mins)")

class JobCardScheduledTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCardScheduledTime
        fields = '__all__'

class JobCardScheduledTimeViewSet(viewsets.ModelViewSet):
    queryset = JobCardScheduledTime.objects.all()
    serializer_class = JobCardScheduledTimeSerializer

class JobCardItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    required_qty = models.FloatField(default=0.0, verbose_name="Required Qty")
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    transferred_qty = models.FloatField(default=0.0, verbose_name="Transferred Qty")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Consumed Qty")

class JobCardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCardItem
        fields = '__all__'

class JobCardItemViewSet(viewsets.ModelViewSet):
    queryset = JobCardItem.objects.all()
    serializer_class = JobCardItemSerializer

class JobCardTimeLog(BaseDocument):
    from_time = models.DateTimeField(blank=True, null=True, verbose_name="From Time")
    to_time = models.DateTimeField(blank=True, null=True, verbose_name="To Time")
    time_in_mins = models.FloatField(default=0.0, verbose_name="Time In Mins")
    completed_qty = models.FloatField(default=0.0, verbose_name="Completed Qty")
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sub Operation')

class JobCardTimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCardTimeLog
        fields = '__all__'

class JobCardTimeLogViewSet(viewsets.ModelViewSet):
    queryset = JobCardTimeLog.objects.all()
    serializer_class = JobCardTimeLogSerializer

class SalesForecast(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('SF.YY.-.######', 'SF.YY.-.######')], blank=True, null=True, verbose_name='Naming Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    selected_items = models.TextField(blank=True, null=True, verbose_name="Select Items")
    parent_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Warehouse')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    demand_number = models.IntegerField(default=0, verbose_name="Number of Weeks / Months")
    status = models.CharField(max_length=255, choices=[('Planned', 'Planned'), ('MPS Generated', 'MPS Generated'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    frequency = models.CharField(max_length=255, choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly')], blank=True, null=True, verbose_name='Frequency')

class SalesForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesForecast
        fields = '__all__'

class SalesForecastViewSet(viewsets.ModelViewSet):
    queryset = SalesForecast.objects.all()
    serializer_class = SalesForecastSerializer

class WorkstationOperatingComponent(BaseDocument):
    component_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Component Name")
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Component Expense Account")

class WorkstationOperatingComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkstationOperatingComponent
        fields = '__all__'

class WorkstationOperatingComponentViewSet(viewsets.ModelViewSet):
    queryset = WorkstationOperatingComponent.objects.all()
    serializer_class = WorkstationOperatingComponentSerializer

class BOMCreatorItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    fg_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Goods Item')
    is_expandable = models.BooleanField(default=False, verbose_name="Is Expandable")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    stock_qty = models.FloatField(default=0.0, verbose_name="Stock Qty")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    do_not_explode = models.BooleanField(default=False, verbose_name="Do Not Explode")
    instruction = models.TextField(blank=True, null=True, verbose_name="Instruction")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Rate")
    sourced_by_supplier = models.BooleanField(default=False, verbose_name="Sourced by Supplier")
    fg_reference_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Finished Goods Reference")
    parent_row_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parent Row No")
    bom_created = models.BooleanField(default=False, verbose_name="BOM Created")
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    is_phantom_item = models.BooleanField(default=False, verbose_name="Is Phantom Item")

class BOMCreatorItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMCreatorItem
        fields = '__all__'

class BOMCreatorItemViewSet(viewsets.ModelViewSet):
    queryset = BOMCreatorItem.objects.all()
    serializer_class = BOMCreatorItemSerializer

class PlantFloor(BaseDocument):
    floor_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Floor Name")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class PlantFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantFloor
        fields = '__all__'

class PlantFloorViewSet(viewsets.ModelViewSet):
    queryset = PlantFloor.objects.all()
    serializer_class = PlantFloorSerializer

class ProductionPlanMaterialRequest(BaseDocument):
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_date = models.DateField(blank=True, null=True, verbose_name="Material Request Date")

class ProductionPlanMaterialRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlanMaterialRequest
        fields = '__all__'

class ProductionPlanMaterialRequestViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlanMaterialRequest.objects.all()
    serializer_class = ProductionPlanMaterialRequestSerializer

class WorkstationCost(BaseDocument):
    operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Operating Cost")
    operating_component = models.ForeignKey('erp_core.WorkstationOperatingComponent', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operating Component')

class WorkstationCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkstationCost
        fields = '__all__'

class WorkstationCostViewSet(viewsets.ModelViewSet):
    queryset = WorkstationCost.objects.all()
    serializer_class = WorkstationCostSerializer

class BOMSecondaryItem(BaseDocument):
    type = models.CharField(max_length=255, choices=[('Co-Product', 'Co-Product'), ('By-Product', 'By-Product'), ('Scrap', 'Scrap'), ('Additional Finished Good', 'Additional Finished Good')], blank=True, null=True, verbose_name='Type')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Cost")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    stock_qty = models.FloatField(default=0.0, verbose_name="Stock Qty")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    cost_allocation_per = models.TextField(blank=True, null=True, verbose_name="Cost Allocation %")
    process_loss_per = models.TextField(blank=True, null=True, verbose_name="Process Loss %")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image_nygv = models.TextField(blank=True, null=True, verbose_name="image_nygv")
    base_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Cost (Company Currency)")
    is_legacy = models.BooleanField(default=False, verbose_name="Is Legacy")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")

class BOMSecondaryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMSecondaryItem
        fields = '__all__'

class BOMSecondaryItemViewSet(viewsets.ModelViewSet):
    queryset = BOMSecondaryItem.objects.all()
    serializer_class = BOMSecondaryItemSerializer

class ManufacturingSettings(BaseDocument):
    allow_overtime = models.BooleanField(default=False, verbose_name="Allow Overtime")
    allow_production_on_holidays = models.BooleanField(default=False, verbose_name="Allow Production on Holidays")
    capacity_planning_for_days = models.IntegerField(default=0, verbose_name="Capacity Planning For (Days)")
    mins_between_operations = models.IntegerField(default=0, verbose_name="Time Between Operations (Mins)")
    overproduction_percentage_for_sales_order = models.TextField(blank=True, null=True, verbose_name="Overproduction Percentage For Sales Order")
    overproduction_percentage_for_work_order = models.TextField(blank=True, null=True, verbose_name="Overproduction Percentage For Work Order")
    backflush_raw_materials_based_on = models.CharField(max_length=255, choices=[('BOM', 'BOM'), ('Material Transferred for Manufacture', 'Material Transferred for Manufacture')], blank=True, null=True, verbose_name='Backflush Raw Materials Based On')
    material_consumption = models.BooleanField(default=False, verbose_name="Allow Continuous Material Consumption")
    update_bom_costs_automatically = models.BooleanField(default=False, verbose_name="Update BOM Cost Automatically")
    disable_capacity_planning = models.BooleanField(default=False, verbose_name="Disable Capacity Planning")
    make_serial_no_batch_from_work_order = models.BooleanField(default=False, verbose_name="Make Serial No / Batch from Work Order")
    add_corrective_operation_cost_in_finished_good_valuation = models.BooleanField(default=False, verbose_name="Add Corrective Operation Cost in Finished Good Valuation")
    job_card_excess_transfer = models.BooleanField(default=False, verbose_name="Allow Excess Material Transfer")
    get_rm_cost_from_consumption_entry = models.BooleanField(default=False, verbose_name="Get Raw Materials Cost from Consumption Entry")
    validate_components_quantities_per_bom = models.BooleanField(default=False, verbose_name="Validate Components and Quantities Per BOM")
    enforce_time_logs = models.BooleanField(default=False, verbose_name="Enforce Time Logs")
    transfer_extra_materials_percentage = models.TextField(blank=True, null=True, verbose_name="Transfer Extra Raw Materials to WIP (%)")
    allow_editing_of_items_and_quantities_in_work_order = models.BooleanField(default=False, verbose_name="Allow Editing of Items and Quantities in Work Order")
    set_op_cost_and_secondary_items_from_sub_assemblies = models.BooleanField(default=False, verbose_name="Set Operating Cost / Secondary Items From Sub-assemblies")

class ManufacturingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturingSettings
        fields = '__all__'

class ManufacturingSettingsViewSet(viewsets.ModelViewSet):
    queryset = ManufacturingSettings.objects.all()
    serializer_class = ManufacturingSettingsSerializer

class WorkOrderItem(BaseDocument):
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    required_qty = models.FloatField(default=0.0, verbose_name="Required Qty")
    transferred_qty = models.FloatField(default=0.0, verbose_name="Transferred Qty")
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    include_item_in_manufacturing = models.BooleanField(default=False, verbose_name="Include Item In Manufacturing")
    consumed_qty = models.FloatField(default=0.0, verbose_name="Consumed Qty")
    available_qty_at_source_warehouse = models.FloatField(default=0.0, verbose_name="Available Qty at Source Warehouse")
    available_qty_at_wip_warehouse = models.FloatField(default=0.0, verbose_name="Available Qty at WIP Warehouse")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    returned_qty = models.FloatField(default=0.0, verbose_name="Returned Qty ")
    operation_row_id = models.IntegerField(default=0, verbose_name="Operation Row Id")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    stock_reserved_qty = models.FloatField(default=0.0, verbose_name="Stock Reserved Qty")
    is_additional_item = models.BooleanField(default=False, verbose_name="Is Additional Item")
    voucher_detail_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail Reference")
    is_customer_provided_item = models.BooleanField(default=False, verbose_name="Is Customer Provided Item")

class WorkOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderItem
        fields = '__all__'

class WorkOrderItemViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderItem.objects.all()
    serializer_class = WorkOrderItemSerializer

class ProductionPlanSubAssemblyItem(BaseDocument):
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    qty = models.FloatField(default=0.0, verbose_name="Qty to Order")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    production_plan_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan Item")
    parent_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good')
    bom_level = models.IntegerField(default=0, verbose_name="Level (BOM)")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    description = models.TextField(blank=True, null=True, verbose_name="description")
    production_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sub Assembly Item Code')
    indent = models.IntegerField(default=0, verbose_name="Indent")
    fg_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    type_of_manufacturing = models.CharField(max_length=255, choices=[('In House', 'In House'), ('Subcontract', 'Subcontract'), ('Material Request', 'Material Request')], blank=True, null=True, verbose_name='Manufacturing Type')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    schedule_date = models.DateTimeField(blank=True, null=True, verbose_name="Schedule Date")
    actual_qty = models.FloatField(default=0.0, verbose_name="Actual Qty")
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    wo_produced_qty = models.FloatField(default=0.0, verbose_name="Produced Qty")
    required_qty = models.FloatField(default=0.0, verbose_name="Required Qty")
    stock_reserved_qty = models.FloatField(default=0.0, verbose_name="Stock Reserved Qty")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")

class ProductionPlanSubAssemblyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlanSubAssemblyItem
        fields = '__all__'

class ProductionPlanSubAssemblyItemViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlanSubAssemblyItem.objects.all()
    serializer_class = ProductionPlanSubAssemblyItemSerializer

class Routing(BaseDocument):
    routing_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Routing Name")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    operations = models.JSONField(default=list, blank=True, null=True, verbose_name="BOM Operation")

class RoutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routing
        fields = '__all__'

class RoutingViewSet(viewsets.ModelViewSet):
    queryset = Routing.objects.all()
    serializer_class = RoutingSerializer

class MasterProductionScheduleItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Delivery Date")
    planned_qty = models.FloatField(default=0.0, verbose_name="Planned Qty")
    order_release_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    cumulative_lead_time = models.IntegerField(default=0, verbose_name="Lead Time")

class MasterProductionScheduleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProductionScheduleItem
        fields = '__all__'

class MasterProductionScheduleItemViewSet(viewsets.ModelViewSet):
    queryset = MasterProductionScheduleItem.objects.all()
    serializer_class = MasterProductionScheduleItemSerializer

class DowntimeEntry(BaseDocument):
    workstation = models.ForeignKey('erp_core.Workstation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation / Machine')
    from_time = models.DateTimeField(blank=True, null=True, verbose_name="From Time")
    to_time = models.DateTimeField(blank=True, null=True, verbose_name="To Time")
    operator = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operator')
    downtime = models.FloatField(default=0.0, verbose_name="Downtime")
    stop_reason = models.CharField(max_length=255, choices=[('Excessive machine set up time', 'Excessive machine set up time'), ('Unplanned machine maintenance', 'Unplanned machine maintenance'), ('On-machine press checks', 'On-machine press checks'), ('Machine operator errors', 'Machine operator errors'), ('Machine malfunction', 'Machine malfunction'), ('Electricity down', 'Electricity down'), ('Other', 'Other')], blank=True, null=True, verbose_name='Stop Reason')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    naming_series = models.CharField(max_length=255, choices=[('DT-', 'DT-')], blank=True, null=True, verbose_name='Naming Series')

class DowntimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DowntimeEntry
        fields = '__all__'

class DowntimeEntryViewSet(viewsets.ModelViewSet):
    queryset = DowntimeEntry.objects.all()
    serializer_class = DowntimeEntrySerializer

class BOMExplosionItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    stock_qty = models.FloatField(default=0.0, verbose_name="Stock Qty")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    qty_consumed_per_unit = models.FloatField(default=0.0, verbose_name="Qty Consumed Per Unit")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    include_item_in_manufacturing = models.BooleanField(default=False, verbose_name="Include Item In Manufacturing")
    sourced_by_supplier = models.BooleanField(default=False, verbose_name="Sourced by Supplier")
    is_sub_assembly_item = models.BooleanField(default=False, verbose_name="Is Sub Assembly Item")

class BOMExplosionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMExplosionItem
        fields = '__all__'

class BOMExplosionItemViewSet(viewsets.ModelViewSet):
    queryset = BOMExplosionItem.objects.all()
    serializer_class = BOMExplosionItemSerializer

class JobCardSecondaryItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Secondary Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Secondary Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    stock_qty = models.FloatField(default=0.0, verbose_name="Qty")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    type = models.CharField(max_length=255, choices=[('Co-Product', 'Co-Product'), ('By-Product', 'By-Product'), ('Scrap', 'Scrap'), ('Additional Finished Good', 'Additional Finished Good')], blank=True, null=True, verbose_name='Type')
    bom_secondary_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Secondary Item Reference")

class JobCardSecondaryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCardSecondaryItem
        fields = '__all__'

class JobCardSecondaryItemViewSet(viewsets.ModelViewSet):
    queryset = JobCardSecondaryItem.objects.all()
    serializer_class = JobCardSecondaryItemSerializer

class SalesForecastItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Delivery Date")
    forecast_qty = models.FloatField(default=0.0, verbose_name="Forecast Qty")
    adjust_qty = models.FloatField(default=0.0, verbose_name="Adjust Qty")
    demand_qty = models.FloatField(default=0.0, verbose_name="Demand Qty")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')

class SalesForecastItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesForecastItem
        fields = '__all__'

class SalesForecastItemViewSet(viewsets.ModelViewSet):
    queryset = SalesForecastItem.objects.all()
    serializer_class = SalesForecastItemSerializer

class BOMWebsiteItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Item Description")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    website_image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")

class BOMWebsiteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMWebsiteItem
        fields = '__all__'

class BOMWebsiteItemViewSet(viewsets.ModelViewSet):
    queryset = BOMWebsiteItem.objects.all()
    serializer_class = BOMWebsiteItemSerializer

class ProductionPlanSalesOrder(BaseDocument):
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    sales_order_date = models.DateField(blank=True, null=True, verbose_name="Sales Order Date")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name="Status")

class ProductionPlanSalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlanSalesOrder
        fields = '__all__'

class ProductionPlanSalesOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlanSalesOrder.objects.all()
    serializer_class = ProductionPlanSalesOrderSerializer

class ProductionPlanItemReference(BaseDocument):
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order Reference')
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    item_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Reference")

class ProductionPlanItemReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlanItemReference
        fields = '__all__'

class ProductionPlanItemReferenceViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlanItemReference.objects.all()
    serializer_class = ProductionPlanItemReferenceSerializer

class BlanketOrder(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MFG-BLR-.YYYY.-', 'MFG-BLR-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    blanket_order_type = models.CharField(max_length=255, choices=[('Selling', 'Selling'), ('Purchasing', 'Purchasing')], blank=True, null=True, verbose_name='Order Type')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Item")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions Details")
    order_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Order No")
    order_date = models.DateField(blank=True, null=True, verbose_name="Order Date")

class BlanketOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlanketOrder
        fields = '__all__'

class BlanketOrderViewSet(viewsets.ModelViewSet):
    queryset = BlanketOrder.objects.all()
    serializer_class = BlanketOrderSerializer

class BlanketOrderItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Quantity")
    terms_and_conditions = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    party_item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Item Code")

class BlanketOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlanketOrderItem
        fields = '__all__'

class BlanketOrderItemViewSet(viewsets.ModelViewSet):
    queryset = BlanketOrderItem.objects.all()
    serializer_class = BlanketOrderItemSerializer

class WorkOrder(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MFG-WO-.YYYY.-', 'MFG-WO-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Not Started', 'Not Started'), ('In Process', 'In Process'), ('Stock Reserved', 'Stock Reserved'), ('Stock Partially Reserved', 'Stock Partially Reserved'), ('Completed', 'Completed'), ('Stopped', 'Stopped'), ('Closed', 'Closed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    production_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item To Manufacture')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    use_multi_level_bom = models.BooleanField(default=False, verbose_name="Use Multi-Level BOM")
    skip_transfer = models.BooleanField(default=False, verbose_name="Skip Material Transfer to WIP Warehouse")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    qty = models.FloatField(default=0.0, verbose_name="Qty To Manufacture")
    material_transferred_for_manufacturing = models.FloatField(default=0.0, verbose_name="Material Transferred for Manufacturing")
    produced_qty = models.FloatField(default=0.0, verbose_name="Manufactured Qty")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    from_wip_warehouse = models.BooleanField(default=False, verbose_name="Backflush Raw Materials From Work-in-Progress Warehouse")
    wip_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Work-in-Progress Warehouse')
    fg_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    scrap_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Scrap Warehouse')
    required_items = models.JSONField(default=list, blank=True, null=True, verbose_name="required_items")
    planned_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Planned Start Date")
    actual_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Actual Start Date")
    planned_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Planned End Date")
    actual_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Actual End Date")
    expected_delivery_date = models.DateField(blank=True, null=True, verbose_name="Expected Delivery Date")
    transfer_material_against = models.CharField(max_length=255, choices=[('Work Order', 'Work Order'), ('Job Card', 'Job Card')], blank=True, null=True, verbose_name='Transfer Material Against')
    operations = models.JSONField(default=list, blank=True, null=True, verbose_name="Operations")
    planned_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Planned Operating Cost")
    actual_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Actual Operating Cost")
    additional_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Operating Cost")
    total_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Operating Cost")
    description = models.TextField(blank=True, null=True, verbose_name="Item Description")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    sales_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    production_plan = models.ForeignKey('erp_core.ProductionPlan', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Production Plan')
    production_plan_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan Item")
    product_bundle_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Product Bundle Item')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    update_consumed_material_cost_in_project = models.BooleanField(default=False, verbose_name="Update Consumed Material Cost In Project")
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    lead_time = models.FloatField(default=0.0, verbose_name="Lead Time")
    has_serial_no = models.BooleanField(default=False, verbose_name="Has Serial No")
    has_batch_no = models.BooleanField(default=False, verbose_name="Has Batch No")
    batch_size = models.FloatField(default=0.0, verbose_name="Batch Size")
    corrective_operation_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Corrective Operation Cost")
    production_plan_sub_assembly_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Production Plan Sub Assembly Item")
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")
    track_semi_finished_goods = models.BooleanField(default=False, verbose_name="Track Semi Finished Goods")
    reserve_stock = models.BooleanField(default=False, verbose_name="Reserve Stock")
    disassembled_qty = models.FloatField(default=0.0, verbose_name="Disassembled Qty")
    mps = models.ForeignKey('erp_core.MasterProductionSchedule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='MPS')
    additional_transferred_qty = models.FloatField(default=0.0, verbose_name="Additional Transferred Qty")
    subcontracting_inward_order = models.ForeignKey('erp_core.SubcontractingInwardOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subcontracting Inward Order')
    subcontracting_inward_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subcontracting Inward Order Item")
    max_producible_qty = models.FloatField(default=0.0, verbose_name="Max Producible Qty")

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class BOMUpdateBatch(BaseDocument):
    level = models.IntegerField(default=0, verbose_name="Level")
    batch_no = models.IntegerField(default=0, verbose_name="Batch No.")
    boms_updated = models.TextField(blank=True, null=True, verbose_name="BOMs Updated")
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')

class BOMUpdateBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMUpdateBatch
        fields = '__all__'

class BOMUpdateBatchViewSet(viewsets.ModelViewSet):
    queryset = BOMUpdateBatch.objects.all()
    serializer_class = BOMUpdateBatchSerializer

class BOMUpdateTool(BaseDocument):
    current_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Current BOM')
    new_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='New BOM')

class BOMUpdateToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMUpdateTool
        fields = '__all__'

class BOMUpdateToolViewSet(viewsets.ModelViewSet):
    queryset = BOMUpdateTool.objects.all()
    serializer_class = BOMUpdateToolSerializer

class WorkstationType(BaseDocument):
    workstation_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Workstation Type")
    hour_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Hour Rate")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    workstation_costs = models.JSONField(default=list, blank=True, null=True, verbose_name="Operating Components Cost")

class WorkstationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkstationType
        fields = '__all__'

class WorkstationTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkstationType.objects.all()
    serializer_class = WorkstationTypeSerializer

class BOMWebsiteOperation(BaseDocument):
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    workstation = models.ForeignKey('erp_core.Workstation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation')
    time_in_mins = models.FloatField(default=0.0, verbose_name="Operation Time")
    website_image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    thumbnail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Thumbnail")

class BOMWebsiteOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMWebsiteOperation
        fields = '__all__'

class BOMWebsiteOperationViewSet(viewsets.ModelViewSet):
    queryset = BOMWebsiteOperation.objects.all()
    serializer_class = BOMWebsiteOperationSerializer

class SubOperation(BaseDocument):
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    time_in_mins = models.FloatField(default=0.0, verbose_name="Operation Time")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class SubOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOperation
        fields = '__all__'

class SubOperationViewSet(viewsets.ModelViewSet):
    queryset = SubOperation.objects.all()
    serializer_class = SubOperationSerializer

class BOMItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item operation')
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No')
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    description = models.TextField(blank=True, null=True, verbose_name="Item Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    stock_qty = models.FloatField(default=0.0, verbose_name="Stock Qty")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Basic Rate (Company Currency)")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    qty_consumed_per_unit = models.FloatField(default=0.0, verbose_name="Qty Consumed Per Unit")
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    include_item_in_manufacturing = models.BooleanField(default=False, verbose_name="Include Item In Manufacturing")
    original_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Original Item')
    has_variants = models.BooleanField(default=False, verbose_name="Has Variants")
    sourced_by_supplier = models.BooleanField(default=False, verbose_name="Sourced by Supplier")
    do_not_explode = models.BooleanField(default=False, verbose_name="Do Not Explode")
    is_stock_item = models.BooleanField(default=False, verbose_name="Is Stock Item")
    operation_row_id = models.IntegerField(default=0, verbose_name="Operation ID")
    is_sub_assembly_item = models.BooleanField(default=False, verbose_name="Is Sub Assembly Item")
    is_phantom_item = models.BooleanField(default=False, verbose_name="Is Phantom Item")

class BOMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItem
        fields = '__all__'

class BOMItemViewSet(viewsets.ModelViewSet):
    queryset = BOMItem.objects.all()
    serializer_class = BOMItemSerializer

class BOM(BaseDocument):
    item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item to Manufacture')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Unit Of Measure')
    quantity = models.FloatField(default=0.0, verbose_name="Quantity (Output Qty)")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    is_default = models.BooleanField(default=False, verbose_name="Is Default")
    with_operations = models.BooleanField(default=False, verbose_name="With Operations")
    inspection_required = models.BooleanField(default=False, verbose_name="Quality Inspection Required")
    allow_alternative_item = models.BooleanField(default=False, verbose_name="Allow Alternative Item")
    set_rate_of_sub_assembly_item_based_on_bom = models.BooleanField(default=False, verbose_name="Set rate of sub-assembly item based on BOM")
    quality_inspection_template = models.ForeignKey('erp_core.QualityInspectionTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection Template')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transfer_material_against = models.CharField(max_length=255, choices=[('Work Order', 'Work Order'), ('Job Card', 'Job Card')], blank=True, null=True, verbose_name='Transfer Material Against')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Conversion Rate")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    rm_cost_as_per = models.CharField(max_length=255, choices=[('Valuation Rate', 'Valuation Rate'), ('Last Purchase Rate', 'Last Purchase Rate'), ('Price List', 'Price List')], blank=True, null=True, verbose_name='Rate Of Materials Based On')
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    routing = models.ForeignKey('erp_core.Routing', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Routing')
    operations = models.JSONField(default=list, blank=True, null=True, verbose_name="Operations")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Components")
    operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Operating Cost")
    raw_material_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Material Cost")
    base_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Operating Cost (Company Currency)")
    base_raw_material_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Material Cost (Company Currency)")
    total_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Cost")
    base_total_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Cost (Company Currency)")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    description = models.TextField(blank=True, null=True, verbose_name="Item Description")
    exploded_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Exploded Items")
    show_in_website = models.BooleanField(default=False, verbose_name="Show in Website")
    route = models.TextField(blank=True, null=True, verbose_name="Route")
    website_image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Website Image")
    thumbnail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Thumbnail")
    web_long_description = models.TextField(blank=True, null=True, verbose_name="Website Description")
    show_items = models.BooleanField(default=False, verbose_name="Show Items")
    show_operations = models.BooleanField(default=False, verbose_name="Show Operations")
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    has_variants = models.BooleanField(default=False, verbose_name="Has Variants")
    process_loss_percentage = models.TextField(blank=True, null=True, verbose_name="% Process Loss")
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")
    fg_based_operating_cost = models.BooleanField(default=False, verbose_name="Finished Goods based Operating Cost")
    operating_cost_per_bom_quantity = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Operating Cost Per BOM Quantity")
    bom_creator = models.ForeignKey('erp_core.BOMCreator', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM Creator')
    bom_creator_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="BOM Creator Item")
    track_semi_finished_goods = models.BooleanField(default=False, verbose_name="Track Semi Finished Goods")
    default_source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Source Warehouse')
    default_target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Target Warehouse')
    is_phantom_bom = models.BooleanField(default=False, verbose_name="Is Phantom BOM")
    secondary_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Secondary Items")
    secondary_items_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Secondary Items Cost")
    base_secondary_items_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Secondary Items Cost (Company Currency)")
    cost_allocation = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Cost Allocation")
    cost_allocation_per = models.TextField(blank=True, null=True, verbose_name="% Cost Allocation")
    backflush_based_on = models.CharField(max_length=255, choices=[('BOM', 'BOM'), ('Material Transferred for Manufacture', 'Material Transferred for Manufacture')], blank=True, null=True, verbose_name='Based On')

class BOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM
        fields = '__all__'

class BOMViewSet(viewsets.ModelViewSet):
    queryset = BOM.objects.all()
    serializer_class = BOMSerializer

class MaterialRequestPlanItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Warehouse')
    material_request_type = models.CharField(max_length=255, choices=[('Purchase', 'Purchase'), ('Material Transfer', 'Material Transfer'), ('Material Issue', 'Material Issue'), ('Manufacture', 'Manufacture'), ('Subcontracting', 'Subcontracting'), ('Customer Provided', 'Customer Provided')], blank=True, null=True, verbose_name='Type')
    quantity = models.FloatField(default=0.0, verbose_name="Required Qty")
    projected_qty = models.FloatField(default=0.0, verbose_name="Projected Qty")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty In Stock")
    min_order_qty = models.FloatField(default=0.0, verbose_name="Minimum Order Quantity")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    requested_qty = models.FloatField(default=0.0, verbose_name="Requested Qty")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Warehouse')
    safety_stock = models.FloatField(default=0.0, verbose_name="Safety Stock")
    ordered_qty = models.FloatField(default=0.0, verbose_name="Ordered Qty")
    reserved_qty_for_production = models.FloatField(default=0.0, verbose_name="Reserved Qty for Production")
    required_bom_qty = models.FloatField(default=0.0, verbose_name="Reqd Qty (BOM)")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    schedule_date = models.DateField(blank=True, null=True, verbose_name="Required By")
    stock_reserved_qty = models.FloatField(default=0.0, verbose_name="Stock Reserved Qty")
    from_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From BOM')
    sub_assembly_item_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sub Assembly Item Reference")
    main_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Main Item Code')

class MaterialRequestPlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequestPlanItem
        fields = '__all__'

class MaterialRequestPlanItemViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequestPlanItem.objects.all()
    serializer_class = MaterialRequestPlanItemSerializer

class Workstation(BaseDocument):
    workstation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Workstation Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    hour_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Hour Rate")
    working_hours = models.JSONField(default=list, blank=True, null=True, verbose_name="Working Hours")
    holiday_list = models.ForeignKey('erp_core.HolidayList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Holiday List')
    production_capacity = models.IntegerField(default=0, verbose_name="Job Capacity")
    workstation_type = models.ForeignKey('erp_core.WorkstationType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation Type')
    plant_floor = models.ForeignKey('erp_core.PlantFloor', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Plant Floor')
    status = models.CharField(max_length=255, choices=[('Production', 'Production'), ('Off', 'Off'), ('Idle', 'Idle'), ('Problem', 'Problem'), ('Maintenance', 'Maintenance'), ('Setup', 'Setup')], blank=True, null=True, verbose_name='Status')
    on_status_image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Active Status")
    off_status_image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Inactive Status")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    total_working_hours = models.FloatField(default=0.0, verbose_name="Total Working Hours")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    workstation_costs = models.JSONField(default=list, blank=True, null=True, verbose_name="Operating Components Cost")

class WorkstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workstation
        fields = '__all__'

class WorkstationViewSet(viewsets.ModelViewSet):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer

class WorkstationOperatingComponentAccount(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')

class WorkstationOperatingComponentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkstationOperatingComponentAccount
        fields = '__all__'

class WorkstationOperatingComponentAccountViewSet(viewsets.ModelViewSet):
    queryset = WorkstationOperatingComponentAccount.objects.all()
    serializer_class = WorkstationOperatingComponentAccountSerializer

class BOMCreator(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    rm_cost_as_per = models.CharField(max_length=255, choices=[('Valuation Rate', 'Valuation Rate'), ('Last Purchase Rate', 'Last Purchase Rate'), ('Price List', 'Price List')], blank=True, null=True, verbose_name='Rate Of Materials Based On')
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Conversion Rate")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    raw_material_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Cost")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Good')
    qty = models.FloatField(default=0.0, verbose_name="Quantity")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    default_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Source Warehouse')
    set_rate_based_on_warehouse = models.BooleanField(default=False, verbose_name="Set Valuation Rate Based on Source Warehouse")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    error_log = models.TextField(blank=True, null=True, verbose_name="Error Log")
    routing = models.ForeignKey('erp_core.Routing', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Routing')
    is_phantom = models.BooleanField(default=False, verbose_name="Is Phantom Item")

class BOMCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMCreator
        fields = '__all__'

class BOMCreatorViewSet(viewsets.ModelViewSet):
    queryset = BOMCreator.objects.all()
    serializer_class = BOMCreatorSerializer

class WorkOrderOperation(BaseDocument):
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM')
    description = models.TextField(blank=True, null=True, verbose_name="Operation Description")
    completed_qty = models.FloatField(default=0.0, verbose_name="Completed Qty")
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Work in Progress', 'Work in Progress'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    workstation = models.ForeignKey('erp_core.Workstation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation')
    planned_start_time = models.DateTimeField(blank=True, null=True, verbose_name="Planned Start Time")
    planned_end_time = models.DateTimeField(blank=True, null=True, verbose_name="Planned End Time")
    time_in_mins = models.FloatField(default=0.0, verbose_name="Time")
    hour_rate = models.FloatField(default=0.0, verbose_name="Hour Rate")
    planned_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Planned Operating Cost")
    actual_start_time = models.DateTimeField(blank=True, null=True, verbose_name="Actual Start Time")
    actual_end_time = models.DateTimeField(blank=True, null=True, verbose_name="Actual End Time")
    actual_operation_time = models.FloatField(default=0.0, verbose_name="Actual Operation Time")
    actual_operating_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Actual Operating Cost")
    batch_size = models.FloatField(default=0.0, verbose_name="Batch Size")
    sequence_id = models.IntegerField(default=0, verbose_name="Sequence ID")
    workstation_type = models.ForeignKey('erp_core.WorkstationType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation Type')
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM No (For Semi-Finished Goods)')
    finished_good = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Semi Finished Goods / Finished Goods')
    wip_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP WH')
    fg_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finished Goods Warehouse')
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    skip_material_transfer = models.BooleanField(default=False, verbose_name="Skip Material Transfer")
    backflush_from_wip_warehouse = models.BooleanField(default=False, verbose_name="Backflush Materials From WIP Warehouse")
    quality_inspection_required = models.BooleanField(default=False, verbose_name="Quality Inspection Required")

class WorkOrderOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderOperation
        fields = '__all__'

class WorkOrderOperationViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderOperation.objects.all()
    serializer_class = WorkOrderOperationSerializer

class JobCard(BaseDocument):
    work_order = models.ForeignKey('erp_core.WorkOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Work Order')
    bom_no = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Final BOM')
    workstation = models.ForeignKey('erp_core.Workstation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation')
    operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Operation')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    for_quantity = models.FloatField(default=0.0, verbose_name="Qty To Manufacture")
    wip_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP Warehouse')
    time_logs = models.JSONField(default=list, blank=True, null=True, verbose_name="Time Logs")
    total_completed_qty = models.FloatField(default=0.0, verbose_name="Total Completed Qty")
    total_time_in_mins = models.FloatField(default=0.0, verbose_name="Total Time in Mins")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    operation_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Operation ID")
    transferred_qty = models.FloatField(default=0.0, verbose_name="Transferred Raw Materials")
    requested_qty = models.FloatField(default=0.0, verbose_name="Requested Qty")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Work In Progress', 'Work In Progress'), ('Material Transferred', 'Material Transferred'), ('On Hold', 'On Hold'), ('Submitted', 'Submitted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    naming_series = models.CharField(max_length=255, choices=[('PO-JOB.#####', 'PO-JOB.#####')], blank=True, null=True, verbose_name='Naming Series')
    production_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Final Product')
    barcode = models.TextField(blank=True, null=True, verbose_name="Barcode")
    item_name = models.TextField(blank=True, null=True, verbose_name="Item Name")
    operation_row_number = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Operation Row Number')
    sequence_id = models.IntegerField(default=0, verbose_name="Sequence Id")
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    sub_operations = models.JSONField(default=list, blank=True, null=True, verbose_name="Sub Operations")
    hour_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Hour Rate")
    is_corrective_job_card = models.BooleanField(default=False, verbose_name="Is Corrective Job Card")
    for_job_card = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Job Card')
    for_operation = models.ForeignKey('erp_core.Operation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Operation')
    employee = models.TextField(blank=True, null=True, verbose_name="Employee")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    quality_inspection_template = models.ForeignKey('erp_core.QualityInspectionTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection Template')
    workstation_type = models.ForeignKey('erp_core.WorkstationType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Workstation Type')
    expected_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Expected Start Date")
    expected_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Expected End Date")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    process_loss_qty = models.FloatField(default=0.0, verbose_name="Process Loss Qty")
    time_required = models.FloatField(default=0.0, verbose_name="Expected Time Required (In Mins)")
    scheduled_time_logs = models.JSONField(default=list, blank=True, null=True, verbose_name="Scheduled Time Logs")
    actual_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Actual Start Date")
    actual_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Actual End Date")
    finished_good = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item to Manufacture')
    target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    operation_row_id = models.IntegerField(default=0, verbose_name="Operation Row ID")
    source_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    semi_fg_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturing BOM')
    is_subcontracted = models.BooleanField(default=False, verbose_name=" Is Subcontracted")
    manufactured_qty = models.FloatField(default=0.0, verbose_name="Manufactured Qty")
    skip_material_transfer = models.BooleanField(default=False, verbose_name="Skip Material Transfer to WIP")
    backflush_from_wip_warehouse = models.BooleanField(default=False, verbose_name="Backflush Materials From WIP Warehouse")
    is_paused = models.BooleanField(default=False, verbose_name="Is Paused")
    track_semi_finished_goods = models.BooleanField(default=False, verbose_name="Track Semi Finished Goods")
    secondary_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Secondary Items")

class JobCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCard
        fields = '__all__'

class JobCardViewSet(viewsets.ModelViewSet):
    queryset = JobCard.objects.all()
    serializer_class = JobCardSerializer

class ProductionPlanMaterialRequestWarehouse(BaseDocument):
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')

class ProductionPlanMaterialRequestWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlanMaterialRequestWarehouse
        fields = '__all__'

class ProductionPlanMaterialRequestWarehouseViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlanMaterialRequestWarehouse.objects.all()
    serializer_class = ProductionPlanMaterialRequestWarehouseSerializer

class Operation(BaseDocument):
    workstation = models.ForeignKey('erp_core.Workstation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Workstation')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    sub_operations = models.JSONField(default=list, blank=True, null=True, verbose_name="sub_operations")
    total_operation_time = models.FloatField(default=0.0, verbose_name="Total Operation Time")
    batch_size = models.IntegerField(default=0, verbose_name="Batch Size")
    create_job_card_based_on_batch_size = models.BooleanField(default=False, verbose_name="Create Job Card based on Batch Size")
    is_corrective_operation = models.BooleanField(default=False, verbose_name="Is Corrective Operation")
    quality_inspection_template = models.ForeignKey('erp_core.QualityInspectionTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection Template')

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

class BOMUpdateLog(BaseDocument):
    current_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Current BOM')
    new_bom = models.ForeignKey('erp_core.BOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='New BOM')
    update_type = models.CharField(max_length=255, choices=[('Replace BOM', 'Replace BOM'), ('Update Cost', 'Update Cost')], blank=True, null=True, verbose_name='Update Type')
    status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    error_log = models.ForeignKey('erp_core.ErrorLog', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Error Log')
    processed_boms = models.TextField(blank=True, null=True, verbose_name="Processed BOMs")
    bom_batches = models.JSONField(default=list, blank=True, null=True, verbose_name="bom_batches")
    current_level = models.IntegerField(default=0, verbose_name="Current Level")

class BOMUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMUpdateLog
        fields = '__all__'

class BOMUpdateLogViewSet(viewsets.ModelViewSet):
    queryset = BOMUpdateLog.objects.all()
    serializer_class = BOMUpdateLogSerializer

class WorkstationWorkingHour(BaseDocument):
    start_time = models.TextField(blank=True, null=True, verbose_name="Start Time")
    end_time = models.TextField(blank=True, null=True, verbose_name="End Time")
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    hours = models.FloatField(default=0.0, verbose_name="Hours")

class WorkstationWorkingHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkstationWorkingHour
        fields = '__all__'

class WorkstationWorkingHourViewSet(viewsets.ModelViewSet):
    queryset = WorkstationWorkingHour.objects.all()
    serializer_class = WorkstationWorkingHourSerializer

class MasterProductionSchedule(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    naming_series = models.CharField(max_length=255, choices=[('MPS.YY.-.######', 'MPS.YY.-.######')], blank=True, null=True, verbose_name='Naming Series')
    parent_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Warehouse')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    sales_orders = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Orders")
    material_requests = models.JSONField(default=list, blank=True, null=True, verbose_name="Material Requests")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    sales_forecast = models.ForeignKey('erp_core.SalesForecast', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Forecast')
    select_items = models.TextField(blank=True, null=True, verbose_name="Select Items")

class MasterProductionScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProductionSchedule
        fields = '__all__'

class MasterProductionScheduleViewSet(viewsets.ModelViewSet):
    queryset = MasterProductionSchedule.objects.all()
    serializer_class = MasterProductionScheduleSerializer
