from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class ProjectTemplateTask(BaseDocument):
    task = models.ForeignKey('erp_core.Task', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Task')
    subject = models.TextField(blank=True, null=True, verbose_name="Subject")

class ProjectTemplateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTemplateTask
        fields = '__all__'

class ProjectTemplateTaskViewSet(viewsets.ModelViewSet):
    queryset = ProjectTemplateTask.objects.all()
    serializer_class = ProjectTemplateTaskSerializer

class ActivityCost(BaseDocument):
    activity_type = models.ForeignKey('erp_core.ActivityType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Activity Type')
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    employee_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Employee Name")
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    billing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billing Rate")
    costing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Costing Rate")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="title")

class ActivityCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCost
        fields = '__all__'

class ActivityCostViewSet(viewsets.ModelViewSet):
    queryset = ActivityCost.objects.all()
    serializer_class = ActivityCostSerializer

class ProjectType(BaseDocument):
    project_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Project Type")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'

class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer

class TaskType(BaseDocument):
    weight = models.FloatField(default=0.0, verbose_name="Weight")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = '__all__'

class TaskTypeViewSet(viewsets.ModelViewSet):
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer

class ProjectUpdate(BaseDocument):
    naming_series = models.CharField(max_length=255, blank=True, null=True, verbose_name="Series")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    sent = models.BooleanField(default=False, verbose_name="Sent")
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    time = models.TextField(blank=True, null=True, verbose_name="Time")
    users = models.JSONField(default=list, blank=True, null=True, verbose_name="Users")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdate
        fields = '__all__'

class ProjectUpdateViewSet(viewsets.ModelViewSet):
    queryset = ProjectUpdate.objects.all()
    serializer_class = ProjectUpdateSerializer

class DependentTask(BaseDocument):
    task = models.ForeignKey('erp_core.Task', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Task')

class DependentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DependentTask
        fields = '__all__'

class DependentTaskViewSet(viewsets.ModelViewSet):
    queryset = DependentTask.objects.all()
    serializer_class = DependentTaskSerializer

class TaskDependsOn(BaseDocument):
    task = models.ForeignKey('erp_core.Task', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Task')
    subject = models.TextField(blank=True, null=True, verbose_name="Subject")
    project = models.TextField(blank=True, null=True, verbose_name="Project")

class TaskDependsOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDependsOn
        fields = '__all__'

class TaskDependsOnViewSet(viewsets.ModelViewSet):
    queryset = TaskDependsOn.objects.all()
    serializer_class = TaskDependsOnSerializer

class ProjectTemplate(BaseDocument):
    project_type = models.ForeignKey('erp_core.ProjectType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project Type')
    tasks = models.JSONField(default=list, blank=True, null=True, verbose_name="Tasks")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class ProjectTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTemplate
        fields = '__all__'

class ProjectTemplateViewSet(viewsets.ModelViewSet):
    queryset = ProjectTemplate.objects.all()
    serializer_class = ProjectTemplateSerializer

class Task(BaseDocument):
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    issue = models.ForeignKey('erp_core.Issue', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Issue')
    type = models.ForeignKey('erp_core.TaskType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Type')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Working', 'Working'), ('Pending Review', 'Pending Review'), ('Overdue', 'Overdue'), ('Template', 'Template'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    priority = models.CharField(max_length=255, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], blank=True, null=True, verbose_name='Priority')
    color = models.TextField(blank=True, null=True, verbose_name="Color")
    parent_task = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Task')
    exp_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Expected Start Date")
    expected_time = models.FloatField(default=0.0, verbose_name="Expected Time (in hours)")
    task_weight = models.FloatField(default=0.0, verbose_name="Weight")
    exp_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Expected End Date")
    progress = models.TextField(blank=True, null=True, verbose_name="% Progress")
    is_milestone = models.BooleanField(default=False, verbose_name="Is Milestone")
    description = models.TextField(blank=True, null=True, verbose_name="Task Description")
    depends_on = models.JSONField(default=list, blank=True, null=True, verbose_name="Dependent Tasks")
    depends_on_tasks = models.TextField(blank=True, null=True, verbose_name="Depends on Tasks")
    act_start_date = models.DateField(blank=True, null=True, verbose_name="Actual Start Date (via Timesheet)")
    actual_time = models.FloatField(default=0.0, verbose_name="Actual Time in Hours (via Timesheet)")
    act_end_date = models.DateField(blank=True, null=True, verbose_name="Actual End Date (via Timesheet)")
    total_costing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Costing Amount (via Timesheet)")
    total_billing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billable Amount (via Timesheet)")
    review_date = models.DateField(blank=True, null=True, verbose_name="Review Date")
    closing_date = models.DateField(blank=True, null=True, verbose_name="Closing Date")
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="Old Parent")
    completed_by = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Completed By')
    is_template = models.BooleanField(default=False, verbose_name="Is Template")
    start = models.IntegerField(default=0, verbose_name="Begin On (Days)")
    duration = models.IntegerField(default=0, verbose_name="Duration (Days)")
    completed_on = models.DateField(blank=True, null=True, verbose_name="Completed On")
    template_task = models.CharField(max_length=255, blank=True, null=True, verbose_name="Template Task")

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TimesheetDetail(BaseDocument):
    activity_type = models.ForeignKey('erp_core.ActivityType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Activity Type')
    from_time = models.DateTimeField(blank=True, null=True, verbose_name="From Time")
    expected_hours = models.FloatField(default=0.0, verbose_name="Expected Hrs")
    hours = models.FloatField(default=0.0, verbose_name="Hrs")
    to_time = models.DateTimeField(blank=True, null=True, verbose_name="To Time")
    completed = models.BooleanField(default=False, verbose_name="Completed")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    task = models.ForeignKey('erp_core.Task', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Task')
    billing_hours = models.FloatField(default=0.0, verbose_name="Billing Hours")
    billing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billing Rate")
    billing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billing Amount")
    costing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Costing Rate")
    costing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Costing Amount")
    sales_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Invoice')
    is_billable = models.BooleanField(default=False, verbose_name="Is Billable")
    project_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Project Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    base_billing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billing Rate")
    base_billing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billing Amount")
    base_costing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Costing Rate")
    base_costing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Costing Amount")

class TimesheetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimesheetDetail
        fields = '__all__'

class TimesheetDetailViewSet(viewsets.ModelViewSet):
    queryset = TimesheetDetail.objects.all()
    serializer_class = TimesheetDetailSerializer

class ProjectsSettings(BaseDocument):
    ignore_workstation_time_overlap = models.BooleanField(default=False, verbose_name="Ignore Workstation Time Overlap")
    ignore_user_time_overlap = models.BooleanField(default=False, verbose_name="Ignore User Time Overlap")
    ignore_employee_time_overlap = models.BooleanField(default=False, verbose_name="Ignore Employee Time Overlap")
    fetch_timesheet_in_sales_invoice = models.BooleanField(default=False, verbose_name="Fetch Timesheet in Sales Invoice")

class ProjectsSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsSettings
        fields = '__all__'

class ProjectsSettingsViewSet(viewsets.ModelViewSet):
    queryset = ProjectsSettings.objects.all()
    serializer_class = ProjectsSettingsSerializer

class ActivityType(BaseDocument):
    activity_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Activity Type")
    costing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Default Costing Rate")
    billing_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Default Billing Rate")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'

class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer

class Project(BaseDocument):
    project_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Project Name")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    project_type = models.ForeignKey('erp_core.ProjectType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project Type')
    is_active = models.CharField(max_length=255, choices=[('Yes', 'Yes'), ('No', 'No')], blank=True, null=True, verbose_name='Is Active')
    percent_complete_method = models.CharField(max_length=255, choices=[('Manual', 'Manual'), ('Task Completion', 'Task Completion'), ('Task Progress', 'Task Progress'), ('Task Weight', 'Task Weight')], blank=True, null=True, verbose_name='% Complete Method')
    percent_complete = models.TextField(blank=True, null=True, verbose_name="% Completed")
    project_template = models.ForeignKey('erp_core.ProjectTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Template')
    expected_start_date = models.DateField(blank=True, null=True, verbose_name="Expected Start Date")
    expected_end_date = models.DateField(blank=True, null=True, verbose_name="Expected End Date")
    priority = models.CharField(max_length=255, choices=[('Medium', 'Medium'), ('Low', 'Low'), ('High', 'High')], blank=True, null=True, verbose_name='Priority')
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    users = models.JSONField(default=list, blank=True, null=True, verbose_name="Users")
    copied_from = models.CharField(max_length=255, blank=True, null=True, verbose_name="Copied From")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")
    actual_start_date = models.DateField(blank=True, null=True, verbose_name="Actual Start Date (via Timesheet)")
    actual_time = models.FloatField(default=0.0, verbose_name="Actual Time in Hours (via Timesheet)")
    actual_end_date = models.DateField(blank=True, null=True, verbose_name="Actual End Date (via Timesheet)")
    estimated_costing = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Estimated Cost")
    total_costing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Costing Amount (via Timesheet)")
    total_purchase_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Purchase Cost (via Purchase Invoice)")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    total_sales_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Sales Amount (via Sales Order)")
    total_billable_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billable Amount (via Timesheet)")
    total_billed_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billed Amount (via Sales Invoice)")
    total_consumed_material_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Consumed Material Cost (via Stock Entry)")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Cost Center')
    gross_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Gross Margin")
    per_gross_margin = models.TextField(blank=True, null=True, verbose_name="Gross Margin %")
    collect_progress = models.BooleanField(default=False, verbose_name="Collect Progress")
    holiday_list = models.ForeignKey('erp_core.HolidayList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Holiday List')
    frequency = models.CharField(max_length=255, choices=[('Hourly', 'Hourly'), ('Twice Daily', 'Twice Daily'), ('Daily', 'Daily'), ('Weekly', 'Weekly')], blank=True, null=True, verbose_name='Frequency To Collect Progress')
    from_time = models.TextField(blank=True, null=True, verbose_name="From Time")
    to_time = models.TextField(blank=True, null=True, verbose_name="To Time")
    first_email = models.TextField(blank=True, null=True, verbose_name="First Email")
    second_email = models.TextField(blank=True, null=True, verbose_name="Second Email")
    daily_time_to_send = models.TextField(blank=True, null=True, verbose_name="Daily Time to send")
    day_to_send = models.CharField(max_length=255, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], blank=True, null=True, verbose_name='Day to Send')
    weekly_time_to_send = models.TextField(blank=True, null=True, verbose_name="Weekly Time to send")
    message = models.TextField(blank=True, null=True, verbose_name="Message")
    naming_series = models.CharField(max_length=255, choices=[('PROJ-.####', 'PROJ-.####')], blank=True, null=True, verbose_name='Series')
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class Timesheet(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('TS-.YYYY.-', 'TS-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    sales_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Invoice')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Partially Billed', 'Partially Billed'), ('Billed', 'Billed'), ('Payslip', 'Payslip'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    employee_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Employee Name")
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    time_logs = models.JSONField(default=list, blank=True, null=True, verbose_name="Time Sheets")
    total_hours = models.FloatField(default=0.0, verbose_name="Total Working Hours")
    total_billable_hours = models.FloatField(default=0.0, verbose_name="Total Billable Hours")
    total_billed_hours = models.FloatField(default=0.0, verbose_name="Total Billed Hours")
    total_costing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Costing Amount")
    total_billable_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billable Amount")
    total_billed_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billed Amount")
    per_billed = models.TextField(blank=True, null=True, verbose_name="% Amount Billed")
    note = models.TextField(blank=True, null=True, verbose_name="Note")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    parent_project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    base_total_costing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Total Costing Amount")
    base_total_billable_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Total Billable Amount")
    base_total_billed_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Total Billed Amount")
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'

class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer

class ProjectUser(BaseDocument):
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')
    email = models.TextField(blank=True, null=True, verbose_name="Email")
    image = models.TextField(blank=True, null=True, verbose_name="Image")
    full_name = models.TextField(blank=True, null=True, verbose_name="Full Name")
    welcome_email_sent = models.BooleanField(default=False, verbose_name="Welcome email sent")
    view_attachments = models.BooleanField(default=False, verbose_name="View attachments")
    hide_timesheets = models.BooleanField(default=False, verbose_name="Hide timesheets")
    project_status = models.TextField(blank=True, null=True, verbose_name="Project Status")

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = '__all__'

class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
