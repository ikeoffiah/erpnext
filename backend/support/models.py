from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class WarrantyClaim(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('SER-WRN-.YYYY.-', 'SER-WRN-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Work In Progress', 'Work In Progress'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    complaint_date = models.DateField(blank=True, null=True, verbose_name="Issue Date")
    serial_no = models.ForeignKey('erp_core.SerialNo', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial No')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    complaint = models.TextField(blank=True, null=True, verbose_name="Issue")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    warranty_amc_status = models.CharField(max_length=255, choices=[('Under Warranty', 'Under Warranty'), ('Out of Warranty', 'Out of Warranty'), ('Under AMC', 'Under AMC'), ('Out of AMC', 'Out of AMC')], blank=True, null=True, verbose_name='Warranty / AMC Status')
    warranty_expiry_date = models.DateField(blank=True, null=True, verbose_name="Warranty Expiry Date")
    amc_expiry_date = models.DateField(blank=True, null=True, verbose_name="AMC Expiry Date")
    resolution_date = models.DateTimeField(blank=True, null=True, verbose_name="Resolution Date")
    resolved_by = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Resolved By')
    resolution_details = models.TextField(blank=True, null=True, verbose_name="Resolution Details")
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    service_address = models.TextField(blank=True, null=True, verbose_name="Service Address")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    complaint_raised_by = models.CharField(max_length=255, blank=True, null=True, verbose_name="Raised By")
    from_company = models.CharField(max_length=255, blank=True, null=True, verbose_name="From Company")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class WarrantyClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarrantyClaim
        fields = '__all__'

class WarrantyClaimViewSet(viewsets.ModelViewSet):
    queryset = WarrantyClaim.objects.all()
    serializer_class = WarrantyClaimSerializer

class SupportSettings(BaseDocument):
    close_issue_after_days = models.IntegerField(default=0, verbose_name="Close Issue After Days")
    get_started_sections = models.TextField(blank=True, null=True, verbose_name="Get Started Sections")
    show_latest_forum_posts = models.BooleanField(default=False, verbose_name="Show Latest Forum Posts")
    forum_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Forum URL")
    get_latest_query = models.CharField(max_length=255, blank=True, null=True, verbose_name="Get Latest Query")
    response_key_list = models.CharField(max_length=255, blank=True, null=True, verbose_name="Response Key List")
    post_title_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Title Key")
    post_description_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Description Key")
    post_route_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Route Key")
    post_route_string = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Route String")
    search_apis = models.JSONField(default=list, blank=True, null=True, verbose_name="Search APIs")
    track_service_level_agreement = models.BooleanField(default=False, verbose_name="Track Service Level Agreement")
    allow_resetting_service_level_agreement = models.BooleanField(default=False, verbose_name="Allow Resetting Service Level Agreement")
    greeting_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Greeting Title")
    greeting_subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Greeting Subtitle")

class SupportSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportSettings
        fields = '__all__'

class SupportSettingsViewSet(viewsets.ModelViewSet):
    queryset = SupportSettings.objects.all()
    serializer_class = SupportSettingsSerializer

class SLAFulfilledOnStatus(BaseDocument):
    status = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Status')

class SLAFulfilledOnStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SLAFulfilledOnStatus
        fields = '__all__'

class SLAFulfilledOnStatusViewSet(viewsets.ModelViewSet):
    queryset = SLAFulfilledOnStatus.objects.all()
    serializer_class = SLAFulfilledOnStatusSerializer

class PauseSLAOnStatus(BaseDocument):
    status = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Status')

class PauseSLAOnStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PauseSLAOnStatus
        fields = '__all__'

class PauseSLAOnStatusViewSet(viewsets.ModelViewSet):
    queryset = PauseSLAOnStatus.objects.all()
    serializer_class = PauseSLAOnStatusSerializer

class Issue(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ISS-.YYYY.-', 'ISS-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    raised_by = models.CharField(max_length=255, blank=True, null=True, verbose_name="Raised By (Email)")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Replied', 'Replied'), ('On Hold', 'On Hold'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    priority = models.ForeignKey('erp_core.IssuePriority', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Priority')
    issue_type = models.ForeignKey('erp_core.IssueType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Issue Type')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    service_level_agreement = models.ForeignKey('erp_core.ServiceLevelAgreement', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Service Level Agreement')
    response_by = models.DateTimeField(blank=True, null=True, verbose_name="Response By")
    first_responded_on = models.DateTimeField(blank=True, null=True, verbose_name="First Responded On")
    lead = models.ForeignKey('erp_core.Lead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Lead')
    contact = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact')
    email_account = models.ForeignKey('erp_core.EmailAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Email Account')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    resolution_details = models.TextField(blank=True, null=True, verbose_name="Resolution Details")
    opening_date = models.DateField(blank=True, null=True, verbose_name="Opening Date")
    opening_time = models.TextField(blank=True, null=True, verbose_name="Opening Time")
    content_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content Type")
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Attachment")
    via_customer_portal = models.BooleanField(default=False, verbose_name="Via Customer Portal")
    service_level_agreement_creation = models.DateTimeField(blank=True, null=True, verbose_name="Service Level Agreement Creation")
    issue_split_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Issue Split From')
    avg_response_time = models.TextField(blank=True, null=True, verbose_name="Average Response Time")
    resolution_time = models.TextField(blank=True, null=True, verbose_name="Resolution Time")
    user_resolution_time = models.TextField(blank=True, null=True, verbose_name="User Resolution Time")
    on_hold_since = models.DateTimeField(blank=True, null=True, verbose_name="On Hold Since")
    total_hold_time = models.TextField(blank=True, null=True, verbose_name="Total Hold Time")
    agreement_status = models.CharField(max_length=255, choices=[('First Response Due', 'First Response Due'), ('Resolution Due', 'Resolution Due'), ('Fulfilled', 'Fulfilled'), ('Failed', 'Failed')], blank=True, null=True, verbose_name='Service Level Agreement Status')
    first_response_time = models.TextField(blank=True, null=True, verbose_name="First Response Time")
    sla_resolution_by = models.DateTimeField(blank=True, null=True, verbose_name="Resolution By")
    sla_resolution_date = models.DateTimeField(blank=True, null=True, verbose_name="Resolution Date")

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class SupportSearchSource(BaseDocument):
    source_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Source Name")
    source_type = models.CharField(max_length=255, choices=[('API', 'API'), ('Link', 'Link')], blank=True, null=True, verbose_name='Source Type')
    base_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Base URL")
    query_route = models.CharField(max_length=255, blank=True, null=True, verbose_name="Query Route String")
    search_term_param_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Search Term Param Name")
    response_result_key_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="Response Result Key Path")
    post_route = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Route String")
    post_route_key_list = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Route Key List")
    post_title_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Title Key")
    post_description_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Post Description Key")
    source_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source DocType')
    result_title_field = models.CharField(max_length=255, blank=True, null=True, verbose_name="Result Title Field")
    result_preview_field = models.CharField(max_length=255, blank=True, null=True, verbose_name="Result Preview Field")
    result_route_field = models.CharField(max_length=255, blank=True, null=True, verbose_name="Result Route Field")

class SupportSearchSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportSearchSource
        fields = '__all__'

class SupportSearchSourceViewSet(viewsets.ModelViewSet):
    queryset = SupportSearchSource.objects.all()
    serializer_class = SupportSearchSourceSerializer

class ServiceDay(BaseDocument):
    workday = models.CharField(max_length=255, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], blank=True, null=True, verbose_name='Workday')
    start_time = models.TextField(blank=True, null=True, verbose_name="Start Time")
    end_time = models.TextField(blank=True, null=True, verbose_name="End Time")

class ServiceDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDay
        fields = '__all__'

class ServiceDayViewSet(viewsets.ModelViewSet):
    queryset = ServiceDay.objects.all()
    serializer_class = ServiceDaySerializer

class ServiceLevelPriority(BaseDocument):
    priority = models.ForeignKey('erp_core.IssuePriority', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Priority')
    resolution_time = models.TextField(blank=True, null=True, verbose_name="Resolution Time")
    default_priority = models.BooleanField(default=False, verbose_name="Default Priority")
    response_time = models.TextField(blank=True, null=True, verbose_name="First Response Time")

class ServiceLevelPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLevelPriority
        fields = '__all__'

class ServiceLevelPriorityViewSet(viewsets.ModelViewSet):
    queryset = ServiceLevelPriority.objects.all()
    serializer_class = ServiceLevelPrioritySerializer

class IssuePriority(BaseDocument):
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class IssuePrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuePriority
        fields = '__all__'

class IssuePriorityViewSet(viewsets.ModelViewSet):
    queryset = IssuePriority.objects.all()
    serializer_class = IssuePrioritySerializer

class ServiceLevelAgreement(BaseDocument):
    service_level = models.CharField(max_length=255, blank=True, null=True, verbose_name="Service Level Name")
    holiday_list = models.ForeignKey('erp_core.HolidayList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Holiday List')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    support_and_resolution = models.JSONField(default=list, blank=True, null=True, verbose_name="Working Hours")
    priorities = models.JSONField(default=list, blank=True, null=True, verbose_name="Priorities")
    entity = models.TextField(blank=True, null=True, verbose_name="Entity")
    entity_type = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Customer Group', 'Customer Group'), ('Territory', 'Territory')], blank=True, null=True, verbose_name='Entity Type')
    default_service_level_agreement = models.BooleanField(default=False, verbose_name="Default Service Level Agreement")
    default_priority = models.ForeignKey('erp_core.IssuePriority', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Priority')
    pause_sla_on = models.JSONField(default=list, blank=True, null=True, verbose_name="SLA Paused On")
    document_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Apply On')
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    sla_fulfilled_on = models.JSONField(default=list, blank=True, null=True, verbose_name="SLA Fulfilled On")
    apply_sla_for_resolution = models.BooleanField(default=False, verbose_name="Apply SLA for Resolution Time")
    condition = models.TextField(blank=True, null=True, verbose_name="Condition")

class ServiceLevelAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLevelAgreement
        fields = '__all__'

class ServiceLevelAgreementViewSet(viewsets.ModelViewSet):
    queryset = ServiceLevelAgreement.objects.all()
    serializer_class = ServiceLevelAgreementSerializer

class IssueType(BaseDocument):
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = '__all__'

class IssueTypeViewSet(viewsets.ModelViewSet):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer
