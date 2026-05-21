from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class TransactionDeletionRecordToDelete(BaseDocument):
    doctype_name = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='DocType')
    company_field = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company Field")
    document_count = models.IntegerField(default=0, verbose_name="Document Count")
    child_doctypes = models.TextField(blank=True, null=True, verbose_name="Child DocTypes")
    deleted = models.BooleanField(default=False, verbose_name="Deleted")

class TransactionDeletionRecordToDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDeletionRecordToDelete
        fields = '__all__'

class TransactionDeletionRecordToDeleteViewSet(viewsets.ModelViewSet):
    queryset = TransactionDeletionRecordToDelete.objects.all()
    serializer_class = TransactionDeletionRecordToDeleteSerializer

class TargetDetail(BaseDocument):
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fiscal Year')
    target_qty = models.FloatField(default=0.0, verbose_name="Target Qty")
    target_amount = models.FloatField(default=0.0, verbose_name="Target  Amount")
    distribution_id = models.ForeignKey('erp_core.MonthlyDistribution', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Distribution')

class TargetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetDetail
        fields = '__all__'

class TargetDetailViewSet(viewsets.ModelViewSet):
    queryset = TargetDetail.objects.all()
    serializer_class = TargetDetailSerializer

class EmployeeInternalWorkHistory(BaseDocument):
    branch = models.ForeignKey('erp_core.Branch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Branch')
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    designation = models.ForeignKey('erp_core.Designation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Designation')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")

class EmployeeInternalWorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInternalWorkHistory
        fields = '__all__'

class EmployeeInternalWorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeInternalWorkHistory.objects.all()
    serializer_class = EmployeeInternalWorkHistorySerializer

class EmailDigestRecipient(BaseDocument):
    recipient = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Recipient')

class EmailDigestRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestRecipient
        fields = '__all__'

class EmailDigestRecipientViewSet(viewsets.ModelViewSet):
    queryset = EmailDigestRecipient.objects.all()
    serializer_class = EmailDigestRecipientSerializer

class Territory(BaseDocument):
    territory_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Territory Name")
    parent_territory = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Territory')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    territory_manager = models.ForeignKey('erp_core.SalesPerson', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory Manager')
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='old_parent')
    targets = models.JSONField(default=list, blank=True, null=True, verbose_name="Targets")

class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = '__all__'

class TerritoryViewSet(viewsets.ModelViewSet):
    queryset = Territory.objects.all()
    serializer_class = TerritorySerializer

class Branch(BaseDocument):
    branch = models.CharField(max_length=255, blank=True, null=True, verbose_name="Branch")

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class CurrencyExchange(BaseDocument):
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    from_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Currency')
    to_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To Currency')
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    for_buying = models.BooleanField(default=False, verbose_name="For Buying")
    for_selling = models.BooleanField(default=False, verbose_name="For Selling")

class CurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchange
        fields = '__all__'

class CurrencyExchangeViewSet(viewsets.ModelViewSet):
    queryset = CurrencyExchange.objects.all()
    serializer_class = CurrencyExchangeSerializer

class SalesPerson(BaseDocument):
    sales_person_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Person Name")
    parent_sales_person = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Sales Person')
    commission_rate = models.CharField(max_length=255, blank=True, null=True, verbose_name="Commission Rate")
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="old_parent")
    targets = models.JSONField(default=list, blank=True, null=True, verbose_name="Targets")

class SalesPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPerson
        fields = '__all__'

class SalesPersonViewSet(viewsets.ModelViewSet):
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializer

class Designation(BaseDocument):
    designation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Designation")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class Company(BaseDocument):
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company")
    abbr = models.CharField(max_length=255, blank=True, null=True, verbose_name="Abbr")
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    default_finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Finance Book')
    domain = models.CharField(max_length=255, blank=True, null=True, verbose_name="Domain")
    parent_company = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Company')
    company_logo = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Company Logo")
    company_description = models.TextField(blank=True, null=True, verbose_name="Company Description")
    sales_monthly_history = models.TextField(blank=True, null=True, verbose_name="Sales Monthly History")
    transactions_annual_history = models.TextField(blank=True, null=True, verbose_name="Transactions Annual History")
    monthly_sales_target = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Monthly Sales Target")
    total_monthly_sales = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Monthly Sales")
    default_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Currency')
    default_letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Letter Head')
    default_holiday_list = models.ForeignKey('erp_core.HolidayList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Holiday List')
    default_warehouse_for_sales_return = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Warehouse for Sales Return')
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')
    create_chart_of_accounts_based_on = models.CharField(max_length=255, choices=[('Standard Template', 'Standard Template'), ('Existing Company', 'Existing Company')], blank=True, null=True, verbose_name='Create Chart Of Accounts Based On')
    chart_of_accounts = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Chart Of Accounts Template')
    existing_company = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Existing Company ')
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax ID")
    date_of_establishment = models.DateField(blank=True, null=True, verbose_name="Date of Establishment")
    default_bank_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Bank Account')
    default_cash_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Cash Account')
    default_receivable_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Receivable Account')
    round_off_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Round Off Account')
    round_off_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Round Off Cost Center')
    write_off_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Account')
    exchange_gain_loss_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Exchange Gain / Loss Account')
    unrealized_exchange_gain_loss_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Unrealized Exchange Gain/Loss Account')
    allow_account_creation_against_child_company = models.BooleanField(default=False, verbose_name="Allow Account Creation Against Child Company")
    default_payable_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payable Account')
    default_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Cost of Goods Sold Account')
    default_income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Income Account')
    default_deferred_revenue_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Deferred Revenue Account')
    default_deferred_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Deferred Expense Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Cost Center')
    credit_limit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Limit")
    payment_terms = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payment Terms Template')
    enable_perpetual_inventory = models.BooleanField(default=False, verbose_name="Enable Perpetual Inventory")
    default_inventory_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Inventory Account')
    stock_adjustment_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Adjustment Account')
    stock_received_but_not_billed = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Received But Not Billed')
    accumulated_depreciation_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accumulated Depreciation Account')
    depreciation_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Depreciation Expense Account')
    series_for_depreciation_entry = models.CharField(max_length=255, blank=True, null=True, verbose_name="Series for Asset Depreciation Entry (Journal Entry)")
    disposal_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gain/Loss Account on Asset Disposal')
    depreciation_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Depreciation Cost Center')
    capital_work_in_progress_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Capital Work In Progress Account')
    asset_received_but_not_billed = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Received But Not Billed')
    exception_budget_approver_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Exception Budget Approver Role')
    date_of_incorporation = models.DateField(blank=True, null=True, verbose_name="Date of Incorporation")
    date_of_commencement = models.DateField(blank=True, null=True, verbose_name="Date of Commencement")
    phone_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone No")
    fax = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fax")
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    registration_details = models.TextField(blank=True, null=True, verbose_name="Registration Details")
    lft = models.IntegerField(default=0, verbose_name="Lft")
    rgt = models.IntegerField(default=0, verbose_name="Rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="old_parent")
    default_selling_terms = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Selling Terms')
    default_buying_terms = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Buying Terms')
    default_in_transit_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default In-Transit Warehouse')
    unrealized_profit_loss_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Unrealized Profit / Loss Account')
    default_discount_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payment Discount Account')
    enable_provisional_accounting_for_non_stock_items = models.BooleanField(default=False, verbose_name="Enable Provisional Accounting For Non Stock Items")
    default_provisional_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Provisional Account')
    default_advance_received_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Advance Received Account')
    default_advance_paid_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Advance Paid Account')
    book_advance_payments_in_separate_party_account = models.BooleanField(default=False, verbose_name="Book Advance Payments in Separate Party Account")
    auto_exchange_rate_revaluation = models.BooleanField(default=False, verbose_name="Auto Create Exchange Rate Revaluation")
    auto_err_frequency = models.CharField(max_length=255, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], blank=True, null=True, verbose_name='Frequency')
    submit_err_jv = models.BooleanField(default=False, verbose_name="Submit ERR Journals?")
    reconcile_on_advance_payment_date = models.BooleanField(default=False, verbose_name="Reconcile on Advance Payment Date")
    default_operating_cost_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Operating Cost Account')
    round_off_for_opening = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Round Off for Opening')
    reconciliation_takes_effect_on = models.CharField(max_length=255, choices=[('Advance Payment Date', 'Advance Payment Date'), ('Oldest Of Invoice Or Advance', 'Oldest Of Invoice Or Advance'), ('Reconciliation Date', 'Reconciliation Date')], blank=True, null=True, verbose_name='Reconciliation Takes Effect On')
    reporting_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reporting Currency')
    purchase_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Expense Account')
    purchase_expense_contra_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Expense Contra Account')
    service_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Service Expense Account')
    enable_item_wise_inventory_account = models.BooleanField(default=False, verbose_name="Enable Item-wise Inventory Account")
    valuation_method = models.CharField(max_length=255, choices=[('FIFO', 'FIFO'), ('Moving Average', 'Moving Average'), ('LIFO', 'LIFO')], blank=True, null=True, verbose_name='Default Stock Valuation Method')
    default_wip_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name=' Default Work In Progress Warehouse ')
    default_fg_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Finished Goods Warehouse')
    default_scrap_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Scrap Warehouse')
    default_sales_contact = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Sales Contact')
    accounts_frozen_till_date = models.DateField(blank=True, null=True, verbose_name="Accounts Frozen Till Date")
    role_allowed_for_frozen_entries = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Roles Allowed to Set and Edit Frozen Account Entries')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class GlobalDefaults(BaseDocument):
    default_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Company')
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')
    default_distance_unit = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Distance Unit')
    default_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Currency')
    hide_currency_symbol = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Hide Currency Symbol')
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    disable_in_words = models.BooleanField(default=False, verbose_name="Disable In Words")
    demo_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Demo Company')
    use_posting_datetime_for_naming_documents = models.BooleanField(default=False, verbose_name="Use Posting Datetime for Naming Documents")

class GlobalDefaultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalDefaults
        fields = '__all__'

class GlobalDefaultsViewSet(viewsets.ModelViewSet):
    queryset = GlobalDefaults.objects.all()
    serializer_class = GlobalDefaultsSerializer

class EmployeeEducation(BaseDocument):
    school_univ = models.TextField(blank=True, null=True, verbose_name="School/University")
    qualification = models.CharField(max_length=255, blank=True, null=True, verbose_name="Qualification")
    level = models.CharField(max_length=255, choices=[('Graduate', 'Graduate'), ('Post Graduate', 'Post Graduate'), ('Under Graduate', 'Under Graduate')], blank=True, null=True, verbose_name='Level')
    year_of_passing = models.IntegerField(default=0, verbose_name="Year of Passing")
    class_per = models.CharField(max_length=255, blank=True, null=True, verbose_name="Class / Percentage")
    maj_opt_subj = models.TextField(blank=True, null=True, verbose_name="Major/Optional Subjects")

class EmployeeEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEducation
        fields = '__all__'

class EmployeeEducationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeEducation.objects.all()
    serializer_class = EmployeeEducationSerializer

class TermsandConditions(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    selling = models.BooleanField(default=False, verbose_name="Selling")
    buying = models.BooleanField(default=False, verbose_name="Buying")
    copy_attachments_to_transaction = models.BooleanField(default=False, verbose_name="Copy Attachments to Transaction")

class TermsandConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsandConditions
        fields = '__all__'

class TermsandConditionsViewSet(viewsets.ModelViewSet):
    queryset = TermsandConditions.objects.all()
    serializer_class = TermsandConditionsSerializer

class Vehicle(BaseDocument):
    license_plate = models.CharField(max_length=255, blank=True, null=True, verbose_name="License Plate")
    make = models.CharField(max_length=255, blank=True, null=True, verbose_name="Make")
    model = models.CharField(max_length=255, blank=True, null=True, verbose_name="Model")
    last_odometer = models.IntegerField(default=0, verbose_name="Odometer Value (Last)")
    acquisition_date = models.DateField(blank=True, null=True, verbose_name="Acquisition Date")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Location")
    chassis_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Chassis No")
    vehicle_value = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Vehicle Value")
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    insurance_company = models.CharField(max_length=255, blank=True, null=True, verbose_name="Insurance Company")
    policy_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Policy No")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    fuel_type = models.CharField(max_length=255, choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Natural Gas', 'Natural Gas'), ('Electric', 'Electric')], blank=True, null=True, verbose_name='Fuel Type')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fuel UOM')
    carbon_check_date = models.DateField(blank=True, null=True, verbose_name="Last Carbon Check")
    color = models.CharField(max_length=255, blank=True, null=True, verbose_name="Color")
    wheels = models.IntegerField(default=0, verbose_name="Wheels")
    doors = models.IntegerField(default=0, verbose_name="Doors")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class Brand(BaseDocument):
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name="Brand Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    brand_defaults = models.JSONField(default=list, blank=True, null=True, verbose_name="Brand Defaults")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AuthorizationControl(BaseDocument):

class AuthorizationControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationControl
        fields = '__all__'

class AuthorizationControlViewSet(viewsets.ModelViewSet):
    queryset = AuthorizationControl.objects.all()
    serializer_class = AuthorizationControlSerializer

class CustomerGroup(BaseDocument):
    customer_group_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Group Name")
    parent_customer_group = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Customer Group')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    default_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Price List')
    payment_terms = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payment Terms Template')
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='old_parent')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    credit_limits = models.JSONField(default=list, blank=True, null=True, verbose_name="Credit Limit")

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = '__all__'

class CustomerGroupViewSet(viewsets.ModelViewSet):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer

class SalesPartner(BaseDocument):
    partner_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Partner Name")
    partner_type = models.ForeignKey('erp_core.SalesPartnerType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Partner Type')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    commission_rate = models.FloatField(default=0.0, verbose_name="Commission Rate")
    targets = models.JSONField(default=list, blank=True, null=True, verbose_name="Targets")
    show_in_website = models.BooleanField(default=False, verbose_name="Show In Website")
    referral_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Referral Code")
    route = models.CharField(max_length=255, blank=True, null=True, verbose_name="Route")
    logo = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Logo")
    partner_website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Partner website")
    introduction = models.TextField(blank=True, null=True, verbose_name="Introduction")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class SalesPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPartner
        fields = '__all__'

class SalesPartnerViewSet(viewsets.ModelViewSet):
    queryset = SalesPartner.objects.all()
    serializer_class = SalesPartnerSerializer

class QuotationLostReason(BaseDocument):
    order_lost_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name="Quotation Lost Reason")

class QuotationLostReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationLostReason
        fields = '__all__'

class QuotationLostReasonViewSet(viewsets.ModelViewSet):
    queryset = QuotationLostReason.objects.all()
    serializer_class = QuotationLostReasonSerializer

class UOM(BaseDocument):
    uom_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="UOM Name")
    must_be_whole_number = models.BooleanField(default=False, verbose_name="Must be Whole Number")
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    symbol = models.CharField(max_length=255, blank=True, null=True, verbose_name="Symbol")
    common_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Common Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    category = models.ForeignKey('erp_core.UOMCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Category')

class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'

class UOMViewSet(viewsets.ModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer

class WebsiteItemGroup(BaseDocument):
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')

class WebsiteItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteItemGroup
        fields = '__all__'

class WebsiteItemGroupViewSet(viewsets.ModelViewSet):
    queryset = WebsiteItemGroup.objects.all()
    serializer_class = WebsiteItemGroupSerializer

class HolidayList(BaseDocument):
    holiday_list_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Holiday List Name")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    total_holidays = models.IntegerField(default=0, verbose_name="Total Holidays")
    weekly_off = models.CharField(max_length=255, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], blank=True, null=True, verbose_name='Weekly Off')
    holidays = models.JSONField(default=list, blank=True, null=True, verbose_name="Holidays")
    color = models.TextField(blank=True, null=True, verbose_name="Color")
    country = models.TextField(blank=True, null=True, verbose_name="Country")
    subdivision = models.TextField(blank=True, null=True, verbose_name="Subdivision")
    is_half_day = models.BooleanField(default=False, verbose_name="Is Half Day")

class HolidayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayList
        fields = '__all__'

class HolidayListViewSet(viewsets.ModelViewSet):
    queryset = HolidayList.objects.all()
    serializer_class = HolidayListSerializer

class UOMConversionFactor(BaseDocument):
    category = models.ForeignKey('erp_core.UOMCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Category')
    from_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From')
    to_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To')
    value = models.FloatField(default=0.0, verbose_name="Value")

class UOMConversionFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMConversionFactor
        fields = '__all__'

class UOMConversionFactorViewSet(viewsets.ModelViewSet):
    queryset = UOMConversionFactor.objects.all()
    serializer_class = UOMConversionFactorSerializer

class DrivingLicenseCategory(BaseDocument):
    class = models.CharField(max_length=255, blank=True, null=True, verbose_name="Driver licence class")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")
    issuing_date = models.DateField(blank=True, null=True, verbose_name="Issuing Date")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Expiry Date")

class DrivingLicenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingLicenseCategory
        fields = '__all__'

class DrivingLicenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = DrivingLicenseCategory.objects.all()
    serializer_class = DrivingLicenseCategorySerializer

class AuthorizationRule(BaseDocument):
    transaction = models.CharField(max_length=255, choices=[('Sales Order', 'Sales Order'), ('Purchase Order', 'Purchase Order'), ('Quotation', 'Quotation'), ('Delivery Note', 'Delivery Note'), ('Sales Invoice', 'Sales Invoice'), ('Purchase Invoice', 'Purchase Invoice'), ('Purchase Receipt', 'Purchase Receipt')], blank=True, null=True, verbose_name='Transaction')
    based_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Average Discount', 'Average Discount'), ('Customerwise Discount', 'Customerwise Discount'), ('Itemwise Discount', 'Itemwise Discount'), ('Item Group wise Discount', 'Item Group wise Discount'), ('Not Applicable', 'Not Applicable')], blank=True, null=True, verbose_name='Based On')
    customer_or_item = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Item', 'Item'), ('Item Group', 'Item Group')], blank=True, null=True, verbose_name='Customer or Item')
    master_name = models.TextField(blank=True, null=True, verbose_name="Customer / Item / Item Group")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    value = models.FloatField(default=0.0, verbose_name="Authorized Value")
    system_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Applicable To (Role)')
    to_emp = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Applicable To (Employee)')
    system_user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Applicable To (User)')
    to_designation = models.ForeignKey('erp_core.Designation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Applicable To (Designation)')
    approving_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Approving Role (above authorized value)')
    approving_user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Approving User  (above authorized value)')

class AuthorizationRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationRule
        fields = '__all__'

class AuthorizationRuleViewSet(viewsets.ModelViewSet):
    queryset = AuthorizationRule.objects.all()
    serializer_class = AuthorizationRuleSerializer

class PartyType(BaseDocument):
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    account_type = models.CharField(max_length=255, choices=[('Payable', 'Payable'), ('Receivable', 'Receivable')], blank=True, null=True, verbose_name='Account Type')

class PartyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyType
        fields = '__all__'

class PartyTypeViewSet(viewsets.ModelViewSet):
    queryset = PartyType.objects.all()
    serializer_class = PartyTypeSerializer

class TransactionDeletionRecordItem(BaseDocument):
    doctype_name = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='DocType')

class TransactionDeletionRecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDeletionRecordItem
        fields = '__all__'

class TransactionDeletionRecordItemViewSet(viewsets.ModelViewSet):
    queryset = TransactionDeletionRecordItem.objects.all()
    serializer_class = TransactionDeletionRecordItemSerializer

class EmployeeExternalWorkHistory(BaseDocument):
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company")
    designation = models.CharField(max_length=255, blank=True, null=True, verbose_name="Designation")
    salary = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Salary")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    contact = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact")
    total_experience = models.CharField(max_length=255, blank=True, null=True, verbose_name="Total Experience")

class EmployeeExternalWorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeExternalWorkHistory
        fields = '__all__'

class EmployeeExternalWorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeExternalWorkHistory.objects.all()
    serializer_class = EmployeeExternalWorkHistorySerializer

class TransactionDeletionRecord(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    doctypes = models.JSONField(default=list, blank=True, null=True, verbose_name="Summary")
    doctypes_to_delete = models.JSONField(default=list, blank=True, null=True, verbose_name="DocTypes To Delete")
    doctypes_to_be_ignored = models.JSONField(default=list, blank=True, null=True, verbose_name="Excluded DocTypes")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('Running', 'Running'), ('Failed', 'Failed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    delete_bin_data_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Skipped', 'Skipped')], blank=True, null=True, verbose_name='Delete Bins')
    delete_leads_and_addresses_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Skipped', 'Skipped')], blank=True, null=True, verbose_name='Delete Leads and Addresses')
    reset_company_default_values_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Skipped', 'Skipped')], blank=True, null=True, verbose_name='Reset Company Default Values')
    clear_notifications_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Skipped', 'Skipped')], blank=True, null=True, verbose_name='Clear Notifications')
    initialize_doctypes_table_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Skipped', 'Skipped')], blank=True, null=True, verbose_name='Initialize Summary Table')
    delete_transactions_status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Skipped', 'Skipped')], blank=True, null=True, verbose_name='Delete Transactions')
    error_log = models.TextField(blank=True, null=True, verbose_name="Error Log")
    process_in_single_transaction = models.BooleanField(default=False, verbose_name="Process in Single Transaction")

class TransactionDeletionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDeletionRecord
        fields = '__all__'

class TransactionDeletionRecordViewSet(viewsets.ModelViewSet):
    queryset = TransactionDeletionRecord.objects.all()
    serializer_class = TransactionDeletionRecordSerializer

class ItemGroup(BaseDocument):
    item_group_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Group Name")
    parent_item_group = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Item Group')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    item_group_defaults = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Group Defaults")
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Taxes")
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='old_parent')

class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = '__all__'

class ItemGroupViewSet(viewsets.ModelViewSet):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer

class Employee(BaseDocument):
    employee = models.CharField(max_length=255, blank=True, null=True, verbose_name="Employee")
    naming_series = models.CharField(max_length=255, choices=[('HR-EMP-', 'HR-EMP-')], blank=True, null=True, verbose_name='Series')
    salutation = models.ForeignKey('erp_core.Salutation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Salutation')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Middle Name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Name")
    employee_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    status = models.CharField(max_length=255, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended'), ('Left', 'Left')], blank=True, null=True, verbose_name='Status')
    employee_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Employee Number")
    gender = models.ForeignKey('erp_core.Gender', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    date_of_joining = models.DateField(blank=True, null=True, verbose_name="Date of Joining")
    emergency_phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Emergency Phone")
    person_to_be_contacted = models.CharField(max_length=255, blank=True, null=True, verbose_name="Emergency Contact Name")
    relation = models.CharField(max_length=255, blank=True, null=True, verbose_name="Relation")
    user_id = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User ID')
    create_user_permission = models.BooleanField(default=False, verbose_name="Create User Permission")
    create_user_automatically = models.BooleanField(default=False, verbose_name="Create User Automatically")
    scheduled_confirmation_date = models.DateField(blank=True, null=True, verbose_name="Offer Date")
    final_confirmation_date = models.DateField(blank=True, null=True, verbose_name="Confirmation Date")
    contract_end_date = models.DateField(blank=True, null=True, verbose_name="Contract End Date")
    notice_number_of_days = models.IntegerField(default=0, verbose_name="Notice (days)")
    date_of_retirement = models.DateField(blank=True, null=True, verbose_name="Date Of Retirement")
    department = models.ForeignKey('erp_core.Department', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Department')
    designation = models.ForeignKey('erp_core.Designation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Designation')
    reports_to = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reports to')
    branch = models.ForeignKey('erp_core.Branch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Branch')
    holiday_list = models.ForeignKey('erp_core.HolidayList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Holiday List')
    salary_mode = models.CharField(max_length=255, choices=[('Bank', 'Bank'), ('Cash', 'Cash'), ('Cheque', 'Cheque')], blank=True, null=True, verbose_name='Salary Mode')
    bank_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank Name")
    bank_ac_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank A/C No.")
    cell_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile")
    prefered_contact_email = models.CharField(max_length=255, choices=[('Company Email', 'Company Email'), ('Personal Email', 'Personal Email'), ('User ID', 'User ID')], blank=True, null=True, verbose_name='Preferred Contact Email')
    prefered_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Preferred Email")
    company_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company Email")
    personal_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Personal Email")
    unsubscribed = models.BooleanField(default=False, verbose_name="Unsubscribed")
    permanent_accommodation_type = models.CharField(max_length=255, choices=[('Rented', 'Rented'), ('Owned', 'Owned')], blank=True, null=True, verbose_name='Permanent Address Is')
    permanent_address = models.TextField(blank=True, null=True, verbose_name="Permanent Address")
    current_accommodation_type = models.CharField(max_length=255, choices=[('Rented', 'Rented'), ('Owned', 'Owned')], blank=True, null=True, verbose_name='Current Address Is')
    current_address = models.TextField(blank=True, null=True, verbose_name="Current Address")
    bio = models.TextField(blank=True, null=True, verbose_name="Bio / Cover Letter")
    passport_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Passport Number")
    date_of_issue = models.DateField(blank=True, null=True, verbose_name="Date of Issue")
    valid_upto = models.DateField(blank=True, null=True, verbose_name="Valid Up To")
    place_of_issue = models.CharField(max_length=255, blank=True, null=True, verbose_name="Place of Issue")
    marital_status = models.CharField(max_length=255, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], blank=True, null=True, verbose_name='Marital Status')
    blood_group = models.CharField(max_length=255, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], blank=True, null=True, verbose_name='Blood Group')
    family_background = models.TextField(blank=True, null=True, verbose_name="Family Background")
    health_details = models.TextField(blank=True, null=True, verbose_name="Health Details")
    education = models.JSONField(default=list, blank=True, null=True, verbose_name="Education")
    external_work_history = models.JSONField(default=list, blank=True, null=True, verbose_name="External Work History")
    internal_work_history = models.JSONField(default=list, blank=True, null=True, verbose_name="Internal Work History")
    resignation_letter_date = models.DateField(blank=True, null=True, verbose_name="Resignation Letter Date")
    relieving_date = models.DateField(blank=True, null=True, verbose_name="Relieving Date")
    reason_for_leaving = models.TextField(blank=True, null=True, verbose_name="Reason for Leaving")
    leave_encashed = models.CharField(max_length=255, choices=[('Yes', 'Yes'), ('No', 'No')], blank=True, null=True, verbose_name='Leave Encashed?')
    encashment_date = models.DateField(blank=True, null=True, verbose_name="Encashment Date")
    held_on = models.DateField(blank=True, null=True, verbose_name="Exit Interview Held On")
    new_workplace = models.CharField(max_length=255, blank=True, null=True, verbose_name="New Workplace")
    feedback = models.TextField(blank=True, null=True, verbose_name="Feedback")
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="Old Parent")
    attendance_device_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Attendance Device ID (Biometric/RF tag ID)")
    salary_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Salary Currency')
    ctc = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Cost to Company (CTC)")
    iban = models.CharField(max_length=255, blank=True, null=True, verbose_name="IBAN")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeGroup(BaseDocument):
    employee_group_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")
    employee_list = models.JSONField(default=list, blank=True, null=True, verbose_name="Employee")

class EmployeeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGroup
        fields = '__all__'

class EmployeeGroupViewSet(viewsets.ModelViewSet):
    queryset = EmployeeGroup.objects.all()
    serializer_class = EmployeeGroupSerializer

class QuotationLostReasonDetail(BaseDocument):
    lost_reason = models.ForeignKey('erp_core.QuotationLostReason', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quotation Lost Reason')

class QuotationLostReasonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationLostReasonDetail
        fields = '__all__'

class QuotationLostReasonDetailViewSet(viewsets.ModelViewSet):
    queryset = QuotationLostReasonDetail.objects.all()
    serializer_class = QuotationLostReasonDetailSerializer

class Incoterm(BaseDocument):
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Code")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class IncotermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incoterm
        fields = '__all__'

class IncotermViewSet(viewsets.ModelViewSet):
    queryset = Incoterm.objects.all()
    serializer_class = IncotermSerializer

class Department(BaseDocument):
    department_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Department")
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Department')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="Old Parent")

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmailDigest(BaseDocument):
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Company')
    frequency = models.CharField(max_length=255, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], blank=True, null=True, verbose_name='How frequently?')
    next_send = models.CharField(max_length=255, blank=True, null=True, verbose_name="Next email will be sent on:")
    income = models.BooleanField(default=False, verbose_name="New Income")
    expenses_booked = models.BooleanField(default=False, verbose_name="New Expenses")
    income_year_to_date = models.BooleanField(default=False, verbose_name="Annual Income")
    expense_year_to_date = models.BooleanField(default=False, verbose_name="Annual Expenses")
    bank_balance = models.BooleanField(default=False, verbose_name="Bank Balance")
    credit_balance = models.BooleanField(default=False, verbose_name="Bank Credit Balance")
    invoiced_amount = models.BooleanField(default=False, verbose_name="Receivables")
    payables = models.BooleanField(default=False, verbose_name="Payables")
    sales_orders_to_bill = models.BooleanField(default=False, verbose_name="Sales Orders to Bill")
    purchase_orders_to_bill = models.BooleanField(default=False, verbose_name="Purchase Orders to Bill")
    sales_order = models.BooleanField(default=False, verbose_name="New Sales Orders")
    purchase_order = models.BooleanField(default=False, verbose_name="New Purchase Orders")
    sales_orders_to_deliver = models.BooleanField(default=False, verbose_name="Sales Orders to Deliver")
    purchase_orders_to_receive = models.BooleanField(default=False, verbose_name="Purchase Orders to Receive")
    sales_invoice = models.BooleanField(default=False, verbose_name="New Sales Invoice")
    purchase_invoice = models.BooleanField(default=False, verbose_name="New Purchase Invoice")
    new_quotations = models.BooleanField(default=False, verbose_name="New Quotations")
    pending_quotations = models.BooleanField(default=False, verbose_name="Open Quotations")
    issue = models.BooleanField(default=False, verbose_name="Open Issues")
    project = models.BooleanField(default=False, verbose_name="Open Projects")
    purchase_orders_items_overdue = models.BooleanField(default=False, verbose_name="Purchase Orders Items Overdue")
    calendar_events = models.BooleanField(default=False, verbose_name="Upcoming Calendar Events")
    todo_list = models.BooleanField(default=False, verbose_name="Open To Do")
    notifications = models.BooleanField(default=False, verbose_name="Open Notifications")
    add_quote = models.BooleanField(default=False, verbose_name="Add Quote")
    recipients = models.TextField(blank=True, null=True, verbose_name="Recipients")

class EmailDigestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigest
        fields = '__all__'

class EmailDigestViewSet(viewsets.ModelViewSet):
    queryset = EmailDigest.objects.all()
    serializer_class = EmailDigestSerializer

class EmployeeGroupTable(BaseDocument):
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    employee_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Employee Name")
    user_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="ERPNext User ID")

class EmployeeGroupTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGroupTable
        fields = '__all__'

class EmployeeGroupTableViewSet(viewsets.ModelViewSet):
    queryset = EmployeeGroupTable.objects.all()
    serializer_class = EmployeeGroupTableSerializer

class SupplierGroup(BaseDocument):
    supplier_group_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Group Name")
    parent_supplier_group = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Supplier Group')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    payment_terms = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Payment Terms Template')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Old Parent')

class SupplierGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierGroup
        fields = '__all__'

class SupplierGroupViewSet(viewsets.ModelViewSet):
    queryset = SupplierGroup.objects.all()
    serializer_class = SupplierGroupSerializer

class Holiday(BaseDocument):
    holiday_date = models.DateField(blank=True, null=True, verbose_name="Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    weekly_off = models.BooleanField(default=False, verbose_name="Weekly Off")
    is_half_day = models.BooleanField(default=False, verbose_name="Is Half Day")

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

class Driver(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('HR-DRI-.YYYY.-', 'HR-DRI-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    status = models.CharField(max_length=255, choices=[('Active', 'Active'), ('Suspended', 'Suspended'), ('Left', 'Left')], blank=True, null=True, verbose_name='Status')
    transporter = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Transporter')
    employee = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    cell_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cellphone Number")
    license_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="License Number")
    issuing_date = models.DateField(blank=True, null=True, verbose_name="Issuing Date")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Expiry Date")
    driving_license_category = models.JSONField(default=list, blank=True, null=True, verbose_name="Driving License Category")
    address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Address')
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
