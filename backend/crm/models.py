from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class ProspectLead(BaseDocument):
    lead = models.ForeignKey('erp_core.Lead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Lead')
    lead_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lead Name")
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name="Status")
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email")
    mobile_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    lead_owner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lead Owner")

class ProspectLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectLead
        fields = '__all__'

class ProspectLeadViewSet(viewsets.ModelViewSet):
    queryset = ProspectLead.objects.all()
    serializer_class = ProspectLeadSerializer

class OpportunityLostReason(BaseDocument):
    lost_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lost Reason")

class OpportunityLostReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityLostReason
        fields = '__all__'

class OpportunityLostReasonViewSet(viewsets.ModelViewSet):
    queryset = OpportunityLostReason.objects.all()
    serializer_class = OpportunityLostReasonSerializer

class CRMSettings(BaseDocument):
    campaign_naming_by = models.CharField(max_length=255, choices=[('Campaign Name', 'Campaign Name'), ('Naming Series', 'Naming Series')], blank=True, null=True, verbose_name='Campaign Naming By')
    default_valid_till = models.CharField(max_length=255, blank=True, null=True, verbose_name="Default Quotation Validity Days")
    allow_lead_duplication_based_on_emails = models.BooleanField(default=False, verbose_name="Allow Lead Duplication based on Emails")
    auto_creation_of_contact = models.BooleanField(default=False, verbose_name="Auto Creation of Contact")
    close_opportunity_after_days = models.IntegerField(default=0, verbose_name="Close Replied Opportunity After Days")
    carry_forward_communication_and_comments = models.BooleanField(default=False, verbose_name="Carry Forward Communication and Comments")
    update_timestamp_on_new_communication = models.BooleanField(default=False, verbose_name="Update timestamp on new communication")

class CRMSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMSettings
        fields = '__all__'

class CRMSettingsViewSet(viewsets.ModelViewSet):
    queryset = CRMSettings.objects.all()
    serializer_class = CRMSettingsSerializer

class MarketSegment(BaseDocument):
    market_segment = models.CharField(max_length=255, blank=True, null=True, verbose_name="Market Segment")

class MarketSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketSegment
        fields = '__all__'

class MarketSegmentViewSet(viewsets.ModelViewSet):
    queryset = MarketSegment.objects.all()
    serializer_class = MarketSegmentSerializer

class AvailabilityOfSlots(BaseDocument):
    day_of_week = models.CharField(max_length=255, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], blank=True, null=True, verbose_name='Day Of Week')
    from_time = models.TextField(blank=True, null=True, verbose_name="From Time")
    to_time = models.TextField(blank=True, null=True, verbose_name="To Time")

class AvailabilityOfSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilityOfSlots
        fields = '__all__'

class AvailabilityOfSlotsViewSet(viewsets.ModelViewSet):
    queryset = AvailabilityOfSlots.objects.all()
    serializer_class = AvailabilityOfSlotsSerializer

class Campaign(BaseDocument):
    campaign_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Campaign Name")
    naming_series = models.CharField(max_length=255, choices=[('SAL-CAM-.YYYY.-', 'SAL-CAM-.YYYY.-')], blank=True, null=True, verbose_name='Naming Series')
    campaign_schedules = models.JSONField(default=list, blank=True, null=True, verbose_name="Campaign Schedules")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class EmailCampaign(BaseDocument):
    campaign_name = models.ForeignKey('erp_core.Campaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    status = models.CharField(max_length=255, choices=[('Scheduled', 'Scheduled'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Unsubscribed', 'Unsubscribed')], blank=True, null=True, verbose_name='Status')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    email_campaign_for = models.CharField(max_length=255, choices=[('Lead', 'Lead'), ('Contact', 'Contact'), ('Email Group', 'Email Group')], blank=True, null=True, verbose_name='Email Campaign For ')
    recipient = models.TextField(blank=True, null=True, verbose_name="Recipient")
    sender = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sender')

class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCampaign
        fields = '__all__'

class EmailCampaignViewSet(viewsets.ModelViewSet):
    queryset = EmailCampaign.objects.all()
    serializer_class = EmailCampaignSerializer

class Contract(BaseDocument):
    party_type = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Supplier', 'Supplier'), ('Employee', 'Employee')], blank=True, null=True, verbose_name='Party Type')
    is_signed = models.BooleanField(default=False, verbose_name="Signed")
    party_name = models.TextField(blank=True, null=True, verbose_name="Party Name")
    party_user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party User')
    status = models.CharField(max_length=255, choices=[('Unsigned', 'Unsigned'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    fulfilment_status = models.CharField(max_length=255, choices=[('N/A', 'N/A'), ('Unfulfilled', 'Unfulfilled'), ('Partially Fulfilled', 'Partially Fulfilled'), ('Fulfilled', 'Fulfilled'), ('Lapsed', 'Lapsed')], blank=True, null=True, verbose_name='Fulfilment Status')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    signee = models.CharField(max_length=255, blank=True, null=True, verbose_name="Signee")
    signed_on = models.DateTimeField(blank=True, null=True, verbose_name="Signed On")
    ip_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="IP Address")
    contract_template = models.ForeignKey('erp_core.ContractTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contract Template')
    contract_terms = models.TextField(blank=True, null=True, verbose_name="Contract Terms")
    requires_fulfilment = models.BooleanField(default=False, verbose_name="Requires Fulfilment")
    fulfilment_deadline = models.DateField(blank=True, null=True, verbose_name="Fulfilment Deadline")
    fulfilment_terms = models.JSONField(default=list, blank=True, null=True, verbose_name="Fulfilment Terms")
    document_type = models.CharField(max_length=255, choices=[('Quotation', 'Quotation'), ('Project', 'Project'), ('Sales Order', 'Sales Order'), ('Purchase Order', 'Purchase Order'), ('Sales Invoice', 'Sales Invoice'), ('Purchase Invoice', 'Purchase Invoice')], blank=True, null=True, verbose_name='Document Type')
    document_name = models.TextField(blank=True, null=True, verbose_name="Document Name")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    signee_company = models.TextField(blank=True, null=True, verbose_name="Signee (Company)")
    signed_by_company = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Signed By (Company)')
    party_full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Full Name")

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class Opportunity(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('CRM-OPP-.YYYY.-', 'CRM-OPP-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    opportunity_from = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity From')
    party_name = models.TextField(blank=True, null=True, verbose_name="Party")
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    opportunity_type = models.ForeignKey('erp_core.OpportunityType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity Type')
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Quotation', 'Quotation'), ('Converted', 'Converted'), ('Lost', 'Lost'), ('Replied', 'Replied'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    order_lost_reason = models.TextField(blank=True, null=True, verbose_name="Detailed Reason")
    expected_closing = models.DateField(blank=True, null=True, verbose_name="Expected Closing Date")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    opportunity_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Opportunity Amount")
    sales_stage = models.ForeignKey('erp_core.SalesStage', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Stage')
    probability = models.TextField(blank=True, null=True, verbose_name="Probability (%)")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer / Lead Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    contact_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Mobile")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Opportunity Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    lost_reasons = models.TextField(blank=True, null=True, verbose_name="Lost Reasons")
    first_response_time = models.TextField(blank=True, null=True, verbose_name="First Response Time")
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    base_opportunity_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Opportunity Amount (Company Currency)")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    competitors = models.TextField(blank=True, null=True, verbose_name="Competitors")
    no_of_employees = models.CharField(max_length=255, choices=[('1-10', '1-10'), ('11-50', '11-50'), ('51-200', '51-200'), ('201-500', '201-500'), ('501-1000', '501-1000'), ('1000+', '1000+')], blank=True, null=True, verbose_name='No of Employees')
    annual_revenue = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Annual Revenue")
    industry = models.ForeignKey('erp_core.IndustryType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Industry')
    market_segment = models.ForeignKey('erp_core.MarketSegment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Market Segment')
    opportunity_owner = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity Owner')
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    whatsapp = models.CharField(max_length=255, blank=True, null=True, verbose_name="WhatsApp")
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone")
    phone_ext = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone Ext.")
    job_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Title")
    notes = models.JSONField(default=list, blank=True, null=True, verbose_name="Notes")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="City")
    state = models.CharField(max_length=255, blank=True, null=True, verbose_name="State/Province")
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class Lead(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('CRM-LEAD-.YYYY.-', 'CRM-LEAD-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    lead_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Organization Name")
    email_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email")
    lead_owner = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Lead Owner')
    status = models.CharField(max_length=255, choices=[('Lead', 'Lead'), ('Open', 'Open'), ('Replied', 'Replied'), ('Opportunity', 'Opportunity'), ('Quotation', 'Quotation'), ('Lost Quotation', 'Lost Quotation'), ('Interested', 'Interested'), ('Converted', 'Converted'), ('Do Not Contact', 'Do Not Contact')], blank=True, null=True, verbose_name='Status')
    salutation = models.ForeignKey('erp_core.Salutation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Salutation')
    gender = models.ForeignKey('erp_core.Gender', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gender')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Customer')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone")
    mobile_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    fax = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fax")
    type = models.CharField(max_length=255, choices=[('Client', 'Client'), ('Channel Partner', 'Channel Partner'), ('Consultant', 'Consultant')], blank=True, null=True, verbose_name='Lead Type')
    market_segment = models.ForeignKey('erp_core.MarketSegment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Market Segment')
    industry = models.ForeignKey('erp_core.IndustryType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Industry')
    request_type = models.CharField(max_length=255, choices=[('Product Enquiry', 'Product Enquiry'), ('Request for Information', 'Request for Information'), ('Suggestions', 'Suggestions'), ('Other', 'Other')], blank=True, null=True, verbose_name='Request Type')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    unsubscribed = models.BooleanField(default=False, verbose_name="Unsubscribed")
    blog_subscriber = models.BooleanField(default=False, verbose_name="Blog Subscriber")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Middle Name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Name")
    no_of_employees = models.CharField(max_length=255, choices=[('1-10', '1-10'), ('11-50', '11-50'), ('51-200', '51-200'), ('201-500', '201-500'), ('501-1000', '501-1000'), ('1000+', '1000+')], blank=True, null=True, verbose_name='No of Employees')
    whatsapp_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="WhatsApp")
    phone_ext = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone Ext.")
    qualified_by = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Qualified By')
    qualified_on = models.DateField(blank=True, null=True, verbose_name="Qualified on")
    qualification_status = models.CharField(max_length=255, choices=[('Unqualified', 'Unqualified'), ('In Process', 'In Process'), ('Qualified', 'Qualified')], blank=True, null=True, verbose_name='Qualification Status')
    job_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Title")
    annual_revenue = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Annual Revenue")
    notes = models.JSONField(default=list, blank=True, null=True, verbose_name="Notes")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="City")
    state = models.CharField(max_length=255, blank=True, null=True, verbose_name="State/Province")
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')
    utm_content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class Competitor(BaseDocument):
    competitor_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Competitor Name")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = '__all__'

class CompetitorViewSet(viewsets.ModelViewSet):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorSerializer

class OpportunityItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    qty = models.FloatField(default=0.0, verbose_name="Qty")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")

class OpportunityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityItem
        fields = '__all__'

class OpportunityItemViewSet(viewsets.ModelViewSet):
    queryset = OpportunityItem.objects.all()
    serializer_class = OpportunityItemSerializer

class Appointment(BaseDocument):
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    customer_phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone Number")
    customer_skype = models.CharField(max_length=255, blank=True, null=True, verbose_name="Skype ID")
    customer_details = models.TextField(blank=True, null=True, verbose_name="Details")
    scheduled_time = models.DateTimeField(blank=True, null=True, verbose_name="Scheduled Time")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Unverified', 'Unverified'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    calendar_event = models.ForeignKey('erp_core.Event', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Calendar Event')
    customer_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email")
    appointment_with = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Appointment With')
    party = models.TextField(blank=True, null=True, verbose_name="Party")

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class CRMNote(BaseDocument):
    note = models.TextField(blank=True, null=True, verbose_name="Note")
    added_by = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Added By')
    added_on = models.DateTimeField(blank=True, null=True, verbose_name="Added On")

class CRMNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMNote
        fields = '__all__'

class CRMNoteViewSet(viewsets.ModelViewSet):
    queryset = CRMNote.objects.all()
    serializer_class = CRMNoteSerializer

class SalesStage(BaseDocument):
    stage_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Stage Name")

class SalesStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesStage
        fields = '__all__'

class SalesStageViewSet(viewsets.ModelViewSet):
    queryset = SalesStage.objects.all()
    serializer_class = SalesStageSerializer

class OpportunityType(BaseDocument):
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class OpportunityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityType
        fields = '__all__'

class OpportunityTypeViewSet(viewsets.ModelViewSet):
    queryset = OpportunityType.objects.all()
    serializer_class = OpportunityTypeSerializer

class CompetitorDetail(BaseDocument):
    competitor = models.ForeignKey('erp_core.Competitor', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Competitor')

class CompetitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitorDetail
        fields = '__all__'

class CompetitorDetailViewSet(viewsets.ModelViewSet):
    queryset = CompetitorDetail.objects.all()
    serializer_class = CompetitorDetailSerializer

class ContractTemplate(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    contract_terms = models.TextField(blank=True, null=True, verbose_name="Contract Terms and Conditions")
    requires_fulfilment = models.BooleanField(default=False, verbose_name="Requires Fulfilment")
    fulfilment_terms = models.JSONField(default=list, blank=True, null=True, verbose_name="Fulfilment Terms and Conditions")

class ContractTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractTemplate
        fields = '__all__'

class ContractTemplateViewSet(viewsets.ModelViewSet):
    queryset = ContractTemplate.objects.all()
    serializer_class = ContractTemplateSerializer

class Prospect(BaseDocument):
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company Name")
    industry = models.ForeignKey('erp_core.IndustryType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Industry')
    market_segment = models.ForeignKey('erp_core.MarketSegment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Market Segment')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    no_of_employees = models.CharField(max_length=255, choices=[('1-10', '1-10'), ('11-50', '11-50'), ('51-200', '51-200'), ('201-500', '201-500'), ('501-1000', '501-1000'), ('1000+', '1000+')], blank=True, null=True, verbose_name='No. of Employees')
    annual_revenue = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Annual Revenue")
    fax = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fax")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    prospect_owner = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Prospect Owner')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    opportunities = models.JSONField(default=list, blank=True, null=True, verbose_name="Opportunities")
    leads = models.JSONField(default=list, blank=True, null=True, verbose_name="leads")
    notes = models.JSONField(default=list, blank=True, null=True, verbose_name="Notes")

class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospect
        fields = '__all__'

class ProspectViewSet(viewsets.ModelViewSet):
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer

class ContractTemplateFulfilmentTerms(BaseDocument):
    requirement = models.CharField(max_length=255, blank=True, null=True, verbose_name="Requirement")

class ContractTemplateFulfilmentTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractTemplateFulfilmentTerms
        fields = '__all__'

class ContractTemplateFulfilmentTermsViewSet(viewsets.ModelViewSet):
    queryset = ContractTemplateFulfilmentTerms.objects.all()
    serializer_class = ContractTemplateFulfilmentTermsSerializer

class OpportunityLostReasonDetail(BaseDocument):
    lost_reason = models.ForeignKey('erp_core.OpportunityLostReason', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity Lost Reason')

class OpportunityLostReasonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityLostReasonDetail
        fields = '__all__'

class OpportunityLostReasonDetailViewSet(viewsets.ModelViewSet):
    queryset = OpportunityLostReasonDetail.objects.all()
    serializer_class = OpportunityLostReasonDetailSerializer

class AppointmentBookingSettings(BaseDocument):
    availability_of_slots = models.JSONField(default=list, blank=True, null=True, verbose_name="Availability Of Slots")
    number_of_agents = models.IntegerField(default=0, verbose_name="Number of Concurrent Appointments")
    holiday_list = models.ForeignKey('erp_core.HolidayList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Holiday List')
    appointment_duration = models.IntegerField(default=0, verbose_name="Appointment Duration (In Minutes)")
    email_reminders = models.BooleanField(default=False, verbose_name="Notify Via Email")
    advance_booking_days = models.IntegerField(default=0, verbose_name="Number of days appointments can be booked in advance")
    agent_list = models.TextField(blank=True, null=True, verbose_name="Agents")
    enable_scheduling = models.BooleanField(default=False, verbose_name="Enable Appointment Scheduling")
    success_redirect_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Success Redirect URL")

class AppointmentBookingSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentBookingSettings
        fields = '__all__'

class AppointmentBookingSettingsViewSet(viewsets.ModelViewSet):
    queryset = AppointmentBookingSettings.objects.all()
    serializer_class = AppointmentBookingSettingsSerializer

class AppointmentBookingSlots(BaseDocument):
    day_of_week = models.CharField(max_length=255, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], blank=True, null=True, verbose_name='Day Of Week')
    from_time = models.TextField(blank=True, null=True, verbose_name="From Time ")
    to_time = models.TextField(blank=True, null=True, verbose_name="To Time")

class AppointmentBookingSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentBookingSlots
        fields = '__all__'

class AppointmentBookingSlotsViewSet(viewsets.ModelViewSet):
    queryset = AppointmentBookingSlots.objects.all()
    serializer_class = AppointmentBookingSlotsSerializer

class LostReasonDetail(BaseDocument):
    lost_reason = models.ForeignKey('erp_core.OpportunityLostReason', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity Lost Reason')

class LostReasonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostReasonDetail
        fields = '__all__'

class LostReasonDetailViewSet(viewsets.ModelViewSet):
    queryset = LostReasonDetail.objects.all()
    serializer_class = LostReasonDetailSerializer

class ProspectOpportunity(BaseDocument):
    opportunity = models.ForeignKey('erp_core.Opportunity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Opportunity')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    stage = models.CharField(max_length=255, blank=True, null=True, verbose_name="Stage")
    probability = models.TextField(blank=True, null=True, verbose_name="Probability")
    expected_closing = models.DateField(blank=True, null=True, verbose_name="Closing")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    deal_owner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Deal Owner")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')

class ProspectOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectOpportunity
        fields = '__all__'

class ProspectOpportunityViewSet(viewsets.ModelViewSet):
    queryset = ProspectOpportunity.objects.all()
    serializer_class = ProspectOpportunitySerializer

class CampaignEmailSchedule(BaseDocument):
    send_after_days = models.IntegerField(default=0, verbose_name="Send After (days)")
    email_template = models.ForeignKey('erp_core.EmailTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Email Template')

class CampaignEmailScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignEmailSchedule
        fields = '__all__'

class CampaignEmailScheduleViewSet(viewsets.ModelViewSet):
    queryset = CampaignEmailSchedule.objects.all()
    serializer_class = CampaignEmailScheduleSerializer

class ContractFulfilmentChecklist(BaseDocument):
    fulfilled = models.BooleanField(default=False, verbose_name="Fulfilled")
    requirement = models.CharField(max_length=255, blank=True, null=True, verbose_name="Requirement")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class ContractFulfilmentChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractFulfilmentChecklist
        fields = '__all__'

class ContractFulfilmentChecklistViewSet(viewsets.ModelViewSet):
    queryset = ContractFulfilmentChecklist.objects.all()
    serializer_class = ContractFulfilmentChecklistSerializer
