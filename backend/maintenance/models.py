from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class MaintenanceVisit(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-MVS-.YYYY.-', 'MAT-MVS-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    mntc_date = models.DateField(blank=True, null=True, verbose_name="Maintenance Date")
    mntc_time = models.TextField(blank=True, null=True, verbose_name="Maintenance Time")
    completion_status = models.CharField(max_length=255, choices=[('Partially Completed', 'Partially Completed'), ('Fully Completed', 'Fully Completed')], blank=True, null=True, verbose_name='Completion Status')
    maintenance_type = models.CharField(max_length=255, choices=[('Scheduled', 'Scheduled'), ('Unscheduled', 'Unscheduled'), ('Breakdown', 'Breakdown')], blank=True, null=True, verbose_name='Maintenance Type')
    purposes = models.JSONField(default=list, blank=True, null=True, verbose_name="Purposes")
    customer_feedback = models.TextField(blank=True, null=True, verbose_name="Customer Feedback")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Cancelled', 'Cancelled'), ('Submitted', 'Submitted')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    maintenance_schedule = models.ForeignKey('erp_core.MaintenanceSchedule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Maintenance Schedule')
    maintenance_schedule_detail = models.ForeignKey('erp_core.MaintenanceScheduleDetail', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Maintenance Schedule Detail')

class MaintenanceVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceVisit
        fields = '__all__'

class MaintenanceVisitViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceVisit.objects.all()
    serializer_class = MaintenanceVisitSerializer

class MaintenanceScheduleDetail(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    scheduled_date = models.DateField(blank=True, null=True, verbose_name="Scheduled Date")
    actual_date = models.DateField(blank=True, null=True, verbose_name="Actual Date")
    sales_person = models.ForeignKey('erp_core.SalesPerson', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Person')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    completion_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Partially Completed', 'Partially Completed'), ('Fully Completed', 'Fully Completed')], blank=True, null=True, verbose_name='Completion Status')
    item_reference = models.ForeignKey('erp_core.MaintenanceScheduleItem', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Reference')

class MaintenanceScheduleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceScheduleDetail
        fields = '__all__'

class MaintenanceScheduleDetailViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceScheduleDetail.objects.all()
    serializer_class = MaintenanceScheduleDetailSerializer

class MaintenanceSchedule(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('MAT-MSH-.YYYY.-', 'MAT-MSH-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Transaction Date")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    schedules = models.JSONField(default=list, blank=True, null=True, verbose_name="Schedules")
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class MaintenanceScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceSchedule
        fields = '__all__'

class MaintenanceScheduleViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceSchedule.objects.all()
    serializer_class = MaintenanceScheduleSerializer

class MaintenanceScheduleItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    periodicity = models.CharField(max_length=255, choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half Yearly', 'Half Yearly'), ('Yearly', 'Yearly'), ('Random', 'Random')], blank=True, null=True, verbose_name='Periodicity')
    no_of_visits = models.IntegerField(default=0, verbose_name="No of Visits")
    sales_person = models.ForeignKey('erp_core.SalesPerson', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Person')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')

class MaintenanceScheduleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceScheduleItem
        fields = '__all__'

class MaintenanceScheduleItemViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceScheduleItem.objects.all()
    serializer_class = MaintenanceScheduleItemSerializer

class MaintenanceVisitPurpose(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    serial_no = models.ForeignKey('erp_core.SerialNo', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial No')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    service_person = models.ForeignKey('erp_core.SalesPerson', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Person')
    work_done = models.TextField(blank=True, null=True, verbose_name="Work Done")
    prevdoc_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Document Type')
    prevdoc_docname = models.TextField(blank=True, null=True, verbose_name="Against Document No")
    maintenance_schedule_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Maintenance Schedule Detail")

class MaintenanceVisitPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceVisitPurpose
        fields = '__all__'

class MaintenanceVisitPurposeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceVisitPurpose.objects.all()
    serializer_class = MaintenanceVisitPurposeSerializer
