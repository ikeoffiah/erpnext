from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Additional imports
from django.db.models import FileField
from django.conf import settings
from django.core.exceptions import ValidationError

class BaseDocument(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="%(class)s_owner")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="%(class)s_modified_by")
    creation = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    docstatus = models.IntegerField(default=0)
    idx = models.IntegerField(default=0)

    class Meta:
        abstract = True

class Currency(BaseDocument):
    pass

class Country(BaseDocument):
    pass

class Account(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Account')
    # Placeholder for account details

class FinanceBook(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Finance Book')
    # Additional fields can be added as needed

class LetterHead(BaseDocument):
    pass

class HolidayList(BaseDocument):
    pass

class Warehouse(BaseDocument):
    pass

class CostCenter(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Cost Center')
    # Placeholder

class PaymentTermsTemplate(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Payment Terms Template')
    # Placeholder

class Role(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Role')
    # Placeholder

class Contact(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Contact')
    # Placeholder

class TermsAndConditions(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Terms and Conditions')
    # Placeholder

class Company(BaseDocument):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Company')
    abbr = models.CharField(max_length=255, blank=True, null=True, verbose_name='Abbreviation')
    is_group = models.BooleanField(default=False, verbose_name='Is Group')
    # Minimal fields for migration; extend later as needed

class BankAccountSubtype(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Bank Account Subtype')

class BankAccountType(BaseDocument):
    name = models.CharField(max_length=255, unique=True, verbose_name='Bank Account Type')

class BankStatementImportLogColumnMap(BaseDocument):
    # Placeholder for column mapping details
    mapping = models.JSONField(default=dict, blank=True, null=True, verbose_name='Column Mapping')

    account_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Account Name')
    account_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='Account Number')
    is_group = models.BooleanField(default=False, verbose_name='Is Group')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    root_type = models.CharField(max_length=255, choices=[('Asset', 'Asset'), ('Liability', 'Liability'), ('Income', 'Income'), ('Expense', 'Expense'), ('Equity', 'Equity')], blank=True, null=True, verbose_name='Root Type')
    report_type = models.CharField(max_length=255, choices=[('Balance Sheet', 'Balance Sheet'), ('Profit and Loss', 'Profit and Loss')], blank=True, null=True, verbose_name='Report Type')
    account_currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    exception_budget_approver_role = models.ForeignKey('Role', on_delete=models.SET_NULL, blank=True, null=True, related_name='company_exception_budget_roles', verbose_name='Exception Budget Approver Role')
    account_type = models.CharField(max_length=255, choices=[('Accumulated Depreciation', 'Accumulated Depreciation'), ('Asset Received But Not Billed', 'Asset Received But Not Billed'), ('Bank', 'Bank'), ('Cash', 'Cash'), ('Chargeable', 'Chargeable'), ('Capital Work in Progress', 'Capital Work in Progress'), ('Cost of Goods Sold', 'Cost of Goods Sold'), ('Current Asset', 'Current Asset'), ('Current Liability', 'Current Liability'), ('Depreciation', 'Depreciation'), ('Direct Expense', 'Direct Expense'), ('Direct Income', 'Direct Income'), ('Equity', 'Equity'), ('Expense Account', 'Expense Account'), ('Expenses Included In Asset Valuation', 'Expenses Included In Asset Valuation'), ('Expenses Included In Valuation', 'Expenses Included In Valuation'), ('Fixed Asset', 'Fixed Asset'), ('Income Account', 'Income Account'), ('Indirect Expense', 'Indirect Expense'), ('Indirect Income', 'Indirect Income'), ('Liability', 'Liability'), ('Payable', 'Payable'), ('Receivable', 'Receivable'), ('Round Off', 'Round Off'), ('Round Off for Opening', 'Round Off for Opening'), ('Stock', 'Stock'), ('Stock Adjustment', 'Stock Adjustment'), ('Stock Received But Not Billed', 'Stock Received But Not Billed'), ('Service Received But Not Billed', 'Service Received But Not Billed'), ('Tax', 'Tax'), ('Temporary', 'Temporary')], blank=True, null=True, verbose_name='Account Type')
    tax_rate = models.FloatField(default=0.0, verbose_name='Tax Rate')
    freeze_account = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Frozen')
    balance_must_be = models.CharField(max_length=255, choices=[('Debit', 'Debit'), ('Credit', 'Credit')], blank=True, null=True, verbose_name='Balance must be')
    lft = models.IntegerField(default=0, verbose_name='Lft')
    rgt = models.IntegerField(default=0, verbose_name='Rgt')
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name='Old Parent')
    include_in_gross = models.BooleanField(default=False, verbose_name='Include in gross')
    disabled = models.BooleanField(default=False, verbose_name='Disable')
    account_category = models.ForeignKey('Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Category')

    def clean(self):
        super().clean()
        self.validate_parent()

    def validate_parent(self):
        if self.parent_account:
            if self.parent_account.name == self.name:
                raise ValidationError("You can not assign itself as parent account")
            if not self.parent_account.is_group:
                raise ValidationError(f"Parent account {self.parent_account.name} can not be a ledger")
            if self.parent_account.company != self.company:
                raise ValidationError(f"Parent account {self.parent_account.name} does not belong to company: {self.company}")
class Bank(BaseDocument):
    bank_name = models.CharField(max_length=255, unique=True, verbose_name='Bank Name')
    swift_number = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name='SWIFT number')
    website = models.URLField(max_length=255, blank=True, null=True, verbose_name='Website')
    address_html = models.TextField(blank=True, null=True, verbose_name='Address HTML')
    contact_html = models.TextField(blank=True, null=True, verbose_name='Contact HTML')
    plaid_access_token = models.CharField(max_length=255, blank=True, null=True, verbose_name='Plaid Access Token', editable=False)

class BankAccount(BaseDocument):
    account_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Account Name')
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Account')
    bank = models.ForeignKey('Bank', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank')
    account_type = models.ForeignKey('BankAccountType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Type')
    account_subtype = models.ForeignKey('BankAccountSubtype', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Subtype')
    is_default = models.BooleanField(default=False, verbose_name='Is Default Account')
    is_company_account = models.BooleanField(default=False, verbose_name='Is Company Account')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    disabled = models.BooleanField(default=False, verbose_name='Disabled')
    is_credit_card = models.BooleanField(default=False, verbose_name='Is Credit Card')
    party_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Party Type')
    party = models.CharField(max_length=255, blank=True, null=True, verbose_name='Party')
    address_html = models.TextField(blank=True, null=True, verbose_name='Address HTML')
    contact_html = models.TextField(blank=True, null=True, verbose_name='Contact HTML')
    integration_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='Integration ID', editable=False)
    last_integration_date = models.DateField(blank=True, null=True, verbose_name='Last Integration Date')
    mask = models.CharField(max_length=255, blank=True, null=True, verbose_name='Mask', editable=False)
    branch_code = models.CharField(max_length=255, blank=True, null=True, verbose_name='Branch Code')
    bank_account_no = models.CharField(max_length=255, blank=True, null=True, verbose_name='Bank Account No')

class BankStatementImportLog(BaseDocument):
    bank_account = models.ForeignKey('BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    file = models.FileField(upload_to='bank_statements/', verbose_name='File')
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started', verbose_name='Status')
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    number_of_transactions = models.PositiveIntegerField(default=0, verbose_name='Number of Transactions')
    closing_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='Closing Balance')
    start_date = models.DateField(blank=True, null=True, verbose_name='Start Date')
    end_date = models.DateField(blank=True, null=True, verbose_name='End Date')
    total_debits = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total Debits')
    total_credits = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total Credits')
    total_debit_transactions = models.PositiveIntegerField(default=0, verbose_name='Total Debit Transactions')
    total_credit_transactions = models.PositiveIntegerField(default=0, verbose_name='Total Credit Transactions')

    # Additional fields for statement format detection could be added as needed

# =====================================================================
# BATCH 1: CRM & SALES
# =====================================================================

class Customer(BaseDocument):
    customer_name = models.CharField(max_length=255, verbose_name='Customer Name')
    customer_group = models.CharField(max_length=255, blank=True, null=True, verbose_name='Customer Group')
    territory = models.CharField(max_length=255, blank=True, null=True, verbose_name='Territory')
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Account')

class Lead(BaseDocument):
    lead_name = models.CharField(max_length=255, verbose_name='Lead Name')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Company Name')
    email_id = models.EmailField(blank=True, null=True, verbose_name='Email Id')
    mobile_no = models.CharField(max_length=50, blank=True, null=True, verbose_name='Mobile No')
    status = models.CharField(max_length=50, default='Lead', verbose_name='Status')

class Opportunity(BaseDocument):
    opportunity_from = models.CharField(max_length=255, choices=[('Lead', 'Lead'), ('Customer', 'Customer')], default='Lead', verbose_name='Opportunity From')
    party_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Party Name')
    opportunity_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Opportunity Amount')
    status = models.CharField(max_length=50, default='Open', verbose_name='Status')

class Quotation(BaseDocument):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    transaction_date = models.DateField(auto_now_add=True, verbose_name='Date')
    valid_till = models.DateField(blank=True, null=True, verbose_name='Valid Till')
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

class SalesOrder(BaseDocument):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    transaction_date = models.DateField(auto_now_add=True, verbose_name='Date')
    delivery_date = models.DateField(blank=True, null=True, verbose_name='Delivery Date')
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

class SalesInvoice(BaseDocument):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    posting_date = models.DateField(auto_now_add=True, verbose_name='Posting Date')
    due_date = models.DateField(blank=True, null=True, verbose_name='Due Date')
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

# =====================================================================
# BATCH 1: PURCHASE & INVENTORY
# =====================================================================

class Supplier(BaseDocument):
    supplier_name = models.CharField(max_length=255, verbose_name='Supplier Name')
    supplier_group = models.CharField(max_length=255, blank=True, null=True, verbose_name='Supplier Group')
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Account')

class Item(BaseDocument):
    item_code = models.CharField(max_length=255, unique=True, verbose_name='Item Code')
    item_name = models.CharField(max_length=255, verbose_name='Item Name')
    item_group = models.CharField(max_length=255, blank=True, null=True, verbose_name='Item Group')
    stock_uom = models.CharField(max_length=50, default='Nos', verbose_name='Default Unit of Measure')
    standard_rate = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Standard Rate')

class PurchaseOrder(BaseDocument):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    transaction_date = models.DateField(auto_now_add=True, verbose_name='Date')
    schedule_date = models.DateField(blank=True, null=True, verbose_name='Reqd by Date')
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

class PurchaseInvoice(BaseDocument):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    posting_date = models.DateField(auto_now_add=True, verbose_name='Posting Date')
    due_date = models.DateField(blank=True, null=True, verbose_name='Due Date')
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

# =====================================================================
# BATCH 2: HR & PAYROLL
# =====================================================================

class Employee(BaseDocument):
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last Name')
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    date_of_joining = models.DateField(blank=True, null=True, verbose_name='Date of Joining')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='Department')
    designation = models.CharField(max_length=255, blank=True, null=True, verbose_name='Designation')
    status = models.CharField(max_length=50, default='Active', verbose_name='Status')

class Attendance(BaseDocument):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    attendance_date = models.DateField(verbose_name='Attendance Date')
    status = models.CharField(max_length=50, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Half Day', 'Half Day'), ('On Leave', 'On Leave')], verbose_name='Status')

class LeaveApplication(BaseDocument):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    leave_type = models.CharField(max_length=255, verbose_name='Leave Type')
    from_date = models.DateField(verbose_name='From Date')
    to_date = models.DateField(verbose_name='To Date')
    status = models.CharField(max_length=50, default='Open', verbose_name='Status')

class SalarySlip(BaseDocument):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    gross_pay = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Gross Pay')
    total_deduction = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total Deduction')
    net_pay = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Net Pay')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

# =====================================================================
# BATCH 2: MANUFACTURING & PROJECTS
# =====================================================================

class BOM(BaseDocument):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item')
    quantity = models.DecimalField(max_digits=18, decimal_places=2, default=1, verbose_name='Quantity')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    is_default = models.BooleanField(default=False, verbose_name='Is Default')

class WorkOrder(BaseDocument):
    production_item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Production Item')
    bom_no = models.ForeignKey(BOM, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='BOM')
    qty = models.DecimalField(max_digits=18, decimal_places=2, default=1, verbose_name='Qty to Manufacture')
    planned_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Planned Start Date')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

class ProductionPlan(BaseDocument):
    posting_date = models.DateField(auto_now_add=True, verbose_name='Date')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')

class Project(BaseDocument):
    project_name = models.CharField(max_length=255, verbose_name='Project Name')
    status = models.CharField(max_length=50, default='Open', verbose_name='Status')
    expected_start_date = models.DateField(blank=True, null=True, verbose_name='Expected Start Date')
    expected_end_date = models.DateField(blank=True, null=True, verbose_name='Expected End Date')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')

class Task(BaseDocument):
    subject = models.CharField(max_length=255, verbose_name='Subject')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    status = models.CharField(max_length=50, default='Open', verbose_name='Status')
    exp_start_date = models.DateField(blank=True, null=True, verbose_name='Expected Start Date')
    exp_end_date = models.DateField(blank=True, null=True, verbose_name='Expected End Date')

class Timesheet(BaseDocument):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')
    total_hours = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Total Hours')

# =====================================================================
# BATCH 2: ASSETS & SUPPORT
# =====================================================================

class Asset(BaseDocument):
    asset_name = models.CharField(max_length=255, verbose_name='Asset Name')
    item_code = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    status = models.CharField(max_length=50, default='Draft', verbose_name='Status')
    purchase_date = models.DateField(blank=True, null=True, verbose_name='Purchase Date')
    gross_purchase_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Gross Purchase Amount')

class AssetDepreciationSchedule(BaseDocument):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, verbose_name='Asset')
    schedule_date = models.DateField(verbose_name='Schedule Date')
    depreciation_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name='Depreciation Amount')

class Issue(BaseDocument):
    subject = models.CharField(max_length=255, verbose_name='Subject')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    status = models.CharField(max_length=50, default='Open', verbose_name='Status')
    priority = models.CharField(max_length=50, default='Medium', verbose_name='Priority')

class ServiceLevelAgreement(BaseDocument):
    sla_name = models.CharField(max_length=255, verbose_name='SLA Name')
    default_priority = models.CharField(max_length=50, default='Medium', verbose_name='Default Priority')
