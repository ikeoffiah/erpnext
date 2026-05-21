from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class CouponCode(BaseDocument):
    coupon_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Coupon Name")
    coupon_type = models.CharField(max_length=255, choices=[('Promotional', 'Promotional'), ('Gift Card', 'Gift Card')], blank=True, null=True, verbose_name='Coupon Type')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    coupon_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Coupon Code")
    pricing_rule = models.ForeignKey('erp_core.PricingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pricing Rule')
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    valid_upto = models.DateField(blank=True, null=True, verbose_name="Valid Up To")
    maximum_use = models.IntegerField(default=0, verbose_name="Maximum Use")
    used = models.IntegerField(default=0, verbose_name="Used")
    description = models.TextField(blank=True, null=True, verbose_name="Coupon Description")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    from_external_ecomm_platform = models.BooleanField(default=False, verbose_name="From External Ecomm Platform")

class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponCode
        fields = '__all__'

class CouponCodeViewSet(viewsets.ModelViewSet):
    queryset = CouponCode.objects.all()
    serializer_class = CouponCodeSerializer

class PeggedCurrencies(BaseDocument):
    pegged_currency_item = models.JSONField(default=list, blank=True, null=True, verbose_name="pegged_currency_item")

class PeggedCurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeggedCurrencies
        fields = '__all__'

class PeggedCurrenciesViewSet(viewsets.ModelViewSet):
    queryset = PeggedCurrencies.objects.all()
    serializer_class = PeggedCurrenciesSerializer

class TaxCategory(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class TaxCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxCategory
        fields = '__all__'

class TaxCategoryViewSet(viewsets.ModelViewSet):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer

class PaymentSchedule(BaseDocument):
    payment_term = models.ForeignKey('erp_core.PaymentTerm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Term')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    invoice_portion = models.TextField(blank=True, null=True, verbose_name="Invoice Portion")
    payment_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Payment Amount")
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount")
    discounted_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discounted Amount")
    outstanding = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding")
    discount_date = models.DateField(blank=True, null=True, verbose_name="Discount Date")
    discount_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Discount Type')
    discount = models.FloatField(default=0.0, verbose_name="Discount")
    base_payment_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Payment Amount (Company Currency)")
    base_outstanding = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding (Company Currency)")
    base_paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount (Company Currency)")
    due_date_based_on = models.CharField(max_length=255, choices=[('Day(s) after invoice date', 'Day(s) after invoice date'), ('Day(s) after the end of the invoice month', 'Day(s) after the end of the invoice month'), ('Month(s) after the end of the invoice month', 'Month(s) after the end of the invoice month')], blank=True, null=True, verbose_name='Due Date Based On')
    credit_days = models.IntegerField(default=0, verbose_name="Credit Days")
    credit_months = models.IntegerField(default=0, verbose_name="Credit Months")
    discount_validity_based_on = models.CharField(max_length=255, choices=[('Day(s) after invoice date', 'Day(s) after invoice date'), ('Day(s) after the end of the invoice month', 'Day(s) after the end of the invoice month'), ('Month(s) after the end of the invoice month', 'Month(s) after the end of the invoice month')], blank=True, null=True, verbose_name='Discount Validity Based On')
    discount_validity = models.IntegerField(default=0, verbose_name="Discount Validity")

class PaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSchedule
        fields = '__all__'

class PaymentScheduleViewSet(viewsets.ModelViewSet):
    queryset = PaymentSchedule.objects.all()
    serializer_class = PaymentScheduleSerializer

class DunningLetterText(BaseDocument):
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Language')
    is_default_language = models.BooleanField(default=False, verbose_name="Is Default Language")
    body_text = models.TextField(blank=True, null=True, verbose_name="Body Text")
    closing_text = models.TextField(blank=True, null=True, verbose_name="Closing Text")

class DunningLetterTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = DunningLetterText
        fields = '__all__'

class DunningLetterTextViewSet(viewsets.ModelViewSet):
    queryset = DunningLetterText.objects.all()
    serializer_class = DunningLetterTextSerializer

class AccountCategory(BaseDocument):
    account_category_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    root_type = models.CharField(max_length=255, choices=[('Asset', 'Asset'), ('Liability', 'Liability'), ('Income', 'Income'), ('Expense', 'Expense'), ('Equity', 'Equity')], blank=True, null=True, verbose_name='Root Type')

class AccountCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCategory
        fields = '__all__'

class AccountCategoryViewSet(viewsets.ModelViewSet):
    queryset = AccountCategory.objects.all()
    serializer_class = AccountCategorySerializer

class PaymentEntry(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ACC-PAY-.YYYY.-', 'ACC-PAY-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    payment_type = models.CharField(max_length=255, choices=[('Receive', 'Receive'), ('Pay', 'Pay'), ('Internal Transfer', 'Internal Transfer')], blank=True, null=True, verbose_name='Payment Type')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    party_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Name")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact')
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email")
    paid_from = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Paid From')
    paid_from_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency (From)')
    paid_to = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Paid To')
    paid_to_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency (To)')
    paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount")
    source_exchange_rate = models.FloatField(default=0.0, verbose_name="Source Exchange Rate")
    base_paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount (Company Currency)")
    received_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Received Amount")
    target_exchange_rate = models.FloatField(default=0.0, verbose_name="Target Exchange Rate")
    base_received_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Received Amount (Company Currency)")
    references = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment References")
    total_allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Allocated Amount")
    base_total_allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Allocated Amount (Company Currency)")
    unallocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Unallocated Amount")
    difference_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference Amount (Company Currency)")
    deductions = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Deductions or Loss")
    reference_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cheque/Reference No")
    reference_date = models.DateField(blank=True, null=True, verbose_name="Cheque/Reference Date")
    clearance_date = models.DateField(blank=True, null=True, verbose_name="Clearance Date")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    bank = models.TextField(blank=True, null=True, verbose_name="Bank")
    bank_account_no = models.TextField(blank=True, null=True, verbose_name="Bank Account No")
    payment_order = models.ForeignKey('erp_core.PaymentOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Order')
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Bank Account')
    party_bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Bank Account')
    payment_order_status = models.CharField(max_length=255, choices=[('Initiated', 'Initiated'), ('Payment Ordered', 'Payment Ordered')], blank=True, null=True, verbose_name='Payment Order Status')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    custom_remarks = models.BooleanField(default=False, verbose_name="Custom Remarks")
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    purchase_taxes_and_charges_template = models.ForeignKey('erp_core.PurchaseTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Taxes and Charges Template')
    sales_taxes_and_charges_template = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Advance Taxes and Charges")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    paid_amount_after_tax = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount After Tax")
    base_paid_amount_after_tax = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount After Tax (Company Currency)")
    received_amount_after_tax = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Received Amount After Tax")
    base_received_amount_after_tax = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Received Amount After Tax (Company Currency)")
    paid_from_account_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Paid From Account Type")
    paid_to_account_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Paid To Account Type")
    book_advance_payments_in_separate_party_account = models.BooleanField(default=False, verbose_name="Book Advance Payments in Separate Party Account")
    base_in_words = models.TextField(blank=True, null=True, verbose_name="In Words (Company Currency)")
    in_words = models.TextField(blank=True, null=True, verbose_name="In Words")
    reconcile_on_advance_payment_date = models.BooleanField(default=False, verbose_name="Reconcile on Advance Payment Date")
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening')
    apply_tds = models.BooleanField(default=False, verbose_name="Consider for Tax Withholding")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')
    ignore_tax_withholding_threshold = models.BooleanField(default=False, verbose_name="Ignore Tax Withholding Threshold")
    tax_withholding_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="Tax Withholding Entries")
    override_tax_withholding_entries = models.BooleanField(default=False, verbose_name="Edit Tax Withholding Entries")

class PaymentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentEntry
        fields = '__all__'

class PaymentEntryViewSet(viewsets.ModelViewSet):
    queryset = PaymentEntry.objects.all()
    serializer_class = PaymentEntrySerializer

class LedgerMergeAccounts(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    merged = models.BooleanField(default=False, verbose_name="Merged")
    account_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Name")

class LedgerMergeAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerMergeAccounts
        fields = '__all__'

class LedgerMergeAccountsViewSet(viewsets.ModelViewSet):
    queryset = LedgerMergeAccounts.objects.all()
    serializer_class = LedgerMergeAccountsSerializer

class CostCenter(BaseDocument):
    cost_center_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cost Center Name")
    cost_center_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cost Center Number")
    parent_cost_center = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Cost Center')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    lft = models.IntegerField(default=0, verbose_name="lft")
    rgt = models.IntegerField(default=0, verbose_name="rgt")
    old_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='old_parent')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'

class CostCenterViewSet(viewsets.ModelViewSet):
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterSerializer

class JournalEntryTemplateAccount(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')

class JournalEntryTemplateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryTemplateAccount
        fields = '__all__'

class JournalEntryTemplateAccountViewSet(viewsets.ModelViewSet):
    queryset = JournalEntryTemplateAccount.objects.all()
    serializer_class = JournalEntryTemplateAccountSerializer

class ClosedDocument(BaseDocument):
    document_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Document Type')
    closed = models.BooleanField(default=False, verbose_name="Closed")

class ClosedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosedDocument
        fields = '__all__'

class ClosedDocumentViewSet(viewsets.ModelViewSet):
    queryset = ClosedDocument.objects.all()
    serializer_class = ClosedDocumentSerializer

class SalesPartnerItem(BaseDocument):
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner ')

class SalesPartnerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPartnerItem
        fields = '__all__'

class SalesPartnerItemViewSet(viewsets.ModelViewSet):
    queryset = SalesPartnerItem.objects.all()
    serializer_class = SalesPartnerItemSerializer

class BankAccountBalance(BaseDocument):
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    balance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Balance")

class BankAccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountBalance
        fields = '__all__'

class BankAccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = BankAccountBalance.objects.all()
    serializer_class = BankAccountBalanceSerializer

class BankAccount(BaseDocument):
    account_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Name")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Account')
    bank = models.ForeignKey('erp_core.Bank', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank')
    account_type = models.ForeignKey('erp_core.BankAccountType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Type')
    account_subtype = models.ForeignKey('erp_core.BankAccountSubtype', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Subtype')
    is_default = models.BooleanField(default=False, verbose_name="Is Default Account")
    is_company_account = models.BooleanField(default=False, verbose_name="Is Company Account")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    iban = models.CharField(max_length=255, blank=True, null=True, verbose_name="IBAN")
    bank_account_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank Account No")
    integration_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Integration ID")
    last_integration_date = models.DateField(blank=True, null=True, verbose_name="Last Integration Date")
    mask = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mask")
    branch_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Branch Code")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    is_credit_card = models.BooleanField(default=False, verbose_name="Is Credit Card")

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class JournalEntryAccount(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    account_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Type")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    debit_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit")
    debit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit in Company Currency")
    credit_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit")
    credit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit in Company Currency")
    reference_type = models.CharField(max_length=255, choices=[('Sales Invoice', 'Sales Invoice'), ('Purchase Invoice', 'Purchase Invoice'), ('Journal Entry', 'Journal Entry'), ('Sales Order', 'Sales Order'), ('Purchase Order', 'Purchase Order'), ('Expense Claim', 'Expense Claim'), ('Asset', 'Asset'), ('Loan', 'Loan'), ('Payroll Entry', 'Payroll Entry'), ('Employee Advance', 'Employee Advance'), ('Exchange Rate Revaluation', 'Exchange Rate Revaluation'), ('Invoice Discounting', 'Invoice Discounting'), ('Fees', 'Fees'), ('Full and Final Statement', 'Full and Final Statement'), ('Payment Entry', 'Payment Entry'), ('Bank Transaction', 'Bank Transaction')], blank=True, null=True, verbose_name='Reference Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    reference_due_date = models.DateField(blank=True, null=True, verbose_name="Reference Due Date")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    is_advance = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Advance')
    user_remark = models.TextField(blank=True, null=True, verbose_name="User Remark")
    against_account = models.TextField(blank=True, null=True, verbose_name="Against Account")
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    reference_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Detail No")
    advance_voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Advance Voucher Type')
    advance_voucher_no = models.TextField(blank=True, null=True, verbose_name="Advance Voucher No")
    is_tax_withholding_account = models.BooleanField(default=False, verbose_name="Is Tax Withholding Account")

class JournalEntryAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryAccount
        fields = '__all__'

class JournalEntryAccountViewSet(viewsets.ModelViewSet):
    queryset = JournalEntryAccount.objects.all()
    serializer_class = JournalEntryAccountSerializer

class FinancialReportRow(BaseDocument):
    reference_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Line Reference")
    display_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Display Name")
    indentation_level = models.IntegerField(default=0, verbose_name="Indent Level")
    data_source = models.CharField(max_length=255, choices=[('Account Data', 'Account Data'), ('Calculated Amount', 'Calculated Amount'), ('Custom API', 'Custom API'), ('Blank Line', 'Blank Line'), ('Column Break', 'Column Break'), ('Section Break', 'Section Break')], blank=True, null=True, verbose_name='Data Source')
    balance_type = models.CharField(max_length=255, choices=[('Opening Balance', 'Opening Balance'), ('Closing Balance', 'Closing Balance'), ('Period Movement (Debits - Credits)', 'Period Movement (Debits - Credits)')], blank=True, null=True, verbose_name='Balance Type')
    bold_text = models.BooleanField(default=False, verbose_name="Bold Text")
    italic_text = models.BooleanField(default=False, verbose_name="Italic Text")
    hidden_calculation = models.BooleanField(default=False, verbose_name="Hidden Line (Internal Use Only)")
    hide_when_empty = models.BooleanField(default=False, verbose_name="Hide If Zero")
    reverse_sign = models.BooleanField(default=False, verbose_name="Reverse Sign")
    calculation_formula = models.TextField(blank=True, null=True, verbose_name="Formula or Account Filter")
    include_in_charts = models.BooleanField(default=False, verbose_name="Include in Charts")
    color = models.TextField(blank=True, null=True, verbose_name="Color")
    fieldtype = models.CharField(max_length=255, choices=[('Currency', 'Currency'), ('Float', 'Float'), ('Int', 'Int'), ('Percent', 'Percent')], blank=True, null=True, verbose_name='Value Type')
    advanced_filtering = models.BooleanField(default=False, verbose_name="Advanced Filtering")

class FinancialReportRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReportRow
        fields = '__all__'

class FinancialReportRowViewSet(viewsets.ModelViewSet):
    queryset = FinancialReportRow.objects.all()
    serializer_class = FinancialReportRowSerializer

class SalesInvoiceReference(BaseDocument):
    sales_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Invoice')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    is_return = models.BooleanField(default=False, verbose_name="Is Return")
    return_against = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against')
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")

class SalesInvoiceReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoiceReference
        fields = '__all__'

class SalesInvoiceReferenceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoiceReference.objects.all()
    serializer_class = SalesInvoiceReferenceSerializer

class BankTransactionRuleDescriptionConditions(BaseDocument):
    check = models.CharField(max_length=255, choices=[('Contains', 'Contains'), ('Starts With', 'Starts With'), ('Ends With', 'Ends With'), ('Regex', 'Regex')], blank=True, null=True, verbose_name='Check')
    value = models.TextField(blank=True, null=True, verbose_name="Value")

class BankTransactionRuleDescriptionConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactionRuleDescriptionConditions
        fields = '__all__'

class BankTransactionRuleDescriptionConditionsViewSet(viewsets.ModelViewSet):
    queryset = BankTransactionRuleDescriptionConditions.objects.all()
    serializer_class = BankTransactionRuleDescriptionConditionsSerializer

class Account(BaseDocument):
    account_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Name")
    account_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Number")
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    root_type = models.CharField(max_length=255, choices=[('Asset', 'Asset'), ('Liability', 'Liability'), ('Income', 'Income'), ('Expense', 'Expense'), ('Equity', 'Equity')], blank=True, null=True, verbose_name='Root Type')
    report_type = models.CharField(max_length=255, choices=[('Balance Sheet', 'Balance Sheet'), ('Profit and Loss', 'Profit and Loss')], blank=True, null=True, verbose_name='Report Type')
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Account')
    account_type = models.CharField(max_length=255, choices=[('Accumulated Depreciation', 'Accumulated Depreciation'), ('Asset Received But Not Billed', 'Asset Received But Not Billed'), ('Bank', 'Bank'), ('Cash', 'Cash'), ('Chargeable', 'Chargeable'), ('Capital Work in Progress', 'Capital Work in Progress'), ('Cost of Goods Sold', 'Cost of Goods Sold'), ('Current Asset', 'Current Asset'), ('Current Liability', 'Current Liability'), ('Depreciation', 'Depreciation'), ('Direct Expense', 'Direct Expense'), ('Direct Income', 'Direct Income'), ('Equity', 'Equity'), ('Expense Account', 'Expense Account'), ('Expenses Included In Asset Valuation', 'Expenses Included In Asset Valuation'), ('Expenses Included In Valuation', 'Expenses Included In Valuation'), ('Fixed Asset', 'Fixed Asset'), ('Income Account', 'Income Account'), ('Indirect Expense', 'Indirect Expense'), ('Indirect Income', 'Indirect Income'), ('Liability', 'Liability'), ('Payable', 'Payable'), ('Receivable', 'Receivable'), ('Round Off', 'Round Off'), ('Round Off for Opening', 'Round Off for Opening'), ('Stock', 'Stock'), ('Stock Adjustment', 'Stock Adjustment'), ('Stock Received But Not Billed', 'Stock Received But Not Billed'), ('Service Received But Not Billed', 'Service Received But Not Billed'), ('Tax', 'Tax'), ('Temporary', 'Temporary')], blank=True, null=True, verbose_name='Account Type')
    tax_rate = models.FloatField(default=0.0, verbose_name="Tax Rate")
    freeze_account = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Frozen')
    balance_must_be = models.CharField(max_length=255, choices=[('Debit', 'Debit'), ('Credit', 'Credit')], blank=True, null=True, verbose_name='Balance must be')
    lft = models.IntegerField(default=0, verbose_name="Lft")
    rgt = models.IntegerField(default=0, verbose_name="Rgt")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="Old Parent")
    include_in_gross = models.BooleanField(default=False, verbose_name="Include in gross")
    disabled = models.BooleanField(default=False, verbose_name="Disable")
    account_category = models.ForeignKey('erp_core.AccountCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Category')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PurchaseTaxesandChargesTemplate(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    is_default = models.BooleanField(default=False, verbose_name="Default")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Purchase Taxes and Charges")
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')

class PurchaseTaxesandChargesTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseTaxesandChargesTemplate
        fields = '__all__'

class PurchaseTaxesandChargesTemplateViewSet(viewsets.ModelViewSet):
    queryset = PurchaseTaxesandChargesTemplate.objects.all()
    serializer_class = PurchaseTaxesandChargesTemplateSerializer

class ShippingRuleCountry(BaseDocument):
    country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country')

class ShippingRuleCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRuleCountry
        fields = '__all__'

class ShippingRuleCountryViewSet(viewsets.ModelViewSet):
    queryset = ShippingRuleCountry.objects.all()
    serializer_class = ShippingRuleCountrySerializer

class LoyaltyProgram(BaseDocument):
    loyalty_program_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Loyalty Program Name")
    loyalty_program_type = models.CharField(max_length=255, choices=[('Single Tier Program', 'Single Tier Program'), ('Multiple Tier Program', 'Multiple Tier Program')], blank=True, null=True, verbose_name='Loyalty Program Type')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    customer_territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Territory')
    auto_opt_in = models.BooleanField(default=False, verbose_name="Auto Opt In (For all customers)")
    collection_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Collection Rules")
    conversion_factor = models.FloatField(default=0.0, verbose_name="Conversion Factor")
    expiry_duration = models.IntegerField(default=0, verbose_name="Expiry Duration (in days)")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')

class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = '__all__'

class LoyaltyProgramViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer

class Subscription(BaseDocument):
    status = models.CharField(max_length=255, choices=[('Trialing', 'Trialing'), ('Active', 'Active'), ('Grace Period', 'Grace Period'), ('Cancelled', 'Cancelled'), ('Unpaid', 'Unpaid'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    cancelation_date = models.DateField(blank=True, null=True, verbose_name="Cancelation Date")
    trial_period_start = models.DateField(blank=True, null=True, verbose_name="Trial Period Start Date")
    trial_period_end = models.DateField(blank=True, null=True, verbose_name="Trial Period End Date")
    current_invoice_start = models.DateField(blank=True, null=True, verbose_name="Current Invoice Start Date")
    current_invoice_end = models.DateField(blank=True, null=True, verbose_name="Current Invoice End Date")
    days_until_due = models.IntegerField(default=0, verbose_name="Days Until Due")
    cancel_at_period_end = models.BooleanField(default=False, verbose_name="Cancel At End Of Period")
    plans = models.JSONField(default=list, blank=True, null=True, verbose_name="Plans")
    apply_additional_discount = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Additional Discount On')
    additional_discount_percentage = models.TextField(blank=True, null=True, verbose_name="Additional Discount Percentage")
    additional_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount")
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    sales_tax_template = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    purchase_tax_template = models.ForeignKey('erp_core.PurchaseTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Taxes and Charges Template')
    follow_calendar_months = models.BooleanField(default=False, verbose_name="Follow Calendar Months")
    generate_new_invoices_past_due_date = models.BooleanField(default=False, verbose_name="Generate New Invoices Past Due Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="Subscription End Date")
    start_date = models.DateField(blank=True, null=True, verbose_name="Subscription Start Date")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    submit_invoice = models.BooleanField(default=False, verbose_name="Submit Generated Invoices")
    generate_invoice_at = models.CharField(max_length=255, choices=[('End of the current subscription period', 'End of the current subscription period'), ('Beginning of the current subscription period', 'Beginning of the current subscription period'), ('Days before the current subscription period', 'Days before the current subscription period')], blank=True, null=True, verbose_name='Generate Invoice At')
    number_of_days = models.IntegerField(default=0, verbose_name="Number of Days")

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class AllowedDimension(BaseDocument):
    accounting_dimension = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accounting Dimension')
    dimension_value = models.TextField(blank=True, null=True, verbose_name="dimension_value")

class AllowedDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedDimension
        fields = '__all__'

class AllowedDimensionViewSet(viewsets.ModelViewSet):
    queryset = AllowedDimension.objects.all()
    serializer_class = AllowedDimensionSerializer

class ChequePrintTemplate(BaseDocument):
    has_print_format = models.BooleanField(default=False, verbose_name="Has Print Format")
    bank_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank Name")
    cheque_size = models.CharField(max_length=255, choices=[('Regular', 'Regular'), ('A4', 'A4')], blank=True, null=True, verbose_name='Cheque Size')
    starting_position_from_top_edge = models.FloatField(default=0.0, verbose_name="Starting position from top edge")
    cheque_width = models.FloatField(default=0.0, verbose_name="Cheque Width")
    cheque_height = models.FloatField(default=0.0, verbose_name="Cheque Height")
    scanned_cheque = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Scanned Cheque")
    is_account_payable = models.BooleanField(default=False, verbose_name="Is Account Payable")
    acc_pay_dist_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    acc_pay_dist_from_left_edge = models.FloatField(default=0.0, verbose_name="Distance from left edge")
    message_to_show = models.CharField(max_length=255, blank=True, null=True, verbose_name="Message to show")
    date_dist_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    date_dist_from_left_edge = models.FloatField(default=0.0, verbose_name="Starting location from left edge")
    payer_name_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    payer_name_from_left_edge = models.FloatField(default=0.0, verbose_name="Starting location from left edge")
    amt_in_words_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    amt_in_words_from_left_edge = models.FloatField(default=0.0, verbose_name="Starting location from left edge")
    amt_in_word_width = models.FloatField(default=0.0, verbose_name="Width of amount in word")
    amt_in_words_line_spacing = models.FloatField(default=0.0, verbose_name="Line spacing for amount in words")
    amt_in_figures_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    amt_in_figures_from_left_edge = models.FloatField(default=0.0, verbose_name="Starting location from left edge")
    acc_no_dist_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    acc_no_dist_from_left_edge = models.FloatField(default=0.0, verbose_name="Starting location from left edge")
    signatory_from_top_edge = models.FloatField(default=0.0, verbose_name="Distance from top edge")
    signatory_from_left_edge = models.FloatField(default=0.0, verbose_name="Starting location from left edge")

class ChequePrintTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChequePrintTemplate
        fields = '__all__'

class ChequePrintTemplateViewSet(viewsets.ModelViewSet):
    queryset = ChequePrintTemplate.objects.all()
    serializer_class = ChequePrintTemplateSerializer

class ItemTaxTemplateDetail(BaseDocument):
    tax_type = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax')
    tax_rate = models.FloatField(default=0.0, verbose_name="Tax Rate")
    not_applicable = models.BooleanField(default=False, verbose_name="Not Applicable")

class ItemTaxTemplateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTaxTemplateDetail
        fields = '__all__'

class ItemTaxTemplateDetailViewSet(viewsets.ModelViewSet):
    queryset = ItemTaxTemplateDetail.objects.all()
    serializer_class = ItemTaxTemplateDetailSerializer

class SubscriptionInvoice(BaseDocument):
    document_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Document Type ')
    invoice = models.TextField(blank=True, null=True, verbose_name="Invoice")

class SubscriptionInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionInvoice
        fields = '__all__'

class SubscriptionInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionInvoice.objects.all()
    serializer_class = SubscriptionInvoiceSerializer

class SubscriptionPlan(BaseDocument):
    plan_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Plan Name")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    price_determination = models.CharField(max_length=255, choices=[('Fixed Rate', 'Fixed Rate'), ('Based On Price List', 'Based On Price List'), ('Monthly Rate', 'Monthly Rate')], blank=True, null=True, verbose_name='Subscription Price Based On')
    cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Cost")
    price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    billing_interval = models.CharField(max_length=255, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year')], blank=True, null=True, verbose_name='Billing Interval')
    billing_interval_count = models.IntegerField(default=0, verbose_name="Billing Interval Count")
    payment_gateway = models.ForeignKey('erp_core.PaymentGatewayAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Gateway')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    product_price_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Product Price ID")

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class BankTransactionRule(BaseDocument):
    rule_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rule Name")
    transaction_type = models.CharField(max_length=255, choices=[('Any', 'Any'), ('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit')], blank=True, null=True, verbose_name='Transaction Type')
    min_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Min Amount")
    max_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Max Amount")
    rule_description = models.TextField(blank=True, null=True, verbose_name="Rule Description")
    description_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Description Rules")
    classify_as = models.CharField(max_length=255, choices=[('Bank Entry', 'Bank Entry'), ('Payment Entry', 'Payment Entry'), ('Transfer', 'Transfer')], blank=True, null=True, verbose_name='Classify As')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    priority = models.IntegerField(default=0, verbose_name="Priority")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    bank_entry_type = models.CharField(max_length=255, choices=[('Single Account', 'Single Account'), ('Multiple Accounts', 'Multiple Accounts')], blank=True, null=True, verbose_name='Bank Entry Type')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")

class BankTransactionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactionRule
        fields = '__all__'

class BankTransactionRuleViewSet(viewsets.ModelViewSet):
    queryset = BankTransactionRule.objects.all()
    serializer_class = BankTransactionRuleSerializer

class DiscountedInvoice(BaseDocument):
    sales_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Invoice')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    debit_to = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Debit to')

class DiscountedInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountedInvoice
        fields = '__all__'

class DiscountedInvoiceViewSet(viewsets.ModelViewSet):
    queryset = DiscountedInvoice.objects.all()
    serializer_class = DiscountedInvoiceSerializer

class BisectAccountingStatements(BaseDocument):
    from_date = models.DateTimeField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateTimeField(blank=True, null=True, verbose_name="To Date")
    algorithm = models.CharField(max_length=255, choices=[('BFS', 'BFS'), ('DFS', 'DFS')], blank=True, null=True, verbose_name='Algorithm')
    current_node = models.ForeignKey('erp_core.BisectNodes', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Current Node')
    current_from_date = models.DateTimeField(blank=True, null=True, verbose_name="current_from_date")
    current_to_date = models.DateTimeField(blank=True, null=True, verbose_name="current_to_date")
    p_l_summary = models.FloatField(default=0.0, verbose_name="p_l_summary")
    b_s_summary = models.FloatField(default=0.0, verbose_name="b_s_summary")
    difference = models.FloatField(default=0.0, verbose_name="difference")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    heading_cppb = models.TextField(blank=True, null=True, verbose_name="Profit and Loss Summary")
    balance_sheet_summary = models.TextField(blank=True, null=True, verbose_name="Balance Sheet Summary")
    difference_heading = models.TextField(blank=True, null=True, verbose_name="Difference")
    bisecting_from = models.TextField(blank=True, null=True, verbose_name="Bisecting From")
    bisecting_to = models.TextField(blank=True, null=True, verbose_name="Bisecting To")

class BisectAccountingStatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BisectAccountingStatements
        fields = '__all__'

class BisectAccountingStatementsViewSet(viewsets.ModelViewSet):
    queryset = BisectAccountingStatements.objects.all()
    serializer_class = BisectAccountingStatementsSerializer

class ProcessPeriodClosingVoucherDetail(BaseDocument):
    processing_date = models.DateField(blank=True, null=True, verbose_name="Processing Date")
    status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    closing_balance = models.TextField(blank=True, null=True, verbose_name="Closing Balance")
    report_type = models.CharField(max_length=255, choices=[('Profit and Loss', 'Profit and Loss'), ('Balance Sheet', 'Balance Sheet')], blank=True, null=True, verbose_name='Report Type')

class ProcessPeriodClosingVoucherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessPeriodClosingVoucherDetail
        fields = '__all__'

class ProcessPeriodClosingVoucherDetailViewSet(viewsets.ModelViewSet):
    queryset = ProcessPeriodClosingVoucherDetail.objects.all()
    serializer_class = ProcessPeriodClosingVoucherDetailSerializer

class POSInvoiceItem(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    customer_item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Item Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name="Brand Name")
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
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="Delivered By Supplier")
    income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Income Account')
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    deferred_revenue_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Deferred Revenue Account')
    service_stop_date = models.DateField(blank=True, null=True, verbose_name="Service Stop Date")
    enable_deferred_revenue = models.BooleanField(default=False, verbose_name="Enable Deferred Revenue")
    service_start_date = models.DateField(blank=True, null=True, verbose_name="Service Start Date")
    service_end_date = models.DateField(blank=True, null=True, verbose_name="Service End Date")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Warehouse (Optional)')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    actual_batch_qty = models.FloatField(default=0.0, verbose_name="Available Batch Qty at Warehouse")
    actual_qty = models.FloatField(default=0.0, verbose_name="Available Qty at Warehouse")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    so_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    delivery_note = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Note')
    dn_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delivery Note Item")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    pos_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="POS Invoice Item")
    grant_commission = models.BooleanField(default=False, verbose_name="Grant Commission")
    has_item_scanned = models.BooleanField(default=False, verbose_name="Has Item Scanned")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")

class POSInvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSInvoiceItem
        fields = '__all__'

class POSInvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = POSInvoiceItem.objects.all()
    serializer_class = POSInvoiceItemSerializer

class BudgetAccount(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    budget_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Budget Amount")

class BudgetAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetAccount
        fields = '__all__'

class BudgetAccountViewSet(viewsets.ModelViewSet):
    queryset = BudgetAccount.objects.all()
    serializer_class = BudgetAccountSerializer

class PricingRule(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    disable = models.BooleanField(default=False, verbose_name="Disable")
    apply_on = models.CharField(max_length=255, choices=[('Item Code', 'Item Code'), ('Item Group', 'Item Group'), ('Brand', 'Brand'), ('Transaction', 'Transaction')], blank=True, null=True, verbose_name='Apply On')
    price_or_product_discount = models.CharField(max_length=255, choices=[('Price', 'Price'), ('Product', 'Product')], blank=True, null=True, verbose_name='Price or Product Discount')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Apply Rule On Item Code")
    item_groups = models.JSONField(default=list, blank=True, null=True, verbose_name="Apply Rule On Item Group")
    brands = models.JSONField(default=list, blank=True, null=True, verbose_name="Apply Rule On Brand")
    mixed_conditions = models.BooleanField(default=False, verbose_name="Mixed Conditions")
    is_cumulative = models.BooleanField(default=False, verbose_name="Is Cumulative")
    coupon_code_based = models.BooleanField(default=False, verbose_name="Coupon Code Based")
    apply_rule_on_other = models.CharField(max_length=255, choices=[('Item Code', 'Item Code'), ('Item Group', 'Item Group'), ('Brand', 'Brand')], blank=True, null=True, verbose_name='Apply Rule On Other')
    other_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    other_item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    other_brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    selling = models.BooleanField(default=False, verbose_name="Selling")
    buying = models.BooleanField(default=False, verbose_name="Buying")
    applicable_for = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Customer Group', 'Customer Group'), ('Territory', 'Territory'), ('Sales Partner', 'Sales Partner'), ('Campaign', 'Campaign'), ('Supplier', 'Supplier'), ('Supplier Group', 'Supplier Group')], blank=True, null=True, verbose_name='Applicable For')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')
    min_qty = models.FloatField(default=0.0, verbose_name="Min Qty (As Per Stock UOM)")
    max_qty = models.FloatField(default=0.0, verbose_name="Max Qty (As Per Stock UOM)")
    min_amt = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Min Amt")
    max_amt = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Max Amt")
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    valid_upto = models.DateField(blank=True, null=True, verbose_name="Valid Up To")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_or_discount = models.CharField(max_length=255, choices=[('Rate', 'Rate'), ('Discount Percentage', 'Discount Percentage'), ('Discount Amount', 'Discount Amount')], blank=True, null=True, verbose_name='Rate or Discount')
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Discount On')
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    discount_percentage = models.FloatField(default=0.0, verbose_name="Discount Percentage")
    for_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Price List')
    same_item = models.BooleanField(default=False, verbose_name="Same Item")
    free_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Free Item')
    free_qty = models.FloatField(default=0.0, verbose_name="Qty")
    free_item_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    free_item_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Free Item Rate")
    threshold_percentage = models.TextField(blank=True, null=True, verbose_name="Threshold for Suggestion (In Percentage)")
    priority = models.CharField(max_length=255, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], blank=True, null=True, verbose_name='Priority')
    apply_multiple_pricing_rules = models.BooleanField(default=False, verbose_name="Apply Multiple Pricing Rules")
    apply_discount_on_rate = models.BooleanField(default=False, verbose_name="Apply Discount on Discounted Rate")
    validate_applied_rule = models.BooleanField(default=False, verbose_name="Validate Applied Rule")
    rule_description = models.TextField(blank=True, null=True, verbose_name="Rule Description")
    promotional_scheme_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Promotional Scheme Id")
    promotional_scheme = models.ForeignKey('erp_core.PromotionalScheme', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Promotional Scheme')
    condition = models.TextField(blank=True, null=True, verbose_name="Condition")
    is_recursive = models.BooleanField(default=False, verbose_name="Is Recursive")
    naming_series = models.CharField(max_length=255, choices=[('PRLE-.####', 'PRLE-.####')], blank=True, null=True, verbose_name='Naming Series')
    round_free_qty = models.BooleanField(default=False, verbose_name="Round Free Qty")
    recurse_for = models.FloatField(default=0.0, verbose_name="Recurse Every (As Per Transaction UOM)")
    apply_recursion_over = models.FloatField(default=0.0, verbose_name="Apply Recursion Over (As Per Transaction UOM)")
    has_priority = models.BooleanField(default=False, verbose_name="Has Priority")
    dont_enforce_free_item_qty = models.BooleanField(default=False, verbose_name="Don't Enforce Free Item Qty")

class PricingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRule
        fields = '__all__'

class PricingRuleViewSet(viewsets.ModelViewSet):
    queryset = PricingRule.objects.all()
    serializer_class = PricingRuleSerializer

class PromotionalScheme(BaseDocument):
    apply_on = models.CharField(max_length=255, choices=[('Item Code', 'Item Code'), ('Item Group', 'Item Group'), ('Brand', 'Brand'), ('Transaction', 'Transaction')], blank=True, null=True, verbose_name='Apply On')
    disable = models.BooleanField(default=False, verbose_name="Disable")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Item Code")
    item_groups = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Item Group")
    brands = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Brand")
    mixed_conditions = models.BooleanField(default=False, verbose_name="Mixed Conditions")
    is_cumulative = models.BooleanField(default=False, verbose_name="Is Cumulative")
    apply_rule_on_other = models.CharField(max_length=255, choices=[('Item Code', 'Item Code'), ('Item Group', 'Item Group'), ('Brand', 'Brand')], blank=True, null=True, verbose_name='Apply Rule On Other')
    other_item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    other_item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    other_brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    selling = models.BooleanField(default=False, verbose_name="Selling")
    buying = models.BooleanField(default=False, verbose_name="Buying")
    applicable_for = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Customer Group', 'Customer Group'), ('Territory', 'Territory'), ('Sales Partner', 'Sales Partner'), ('Campaign', 'Campaign'), ('Supplier', 'Supplier'), ('Supplier Group', 'Supplier Group')], blank=True, null=True, verbose_name='Applicable For')
    customer = models.TextField(blank=True, null=True, verbose_name="Customer")
    customer_group = models.TextField(blank=True, null=True, verbose_name="Customer Group")
    territory = models.TextField(blank=True, null=True, verbose_name="Territory")
    sales_partner = models.TextField(blank=True, null=True, verbose_name="Sales Partner")
    campaign = models.TextField(blank=True, null=True, verbose_name="Campaign")
    supplier = models.TextField(blank=True, null=True, verbose_name="Supplier")
    supplier_group = models.TextField(blank=True, null=True, verbose_name="Supplier Group")
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    valid_upto = models.DateField(blank=True, null=True, verbose_name="Valid Up To")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    price_discount_slabs = models.JSONField(default=list, blank=True, null=True, verbose_name="Promotional Scheme Price Discount")
    product_discount_slabs = models.JSONField(default=list, blank=True, null=True, verbose_name="Promotional Scheme Product Discount")

class PromotionalSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionalScheme
        fields = '__all__'

class PromotionalSchemeViewSet(viewsets.ModelViewSet):
    queryset = PromotionalScheme.objects.all()
    serializer_class = PromotionalSchemeSerializer

class PeggedCurrencyDetails(BaseDocument):
    source_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    pegged_exchange_rate = models.CharField(max_length=255, blank=True, null=True, verbose_name="Exchange Rate")
    pegged_against = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pegged Against')

class PeggedCurrencyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeggedCurrencyDetails
        fields = '__all__'

class PeggedCurrencyDetailsViewSet(viewsets.ModelViewSet):
    queryset = PeggedCurrencyDetails.objects.all()
    serializer_class = PeggedCurrencyDetailsSerializer

class PaymentReference(BaseDocument):
    payment_term = models.ForeignKey('erp_core.PaymentTerm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Term')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    payment_schedule = models.ForeignKey('erp_core.PaymentSchedule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Schedule')

class PaymentReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReference
        fields = '__all__'

class PaymentReferenceViewSet(viewsets.ModelViewSet):
    queryset = PaymentReference.objects.all()
    serializer_class = PaymentReferenceSerializer

class PaymentOrderReference(BaseDocument):
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Name")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    payment_request = models.ForeignKey('erp_core.PaymentRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Request')
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    payment_reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Payment Reference")

class PaymentOrderReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOrderReference
        fields = '__all__'

class PaymentOrderReferenceViewSet(viewsets.ModelViewSet):
    queryset = PaymentOrderReference.objects.all()
    serializer_class = PaymentOrderReferenceSerializer

class ShippingRuleCondition(BaseDocument):
    from_value = models.FloatField(default=0.0, verbose_name="From Value")
    to_value = models.FloatField(default=0.0, verbose_name="To Value")
    shipping_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Shipping Amount")

class ShippingRuleConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRuleCondition
        fields = '__all__'

class ShippingRuleConditionViewSet(viewsets.ModelViewSet):
    queryset = ShippingRuleCondition.objects.all()
    serializer_class = ShippingRuleConditionSerializer

class POSOpeningEntryDetail(BaseDocument):
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    opening_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Opening Amount")

class POSOpeningEntryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSOpeningEntryDetail
        fields = '__all__'

class POSOpeningEntryDetailViewSet(viewsets.ModelViewSet):
    queryset = POSOpeningEntryDetail.objects.all()
    serializer_class = POSOpeningEntryDetailSerializer

class POSProfile(BaseDocument):
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    country = models.TextField(blank=True, null=True, verbose_name="Country")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address')
    applicable_for_users = models.JSONField(default=list, blank=True, null=True, verbose_name="Applicable for Users")
    payments = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Methods")
    item_groups = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Groups")
    customer_groups = models.JSONField(default=list, blank=True, null=True, verbose_name="Customer Groups")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms and Conditions')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    write_off_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Account')
    write_off_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Cost Center')
    account_for_change_amount = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account for Change Amount')
    income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Income Account')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    taxes_and_charges = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Taxes and Charges')
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Discount On')
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    print_format = models.ForeignKey('erp_core.PrintFormat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Format')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    update_stock = models.BooleanField(default=False, verbose_name="Update Stock")
    hide_unavailable_items = models.BooleanField(default=False, verbose_name="Hide Unavailable Items")
    hide_images = models.BooleanField(default=False, verbose_name="Hide Images")
    auto_add_item_to_cart = models.BooleanField(default=False, verbose_name="Automatically Add Filtered Item To Cart")
    allow_rate_change = models.BooleanField(default=False, verbose_name="Allow User to Edit Rate")
    allow_discount_change = models.BooleanField(default=False, verbose_name="Allow User to Edit Discount")
    validate_stock_on_save = models.BooleanField(default=False, verbose_name="Validate Stock on Save")
    write_off_limit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Limit")
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    utm_medium = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    print_receipt_on_order_complete = models.BooleanField(default=False, verbose_name="Print Receipt on Order Complete")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    set_grand_total_to_default_mop = models.BooleanField(default=False, verbose_name="Set Grand Total to Default Payment Method")
    action_on_new_invoice = models.CharField(max_length=255, choices=[('Always Ask', 'Always Ask'), ('Save Changes and Load New Invoice', 'Save Changes and Load New Invoice'), ('Discard Changes and Load New Invoice', 'Discard Changes and Load New Invoice')], blank=True, null=True, verbose_name='Action on New Invoice')
    allow_partial_payment = models.BooleanField(default=False, verbose_name="Allow Partial Payment")
    allow_warehouse_change = models.BooleanField(default=False, verbose_name="Allow User to Edit Warehouse")

class POSProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSProfile
        fields = '__all__'

class POSProfileViewSet(viewsets.ModelViewSet):
    queryset = POSProfile.objects.all()
    serializer_class = POSProfileSerializer

class RepostAllowedTypes(BaseDocument):
    document_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Doctype')

class RepostAllowedTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostAllowedTypes
        fields = '__all__'

class RepostAllowedTypesViewSet(viewsets.ModelViewSet):
    queryset = RepostAllowedTypes.objects.all()
    serializer_class = RepostAllowedTypesSerializer

class AdvancePaymentLedgerEntry(BaseDocument):
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    against_voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Voucher Type')
    against_voucher_no = models.TextField(blank=True, null=True, verbose_name="Against Voucher No")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    event = models.CharField(max_length=255, blank=True, null=True, verbose_name="Event")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    delinked = models.BooleanField(default=False, verbose_name="DeLinked")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")

class AdvancePaymentLedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancePaymentLedgerEntry
        fields = '__all__'

class AdvancePaymentLedgerEntryViewSet(viewsets.ModelViewSet):
    queryset = AdvancePaymentLedgerEntry.objects.all()
    serializer_class = AdvancePaymentLedgerEntrySerializer

class BankClearanceDetail(BaseDocument):
    payment_document = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Document')
    payment_entry = models.TextField(blank=True, null=True, verbose_name="Payment Entry")
    against_account = models.CharField(max_length=255, blank=True, null=True, verbose_name="Against Account")
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name="Amount")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    cheque_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cheque Number")
    cheque_date = models.DateField(blank=True, null=True, verbose_name="Cheque Date")
    clearance_date = models.DateField(blank=True, null=True, verbose_name="Clearance Date")

class BankClearanceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankClearanceDetail
        fields = '__all__'

class BankClearanceDetailViewSet(viewsets.ModelViewSet):
    queryset = BankClearanceDetail.objects.all()
    serializer_class = BankClearanceDetailSerializer

class CashierClosingPayments(BaseDocument):
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    amount = models.FloatField(default=0.0, verbose_name="Amount")

class CashierClosingPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashierClosingPayments
        fields = '__all__'

class CashierClosingPaymentsViewSet(viewsets.ModelViewSet):
    queryset = CashierClosingPayments.objects.all()
    serializer_class = CashierClosingPaymentsSerializer

class PaymentReconciliationInvoice(BaseDocument):
    invoice_type = models.CharField(max_length=255, choices=[('Sales Invoice', 'Sales Invoice'), ('Purchase Invoice', 'Purchase Invoice'), ('Journal Entry', 'Journal Entry')], blank=True, null=True, verbose_name='Invoice Type')
    invoice_number = models.TextField(blank=True, null=True, verbose_name="Invoice Number")
    invoice_date = models.DateField(blank=True, null=True, verbose_name="Invoice Date")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")

class PaymentReconciliationInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReconciliationInvoice
        fields = '__all__'

class PaymentReconciliationInvoiceViewSet(viewsets.ModelViewSet):
    queryset = PaymentReconciliationInvoice.objects.all()
    serializer_class = PaymentReconciliationInvoiceSerializer

class BankTransactionRuleAccounts(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    party_type = models.ForeignKey('erp_core.PartyType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    debit = models.CharField(max_length=255, blank=True, null=True, verbose_name="Debit")
    credit = models.CharField(max_length=255, blank=True, null=True, verbose_name="Credit")
    user_remark = models.TextField(blank=True, null=True, verbose_name="User Remark")

class BankTransactionRuleAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactionRuleAccounts
        fields = '__all__'

class BankTransactionRuleAccountsViewSet(viewsets.ModelViewSet):
    queryset = BankTransactionRuleAccounts.objects.all()
    serializer_class = BankTransactionRuleAccountsSerializer

class PaymentTermsTemplate(BaseDocument):
    template_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Template Name")
    terms = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Terms")
    allocate_payment_based_on_payment_terms = models.BooleanField(default=False, verbose_name="Allocate Payment Based On Payment Terms")

class PaymentTermsTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTermsTemplate
        fields = '__all__'

class PaymentTermsTemplateViewSet(viewsets.ModelViewSet):
    queryset = PaymentTermsTemplate.objects.all()
    serializer_class = PaymentTermsTemplateSerializer

class OverduePayment(BaseDocument):
    payment_term = models.ForeignKey('erp_core.PaymentTerm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Term')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    invoice_portion = models.TextField(blank=True, null=True, verbose_name="Invoice Portion")
    payment_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Payment Amount")
    outstanding = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding")
    paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount")
    discounted_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discounted Amount")
    sales_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Invoice')
    payment_schedule = models.CharField(max_length=255, blank=True, null=True, verbose_name="Payment Schedule")
    overdue_days = models.CharField(max_length=255, blank=True, null=True, verbose_name="Overdue Days")
    dunning_level = models.IntegerField(default=0, verbose_name="Dunning Level")
    interest = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Interest")

class OverduePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverduePayment
        fields = '__all__'

class OverduePaymentViewSet(viewsets.ModelViewSet):
    queryset = OverduePayment.objects.all()
    serializer_class = OverduePaymentSerializer

class ExchangeRateRevaluationAccount(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    balance_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Balance In Account Currency")
    current_exchange_rate = models.FloatField(default=0.0, verbose_name="Current Exchange Rate")
    balance_in_base_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Balance In Base Currency")
    new_exchange_rate = models.FloatField(default=0.0, verbose_name="New Exchange Rate")
    new_balance_in_base_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="New Balance In Base Currency")
    gain_loss = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Gain/Loss")
    zero_balance = models.BooleanField(default=False, verbose_name="Zero Balance")
    new_balance_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="New Balance In Account Currency")

class ExchangeRateRevaluationAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateRevaluationAccount
        fields = '__all__'

class ExchangeRateRevaluationAccountViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRateRevaluationAccount.objects.all()
    serializer_class = ExchangeRateRevaluationAccountSerializer

class UnreconcilePayment(BaseDocument):
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    allocations = models.JSONField(default=list, blank=True, null=True, verbose_name="Allocations")

class UnreconcilePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnreconcilePayment
        fields = '__all__'

class UnreconcilePaymentViewSet(viewsets.ModelViewSet):
    queryset = UnreconcilePayment.objects.all()
    serializer_class = UnreconcilePaymentSerializer

class MonthlyDistributionPercentage(BaseDocument):
    month = models.CharField(max_length=255, blank=True, null=True, verbose_name="Month")
    percentage_allocation = models.FloatField(default=0.0, verbose_name="Percentage Allocation")

class MonthlyDistributionPercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyDistributionPercentage
        fields = '__all__'

class MonthlyDistributionPercentageViewSet(viewsets.ModelViewSet):
    queryset = MonthlyDistributionPercentage.objects.all()
    serializer_class = MonthlyDistributionPercentageSerializer

class JournalEntry(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    voucher_type = models.CharField(max_length=255, choices=[('Journal Entry', 'Journal Entry'), ('Inter Company Journal Entry', 'Inter Company Journal Entry'), ('Bank Entry', 'Bank Entry'), ('Cash Entry', 'Cash Entry'), ('Credit Card Entry', 'Credit Card Entry'), ('Debit Note', 'Debit Note'), ('Credit Note', 'Credit Note'), ('Contra Entry', 'Contra Entry'), ('Excise Entry', 'Excise Entry'), ('Write Off Entry', 'Write Off Entry'), ('Opening Entry', 'Opening Entry'), ('Depreciation Entry', 'Depreciation Entry'), ('Asset Disposal', 'Asset Disposal'), ('Periodic Accounting Entry', 'Periodic Accounting Entry'), ('Exchange Rate Revaluation', 'Exchange Rate Revaluation'), ('Exchange Gain Or Loss', 'Exchange Gain Or Loss'), ('Deferred Revenue', 'Deferred Revenue'), ('Deferred Expense', 'Deferred Expense')], blank=True, null=True, verbose_name='Entry Type')
    naming_series = models.CharField(max_length=255, choices=[('ACC-JV-.YYYY.-', 'ACC-JV-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounting Entries")
    cheque_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Number")
    cheque_date = models.DateField(blank=True, null=True, verbose_name="Reference Date")
    user_remark = models.TextField(blank=True, null=True, verbose_name="User Remark")
    total_debit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Debit")
    total_credit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Credit")
    difference = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference (Dr - Cr)")
    multi_currency = models.BooleanField(default=False, verbose_name="Multi Currency")
    total_amount_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Total Amount Currency')
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Amount")
    total_amount_in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="Total Amount in Words")
    clearance_date = models.DateField(blank=True, null=True, verbose_name="Clearance Date")
    remark = models.TextField(blank=True, null=True, verbose_name="Remark")
    inter_company_journal_entry_reference = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Journal Entry Reference')
    bill_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bill No")
    bill_date = models.DateField(blank=True, null=True, verbose_name="Bill Date")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    write_off_based_on = models.CharField(max_length=255, choices=[('Accounts Receivable', 'Accounts Receivable'), ('Accounts Payable', 'Accounts Payable')], blank=True, null=True, verbose_name='Write Off Based On')
    write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount")
    pay_to_recd_from = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pay To / Recd From")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    payment_order = models.ForeignKey('erp_core.PaymentOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Order')
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening')
    stock_entry = models.ForeignKey('erp_core.StockEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Entry')
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    from_template = models.ForeignKey('erp_core.JournalEntryTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Template')
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    apply_tds = models.BooleanField(default=False, verbose_name="Consider for Tax Withholding ")
    reversal_of = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reversal Of')
    process_deferred_accounting = models.ForeignKey('erp_core.ProcessDeferredAccounting', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Process Deferred Accounting')
    is_system_generated = models.BooleanField(default=False, verbose_name="Is System Generated")
    periodic_entry_difference_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Periodic Entry Difference Account')
    for_all_stock_asset_accounts = models.BooleanField(default=False, verbose_name="For All Stock Asset Accounts")
    stock_asset_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock Asset Account')
    party_not_required = models.BooleanField(default=False, verbose_name="Party Not Required")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')
    ignore_tax_withholding_threshold = models.BooleanField(default=False, verbose_name="Ignore Tax Withholding Threshold")
    override_tax_withholding_entries = models.BooleanField(default=False, verbose_name="Edit Tax Withholding Entries")
    tax_withholding_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="Tax Withholding Entries")
    custom_remark = models.BooleanField(default=False, verbose_name="Custom Remark")

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class RepostPaymentLedger(BaseDocument):
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    repost_vouchers = models.JSONField(default=list, blank=True, null=True, verbose_name="Selected Vouchers")
    repost_status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('Failed', 'Failed'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Repost Status')
    add_manually = models.BooleanField(default=False, verbose_name="Add Manually")
    repost_error_log = models.TextField(blank=True, null=True, verbose_name="Repost Error Log")

class RepostPaymentLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostPaymentLedger
        fields = '__all__'

class RepostPaymentLedgerViewSet(viewsets.ModelViewSet):
    queryset = RepostPaymentLedger.objects.all()
    serializer_class = RepostPaymentLedgerSerializer

class SalesInvoiceItem(BaseDocument):
    barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Barcode")
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    customer_item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Item Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
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
    base_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate (Company Currency)")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    pricing_rules = models.TextField(blank=True, null=True, verbose_name="Pricing Rules")
    is_free_item = models.BooleanField(default=False, verbose_name="Is Free Item")
    net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Rate (Company Currency)")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="Delivered By Supplier")
    income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Income Account')
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Account')
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    deferred_revenue_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Deferred Revenue Account')
    service_stop_date = models.DateField(blank=True, null=True, verbose_name="Service Stop Date")
    enable_deferred_revenue = models.BooleanField(default=False, verbose_name="Enable Deferred Revenue")
    service_start_date = models.DateField(blank=True, null=True, verbose_name="Service Start Date")
    service_end_date = models.DateField(blank=True, null=True, verbose_name="Service End Date")
    weight_per_unit = models.FloatField(default=0.0, verbose_name="Weight Per Unit")
    total_weight = models.FloatField(default=0.0, verbose_name="Total Weight")
    weight_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Weight UOM')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Target Warehouse')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name="Brand Name")
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    actual_batch_qty = models.FloatField(default=0.0, verbose_name="Available Batch Qty at Warehouse")
    actual_qty = models.FloatField(default=0.0, verbose_name="Qty (Warehouse)")
    sales_order = models.ForeignKey('erp_core.SalesOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Order')
    so_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Order Item")
    delivery_note = models.ForeignKey('erp_core.DeliveryNote', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Delivery Note')
    dn_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delivery Note Item")
    delivered_qty = models.FloatField(default=0.0, verbose_name="Delivered Qty")
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    sales_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Invoice Item")
    incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Incoming Rate (Costing)")
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    discount_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Discount Account')
    grant_commission = models.BooleanField(default=False, verbose_name="Grant Commission")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    purchase_order_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    has_item_scanned = models.BooleanField(default=False, verbose_name="Has Item Scanned")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    company_total_stock = models.FloatField(default=0.0, verbose_name="Qty (Company)")
    pos_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="POS Invoice Item")
    pos_invoice = models.ForeignKey('erp_core.POSInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Invoice')
    scio_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="SCIO Detail")
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    apply_tds = models.BooleanField(default=False, verbose_name="Consider for Tax Withholding")

class SalesInvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoiceItem
        fields = '__all__'

class SalesInvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoiceItem.objects.all()
    serializer_class = SalesInvoiceItemSerializer

class BankGuarantee(BaseDocument):
    bg_type = models.CharField(max_length=255, choices=[('Receiving', 'Receiving'), ('Providing', 'Providing')], blank=True, null=True, verbose_name='Bank Guarantee Type')
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Document Type')
    reference_docname = models.TextField(blank=True, null=True, verbose_name="Reference Document Name")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    validity = models.IntegerField(default=0, verbose_name="Validity in Days")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    bank = models.ForeignKey('erp_core.Bank', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank')
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    bank_account_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank Account No")
    iban = models.CharField(max_length=255, blank=True, null=True, verbose_name="IBAN")
    branch_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Branch Code")
    swift_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="SWIFT number")
    more_information = models.TextField(blank=True, null=True, verbose_name="Clauses and Conditions")
    bank_guarantee_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank Guarantee Number")
    name_of_beneficiary = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name of Beneficiary")
    margin_money = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Margin Money")
    charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Charges Incurred")
    fixed_deposit_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fixed Deposit Number")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class BankGuaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankGuarantee
        fields = '__all__'

class BankGuaranteeViewSet(viewsets.ModelViewSet):
    queryset = BankGuarantee.objects.all()
    serializer_class = BankGuaranteeSerializer

class CashierClosing(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('POS-CLO-', 'POS-CLO-')], blank=True, null=True, verbose_name='Series')
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    from_time = models.TextField(blank=True, null=True, verbose_name="From Time")
    time = models.TextField(blank=True, null=True, verbose_name="To Time")
    expense = models.FloatField(default=0.0, verbose_name="Expense")
    custody = models.FloatField(default=0.0, verbose_name="Custody")
    returns = models.FloatField(default=0.0, verbose_name="Returns")
    outstanding_amount = models.FloatField(default=0.0, verbose_name="Outstanding Amount")
    payments = models.JSONField(default=list, blank=True, null=True, verbose_name="Payments")
    net_amount = models.FloatField(default=0.0, verbose_name="Net Amount")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class CashierClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashierClosing
        fields = '__all__'

class CashierClosingViewSet(viewsets.ModelViewSet):
    queryset = CashierClosing.objects.all()
    serializer_class = CashierClosingSerializer

class TransactionDeletionRecordDetails(BaseDocument):
    doctype_name = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='DocType')
    docfield_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="DocField")
    no_of_docs = models.IntegerField(default=0, verbose_name="No of Docs")
    done = models.BooleanField(default=False, verbose_name="Done")

class TransactionDeletionRecordDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDeletionRecordDetails
        fields = '__all__'

class TransactionDeletionRecordDetailsViewSet(viewsets.ModelViewSet):
    queryset = TransactionDeletionRecordDetails.objects.all()
    serializer_class = TransactionDeletionRecordDetailsSerializer

class BankTransactionMapping(BaseDocument):
    bank_transaction_field = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Field in Bank Transaction')
    file_field = models.CharField(max_length=255, blank=True, null=True, verbose_name="Column in Bank File")

class BankTransactionMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactionMapping
        fields = '__all__'

class BankTransactionMappingViewSet(viewsets.ModelViewSet):
    queryset = BankTransactionMapping.objects.all()
    serializer_class = BankTransactionMappingSerializer

class ShareBalance(BaseDocument):
    share_type = models.ForeignKey('erp_core.ShareType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Share Type')
    from_no = models.IntegerField(default=0, verbose_name="From No")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    no_of_shares = models.IntegerField(default=0, verbose_name="No of Shares")
    to_no = models.IntegerField(default=0, verbose_name="To No")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    is_company = models.BooleanField(default=False, verbose_name="Is Company")
    current_state = models.CharField(max_length=255, choices=[('Issued', 'Issued'), ('Purchased', 'Purchased')], blank=True, null=True, verbose_name='Current State')

class ShareBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareBalance
        fields = '__all__'

class ShareBalanceViewSet(viewsets.ModelViewSet):
    queryset = ShareBalance.objects.all()
    serializer_class = ShareBalanceSerializer

class PaymentTerm(BaseDocument):
    payment_term_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Payment Term Name")
    invoice_portion = models.FloatField(default=0.0, verbose_name="Invoice Portion (%)")
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    due_date_based_on = models.CharField(max_length=255, choices=[('Day(s) after invoice date', 'Day(s) after invoice date'), ('Day(s) after the end of the invoice month', 'Day(s) after the end of the invoice month'), ('Month(s) after the end of the invoice month', 'Month(s) after the end of the invoice month')], blank=True, null=True, verbose_name='Due Date Based On')
    credit_days = models.IntegerField(default=0, verbose_name="Credit Days")
    credit_months = models.IntegerField(default=0, verbose_name="Credit Months")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    discount_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Discount Type')
    discount = models.FloatField(default=0.0, verbose_name="Discount")
    discount_validity_based_on = models.CharField(max_length=255, choices=[('Day(s) after invoice date', 'Day(s) after invoice date'), ('Day(s) after the end of the invoice month', 'Day(s) after the end of the invoice month'), ('Month(s) after the end of the invoice month', 'Month(s) after the end of the invoice month')], blank=True, null=True, verbose_name='Discount Validity Based On')
    discount_validity = models.IntegerField(default=0, verbose_name="Discount Validity")

class PaymentTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTerm
        fields = '__all__'

class PaymentTermViewSet(viewsets.ModelViewSet):
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer

class TerritoryItem(BaseDocument):
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')

class TerritoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritoryItem
        fields = '__all__'

class TerritoryItemViewSet(viewsets.ModelViewSet):
    queryset = TerritoryItem.objects.all()
    serializer_class = TerritoryItemSerializer

class TaxWithholdingRate(BaseDocument):
    tax_withholding_rate = models.FloatField(default=0.0, verbose_name="Tax Withholding Rate")
    single_threshold = models.FloatField(default=0.0, verbose_name="Transaction Threshold")
    cumulative_threshold = models.FloatField(default=0.0, verbose_name="Cumulative Threshold")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')

class TaxWithholdingRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxWithholdingRate
        fields = '__all__'

class TaxWithholdingRateViewSet(viewsets.ModelViewSet):
    queryset = TaxWithholdingRate.objects.all()
    serializer_class = TaxWithholdingRateSerializer

class LedgerHealth(BaseDocument):
    voucher_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Type")
    voucher_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher No")
    debit_credit_mismatch = models.BooleanField(default=False, verbose_name="Debit-Credit mismatch")
    checked_on = models.DateTimeField(blank=True, null=True, verbose_name="Checked On")
    general_and_payment_ledger_mismatch = models.BooleanField(default=False, verbose_name="General and Payment Ledger mismatch")

class LedgerHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerHealth
        fields = '__all__'

class LedgerHealthViewSet(viewsets.ModelViewSet):
    queryset = LedgerHealth.objects.all()
    serializer_class = LedgerHealthSerializer

class UnreconcilePaymentEntries(BaseDocument):
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated Amount")
    unlinked = models.BooleanField(default=False, verbose_name="Unlinked")
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Type')
    account = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account")
    party_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Type")
    party = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')

class UnreconcilePaymentEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnreconcilePaymentEntries
        fields = '__all__'

class UnreconcilePaymentEntriesViewSet(viewsets.ModelViewSet):
    queryset = UnreconcilePaymentEntries.objects.all()
    serializer_class = UnreconcilePaymentEntriesSerializer

class TaxWithholdingEntry(BaseDocument):
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax ID")
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    tax_rate = models.TextField(blank=True, null=True, verbose_name="Tax Rate")
    taxable_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Taxable Amount")
    lower_deduction_certificate = models.ForeignKey('erp_core.LowerDeductionCertificate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Lower Deduction Certificate')
    status = models.CharField(max_length=255, choices=[('Settled', 'Settled'), ('Under Withheld', 'Under Withheld'), ('Over Withheld', 'Over Withheld'), ('Duplicate', 'Duplicate'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    withholding_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Withholding Document Type')
    withholding_name = models.TextField(blank=True, null=True, verbose_name="Withholding Document Name")
    taxable_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Taxable Document Type')
    taxable_name = models.TextField(blank=True, null=True, verbose_name="Taxable Document Name")
    taxable_date = models.DateField(blank=True, null=True, verbose_name="Taxable Date")
    withholding_date = models.DateField(blank=True, null=True, verbose_name="Withholding Date")
    under_withheld_reason = models.CharField(max_length=255, choices=[('Threshold Exemption', 'Threshold Exemption'), ('Lower Deduction Certificate', 'Lower Deduction Certificate')], blank=True, null=True, verbose_name='Under Withheld Reason')
    withholding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Tax Withheld")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    created_by_migration = models.BooleanField(default=False, verbose_name="Created By Migration")

class TaxWithholdingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxWithholdingEntry
        fields = '__all__'

class TaxWithholdingEntryViewSet(viewsets.ModelViewSet):
    queryset = TaxWithholdingEntry.objects.all()
    serializer_class = TaxWithholdingEntrySerializer

class AccountingDimensionDetail(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    reference_document = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Document')
    default_dimension = models.TextField(blank=True, null=True, verbose_name="Default Dimension")
    mandatory_for_bs = models.BooleanField(default=False, verbose_name="Mandatory For Balance Sheet")
    mandatory_for_pl = models.BooleanField(default=False, verbose_name="Mandatory For Profit and Loss Account")
    automatically_post_balancing_accounting_entry = models.BooleanField(default=False, verbose_name="Automatically post balancing accounting entry")
    offsetting_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Offsetting Account')

class AccountingDimensionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDimensionDetail
        fields = '__all__'

class AccountingDimensionDetailViewSet(viewsets.ModelViewSet):
    queryset = AccountingDimensionDetail.objects.all()
    serializer_class = AccountingDimensionDetailSerializer

class AccountingDimensionFilter(BaseDocument):
    accounting_dimension = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Accounting Dimension')
    allow_or_restrict = models.CharField(max_length=255, choices=[('Allow', 'Allow'), ('Restrict', 'Restrict')], blank=True, null=True, verbose_name='Allow Or Restrict Dimension')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Applicable On Account")
    dimensions = models.JSONField(default=list, blank=True, null=True, verbose_name="Applicable Dimension")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    apply_restriction_on_values = models.BooleanField(default=False, verbose_name="Apply restriction on dimension values")
    fieldname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fieldname")

class AccountingDimensionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDimensionFilter
        fields = '__all__'

class AccountingDimensionFilterViewSet(viewsets.ModelViewSet):
    queryset = AccountingDimensionFilter.objects.all()
    serializer_class = AccountingDimensionFilterSerializer

class PurchaseInvoice(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('ACC-PINV-.YYYY.-', 'ACC-PINV-.YYYY.-'), ('ACC-PINV-RET-.YYYY.-', 'ACC-PINV-RET-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Name")
    tax_id = models.TextField(blank=True, null=True, verbose_name="Tax Id")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    is_paid = models.BooleanField(default=False, verbose_name="Is Paid")
    is_return = models.BooleanField(default=False, verbose_name="Is Return (Debit Note)")
    apply_tds = models.BooleanField(default=False, verbose_name="Consider for Tax Withholding")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    on_hold = models.BooleanField(default=False, verbose_name="Hold Invoice")
    release_date = models.DateField(blank=True, null=True, verbose_name="Release Date")
    hold_comment = models.TextField(blank=True, null=True, verbose_name="Reason For Putting On Hold")
    bill_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Invoice No")
    bill_date = models.DateField(blank=True, null=True, verbose_name="Supplier Invoice Date")
    return_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against Purchase Invoice')
    update_billed_amount_in_purchase_order = models.BooleanField(default=False, verbose_name="Update Billed Amount in Purchase Order")
    update_billed_amount_in_purchase_receipt = models.BooleanField(default=False, verbose_name="Update Billed Amount in Purchase Receipt")
    supplier_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Supplier Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.TextField(blank=True, null=True, verbose_name="Contact Email")
    shipping_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Shipping Address')
    shipping_address_display = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    buying_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Accepted Warehouse')
    rejected_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Warehouse')
    is_subcontracted = models.BooleanField(default=False, verbose_name="Is Subcontracted")
    update_stock = models.BooleanField(default=False, verbose_name="Update Stock")
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Detail")
    supplied_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Supplied Items")
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
    base_grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    base_rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    base_rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    base_in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    total_advance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Advance")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    cash_bank_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cash/Bank Account')
    clearance_date = models.DateField(blank=True, null=True, verbose_name="Clearance Date")
    paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount")
    base_paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount (Company Currency)")
    write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount")
    base_write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount (Company Currency)")
    write_off_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Account')
    write_off_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Cost Center')
    allocate_advances_automatically = models.BooleanField(default=False, verbose_name="Set Advances and Allocate (FIFO)")
    advances = models.JSONField(default=list, blank=True, null=True, verbose_name="Advances")
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    payment_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Schedule")
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Print Language")
    is_internal_supplier = models.BooleanField(default=False, verbose_name="Is Internal Supplier")
    credit_to = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Credit To')
    party_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Account Currency')
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening Entry')
    against_expense_account = models.TextField(blank=True, null=True, verbose_name="Against Expense Account")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Return', 'Return'), ('Debit Note Issued', 'Debit Note Issued'), ('Submitted', 'Submitted'), ('Paid', 'Paid'), ('Partly Paid', 'Partly Paid'), ('Unpaid', 'Unpaid'), ('Overdue', 'Overdue'), ('Cancelled', 'Cancelled'), ('Internal Transfer', 'Internal Transfer')], blank=True, null=True, verbose_name='Status')
    inter_company_invoice_reference = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Invoice Reference')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    billing_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Billing Address')
    billing_address_display = models.TextField(blank=True, null=True, verbose_name="Billing Address")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    unrealized_profit_loss_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Unrealized Profit / Loss Account')
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    set_from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set From Warehouse')
    supplier_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Warehouse')
    per_received = models.TextField(blank=True, null=True, verbose_name="Per Received")
    ignore_default_payment_terms_template = models.BooleanField(default=False, verbose_name="Ignore Default Payment Terms Template")
    subscription = models.ForeignKey('erp_core.Subscription', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subscription')
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    only_include_allocated_payments = models.BooleanField(default=False, verbose_name="Only Include Allocated Payments")
    use_company_roundoff_cost_center = models.BooleanField(default=False, verbose_name="Use Company Default Round Off Cost Center")
    use_transaction_date_exchange_rate = models.BooleanField(default=False, verbose_name="Use Transaction Date Exchange Rate")
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')
    update_outstanding_for_self = models.BooleanField(default=False, verbose_name="Update Outstanding for Self")
    sender = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sender")
    dispatch_address_display = models.TextField(blank=True, null=True, verbose_name="Dispatch Address")
    dispatch_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select Dispatch Address ')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    claimed_landed_cost_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Claimed Landed Cost Amount (Company Currency)")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')
    tax_withholding_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="Tax Withholding Entries")
    ignore_tax_withholding_threshold = models.BooleanField(default=False, verbose_name="Ignore Tax Withholding Threshold")
    override_tax_withholding_entries = models.BooleanField(default=False, verbose_name="Edit Tax Withholding Entries")

class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'

class PurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer

class PaymentTermsTemplateDetail(BaseDocument):
    payment_term = models.ForeignKey('erp_core.PaymentTerm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Term')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    invoice_portion = models.FloatField(default=0.0, verbose_name="Invoice Portion (%)")
    due_date_based_on = models.CharField(max_length=255, choices=[('Day(s) after invoice date', 'Day(s) after invoice date'), ('Day(s) after the end of the invoice month', 'Day(s) after the end of the invoice month'), ('Month(s) after the end of the invoice month', 'Month(s) after the end of the invoice month')], blank=True, null=True, verbose_name='Due Date Based On')
    credit_days = models.IntegerField(default=0, verbose_name="Credit Days")
    credit_months = models.IntegerField(default=0, verbose_name="Credit Months")
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    discount_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Discount Type')
    discount = models.FloatField(default=0.0, verbose_name="Discount")
    discount_validity_based_on = models.CharField(max_length=255, choices=[('Day(s) after invoice date', 'Day(s) after invoice date'), ('Day(s) after the end of the invoice month', 'Day(s) after the end of the invoice month'), ('Month(s) after the end of the invoice month', 'Month(s) after the end of the invoice month')], blank=True, null=True, verbose_name='Discount Validity Based On')
    discount_validity = models.IntegerField(default=0, verbose_name="Discount Validity")

class PaymentTermsTemplateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTermsTemplateDetail
        fields = '__all__'

class PaymentTermsTemplateDetailViewSet(viewsets.ModelViewSet):
    queryset = PaymentTermsTemplateDetail.objects.all()
    serializer_class = PaymentTermsTemplateDetailSerializer

class CostCenterAllocationPercentage(BaseDocument):
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    percentage = models.TextField(blank=True, null=True, verbose_name="Percentage (%)")

class CostCenterAllocationPercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenterAllocationPercentage
        fields = '__all__'

class CostCenterAllocationPercentageViewSet(viewsets.ModelViewSet):
    queryset = CostCenterAllocationPercentage.objects.all()
    serializer_class = CostCenterAllocationPercentageSerializer

class PaymentLedgerEntry(BaseDocument):
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    account_type = models.CharField(max_length=255, choices=[('Receivable', 'Receivable'), ('Payable', 'Payable')], blank=True, null=True, verbose_name='Account Type')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    against_voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Voucher Type')
    against_voucher_no = models.TextField(blank=True, null=True, verbose_name="Against Voucher No")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    amount_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount in Account Currency")
    delinked = models.BooleanField(default=False, verbose_name="DeLinked")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail No")

class PaymentLedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentLedgerEntry
        fields = '__all__'

class PaymentLedgerEntryViewSet(viewsets.ModelViewSet):
    queryset = PaymentLedgerEntry.objects.all()
    serializer_class = PaymentLedgerEntrySerializer

class LedgerMerge(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    merge_accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts to Merge")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Partial Success', 'Partial Success'), ('Error', 'Error')], blank=True, null=True, verbose_name='Status')
    root_type = models.CharField(max_length=255, choices=[('Asset', 'Asset'), ('Liability', 'Liability'), ('Income', 'Income'), ('Expense', 'Expense'), ('Equity', 'Equity')], blank=True, null=True, verbose_name='Root Type')
    account_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Name")
    is_group = models.BooleanField(default=False, verbose_name="Is Group")

class LedgerMergeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerMerge
        fields = '__all__'

class LedgerMergeViewSet(viewsets.ModelViewSet):
    queryset = LedgerMerge.objects.all()
    serializer_class = LedgerMergeSerializer

class ModeofPayment(BaseDocument):
    mode_of_payment = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mode of Payment")
    type = models.CharField(max_length=255, choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('General', 'General'), ('Phone', 'Phone')], blank=True, null=True, verbose_name='Type')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    enabled = models.BooleanField(default=False, verbose_name="Enabled")

class ModeofPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeofPayment
        fields = '__all__'

class ModeofPaymentViewSet(viewsets.ModelViewSet):
    queryset = ModeofPayment.objects.all()
    serializer_class = ModeofPaymentSerializer

class Bank(BaseDocument):
    bank_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bank Name")
    swift_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="SWIFT number")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    bank_transaction_mapping = models.JSONField(default=list, blank=True, null=True, verbose_name="Bank Transaction Mapping")
    plaid_access_token = models.CharField(max_length=255, blank=True, null=True, verbose_name="Plaid Access Token")

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class LoyaltyPointEntry(BaseDocument):
    loyalty_program = models.ForeignKey('erp_core.LoyaltyProgram', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Loyalty Program')
    loyalty_program_tier = models.CharField(max_length=255, blank=True, null=True, verbose_name="Loyalty Program Tier")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    redeem_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Redeem Against')
    loyalty_points = models.IntegerField(default=0, verbose_name="Loyalty Points")
    purchase_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Purchase Amount")
    expiry_date = models.DateField(blank=True, null=True, verbose_name="Expiry Date")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    invoice_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Invoice Type')
    invoice = models.TextField(blank=True, null=True, verbose_name="Invoice")
    discretionary_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name="Discretionary Reason")

class LoyaltyPointEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyPointEntry
        fields = '__all__'

class LoyaltyPointEntryViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyPointEntry.objects.all()
    serializer_class = LoyaltyPointEntrySerializer

class ProcessStatementOfAccountsCC(BaseDocument):
    cc = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='CC')

class ProcessStatementOfAccountsCCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStatementOfAccountsCC
        fields = '__all__'

class ProcessStatementOfAccountsCCViewSet(viewsets.ModelViewSet):
    queryset = ProcessStatementOfAccountsCC.objects.all()
    serializer_class = ProcessStatementOfAccountsCCSerializer

class CustomerItem(BaseDocument):
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer ')

class CustomerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerItem
        fields = '__all__'

class CustomerItemViewSet(viewsets.ModelViewSet):
    queryset = CustomerItem.objects.all()
    serializer_class = CustomerItemSerializer

class SupplierGroupItem(BaseDocument):
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')

class SupplierGroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierGroupItem
        fields = '__all__'

class SupplierGroupItemViewSet(viewsets.ModelViewSet):
    queryset = SupplierGroupItem.objects.all()
    serializer_class = SupplierGroupItemSerializer

class BankStatementImportLog(BaseDocument):
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    number_of_transactions = models.IntegerField(default=0, verbose_name="Number of Transactions")
    closing_balance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Closing Balance")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="File")
    detected_date_format = models.CharField(max_length=255, blank=True, null=True, verbose_name="Detected Date Format")
    detected_amount_format = models.CharField(max_length=255, choices=[('Separate columns for withdrawal and deposit', 'Separate columns for withdrawal and deposit'), ('Amount column has "CR"/"DR" values', 'Amount column has "CR"/"DR" values'), ('Amount column has positive/negative values', 'Amount column has positive/negative values'), ('Transaction type column has "CR"/"DR" values', 'Transaction type column has "CR"/"DR" values'), ('Transaction type column has "Deposit"/"Withdrawal" values', 'Transaction type column has "Deposit"/"Withdrawal" values'), ('Transaction type column has "C"/"D" values', 'Transaction type column has "C"/"D" values')], blank=True, null=True, verbose_name='Detected Amount Format')
    detected_header_index = models.IntegerField(default=0, verbose_name="Detected Header Index")
    detected_transaction_starting_index = models.IntegerField(default=0, verbose_name="Detected Transaction Starting Index")
    detected_transaction_ending_index = models.IntegerField(default=0, verbose_name="Detected Transaction Ending Index")
    column_mapping = models.JSONField(default=list, blank=True, null=True, verbose_name="Column Mapping")
    status = models.CharField(max_length=255, choices=[('Not Started', 'Not Started'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    total_debits = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Debits")
    total_credits = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Credits")
    total_debit_transactions = models.IntegerField(default=0, verbose_name="Total Debit Transactions")
    total_credit_transactions = models.IntegerField(default=0, verbose_name="Total Credit Transactions")

class BankStatementImportLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatementImportLog
        fields = '__all__'

class BankStatementImportLogViewSet(viewsets.ModelViewSet):
    queryset = BankStatementImportLog.objects.all()
    serializer_class = BankStatementImportLogSerializer

class PaymentGatewayAccount(BaseDocument):
    payment_gateway = models.ForeignKey('erp_core.PaymentGateway', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Gateway')
    is_default = models.BooleanField(default=False, verbose_name="Is Default")
    payment_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Account')
    currency = models.TextField(blank=True, null=True, verbose_name="Currency")
    message = models.TextField(blank=True, null=True, verbose_name="Default Payment Request Message")
    payment_channel = models.CharField(max_length=255, choices=[('Email', 'Email'), ('Phone', 'Phone'), ('Other', 'Other')], blank=True, null=True, verbose_name='Payment Channel')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class PaymentGatewayAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentGatewayAccount
        fields = '__all__'

class PaymentGatewayAccountViewSet(viewsets.ModelViewSet):
    queryset = PaymentGatewayAccount.objects.all()
    serializer_class = PaymentGatewayAccountSerializer

class PromotionalSchemePriceDiscount(BaseDocument):
    disable = models.BooleanField(default=False, verbose_name="Disable")
    rule_description = models.TextField(blank=True, null=True, verbose_name="Rule Description")
    min_qty = models.FloatField(default=0.0, verbose_name="Min Qty")
    max_qty = models.FloatField(default=0.0, verbose_name="Max Qty")
    min_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Min Amount")
    max_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Max Amount")
    rate_or_discount = models.CharField(max_length=255, choices=[('Rate', 'Rate'), ('Discount Percentage', 'Discount Percentage'), ('Discount Amount', 'Discount Amount')], blank=True, null=True, verbose_name='Discount Type')
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
    discount_percentage = models.FloatField(default=0.0, verbose_name="Discount Percentage")
    for_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='For Price List')
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    threshold_percentage = models.TextField(blank=True, null=True, verbose_name="Threshold for Suggestion")
    validate_applied_rule = models.BooleanField(default=False, verbose_name="Validate Applied Rule")
    priority = models.CharField(max_length=255, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], blank=True, null=True, verbose_name='Priority')
    apply_multiple_pricing_rules = models.BooleanField(default=False, verbose_name="Apply Multiple Pricing Rules")
    apply_discount_on_rate = models.BooleanField(default=False, verbose_name="Apply Discount on Rate")

class PromotionalSchemePriceDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionalSchemePriceDiscount
        fields = '__all__'

class PromotionalSchemePriceDiscountViewSet(viewsets.ModelViewSet):
    queryset = PromotionalSchemePriceDiscount.objects.all()
    serializer_class = PromotionalSchemePriceDiscountSerializer

class PaymentReconciliation(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    receivable_payable_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Receivable / Payable Account')
    bank_cash_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank / Cash Account')
    payments = models.JSONField(default=list, blank=True, null=True, verbose_name="Payments")
    invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="Invoices")
    allocation = models.JSONField(default=list, blank=True, null=True, verbose_name="Allocation")
    from_invoice_date = models.DateField(blank=True, null=True, verbose_name="From Invoice Date")
    to_invoice_date = models.DateField(blank=True, null=True, verbose_name="To Invoice Date")
    minimum_invoice_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Minimum Invoice Amount")
    invoice_limit = models.IntegerField(default=0, verbose_name="Invoice Limit")
    from_payment_date = models.DateField(blank=True, null=True, verbose_name="From Payment Date")
    to_payment_date = models.DateField(blank=True, null=True, verbose_name="To Payment Date")
    minimum_payment_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Minimum Payment Amount")
    maximum_payment_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Maximum Payment Amount")
    payment_limit = models.IntegerField(default=0, verbose_name="Payment Limit")
    maximum_invoice_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Maximum Invoice Amount")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    default_advance_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Advance Account')
    invoice_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Filter on Invoice")
    payment_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Filter on Payment")

class PaymentReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReconciliation
        fields = '__all__'

class PaymentReconciliationViewSet(viewsets.ModelViewSet):
    queryset = PaymentReconciliation.objects.all()
    serializer_class = PaymentReconciliationSerializer

class PSOACostCenter(BaseDocument):
    cost_center_name = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')

class PSOACostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSOACostCenter
        fields = '__all__'

class PSOACostCenterViewSet(viewsets.ModelViewSet):
    queryset = PSOACostCenter.objects.all()
    serializer_class = PSOACostCenterSerializer

class BudgetDistribution(BaseDocument):
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    percent = models.TextField(blank=True, null=True, verbose_name="Percent")

class BudgetDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetDistribution
        fields = '__all__'

class BudgetDistributionViewSet(viewsets.ModelViewSet):
    queryset = BudgetDistribution.objects.all()
    serializer_class = BudgetDistributionSerializer

class PricingRuleBrand(BaseDocument):
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class PricingRuleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRuleBrand
        fields = '__all__'

class PricingRuleBrandViewSet(viewsets.ModelViewSet):
    queryset = PricingRuleBrand.objects.all()
    serializer_class = PricingRuleBrandSerializer

class AccountingPeriod(BaseDocument):
    period_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Period Name")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    closed_documents = models.JSONField(default=list, blank=True, null=True, verbose_name="Closed Documents")
    exempted_role = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Exempted Role')

class AccountingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingPeriod
        fields = '__all__'

class AccountingPeriodViewSet(viewsets.ModelViewSet):
    queryset = AccountingPeriod.objects.all()
    serializer_class = AccountingPeriodSerializer

class FiscalYearCompany(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class FiscalYearCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYearCompany
        fields = '__all__'

class FiscalYearCompanyViewSet(viewsets.ModelViewSet):
    queryset = FiscalYearCompany.objects.all()
    serializer_class = FiscalYearCompanySerializer

class AllowedToTransactWith(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class AllowedToTransactWithSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedToTransactWith
        fields = '__all__'

class AllowedToTransactWithViewSet(viewsets.ModelViewSet):
    queryset = AllowedToTransactWith.objects.all()
    serializer_class = AllowedToTransactWithSerializer

class MonthlyDistribution(BaseDocument):
    distribution_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Distribution Name")
    fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fiscal Year')
    percentages = models.JSONField(default=list, blank=True, null=True, verbose_name="Monthly Distribution Percentages")

class MonthlyDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyDistribution
        fields = '__all__'

class MonthlyDistributionViewSet(viewsets.ModelViewSet):
    queryset = MonthlyDistribution.objects.all()
    serializer_class = MonthlyDistributionSerializer

class SalesTaxesandCharges(BaseDocument):
    charge_type = models.CharField(max_length=255, choices=[('Actual', 'Actual'), ('On Net Total', 'On Net Total'), ('On Previous Row Amount', 'On Previous Row Amount'), ('On Previous Row Total', 'On Previous Row Total'), ('On Item Quantity', 'On Item Quantity')], blank=True, null=True, verbose_name='Type')
    row_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row #")
    account_head = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Head')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    included_in_print_rate = models.BooleanField(default=False, verbose_name="Is this Tax included in Basic Rate?")
    rate = models.FloatField(default=0.0, verbose_name="Tax Rate")
    tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    tax_amount_after_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Tax Amount After Discount Amount")
    base_tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_tax_amount_after_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Tax Amount After Discount Amount (Company Currency)")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    included_in_paid_amount = models.BooleanField(default=False, verbose_name="Considered In Paid Amount")
    dont_recompute_tax = models.BooleanField(default=False, verbose_name="Don't Recompute Tax")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    set_by_item_tax_template = models.BooleanField(default=False, verbose_name="Set by Item Tax Template")
    is_tax_withholding_account = models.BooleanField(default=False, verbose_name="Is Tax Withholding Account")

class SalesTaxesandChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTaxesandCharges
        fields = '__all__'

class SalesTaxesandChargesViewSet(viewsets.ModelViewSet):
    queryset = SalesTaxesandCharges.objects.all()
    serializer_class = SalesTaxesandChargesSerializer

class ExchangeRateRevaluation(BaseDocument):
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Exchange Rate Revaluation Account")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    gain_loss_unbooked = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Gain/Loss from Revaluation")
    gain_loss_booked = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Gain/Loss already booked")
    total_gain_loss = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Gain/Loss")
    rounding_loss_allowance = models.FloatField(default=0.0, verbose_name="Rounding Loss Allowance")

class ExchangeRateRevaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateRevaluation
        fields = '__all__'

class ExchangeRateRevaluationViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRateRevaluation.objects.all()
    serializer_class = ExchangeRateRevaluationSerializer

class RepostAccountingLedger(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    vouchers = models.JSONField(default=list, blank=True, null=True, verbose_name="Vouchers")
    delete_cancelled_entries = models.BooleanField(default=False, verbose_name="Delete Cancelled Ledger Entries")

class RepostAccountingLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostAccountingLedger
        fields = '__all__'

class RepostAccountingLedgerViewSet(viewsets.ModelViewSet):
    queryset = RepostAccountingLedger.objects.all()
    serializer_class = RepostAccountingLedgerSerializer

class ItemTaxTemplate(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Tax Rates")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class ItemTaxTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTaxTemplate
        fields = '__all__'

class ItemTaxTemplateViewSet(viewsets.ModelViewSet):
    queryset = ItemTaxTemplate.objects.all()
    serializer_class = ItemTaxTemplateSerializer

class TaxWithholdingCategory(BaseDocument):
    category_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Category Name")
    rates = models.JSONField(default=list, blank=True, null=True, verbose_name="Rates")
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounts")
    tax_on_excess_amount = models.BooleanField(default=False, verbose_name="Only Deduct Tax On Excess Amount ")
    round_off_tax_amount = models.BooleanField(default=False, verbose_name="Round Off Tax Amount")
    tax_deduction_basis = models.CharField(max_length=255, choices=[('Gross Total', 'Gross Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Deduct Tax On Basis')
    disable_cumulative_threshold = models.BooleanField(default=False, verbose_name="Disable Cumulative Threshold")
    disable_transaction_threshold = models.BooleanField(default=False, verbose_name="Disable Transaction Threshold")

class TaxWithholdingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxWithholdingCategory
        fields = '__all__'

class TaxWithholdingCategoryViewSet(viewsets.ModelViewSet):
    queryset = TaxWithholdingCategory.objects.all()
    serializer_class = TaxWithholdingCategorySerializer

class JournalEntryTemplate(BaseDocument):
    voucher_type = models.CharField(max_length=255, choices=[('Journal Entry', 'Journal Entry'), ('Inter Company Journal Entry', 'Inter Company Journal Entry'), ('Bank Entry', 'Bank Entry'), ('Cash Entry', 'Cash Entry'), ('Credit Card Entry', 'Credit Card Entry'), ('Debit Note', 'Debit Note'), ('Credit Note', 'Credit Note'), ('Contra Entry', 'Contra Entry'), ('Excise Entry', 'Excise Entry'), ('Write Off Entry', 'Write Off Entry'), ('Opening Entry', 'Opening Entry'), ('Depreciation Entry', 'Depreciation Entry'), ('Exchange Rate Revaluation', 'Exchange Rate Revaluation')], blank=True, null=True, verbose_name='Journal Entry Type')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening')
    accounts = models.JSONField(default=list, blank=True, null=True, verbose_name="Accounting Entries")
    naming_series = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Series')
    template_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Template Title")
    multi_currency = models.BooleanField(default=False, verbose_name="Multi Currency")

class JournalEntryTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryTemplate
        fields = '__all__'

class JournalEntryTemplateViewSet(viewsets.ModelViewSet):
    queryset = JournalEntryTemplate.objects.all()
    serializer_class = JournalEntryTemplateSerializer

class PaymentOrder(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('PMO-', 'PMO-')], blank=True, null=True, verbose_name='Series')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    party = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    references = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Order Reference")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    payment_order_type = models.CharField(max_length=255, choices=[('Payment Request', 'Payment Request'), ('Payment Entry', 'Payment Entry')], blank=True, null=True, verbose_name='Payment Order Type')
    company_bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Bank Account')
    company_bank = models.ForeignKey('erp_core.Bank', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank')
    account = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account")

class PaymentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOrder
        fields = '__all__'

class PaymentOrderViewSet(viewsets.ModelViewSet):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderSerializer

class SubscriptionPlanDetail(BaseDocument):
    qty = models.IntegerField(default=0, verbose_name="Quantity")
    plan = models.ForeignKey('erp_core.SubscriptionPlan', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Plan')

class SubscriptionPlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlanDetail
        fields = '__all__'

class SubscriptionPlanDetailViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlanDetail.objects.all()
    serializer_class = SubscriptionPlanDetailSerializer

class POSField(BaseDocument):
    fieldname = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Fieldname')
    fieldtype = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fieldtype")
    label = models.CharField(max_length=255, blank=True, null=True, verbose_name="Label")
    options = models.TextField(blank=True, null=True, verbose_name="Options")
    reqd = models.BooleanField(default=False, verbose_name="Mandatory")
    read_only = models.BooleanField(default=False, verbose_name="Read Only")
    default_value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Default Value")

class POSFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSField
        fields = '__all__'

class POSFieldViewSet(viewsets.ModelViewSet):
    queryset = POSField.objects.all()
    serializer_class = POSFieldSerializer

class PeriodClosingVoucher(BaseDocument):
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Transaction Date")
    fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fiscal Year')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    closing_account_head = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Closing Account Head')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    gle_processing_status = models.CharField(max_length=255, choices=[('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Failed', 'Failed')], blank=True, null=True, verbose_name='GL Entry Processing Status')
    error_message = models.TextField(blank=True, null=True, verbose_name="Error Message")
    period_end_date = models.DateField(blank=True, null=True, verbose_name="Period End Date")
    period_start_date = models.DateField(blank=True, null=True, verbose_name="Period Start Date")

class PeriodClosingVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodClosingVoucher
        fields = '__all__'

class PeriodClosingVoucherViewSet(viewsets.ModelViewSet):
    queryset = PeriodClosingVoucher.objects.all()
    serializer_class = PeriodClosingVoucherSerializer

class POSInvoiceReference(BaseDocument):
    pos_invoice = models.ForeignKey('erp_core.POSInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Invoice')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    is_return = models.BooleanField(default=False, verbose_name="Is Return")
    return_against = models.ForeignKey('erp_core.POSInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against')

class POSInvoiceReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSInvoiceReference
        fields = '__all__'

class POSInvoiceReferenceViewSet(viewsets.ModelViewSet):
    queryset = POSInvoiceReference.objects.all()
    serializer_class = POSInvoiceReferenceSerializer

class BankTransaction(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ACC-BTN-.YYYY.-', 'ACC-BTN-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Settled', 'Settled'), ('Unreconciled', 'Unreconciled'), ('Reconciled', 'Reconciled'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    reference_number = models.TextField(blank=True, null=True, verbose_name="Reference Number")
    transaction_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Transaction ID")
    payment_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Entries")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated Amount")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    unallocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Unallocated Amount")
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    deposit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Deposit")
    withdrawal = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Withdrawal")
    transaction_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Transaction Type")
    bank_party_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Name/Account Holder (Bank Statement)")
    bank_party_iban = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party IBAN (Bank Statement)")
    bank_party_account_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Account No. (Bank Statement)")
    included_fee = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Included Fee")
    excluded_fee = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Excluded Fee")
    is_rule_evaluated = models.BooleanField(default=False, verbose_name="Is Rule Evaluated")
    matched_transaction_rule = models.ForeignKey('erp_core.BankTransactionRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Matched Transaction Rule')

class BankTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransaction
        fields = '__all__'

class BankTransactionViewSet(viewsets.ModelViewSet):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer

class POSProfileUser(BaseDocument):
    default = models.BooleanField(default=False, verbose_name="Default")
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')

class POSProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSProfileUser
        fields = '__all__'

class POSProfileUserViewSet(viewsets.ModelViewSet):
    queryset = POSProfileUser.objects.all()
    serializer_class = POSProfileUserSerializer

class SalesInvoiceAdvance(BaseDocument):
    reference_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    reference_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row")
    advance_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Advance amount")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated amount")
    exchange_gain_loss = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Exchange Gain/Loss")
    ref_exchange_rate = models.FloatField(default=0.0, verbose_name="Reference Exchange Rate")
    difference_posting_date = models.DateField(blank=True, null=True, verbose_name="Difference Posting Date")

class SalesInvoiceAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoiceAdvance
        fields = '__all__'

class SalesInvoiceAdvanceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoiceAdvance.objects.all()
    serializer_class = SalesInvoiceAdvanceSerializer

class PricingRuleItemGroup(BaseDocument):
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class PricingRuleItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRuleItemGroup
        fields = '__all__'

class PricingRuleItemGroupViewSet(viewsets.ModelViewSet):
    queryset = PricingRuleItemGroup.objects.all()
    serializer_class = PricingRuleItemGroupSerializer

class BankStatementImportLogColumnMap(BaseDocument):
    header_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Header Text")
    maps_to = models.CharField(max_length=255, choices=[('Do not import', 'Do not import'), ('Date', 'Date'), ('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit'), ('Amount', 'Amount'), ('Description', 'Description'), ('Reference', 'Reference'), ('Transaction Type', 'Transaction Type'), ('Debit/Credit', 'Debit/Credit'), ('Balance', 'Balance'), ('Included Fee', 'Included Fee'), ('Excluded Fee', 'Excluded Fee'), ('Party Name/Account Holder', 'Party Name/Account Holder'), ('Party Account No.', 'Party Account No.'), ('Party IBAN', 'Party IBAN')], blank=True, null=True, verbose_name='Maps To')
    index = models.IntegerField(default=0, verbose_name="Index")
    variable = models.CharField(max_length=255, blank=True, null=True, verbose_name="Variable")

class BankStatementImportLogColumnMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatementImportLogColumnMap
        fields = '__all__'

class BankStatementImportLogColumnMapViewSet(viewsets.ModelViewSet):
    queryset = BankStatementImportLogColumnMap.objects.all()
    serializer_class = BankStatementImportLogColumnMapSerializer

class POSClosingEntry(BaseDocument):
    period_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Period Start Date")
    period_end_date = models.DateTimeField(blank=True, null=True, verbose_name="Period End Date")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    pos_profile = models.ForeignKey('erp_core.POSProfile', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Profile')
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cashier')
    payment_reconciliation = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Reconciliation")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total")
    total_quantity = models.FloatField(default=0.0, verbose_name="Total Quantity")
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Taxes")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    pos_opening_entry = models.ForeignKey('erp_core.POSOpeningEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Opening Entry')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Queued', 'Queued'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    error_message = models.TextField(blank=True, null=True, verbose_name="Error")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    pos_invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="POS Transactions")
    sales_invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Invoice Transactions")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")

class POSClosingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = POSClosingEntry
        fields = '__all__'

class POSClosingEntryViewSet(viewsets.ModelViewSet):
    queryset = POSClosingEntry.objects.all()
    serializer_class = POSClosingEntrySerializer

class LoyaltyProgramCollection(BaseDocument):
    tier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tier Name")
    min_spent = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Minimum Total Spent")
    collection_factor = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Collection Factor (=1 LP)")

class LoyaltyProgramCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgramCollection
        fields = '__all__'

class LoyaltyProgramCollectionViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyProgramCollection.objects.all()
    serializer_class = LoyaltyProgramCollectionSerializer

class POSSearchFields(BaseDocument):
    fieldname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fieldname")
    field = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Field')

class POSSearchFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSSearchFields
        fields = '__all__'

class POSSearchFieldsViewSet(viewsets.ModelViewSet):
    queryset = POSSearchFields.objects.all()
    serializer_class = POSSearchFieldsSerializer

class ProcessPaymentReconciliationLog(BaseDocument):
    allocations = models.JSONField(default=list, blank=True, null=True, verbose_name="Allocations")
    reconciled = models.BooleanField(default=False, verbose_name="Reconciled")
    total_allocations = models.IntegerField(default=0, verbose_name="Total Allocations")
    allocated = models.BooleanField(default=False, verbose_name="Allocated")
    reconciled_entries = models.IntegerField(default=0, verbose_name="Reconciled Entries")
    error_log = models.TextField(blank=True, null=True, verbose_name="Reconciliation Error Log")
    process_pr = models.ForeignKey('erp_core.ProcessPaymentReconciliation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Document')
    status = models.CharField(max_length=255, choices=[('Running', 'Running'), ('Paused', 'Paused'), ('Reconciled', 'Reconciled'), ('Partially Reconciled', 'Partially Reconciled'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')

class ProcessPaymentReconciliationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessPaymentReconciliationLog
        fields = '__all__'

class ProcessPaymentReconciliationLogViewSet(viewsets.ModelViewSet):
    queryset = ProcessPaymentReconciliationLog.objects.all()
    serializer_class = ProcessPaymentReconciliationLogSerializer

class BankTransactionPayments(BaseDocument):
    payment_document = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Document')
    payment_entry = models.TextField(blank=True, null=True, verbose_name="Payment Entry")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated Amount")
    clearance_date = models.DateField(blank=True, null=True, verbose_name="Clearance Date")
    reconciliation_type = models.CharField(max_length=255, choices=[('Matched', 'Matched'), ('Voucher Created', 'Voucher Created')], blank=True, null=True, verbose_name='Reconciliation Type')

class BankTransactionPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactionPayments
        fields = '__all__'

class BankTransactionPaymentsViewSet(viewsets.ModelViewSet):
    queryset = BankTransactionPayments.objects.all()
    serializer_class = BankTransactionPaymentsSerializer

class CurrencyExchangeSettingsDetails(BaseDocument):
    key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Key")
    value = models.CharField(max_length=255, blank=True, null=True, verbose_name="Value")

class CurrencyExchangeSettingsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchangeSettingsDetails
        fields = '__all__'

class CurrencyExchangeSettingsDetailsViewSet(viewsets.ModelViewSet):
    queryset = CurrencyExchangeSettingsDetails.objects.all()
    serializer_class = CurrencyExchangeSettingsDetailsSerializer

class PromotionalSchemeProductDiscount(BaseDocument):
    disable = models.BooleanField(default=False, verbose_name="Disable")
    rule_description = models.TextField(blank=True, null=True, verbose_name="Rule Description")
    min_qty = models.FloatField(default=0.0, verbose_name="Min Qty")
    max_qty = models.FloatField(default=0.0, verbose_name="Max Qty")
    min_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Min Amount")
    max_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Max Amount")
    same_item = models.BooleanField(default=False, verbose_name="Same Item")
    free_item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    free_qty = models.FloatField(default=0.0, verbose_name="Qty")
    free_item_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    free_item_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Warehouse')
    threshold_percentage = models.TextField(blank=True, null=True, verbose_name="Threshold for Suggestion")
    priority = models.CharField(max_length=255, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], blank=True, null=True, verbose_name='Priority')
    apply_multiple_pricing_rules = models.BooleanField(default=False, verbose_name="Apply Multiple Pricing Rules")
    is_recursive = models.BooleanField(default=False, verbose_name="Is Recursive")
    recurse_for = models.FloatField(default=0.0, verbose_name="Recurse Every (As Per Transaction UOM)")
    apply_recursion_over = models.FloatField(default=0.0, verbose_name="Apply Recursion Over (As Per Transaction UOM)")
    round_free_qty = models.BooleanField(default=False, verbose_name="Round Free Qty")

class PromotionalSchemeProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionalSchemeProductDiscount
        fields = '__all__'

class PromotionalSchemeProductDiscountViewSet(viewsets.ModelViewSet):
    queryset = PromotionalSchemeProductDiscount.objects.all()
    serializer_class = PromotionalSchemeProductDiscountSerializer

class BankStatementImport(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    bank = models.ForeignKey('erp_core.Bank', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank')
    import_file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Import File")
    template_options = models.TextField(blank=True, null=True, verbose_name="Template Options")
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Partial Success', 'Partial Success'), ('Error', 'Error')], blank=True, null=True, verbose_name='Status')
    template_warnings = models.TextField(blank=True, null=True, verbose_name="Template Warnings")
    show_failed_logs = models.BooleanField(default=False, verbose_name="Show Failed Logs")
    google_sheets_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Import from Google Sheets")
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Document Type')
    import_type = models.CharField(max_length=255, choices=[('Insert New Records', 'Insert New Records'), ('Update Existing Records', 'Update Existing Records')], blank=True, null=True, verbose_name='Import Type')
    submit_after_import = models.BooleanField(default=False, verbose_name="Submit After Import")
    mute_emails = models.BooleanField(default=False, verbose_name="Don't Send Emails")
    custom_delimiters = models.BooleanField(default=False, verbose_name="Custom delimiters")
    delimiter_options = models.CharField(max_length=255, blank=True, null=True, verbose_name="Delimiter options")
    use_csv_sniffer = models.BooleanField(default=False, verbose_name="Use CSV Sniffer")
    import_mt940_fromat = models.BooleanField(default=False, verbose_name="Import MT940 Fromat")

class BankStatementImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatementImport
        fields = '__all__'

class BankStatementImportViewSet(viewsets.ModelViewSet):
    queryset = BankStatementImport.objects.all()
    serializer_class = BankStatementImportSerializer

class ModeofPaymentAccount(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    default_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Account')

class ModeofPaymentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeofPaymentAccount
        fields = '__all__'

class ModeofPaymentAccountViewSet(viewsets.ModelViewSet):
    queryset = ModeofPaymentAccount.objects.all()
    serializer_class = ModeofPaymentAccountSerializer

class DunningType(BaseDocument):
    dunning_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dunning Type")
    dunning_fee = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Dunning Fee")
    dunning_letter_text = models.JSONField(default=list, blank=True, null=True, verbose_name="dunning_letter_text")
    rate_of_interest = models.FloatField(default=0.0, verbose_name="Rate of Interest (%) Yearly")
    is_default = models.BooleanField(default=False, verbose_name="Is Default")
    income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Income Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class DunningTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DunningType
        fields = '__all__'

class DunningTypeViewSet(viewsets.ModelViewSet):
    queryset = DunningType.objects.all()
    serializer_class = DunningTypeSerializer

class ProcessStatementOfAccounts(BaseDocument):
    frequency = models.CharField(max_length=255, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Biweekly', 'Biweekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly')], blank=True, null=True, verbose_name='Frequency')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    cost_center = models.TextField(blank=True, null=True, verbose_name="Cost Center")
    project = models.TextField(blank=True, null=True, verbose_name="Project")
    customer_collection = models.CharField(max_length=255, choices=[('Customer Group', 'Customer Group'), ('Territory', 'Territory'), ('Sales Partner', 'Sales Partner'), ('Sales Person', 'Sales Person')], blank=True, null=True, verbose_name='Select Customers By')
    collection_name = models.TextField(blank=True, null=True, verbose_name="Recipient")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    orientation = models.CharField(max_length=255, choices=[('Landscape', 'Landscape'), ('Portrait', 'Portrait')], blank=True, null=True, verbose_name='Orientation')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    include_ageing = models.BooleanField(default=False, verbose_name="Include Ageing Summary")
    ageing_based_on = models.CharField(max_length=255, choices=[('Due Date', 'Due Date'), ('Posting Date', 'Posting Date')], blank=True, null=True, verbose_name='Ageing Based On')
    enable_auto_email = models.BooleanField(default=False, verbose_name="Enable Auto Email")
    primary_mandatory = models.BooleanField(default=False, verbose_name="Send To Primary Contact")
    cc_to = models.TextField(blank=True, null=True, verbose_name="CC To")
    filter_duration = models.IntegerField(default=0, verbose_name="Filter Duration (Months)")
    customers = models.JSONField(default=list, blank=True, null=True, verbose_name="Customers")
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    terms_and_conditions = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms and Conditions')
    include_break = models.BooleanField(default=False, verbose_name="Page Break After Each SoA")
    show_net_values_in_party_account = models.BooleanField(default=False, verbose_name="Show Net Values in Party Account")
    sender = models.ForeignKey('erp_core.EmailAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sender')
    report = models.CharField(max_length=255, choices=[('General Ledger', 'General Ledger'), ('Accounts Receivable', 'Accounts Receivable')], blank=True, null=True, verbose_name='Report')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    sales_person = models.ForeignKey('erp_core.SalesPerson', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Person')
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    based_on_payment_terms = models.BooleanField(default=False, verbose_name="Based On Payment Terms")
    pdf_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="PDF Name")
    ignore_exchange_rate_revaluation_journals = models.BooleanField(default=False, verbose_name="Ignore Exchange Rate Revaluation and Gain / Loss Journals")
    ignore_cr_dr_notes = models.BooleanField(default=False, verbose_name="Ignore System Generated Credit / Debit Notes")
    show_remarks = models.BooleanField(default=False, verbose_name="Show Remarks")
    categorize_by = models.CharField(max_length=255, choices=[('Categorize by Voucher', 'Categorize by Voucher'), ('Categorize by Voucher (Consolidated)', 'Categorize by Voucher (Consolidated)')], blank=True, null=True, verbose_name='Categorize By')
    show_future_payments = models.BooleanField(default=False, verbose_name="Show Future Payments")
    print_format = models.ForeignKey('erp_core.PrintFormat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Format')

class ProcessStatementOfAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStatementOfAccounts
        fields = '__all__'

class ProcessStatementOfAccountsViewSet(viewsets.ModelViewSet):
    queryset = ProcessStatementOfAccounts.objects.all()
    serializer_class = ProcessStatementOfAccountsSerializer

class AdvanceTaxesandCharges(BaseDocument):
    charge_type = models.CharField(max_length=255, choices=[('Actual', 'Actual'), ('On Paid Amount', 'On Paid Amount'), ('On Previous Row Amount', 'On Previous Row Amount'), ('On Previous Row Total', 'On Previous Row Total')], blank=True, null=True, verbose_name='Type')
    row_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row #")
    account_head = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Head')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    rate = models.FloatField(default=0.0, verbose_name="Tax Rate")
    tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    base_tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    add_deduct_tax = models.CharField(max_length=255, choices=[('Add', 'Add'), ('Deduct', 'Deduct')], blank=True, null=True, verbose_name='Add Or Deduct')
    included_in_paid_amount = models.BooleanField(default=False, verbose_name="Considered In Paid Amount")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    set_by_item_tax_template = models.BooleanField(default=False, verbose_name="Set by Item Tax Template")
    is_tax_withholding_account = models.BooleanField(default=False, verbose_name="Is Tax Withholding Account")

class AdvanceTaxesandChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvanceTaxesandCharges
        fields = '__all__'

class AdvanceTaxesandChargesViewSet(viewsets.ModelViewSet):
    queryset = AdvanceTaxesandCharges.objects.all()
    serializer_class = AdvanceTaxesandChargesSerializer

class PricingRuleItemCode(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Code')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class PricingRuleItemCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRuleItemCode
        fields = '__all__'

class PricingRuleItemCodeViewSet(viewsets.ModelViewSet):
    queryset = PricingRuleItemCode.objects.all()
    serializer_class = PricingRuleItemCodeSerializer

class CustomerGroupItem(BaseDocument):
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')

class CustomerGroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroupItem
        fields = '__all__'

class CustomerGroupItemViewSet(viewsets.ModelViewSet):
    queryset = CustomerGroupItem.objects.all()
    serializer_class = CustomerGroupItemSerializer

class PaymentRequest(BaseDocument):
    payment_request_type = models.CharField(max_length=255, choices=[('Outward', 'Outward'), ('Inward', 'Inward')], blank=True, null=True, verbose_name='Payment Request Type')
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Transaction Date")
    naming_series = models.CharField(max_length=255, choices=[('ACC-PRQ-.YYYY.-', 'ACC-PRQ-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Doctype')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    is_a_subscription = models.BooleanField(default=False, verbose_name="Is a Subscription")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Transaction Currency')
    subscription_plans = models.JSONField(default=list, blank=True, null=True, verbose_name="Subscription Plans")
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    bank = models.ForeignKey('erp_core.Bank', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank')
    bank_account_no = models.TextField(blank=True, null=True, verbose_name="Bank Account No")
    account = models.TextField(blank=True, null=True, verbose_name="Account")
    iban = models.TextField(blank=True, null=True, verbose_name="IBAN")
    branch_code = models.TextField(blank=True, null=True, verbose_name="Branch Code")
    swift_number = models.TextField(blank=True, null=True, verbose_name="SWIFT Number")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    print_format = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Print Format')
    email_to = models.CharField(max_length=255, blank=True, null=True, verbose_name="To")
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")
    payment_gateway_account = models.ForeignKey('erp_core.PaymentGatewayAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Gateway Account')
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Requested', 'Requested'), ('Initiated', 'Initiated'), ('Partially Paid', 'Partially Paid'), ('Payment Ordered', 'Payment Ordered'), ('Paid', 'Paid'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    make_sales_invoice = models.BooleanField(default=False, verbose_name="Make Sales Invoice")
    message = models.TextField(blank=True, null=True, verbose_name="Message")
    mute_email = models.BooleanField(default=False, verbose_name="Mute Email")
    payment_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Payment URL")
    payment_gateway = models.TextField(blank=True, null=True, verbose_name="Payment Gateway")
    payment_account = models.TextField(blank=True, null=True, verbose_name="Payment Account")
    payment_channel = models.CharField(max_length=255, choices=[('Email', 'Email'), ('Phone', 'Phone'), ('Other', 'Other')], blank=True, null=True, verbose_name='Payment Channel')
    payment_order = models.ForeignKey('erp_core.PaymentOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Order')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    failed_reason = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reason for Failure")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    party_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Account Currency')
    party_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Name")
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone Number")
    payment_reference = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Reference")

class PaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = '__all__'

class PaymentRequestViewSet(viewsets.ModelViewSet):
    queryset = PaymentRequest.objects.all()
    serializer_class = PaymentRequestSerializer

class OpeningInvoiceCreationTool(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    create_missing_party = models.BooleanField(default=False, verbose_name="Create Missing Party")
    invoice_type = models.CharField(max_length=255, choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], blank=True, null=True, verbose_name='Invoice Type')
    invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="invoices")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')

class OpeningInvoiceCreationToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningInvoiceCreationTool
        fields = '__all__'

class OpeningInvoiceCreationToolViewSet(viewsets.ModelViewSet):
    queryset = OpeningInvoiceCreationTool.objects.all()
    serializer_class = OpeningInvoiceCreationToolSerializer

class RepostPaymentLedgerItems(BaseDocument):
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")

class RepostPaymentLedgerItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostPaymentLedgerItems
        fields = '__all__'

class RepostPaymentLedgerItemsViewSet(viewsets.ModelViewSet):
    queryset = RepostPaymentLedgerItems.objects.all()
    serializer_class = RepostPaymentLedgerItemsSerializer

class FiscalYear(BaseDocument):
    year = models.CharField(max_length=255, blank=True, null=True, verbose_name="Year Name")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    year_start_date = models.DateField(blank=True, null=True, verbose_name="Year Start Date")
    year_end_date = models.DateField(blank=True, null=True, verbose_name="Year End Date")
    companies = models.JSONField(default=list, blank=True, null=True, verbose_name="Companies")
    auto_created = models.BooleanField(default=False, verbose_name="Auto Created")
    is_short_year = models.BooleanField(default=False, verbose_name="Is Short/Long Year")

class FiscalYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYear
        fields = '__all__'

class FiscalYearViewSet(viewsets.ModelViewSet):
    queryset = FiscalYear.objects.all()
    serializer_class = FiscalYearSerializer

class PurchaseInvoiceItem(BaseDocument):
    item_code = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    image_view = models.TextField(blank=True, null=True, verbose_name="Image View")
    received_qty = models.FloatField(default=0.0, verbose_name="Received Qty")
    qty = models.FloatField(default=0.0, verbose_name="Accepted Qty")
    rejected_qty = models.FloatField(default=0.0, verbose_name="Rejected Qty")
    stock_uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Stock UOM')
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    conversion_factor = models.FloatField(default=0.0, verbose_name="UOM Conversion Factor")
    stock_qty = models.FloatField(default=0.0, verbose_name="Accepted Qty in Stock UOM")
    price_list_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Price List Rate")
    discount_percentage = models.TextField(blank=True, null=True, verbose_name="Discount on Price List Rate (%)")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Discount Amount")
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
    warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accepted Warehouse')
    rejected_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Warehouse')
    quality_inspection = models.ForeignKey('erp_core.QualityInspection', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Quality Inspection')
    batch_no = models.ForeignKey('erp_core.Batch', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Batch No')
    serial_no = models.TextField(blank=True, null=True, verbose_name="Serial No")
    rejected_serial_no = models.TextField(blank=True, null=True, verbose_name="Rejected Serial No")
    expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Head')
    item_tax_template = models.ForeignKey('erp_core.ItemTaxTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Tax Template')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    deferred_expense_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Deferred Expense Account')
    service_stop_date = models.DateField(blank=True, null=True, verbose_name="Service Stop Date")
    enable_deferred_expense = models.BooleanField(default=False, verbose_name="Enable Deferred Expense")
    service_start_date = models.DateField(blank=True, null=True, verbose_name="Service Start Date")
    service_end_date = models.DateField(blank=True, null=True, verbose_name="Service End Date")
    allow_zero_valuation_rate = models.BooleanField(default=False, verbose_name="Allow Zero Valuation Rate")
    brand = models.ForeignKey('erp_core.Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Brand')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    item_tax_rate = models.TextField(blank=True, null=True, verbose_name="Item Tax Rate")
    item_tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Item Tax Amount Included in Value")
    purchase_order = models.ForeignKey('erp_core.PurchaseOrder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Order')
    include_exploded_items = models.BooleanField(default=False, verbose_name="Include Exploded Items")
    is_fixed_asset = models.BooleanField(default=False, verbose_name="Is Fixed Asset")
    asset_location = models.ForeignKey('erp_core.Location', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Location')
    po_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Order Item")
    purchase_receipt = models.ForeignKey('erp_core.PurchaseReceipt', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Receipt')
    page_break = models.BooleanField(default=False, verbose_name="Page Break")
    pr_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Receipt Detail")
    valuation_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Valuation Rate")
    rm_supp_cost = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Raw Materials Supplied Cost")
    landed_cost_voucher_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Landed Cost Voucher Amount")
    manufacturer = models.ForeignKey('erp_core.Manufacturer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Manufacturer')
    manufacturer_part_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer Part Number")
    asset_category = models.ForeignKey('erp_core.AssetCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Category')
    from_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Warehouse')
    purchase_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase Invoice Item")
    stock_uom_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate of Stock UOM")
    sales_invoice_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Invoice Item")
    margin_type = models.CharField(max_length=255, choices=[('Percentage', 'Percentage'), ('Amount', 'Amount')], blank=True, null=True, verbose_name='Margin Type')
    margin_rate_or_amount = models.FloatField(default=0.0, verbose_name="Margin Rate or Amount")
    rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin")
    base_rate_with_margin = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate With Margin (Company Currency)")
    product_bundle = models.ForeignKey('erp_core.ProductBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Product Bundle')
    apply_tds = models.BooleanField(default=False, verbose_name="Consider for Tax Withholding")
    serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial and Batch Bundle')
    rejected_serial_and_batch_bundle = models.ForeignKey('erp_core.SerialandBatchBundle', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Rejected Serial and Batch Bundle')
    wip_composite_asset = models.ForeignKey('erp_core.Asset', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='WIP Composite Asset')
    use_serial_batch_fields = models.BooleanField(default=False, verbose_name="Use Serial No / Batch Fields")
    material_request = models.ForeignKey('erp_core.MaterialRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Material Request')
    material_request_item = models.CharField(max_length=255, blank=True, null=True, verbose_name="Material Request Item")
    sales_incoming_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Sales Incoming Rate")
    distributed_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Distributed Discount Amount")
    tax_withholding_category = models.ForeignKey('erp_core.TaxWithholdingCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Category')
    delivered_by_supplier = models.BooleanField(default=False, verbose_name="Delivered by Supplier")

class PurchaseInvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceItem
        fields = '__all__'

class PurchaseInvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoiceItem.objects.all()
    serializer_class = PurchaseInvoiceItemSerializer

class POSCustomerGroup(BaseDocument):
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')

class POSCustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSCustomerGroup
        fields = '__all__'

class POSCustomerGroupViewSet(viewsets.ModelViewSet):
    queryset = POSCustomerGroup.objects.all()
    serializer_class = POSCustomerGroupSerializer

class SalesInvoice(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ACC-SINV-.YYYY.-', 'ACC-SINV-.YYYY.-'), ('ACC-SINV-RET-.YYYY.-', 'ACC-SINV-RET-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.TextField(blank=True, null=True, verbose_name="Customer Name")
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax Id")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    is_pos = models.BooleanField(default=False, verbose_name="Include Payment (POS)")
    pos_profile = models.ForeignKey('erp_core.POSProfile', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Profile')
    is_return = models.BooleanField(default=False, verbose_name="Is Return (Credit Note)")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    due_date = models.DateField(blank=True, null=True, verbose_name="Payment Due Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    return_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against')
    update_billed_amount_in_sales_order = models.BooleanField(default=False, verbose_name="Update Billed Amount in Sales Order")
    po_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Purchase Order")
    po_date = models.DateField(blank=True, null=True, verbose_name="Customer's Purchase Order Date")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    shipping_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address Name')
    shipping_address = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address Name')
    company_address_display = models.TextField(blank=True, null=True, verbose_name="Company Address")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    update_stock = models.BooleanField(default=False, verbose_name="Update Stock")
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Detail")
    packed_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Packed Items")
    timesheets = models.JSONField(default=list, blank=True, null=True, verbose_name="Time Sheets")
    total_billing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billing Amount")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total (Company Currency)")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total")
    total_net_weight = models.FloatField(default=0.0, verbose_name="Total Net Weight")
    taxes_and_charges = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    shipping_rule = models.ForeignKey('erp_core.ShippingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Rule')
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Taxes and Charges")
    other_charges_calculation = models.TextField(blank=True, null=True, verbose_name="Taxes and Charges Calculation")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    loyalty_points = models.IntegerField(default=0, verbose_name="Loyalty Points")
    loyalty_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Loyalty Amount")
    redeem_loyalty_points = models.BooleanField(default=False, verbose_name="Redeem Loyalty Points")
    loyalty_program = models.ForeignKey('erp_core.LoyaltyProgram', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Loyalty Program')
    loyalty_redemption_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Redemption Account')
    loyalty_redemption_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Redemption Cost Center')
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Additional Discount On')
    base_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount (Company Currency)")
    additional_discount_percentage = models.FloatField(default=0.0, verbose_name="Additional Discount Percentage")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount")
    base_grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    base_rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    base_rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    base_in_words = models.TextField(blank=True, null=True, verbose_name="In Words")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    in_words = models.TextField(blank=True, null=True, verbose_name="In Words")
    total_advance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Advance")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    allocate_advances_automatically = models.BooleanField(default=False, verbose_name="Allocate Advances Automatically (FIFO)")
    advances = models.JSONField(default=list, blank=True, null=True, verbose_name="Advances")
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    payment_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Schedule")
    cash_bank_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cash/Bank Account')
    payments = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Invoice Payment")
    base_paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount (Company Currency)")
    paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount")
    base_change_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Change Amount (Company Currency)")
    change_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Change Amount")
    account_for_change_amount = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account for Change Amount')
    write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount")
    base_write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount (Company Currency)")
    write_off_outstanding_amount_automatically = models.BooleanField(default=False, verbose_name="Write Off Outstanding Amount")
    write_off_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Account')
    write_off_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Cost Center')
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions Details")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    inter_company_invoice_reference = models.ForeignKey('erp_core.PurchaseInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Invoice Reference')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    is_discounted = models.BooleanField(default=False, verbose_name="Is Discounted")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Return', 'Return'), ('Credit Note Issued', 'Credit Note Issued'), ('Submitted', 'Submitted'), ('Paid', 'Paid'), ('Partly Paid', 'Partly Paid'), ('Unpaid', 'Unpaid'), ('Unpaid and Discounted', 'Unpaid and Discounted'), ('Partly Paid and Discounted', 'Partly Paid and Discounted'), ('Overdue and Discounted', 'Overdue and Discounted'), ('Overdue', 'Overdue'), ('Cancelled', 'Cancelled'), ('Internal Transfer', 'Internal Transfer')], blank=True, null=True, verbose_name='Status')
    debit_to = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Debit To')
    party_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Account Currency')
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening Entry')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    commission_rate = models.FloatField(default=0.0, verbose_name="Commission Rate (%)")
    total_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Commission")
    sales_team = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Contributions and Incentives")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    against_income_account = models.TextField(blank=True, null=True, verbose_name="Against Income Account")
    is_consolidated = models.BooleanField(default=False, verbose_name="Is Consolidated")
    is_internal_customer = models.BooleanField(default=False, verbose_name="Is Internal Customer")
    company_tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company Tax ID")
    unrealized_profit_loss_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Unrealized Profit / Loss Account')
    represents_company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Represents Company')
    set_target_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Set Target Warehouse')
    is_debit_note = models.BooleanField(default=False, verbose_name="Is Rate Adjustment Entry (Debit Note)")
    disable_rounded_total = models.BooleanField(default=False, verbose_name="Disable Rounded Total")
    additional_discount_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Discount Account')
    dispatch_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dispatch Address Name')
    dispatch_address = models.TextField(blank=True, null=True, verbose_name="Dispatch Address")
    ignore_default_payment_terms_template = models.BooleanField(default=False, verbose_name="Ignore Default Payment Terms Template")
    total_billing_hours = models.FloatField(default=0.0, verbose_name="Total Billing Hours")
    amount_eligible_for_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount Eligible for Commission")
    subscription = models.ForeignKey('erp_core.Subscription', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subscription')
    is_cash_or_non_trade_discount = models.BooleanField(default=False, verbose_name="Is Cash or Non Trade Discount")
    incoterm = models.ForeignKey('erp_core.Incoterm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Incoterm')
    named_place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Named Place")
    only_include_allocated_payments = models.BooleanField(default=False, verbose_name="Only Include Allocated Payments")
    use_company_roundoff_cost_center = models.BooleanField(default=False, verbose_name="Use Company default Cost Center for Round off")
    update_billed_amount_in_delivery_note = models.BooleanField(default=False, verbose_name="Update Billed Amount in Delivery Note")
    dont_create_loyalty_points = models.BooleanField(default=False, verbose_name="Don't Create Loyalty Points")
    coupon_code = models.ForeignKey('erp_core.CouponCode', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Coupon Code')
    update_outstanding_for_self = models.BooleanField(default=False, verbose_name="Update Outstanding for Self")
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_content = models.CharField(max_length=255, blank=True, null=True, verbose_name="Content")
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    company_contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Contact Person')
    is_created_using_pos = models.BooleanField(default=False, verbose_name="Is created using POS")
    pos_closing_entry = models.ForeignKey('erp_core.POSClosingEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Closing Entry')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    has_subcontracted = models.BooleanField(default=False, verbose_name="Has Subcontracted")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    apply_tds = models.BooleanField(default=False, verbose_name="Consider for Tax Withholding")
    tax_withholding_group = models.ForeignKey('erp_core.TaxWithholdingGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Withholding Group')
    tax_withholding_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="Tax Withholding Entries")
    ignore_tax_withholding_threshold = models.BooleanField(default=False, verbose_name="Ignore Tax Withholding Threshold")
    override_tax_withholding_entries = models.BooleanField(default=False, verbose_name="Edit Tax Withholding Entries")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = '__all__'

class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer

class POSSettings(BaseDocument):
    invoice_fields = models.JSONField(default=list, blank=True, null=True, verbose_name="POS Additional Fields")
    pos_search_fields = models.JSONField(default=list, blank=True, null=True, verbose_name="POS Search Fields")
    invoice_type = models.CharField(max_length=255, choices=[('Sales Invoice', 'Sales Invoice'), ('POS Invoice', 'POS Invoice')], blank=True, null=True, verbose_name='Invoice Type Created via POS Screen')
    post_change_gl_entries = models.BooleanField(default=False, verbose_name="Create Ledger Entries for Change Amount")

class POSSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSSettings
        fields = '__all__'

class POSSettingsViewSet(viewsets.ModelViewSet):
    queryset = POSSettings.objects.all()
    serializer_class = POSSettingsSerializer

class POSItemGroup(BaseDocument):
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')

class POSItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSItemGroup
        fields = '__all__'

class POSItemGroupViewSet(viewsets.ModelViewSet):
    queryset = POSItemGroup.objects.all()
    serializer_class = POSItemGroupSerializer

class Budget(BaseDocument):
    budget_against = models.CharField(max_length=255, choices=[('Cost Center', 'Cost Center'), ('Project', 'Project')], blank=True, null=True, verbose_name='Budget Against')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    applicable_on_material_request = models.BooleanField(default=False, verbose_name="Applicable on Material Request")
    action_if_annual_budget_exceeded_on_mr = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Annual Budget Exceeded on MR')
    action_if_accumulated_monthly_budget_exceeded_on_mr = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Accumulated Monthly Budget Exceeded on MR')
    applicable_on_purchase_order = models.BooleanField(default=False, verbose_name="Applicable on Purchase Order")
    action_if_annual_budget_exceeded_on_po = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Annual Budget Exceeded on PO')
    action_if_accumulated_monthly_budget_exceeded_on_po = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Accumulated Monthly Budget Exceeded on PO')
    applicable_on_booking_actual_expenses = models.BooleanField(default=False, verbose_name="Applicable on booking actual expenses")
    action_if_annual_budget_exceeded = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Annual Budget Exceeded on Actual')
    action_if_accumulated_monthly_budget_exceeded = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Accumulated Monthly Budget Exceeded on Actual')
    naming_series = models.CharField(max_length=255, choices=[('BUDGET-.########', 'BUDGET-.########')], blank=True, null=True, verbose_name='Series')
    applicable_on_cumulative_expense = models.BooleanField(default=False, verbose_name="Applicable on Cumulative Expense")
    action_if_annual_exceeded_on_cumulative_expense = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Anual Budget Exceeded on Cumulative Expense')
    action_if_accumulated_monthly_exceeded_on_cumulative_expense = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn'), ('Ignore', 'Ignore')], blank=True, null=True, verbose_name='Action if Accumulative Monthly Budget Exceeded on Cumulative Expense')
    budget_distribution = models.JSONField(default=list, blank=True, null=True, verbose_name="Budget Distribution")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    budget_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Budget Amount")
    revision_of = models.CharField(max_length=255, blank=True, null=True, verbose_name="Revision Of")
    distribute_equally = models.BooleanField(default=False, verbose_name="Distribute Equally")
    from_fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Fiscal Year')
    to_fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To Fiscal Year')
    budget_start_date = models.DateField(blank=True, null=True, verbose_name="Budget Start Date")
    budget_end_date = models.DateField(blank=True, null=True, verbose_name="Budget End Date")
    distribution_frequency = models.CharField(max_length=255, choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half-Yearly', 'Half-Yearly'), ('Yearly', 'Yearly')], blank=True, null=True, verbose_name='Distribution Frequency')
    budget_distribution_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Budget Distribution Total")

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class PaymentReconciliationPayment(BaseDocument):
    reference_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    is_advance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Is Advance")
    reference_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    difference_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference Amount")
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")

class PaymentReconciliationPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReconciliationPayment
        fields = '__all__'

class PaymentReconciliationPaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentReconciliationPayment.objects.all()
    serializer_class = PaymentReconciliationPaymentSerializer

class PaymentEntryDeduction(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    is_exchange_gain_loss = models.BooleanField(default=False, verbose_name="Is Exchange Gain / Loss?")

class PaymentEntryDeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentEntryDeduction
        fields = '__all__'

class PaymentEntryDeductionViewSet(viewsets.ModelViewSet):
    queryset = PaymentEntryDeduction.objects.all()
    serializer_class = PaymentEntryDeductionSerializer

class POSOpeningEntry(BaseDocument):
    period_start_date = models.DateTimeField(blank=True, null=True, verbose_name="Period Start Date")
    period_end_date = models.DateField(blank=True, null=True, verbose_name="Period End Date")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    pos_profile = models.ForeignKey('erp_core.POSProfile', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Profile')
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cashier')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    set_posting_date = models.BooleanField(default=False, verbose_name="Set Posting Date")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Closed', 'Closed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    pos_closing_entry = models.CharField(max_length=255, blank=True, null=True, verbose_name="POS Closing Entry")
    balance_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Opening Balance Details")

class POSOpeningEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = POSOpeningEntry
        fields = '__all__'

class POSOpeningEntryViewSet(viewsets.ModelViewSet):
    queryset = POSOpeningEntry.objects.all()
    serializer_class = POSOpeningEntrySerializer

class ProcessPaymentReconciliation(BaseDocument):
    status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed'), ('Partially Reconciled', 'Partially Reconciled'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    receivable_payable_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Receivable/Payable Account')
    from_invoice_date = models.DateField(blank=True, null=True, verbose_name="From Invoice Date")
    to_invoice_date = models.DateField(blank=True, null=True, verbose_name="To Invoice Date")
    from_payment_date = models.DateField(blank=True, null=True, verbose_name="From Payment Date")
    to_payment_date = models.DateField(blank=True, null=True, verbose_name="To Payment Date")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    bank_cash_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank/Cash Account')
    error_log = models.TextField(blank=True, null=True, verbose_name="Error Log")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    default_advance_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Advance Account')

class ProcessPaymentReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessPaymentReconciliation
        fields = '__all__'

class ProcessPaymentReconciliationViewSet(viewsets.ModelViewSet):
    queryset = ProcessPaymentReconciliation.objects.all()
    serializer_class = ProcessPaymentReconciliationSerializer

class AccountingDimension(BaseDocument):
    label = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dimension Name")
    fieldname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fieldname")
    document_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Document Type')
    disabled = models.BooleanField(default=False, verbose_name="Disable")
    dimension_defaults = models.JSONField(default=list, blank=True, null=True, verbose_name="Dimension Defaults")

class AccountingDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDimension
        fields = '__all__'

class AccountingDimensionViewSet(viewsets.ModelViewSet):
    queryset = AccountingDimension.objects.all()
    serializer_class = AccountingDimensionSerializer

class POSClosingEntryDetail(BaseDocument):
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    expected_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Expected Amount")
    difference = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference")
    opening_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Opening Amount")
    closing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Closing Amount")

class POSClosingEntryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSClosingEntryDetail
        fields = '__all__'

class POSClosingEntryDetailViewSet(viewsets.ModelViewSet):
    queryset = POSClosingEntryDetail.objects.all()
    serializer_class = POSClosingEntryDetailSerializer

class POSInvoice(BaseDocument):
    naming_series = models.CharField(max_length=255, choices=[('ACC-PSINV-.YYYY.-', 'ACC-PSINV-.YYYY.-')], blank=True, null=True, verbose_name='Series')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    tax_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax Id")
    is_pos = models.BooleanField(default=False, verbose_name="Include Payment (POS)")
    pos_profile = models.ForeignKey('erp_core.POSProfile', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Profile')
    is_return = models.BooleanField(default=False, verbose_name="Is Return (Credit Note)")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    set_posting_time = models.BooleanField(default=False, verbose_name="Edit Posting Date and Time")
    due_date = models.DateField(blank=True, null=True, verbose_name="Payment Due Date")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    return_against = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Return Against')
    update_billed_amount_in_sales_order = models.BooleanField(default=False, verbose_name="Update Billed Amount in Sales Order")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    po_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer's Purchase Order")
    po_date = models.DateField(blank=True, null=True, verbose_name="Customer's Purchase Order Date")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile No")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    territory = models.ForeignKey('erp_core.Territory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Territory')
    shipping_address_name = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Address Name')
    shipping_address = models.TextField(blank=True, null=True, verbose_name="Shipping Address")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address Name')
    company_address_display = models.TextField(blank=True, null=True, verbose_name="Company Address")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    selling_price_list = models.ForeignKey('erp_core.PriceList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List')
    price_list_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Price List Currency')
    plc_conversion_rate = models.FloatField(default=0.0, verbose_name="Price List Exchange Rate")
    ignore_pricing_rule = models.BooleanField(default=False, verbose_name="Ignore Pricing Rule")
    set_warehouse = models.ForeignKey('erp_core.Warehouse', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source Warehouse')
    update_stock = models.BooleanField(default=False, verbose_name="Update Stock")
    scan_barcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scan Barcode")
    items = models.JSONField(default=list, blank=True, null=True, verbose_name="Items")
    pricing_rules = models.JSONField(default=list, blank=True, null=True, verbose_name="Pricing Rule Detail")
    packed_items = models.JSONField(default=list, blank=True, null=True, verbose_name="Packed Items")
    timesheets = models.JSONField(default=list, blank=True, null=True, verbose_name="Time Sheets")
    total_billing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Billing Amount")
    total_qty = models.FloatField(default=0.0, verbose_name="Total Quantity")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total (Company Currency)")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    net_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Total")
    total_net_weight = models.FloatField(default=0.0, verbose_name="Total Net Weight")
    taxes_and_charges = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Taxes and Charges Template')
    shipping_rule = models.ForeignKey('erp_core.ShippingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Rule')
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Taxes and Charges")
    other_charges_calculation = models.TextField(blank=True, null=True, verbose_name="Taxes and Charges Calculation")
    base_total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges (Company Currency)")
    total_taxes_and_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Taxes and Charges")
    loyalty_points = models.IntegerField(default=0, verbose_name="Loyalty Points")
    loyalty_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Loyalty Amount")
    redeem_loyalty_points = models.BooleanField(default=False, verbose_name="Redeem Loyalty Points")
    loyalty_program = models.ForeignKey('erp_core.LoyaltyProgram', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Loyalty Program')
    loyalty_redemption_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Redemption Account')
    loyalty_redemption_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Redemption Cost Center')
    apply_discount_on = models.CharField(max_length=255, choices=[('Grand Total', 'Grand Total'), ('Net Total', 'Net Total')], blank=True, null=True, verbose_name='Apply Additional Discount On')
    base_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount (Company Currency)")
    additional_discount_percentage = models.FloatField(default=0.0, verbose_name="Additional Discount Percentage")
    discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Additional Discount Amount")
    base_grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total (Company Currency)")
    base_rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment (Company Currency)")
    base_rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total (Company Currency)")
    base_in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words (Company Currency)")
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    rounding_adjustment = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounding Adjustment")
    rounded_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rounded Total")
    in_words = models.CharField(max_length=255, blank=True, null=True, verbose_name="In Words")
    total_advance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Advance")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    allocate_advances_automatically = models.BooleanField(default=False, verbose_name="Allocate Advances Automatically (FIFO)")
    advances = models.JSONField(default=list, blank=True, null=True, verbose_name="Advances")
    payment_terms_template = models.ForeignKey('erp_core.PaymentTermsTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Terms Template')
    payment_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Schedule")
    cash_bank_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cash/Bank Account')
    payments = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Invoice Payment")
    base_paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount (Company Currency)")
    paid_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Paid Amount")
    base_change_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Change Amount (Company Currency)")
    change_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Change Amount")
    account_for_change_amount = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account for Change Amount')
    write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount")
    base_write_off_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Write Off Amount (Company Currency)")
    write_off_outstanding_amount_automatically = models.BooleanField(default=False, verbose_name="Write Off Outstanding Amount")
    write_off_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Account')
    write_off_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Write Off Cost Center')
    tc_name = models.ForeignKey('erp_core.TermsandConditions', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Terms')
    terms = models.TextField(blank=True, null=True, verbose_name="Terms and Conditions Details")
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    group_same_items = models.BooleanField(default=False, verbose_name="Group same items")
    language = models.CharField(max_length=255, blank=True, null=True, verbose_name="Print Language")
    select_print_heading = models.ForeignKey('erp_core.PrintHeading', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Heading')
    inter_company_invoice_reference = models.ForeignKey('erp_core.PurchaseInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Inter Company Invoice Reference')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    is_discounted = models.BooleanField(default=False, verbose_name="Is Discounted")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Return', 'Return'), ('Credit Note Issued', 'Credit Note Issued'), ('Consolidated', 'Consolidated'), ('Submitted', 'Submitted'), ('Paid', 'Paid'), ('Partly Paid', 'Partly Paid'), ('Unpaid', 'Unpaid'), ('Partly Paid and Discounted', 'Partly Paid and Discounted'), ('Unpaid and Discounted', 'Unpaid and Discounted'), ('Overdue and Discounted', 'Overdue and Discounted'), ('Overdue', 'Overdue'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    debit_to = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Debit To')
    party_account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Account Currency')
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening Entry')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    sales_partner = models.ForeignKey('erp_core.SalesPartner', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Partner')
    commission_rate = models.FloatField(default=0.0, verbose_name="Commission Rate (%)")
    total_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Commission")
    sales_team = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Team")
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    auto_repeat = models.ForeignKey('erp_core.AutoRepeat', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Auto Repeat')
    against_income_account = models.TextField(blank=True, null=True, verbose_name="Against Income Account")
    consolidated_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Consolidated Sales Invoice')
    coupon_code = models.ForeignKey('erp_core.CouponCode', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Coupon Code')
    amount_eligible_for_commission = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount Eligible for Commission")
    update_billed_amount_in_delivery_note = models.BooleanField(default=False, verbose_name="Update Billed Amount in Delivery Note")
    utm_medium = models.ForeignKey('erp_core.UTMMedium', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Medium')
    utm_campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')
    utm_source = models.ForeignKey('erp_core.UTMSource', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Source')
    company_contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Contact Person')
    last_scanned_warehouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Scanned Warehouse")
    item_wise_tax_details = models.JSONField(default=list, blank=True, null=True, verbose_name="Item Wise Tax Details")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")

class POSInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSInvoice
        fields = '__all__'

class POSInvoiceViewSet(viewsets.ModelViewSet):
    queryset = POSInvoice.objects.all()
    serializer_class = POSInvoiceSerializer

class SouthAfricaVATAccount(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')

class SouthAfricaVATAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SouthAfricaVATAccount
        fields = '__all__'

class SouthAfricaVATAccountViewSet(viewsets.ModelViewSet):
    queryset = SouthAfricaVATAccount.objects.all()
    serializer_class = SouthAfricaVATAccountSerializer

class PartyAccount(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Account')
    advance_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Advance Account')

class PartyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyAccount
        fields = '__all__'

class PartyAccountViewSet(viewsets.ModelViewSet):
    queryset = PartyAccount.objects.all()
    serializer_class = PartyAccountSerializer

class ShareTransfer(BaseDocument):
    transfer_type = models.CharField(max_length=255, choices=[('Issue', 'Issue'), ('Purchase', 'Purchase'), ('Transfer', 'Transfer')], blank=True, null=True, verbose_name='Transfer Type')
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    from_shareholder = models.ForeignKey('erp_core.Shareholder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Shareholder')
    from_folio_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="From Folio No")
    equity_or_liability_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Equity/Liability Account')
    asset_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Asset Account')
    to_shareholder = models.ForeignKey('erp_core.Shareholder', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To Shareholder')
    to_folio_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="To Folio No")
    share_type = models.ForeignKey('erp_core.ShareType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Share Type')
    from_no = models.IntegerField(default=0, verbose_name="From No")
    rate = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Rate")
    no_of_shares = models.IntegerField(default=0, verbose_name="No of Shares")
    to_no = models.IntegerField(default=0, verbose_name="To No")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class ShareTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareTransfer
        fields = '__all__'

class ShareTransferViewSet(viewsets.ModelViewSet):
    queryset = ShareTransfer.objects.all()
    serializer_class = ShareTransferSerializer

class LedgerHealthMonitor(BaseDocument):
    enable_health_monitor = models.BooleanField(default=False, verbose_name="Enable Health Monitor")
    debit_credit_mismatch = models.BooleanField(default=False, verbose_name="Debit-Credit Mismatch")
    general_and_payment_ledger_mismatch = models.BooleanField(default=False, verbose_name="Discrepancy between General and Payment Ledger")
    monitor_for_last_x_days = models.IntegerField(default=0, verbose_name="Monitor for Last 'X' days")
    companies = models.JSONField(default=list, blank=True, null=True, verbose_name="companies")

class LedgerHealthMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerHealthMonitor
        fields = '__all__'

class LedgerHealthMonitorViewSet(viewsets.ModelViewSet):
    queryset = LedgerHealthMonitor.objects.all()
    serializer_class = LedgerHealthMonitorSerializer

class InvoiceDiscounting(BaseDocument):
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    loan_start_date = models.DateField(blank=True, null=True, verbose_name="Loan Start Date")
    loan_period = models.IntegerField(default=0, verbose_name="Loan Period (Days)")
    loan_end_date = models.DateField(blank=True, null=True, verbose_name="Loan End Date")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Sanctioned', 'Sanctioned'), ('Disbursed', 'Disbursed'), ('Settled', 'Settled'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="Invoices")
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Amount")
    bank_charges = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Bank Charges")
    short_term_loan = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Short Term Loan Account')
    bank_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    bank_charges_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Charges Account')
    accounts_receivable_credit = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accounts Receivable Credit Account')
    accounts_receivable_discounted = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accounts Receivable Discounted Account')
    accounts_receivable_unpaid = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accounts Receivable Unpaid Account')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class InvoiceDiscountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDiscounting
        fields = '__all__'

class InvoiceDiscountingViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDiscounting.objects.all()
    serializer_class = InvoiceDiscountingSerializer

class ShippingRule(BaseDocument):
    label = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shipping Rule Label")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    shipping_rule_type = models.CharField(max_length=255, choices=[('Selling', 'Selling'), ('Buying', 'Buying')], blank=True, null=True, verbose_name='Shipping Rule Type')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    calculate_based_on = models.CharField(max_length=255, choices=[('Fixed', 'Fixed'), ('Net Total', 'Net Total'), ('Net Weight', 'Net Weight')], blank=True, null=True, verbose_name='Calculate Based On')
    shipping_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Shipping Amount")
    conditions = models.JSONField(default=list, blank=True, null=True, verbose_name="Shipping Rule Conditions")
    countries = models.JSONField(default=list, blank=True, null=True, verbose_name="Valid for Countries")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')

class ShippingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRule
        fields = '__all__'

class ShippingRuleViewSet(viewsets.ModelViewSet):
    queryset = ShippingRule.objects.all()
    serializer_class = ShippingRuleSerializer

class POSPaymentMethod(BaseDocument):
    default = models.BooleanField(default=False, verbose_name="Default")
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    allow_in_returns = models.BooleanField(default=False, verbose_name="Allow In Returns")

class POSPaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSPaymentMethod
        fields = '__all__'

class POSPaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = POSPaymentMethod.objects.all()
    serializer_class = POSPaymentMethodSerializer

class Dunning(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    naming_series = models.CharField(max_length=255, choices=[('DUNN-.MM.-.YY.-', 'DUNN-.MM.-.YY.-')], blank=True, null=True, verbose_name='Series')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Date")
    dunning_type = models.ForeignKey('erp_core.DunningType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dunning Type')
    dunning_fee = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Dunning Fee")
    language = models.ForeignKey('erp_core.Language', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Print Language')
    letter_head = models.ForeignKey('erp_core.LetterHead', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Letter Head')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    body_text = models.TextField(blank=True, null=True, verbose_name="Body Text")
    closing_text = models.TextField(blank=True, null=True, verbose_name="Closing Text")
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    rate_of_interest = models.FloatField(default=0.0, verbose_name="Rate of Interest (%) Yearly")
    address_display = models.TextField(blank=True, null=True, verbose_name="Address")
    contact_display = models.TextField(blank=True, null=True, verbose_name="Contact")
    contact_mobile = models.TextField(blank=True, null=True, verbose_name="Mobile No")
    company_address_display = models.TextField(blank=True, null=True, verbose_name="Company Address Display")
    contact_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Contact Email")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    grand_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    status = models.CharField(max_length=255, choices=[('Draft', 'Draft'), ('Resolved', 'Resolved'), ('Unresolved', 'Unresolved'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    income_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Income Account')
    overdue_payments = models.JSONField(default=list, blank=True, null=True, verbose_name="Overdue Payments")
    total_interest = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Interest")
    total_outstanding = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total Outstanding")
    customer_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Address')
    contact_person = models.ForeignKey('erp_core.Contact', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Contact Person')
    dunning_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Dunning Amount")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    spacer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Spacer")
    company_address = models.ForeignKey('erp_core.Address', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company Address')
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    conversion_rate = models.FloatField(default=0.0, verbose_name="Conversion Rate")
    base_dunning_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Dunning Amount (Company Currency)")

class DunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dunning
        fields = '__all__'

class DunningViewSet(viewsets.ModelViewSet):
    queryset = Dunning.objects.all()
    serializer_class = DunningSerializer

class ApplicableOnAccount(BaseDocument):
    applicable_on_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Accounts')
    is_mandatory = models.BooleanField(default=False, verbose_name="Is Mandatory")

class ApplicableOnAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicableOnAccount
        fields = '__all__'

class ApplicableOnAccountViewSet(viewsets.ModelViewSet):
    queryset = ApplicableOnAccount.objects.all()
    serializer_class = ApplicableOnAccountSerializer

class ProcessPeriodClosingVoucher(BaseDocument):
    parent_pcv = models.ForeignKey('erp_core.PeriodClosingVoucher', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='PCV')
    status = models.CharField(max_length=255, choices=[('Queued', 'Queued'), ('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    p_l_closing_balance = models.TextField(blank=True, null=True, verbose_name="P&L Closing Balance")
    normal_balances = models.JSONField(default=list, blank=True, null=True, verbose_name="Dates to Process")
    z_opening_balances = models.JSONField(default=list, blank=True, null=True, verbose_name="Opening Balances")
    bs_closing_balance = models.TextField(blank=True, null=True, verbose_name="Balance Sheet Closing Balance")

class ProcessPeriodClosingVoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessPeriodClosingVoucher
        fields = '__all__'

class ProcessPeriodClosingVoucherViewSet(viewsets.ModelViewSet):
    queryset = ProcessPeriodClosingVoucher.objects.all()
    serializer_class = ProcessPeriodClosingVoucherSerializer

class PaymentEntryReference(BaseDocument):
    reference_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Name")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    bill_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Supplier Invoice No")
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Grand Total")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated")
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    payment_term = models.ForeignKey('erp_core.PaymentTerm', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Term')
    exchange_gain_loss = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Exchange Gain/Loss")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    account_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Type")
    payment_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Payment Type")
    payment_request = models.ForeignKey('erp_core.PaymentRequest', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Payment Request')
    payment_term_outstanding = models.FloatField(default=0.0, verbose_name="Payment Term Outstanding")
    payment_request_outstanding = models.FloatField(default=0.0, verbose_name="Payment Request Outstanding")
    reconcile_effect_on = models.DateField(blank=True, null=True, verbose_name="Reconcile Effect On")
    advance_voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Advance Voucher Type')
    advance_voucher_no = models.TextField(blank=True, null=True, verbose_name="Advance Voucher No")

class PaymentEntryReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentEntryReference
        fields = '__all__'

class PaymentEntryReferenceViewSet(viewsets.ModelViewSet):
    queryset = PaymentEntryReference.objects.all()
    serializer_class = PaymentEntryReferenceSerializer

class GLEntry(BaseDocument):
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    transaction_date = models.DateField(blank=True, null=True, verbose_name="Transaction Date")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    debit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount")
    credit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    debit_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount in Account Currency")
    credit_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount in Account Currency")
    against = models.TextField(blank=True, null=True, verbose_name="Against")
    against_voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Against Voucher Type')
    against_voucher = models.TextField(blank=True, null=True, verbose_name="Against Voucher")
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")
    voucher_detail_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Voucher Detail No")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    is_opening = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Opening')
    is_advance = models.CharField(max_length=255, choices=[('No', 'No'), ('Yes', 'Yes')], blank=True, null=True, verbose_name='Is Advance')
    fiscal_year = models.ForeignKey('erp_core.FiscalYear', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Fiscal Year')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    to_rename = models.BooleanField(default=False, verbose_name="To Rename")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    is_cancelled = models.BooleanField(default=False, verbose_name="Is Cancelled")
    transaction_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Transaction Currency')
    transaction_exchange_rate = models.FloatField(default=0.0, verbose_name="Transaction Exchange Rate")
    debit_in_transaction_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount in Transaction Currency")
    credit_in_transaction_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount in Transaction Currency")
    voucher_subtype = models.TextField(blank=True, null=True, verbose_name="Voucher Subtype")
    debit_in_reporting_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount in Reporting Currency")
    credit_in_reporting_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount in Reporting Currency")
    reporting_currency_exchange_rate = models.FloatField(default=0.0, verbose_name="Reporting Currency Exchange Rate")

class GLEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GLEntry
        fields = '__all__'

class GLEntryViewSet(viewsets.ModelViewSet):
    queryset = GLEntry.objects.all()
    serializer_class = GLEntrySerializer

class RepostAccountingLedgerItems(BaseDocument):
    voucher_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Voucher Type')
    voucher_no = models.TextField(blank=True, null=True, verbose_name="Voucher No")

class RepostAccountingLedgerItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostAccountingLedgerItems
        fields = '__all__'

class RepostAccountingLedgerItemsViewSet(viewsets.ModelViewSet):
    queryset = RepostAccountingLedgerItems.objects.all()
    serializer_class = RepostAccountingLedgerItemsSerializer

class SubscriptionSettings(BaseDocument):
    grace_period = models.IntegerField(default=0, verbose_name="Grace Period")
    cancel_after_grace = models.BooleanField(default=False, verbose_name="Cancel Subscription After Grace Period")
    prorate = models.BooleanField(default=False, verbose_name="Prorate")

class SubscriptionSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionSettings
        fields = '__all__'

class SubscriptionSettingsViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionSettings.objects.all()
    serializer_class = SubscriptionSettingsSerializer

class SalesInvoiceTimesheet(BaseDocument):
    time_sheet = models.ForeignKey('erp_core.Timesheet', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Time Sheet')
    billing_hours = models.FloatField(default=0.0, verbose_name="Billing Hours")
    billing_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Billing Amount")
    timesheet_detail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Timesheet Detail")
    activity_type = models.ForeignKey('erp_core.ActivityType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Activity Type')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    from_time = models.DateTimeField(blank=True, null=True, verbose_name="From Time")
    to_time = models.DateTimeField(blank=True, null=True, verbose_name="To Time")
    project_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Project Name")

class SalesInvoiceTimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoiceTimesheet
        fields = '__all__'

class SalesInvoiceTimesheetViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoiceTimesheet.objects.all()
    serializer_class = SalesInvoiceTimesheetSerializer

class POSClosingEntryTaxes(BaseDocument):
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    account_head = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Head')

class POSClosingEntryTaxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSClosingEntryTaxes
        fields = '__all__'

class POSClosingEntryTaxesViewSet(viewsets.ModelViewSet):
    queryset = POSClosingEntryTaxes.objects.all()
    serializer_class = POSClosingEntryTaxesSerializer

class ProcessSubscription(BaseDocument):
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    subscription = models.ForeignKey('erp_core.Subscription', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subscription')

class ProcessSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessSubscription
        fields = '__all__'

class ProcessSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = ProcessSubscription.objects.all()
    serializer_class = ProcessSubscriptionSerializer

class FinancialReportTemplate(BaseDocument):
    template_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Template Name")
    report_type = models.CharField(max_length=255, choices=[('Profit and Loss Statement', 'Profit and Loss Statement'), ('Balance Sheet', 'Balance Sheet'), ('Cash Flow', 'Cash Flow'), ('Custom Financial Statement', 'Custom Financial Statement')], blank=True, null=True, verbose_name='Report Type')
    module = models.ForeignKey('erp_core.ModuleDef', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Module (for Export)')
    rows = models.JSONField(default=list, blank=True, null=True, verbose_name="Report Line Items")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")

class FinancialReportTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReportTemplate
        fields = '__all__'

class FinancialReportTemplateViewSet(viewsets.ModelViewSet):
    queryset = FinancialReportTemplate.objects.all()
    serializer_class = FinancialReportTemplateSerializer

class PurchaseInvoiceAdvance(BaseDocument):
    reference_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    reference_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row")
    advance_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Advance Amount")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated Amount")
    exchange_gain_loss = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Exchange Gain/Loss")
    ref_exchange_rate = models.FloatField(default=0.0, verbose_name="Reference Exchange Rate")
    difference_posting_date = models.DateField(blank=True, null=True, verbose_name="Difference Posting Date")

class PurchaseInvoiceAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceAdvance
        fields = '__all__'

class PurchaseInvoiceAdvanceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoiceAdvance.objects.all()
    serializer_class = PurchaseInvoiceAdvanceSerializer

class ItemWiseTaxDetail(BaseDocument):
    item_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Row")
    tax_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tax Row")
    rate = models.FloatField(default=0.0, verbose_name="Tax Rate")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Tax Amount")
    taxable_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Taxable Amount")

class ItemWiseTaxDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemWiseTaxDetail
        fields = '__all__'

class ItemWiseTaxDetailViewSet(viewsets.ModelViewSet):
    queryset = ItemWiseTaxDetail.objects.all()
    serializer_class = ItemWiseTaxDetailSerializer

class ProcessPaymentReconciliationLogAllocations(BaseDocument):
    reference_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Type')
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    reference_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row")
    invoice_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Invoice Type')
    invoice_number = models.TextField(blank=True, null=True, verbose_name="Invoice Number")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated Amount")
    unreconciled_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Unreconciled Amount")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    is_advance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Is Advance")
    difference_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference Amount")
    difference_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Difference Account')
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    reconciled = models.BooleanField(default=False, verbose_name="Reconciled")
    gain_loss_posting_date = models.DateField(blank=True, null=True, verbose_name="Difference Posting Date")

class ProcessPaymentReconciliationLogAllocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessPaymentReconciliationLogAllocations
        fields = '__all__'

class ProcessPaymentReconciliationLogAllocationsViewSet(viewsets.ModelViewSet):
    queryset = ProcessPaymentReconciliationLogAllocations.objects.all()
    serializer_class = ProcessPaymentReconciliationLogAllocationsSerializer

class BankReconciliationTool(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    bank_statement_from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    bank_statement_to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    account_opening_balance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Account Opening Balance")
    bank_statement_closing_balance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Closing Balance")
    from_reference_date = models.DateField(blank=True, null=True, verbose_name="From Reference Date")
    to_reference_date = models.DateField(blank=True, null=True, verbose_name="To Reference Date")
    filter_by_reference_date = models.BooleanField(default=False, verbose_name="Filter by Reference Date")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')

class BankReconciliationToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankReconciliationTool
        fields = '__all__'

class BankReconciliationToolViewSet(viewsets.ModelViewSet):
    queryset = BankReconciliationTool.objects.all()
    serializer_class = BankReconciliationToolSerializer

class CurrencyExchangeSettings(BaseDocument):
    api_endpoint = models.CharField(max_length=255, blank=True, null=True, verbose_name="API Endpoint")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Example URL")
    req_params = models.JSONField(default=list, blank=True, null=True, verbose_name="Parameters")
    result_key = models.JSONField(default=list, blank=True, null=True, verbose_name="Result Key")
    service_provider = models.CharField(max_length=255, choices=[('frankfurter.dev', 'frankfurter.dev'), ('exchangerate.host', 'exchangerate.host'), ('Custom', 'Custom')], blank=True, null=True, verbose_name='Service Provider')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    access_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Access Key")
    use_http = models.BooleanField(default=False, verbose_name="Use HTTP Protocol")

class CurrencyExchangeSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchangeSettings
        fields = '__all__'

class CurrencyExchangeSettingsViewSet(viewsets.ModelViewSet):
    queryset = CurrencyExchangeSettings.objects.all()
    serializer_class = CurrencyExchangeSettingsSerializer

class TaxWithholdingGroup(BaseDocument):
    group_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Group Name")

class TaxWithholdingGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxWithholdingGroup
        fields = '__all__'

class TaxWithholdingGroupViewSet(viewsets.ModelViewSet):
    queryset = TaxWithholdingGroup.objects.all()
    serializer_class = TaxWithholdingGroupSerializer

class AccountsSettings(BaseDocument):
    determine_address_tax_category_from = models.CharField(max_length=255, choices=[('Billing Address', 'Billing Address'), ('Shipping Address', 'Shipping Address')], blank=True, null=True, verbose_name='Determine Address Tax Category From')
    credit_controller = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role allowed to bypass Credit Limit')
    check_supplier_invoice_uniqueness = models.BooleanField(default=False, verbose_name="Check Supplier Invoice Number Uniqueness")
    make_payment_via_journal_entry = models.BooleanField(default=False, verbose_name="Make Payment via Journal Entry")
    unlink_payment_on_cancellation_of_invoice = models.BooleanField(default=False, verbose_name="Unlink Payment on Cancellation of Invoice")
    unlink_advance_payment_on_cancelation_of_order = models.BooleanField(default=False, verbose_name="Unlink Advance Payment on Cancellation of Order")
    book_asset_depreciation_entry_automatically = models.BooleanField(default=False, verbose_name="Book Asset Depreciation Entry Automatically")
    add_taxes_from_item_tax_template = models.BooleanField(default=False, verbose_name="Automatically Add Taxes and Charges from Item Tax Template")
    show_inclusive_tax_in_print = models.BooleanField(default=False, verbose_name="Show Inclusive Tax in Print")
    show_payment_schedule_in_print = models.BooleanField(default=False, verbose_name="Show Payment Schedule in Print")
    allow_stale = models.BooleanField(default=False, verbose_name="Allow Stale Exchange Rates")
    stale_days = models.IntegerField(default=0, verbose_name="Stale Days")
    automatically_fetch_payment_terms = models.BooleanField(default=False, verbose_name="Automatically Fetch Payment Terms from Order/Quotation")
    over_billing_allowance = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Over Billing Allowance (%)")
    automatically_process_deferred_accounting_entry = models.BooleanField(default=False, verbose_name="Automatically Process Deferred Accounting Entry")
    book_deferred_entries_via_journal_entry = models.BooleanField(default=False, verbose_name="Book Deferred Entries Via Journal Entry")
    submit_journal_entries = models.BooleanField(default=False, verbose_name="Submit Journal Entries")
    book_deferred_entries_based_on = models.CharField(max_length=255, choices=[('Days', 'Days'), ('Months', 'Months')], blank=True, null=True, verbose_name='Book Deferred Entries Based On')
    delete_linked_ledger_entries = models.BooleanField(default=False, verbose_name="Delete Accounting and Stock Ledger Entries on deletion of Transaction")
    role_allowed_to_over_bill = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role Allowed to Over Bill ')
    enable_common_party_accounting = models.BooleanField(default=False, verbose_name="Enable Common Party Accounting")
    allow_multi_currency_invoices_against_single_party_account = models.BooleanField(default=False, verbose_name="Allow multi-currency invoices against single party account ")
    show_balance_in_coa = models.BooleanField(default=False, verbose_name="Show Balances in Chart Of Accounts")
    book_tax_discount_loss = models.BooleanField(default=False, verbose_name="Book Tax Loss on Early Payment Discount")
    merge_similar_account_heads = models.BooleanField(default=False, verbose_name="Merge Similar Account Heads")
    auto_reconcile_payments = models.BooleanField(default=False, verbose_name="Auto Reconcile Payments")
    show_taxes_as_table_in_print = models.BooleanField(default=False, verbose_name="Show Taxes as Table in Print")
    enable_party_matching = models.BooleanField(default=False, verbose_name="Enable Automatic Party Matching")
    enable_fuzzy_matching = models.BooleanField(default=False, verbose_name="Enable Fuzzy Matching")
    ignore_account_closing_balance = models.BooleanField(default=False, verbose_name="Ignore Account Closing Balance")
    round_row_wise_tax = models.BooleanField(default=False, verbose_name="Round Tax Amount Row-wise")
    general_ledger_remarks_length = models.IntegerField(default=0, verbose_name="General Ledger")
    receivable_payable_remarks_length = models.IntegerField(default=0, verbose_name="Accounts Receivable/Payable")
    enable_immutable_ledger = models.BooleanField(default=False, verbose_name="Enable Immutable Ledger")
    calculate_depr_using_total_days = models.BooleanField(default=False, verbose_name="Calculate daily depreciation using total days in depreciation period")
    create_pr_in_draft_status = models.BooleanField(default=False, verbose_name="Create in Draft Status")
    auto_reconciliation_job_trigger = models.IntegerField(default=0, verbose_name="Auto Reconciliation Job Trigger")
    reconciliation_queue_size = models.IntegerField(default=0, verbose_name="Reconciliation Queue Size")
    ignore_is_opening_check_for_reporting = models.BooleanField(default=False, verbose_name="Ignore Is Opening check for reporting")
    exchange_gain_loss_posting_date = models.CharField(max_length=255, choices=[('Invoice', 'Invoice'), ('Payment', 'Payment'), ('Reconciliation Date', 'Reconciliation Date')], blank=True, null=True, verbose_name='Posting Date Inheritance for Exchange Gain / Loss')
    receivable_payable_fetch_method = models.CharField(max_length=255, choices=[('Buffered Cursor', 'Buffered Cursor'), ('UnBuffered Cursor', 'UnBuffered Cursor')], blank=True, null=True, verbose_name='Data Fetch Method')
    maintain_same_internal_transaction_rate = models.BooleanField(default=False, verbose_name="Maintain Same Rate Throughout Internal Transaction")
    maintain_same_rate_action = models.CharField(max_length=255, choices=[('Stop', 'Stop'), ('Warn', 'Warn')], blank=True, null=True, verbose_name='Action if Same Rate is Not Maintained Throughout  Internal Transaction')
    role_to_override_stop_action = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role Allowed to Override Stop Action')
    confirm_before_resetting_posting_date = models.BooleanField(default=False, verbose_name="Confirm before resetting posting date")
    allow_pegged_currencies_exchange_rates = models.BooleanField(default=False, verbose_name="Allow Implicit Pegged Currency Conversion")
    add_taxes_from_taxes_and_charges_template = models.BooleanField(default=False, verbose_name="Automatically Add Taxes from Taxes and Charges Template")
    fetch_valuation_rate_for_internal_transaction = models.BooleanField(default=False, verbose_name="Fetch Valuation Rate for Internal Transaction")
    use_legacy_budget_controller = models.BooleanField(default=False, verbose_name="Use Legacy Budget Controller")
    use_legacy_controller_for_pcv = models.BooleanField(default=False, verbose_name="Use Legacy Controller For Period Closing Voucher")
    role_to_notify_on_depreciation_failure = models.ForeignKey('erp_core.Role', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Role to Notify on Depreciation Failure')
    default_ageing_range = models.CharField(max_length=255, blank=True, null=True, verbose_name="Default Ageing Range")
    enable_discounts_and_margin = models.BooleanField(default=False, verbose_name="Enable Discounts and Margin")
    enable_loyalty_point_program = models.BooleanField(default=False, verbose_name="Enable Loyalty Point Program")
    enable_accounting_dimensions = models.BooleanField(default=False, verbose_name="Enable Accounting Dimensions")
    enable_subscription = models.BooleanField(default=False, verbose_name="Enable Subscription")
    fetch_payment_schedule_in_payment_request = models.BooleanField(default=False, verbose_name="Fetch Payment Schedule In Payment Request")
    transfer_match_days = models.IntegerField(default=0, verbose_name="Match transfers within 'N' days")
    automatically_run_rules_on_unreconciled_transactions = models.BooleanField(default=False, verbose_name="Automatically run rules on unreconciled transactions")
    repost_allowed_types = models.JSONField(default=list, blank=True, null=True, verbose_name="Allowed Doctypes")
    preview_mode = models.BooleanField(default=False, verbose_name="Preview Mode")

class AccountsSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsSettings
        fields = '__all__'

class AccountsSettingsViewSet(viewsets.ModelViewSet):
    queryset = AccountsSettings.objects.all()
    serializer_class = AccountsSettingsSerializer

class Shareholder(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    naming_series = models.CharField(max_length=255, choices=[('ACC-SH-.YYYY.-', 'ACC-SH-.YYYY.-')], blank=True, null=True, verbose_name='naming_series')
    folio_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Folio no.")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    is_company = models.BooleanField(default=False, verbose_name="Is Company")
    share_balance = models.JSONField(default=list, blank=True, null=True, verbose_name="Share Balance")
    contact_list = models.TextField(blank=True, null=True, verbose_name="Contact List")

class ShareholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shareholder
        fields = '__all__'

class ShareholderViewSet(viewsets.ModelViewSet):
    queryset = Shareholder.objects.all()
    serializer_class = ShareholderSerializer

class TaxRule(BaseDocument):
    tax_type = models.CharField(max_length=255, choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], blank=True, null=True, verbose_name='Tax Type')
    use_for_shopping_cart = models.BooleanField(default=False, verbose_name="Use for Shopping Cart")
    sales_tax_template = models.ForeignKey('erp_core.SalesTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sales Tax Template')
    purchase_tax_template = models.ForeignKey('erp_core.PurchaseTaxesandChargesTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Purchase Tax Template')
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')
    item = models.ForeignKey('erp_core.Item', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item')
    billing_city = models.CharField(max_length=255, blank=True, null=True, verbose_name="Billing City")
    billing_county = models.CharField(max_length=255, blank=True, null=True, verbose_name="Billing County")
    billing_state = models.CharField(max_length=255, blank=True, null=True, verbose_name="Billing State")
    billing_zipcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Billing Zipcode")
    billing_country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Billing Country')
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    supplier_group = models.ForeignKey('erp_core.SupplierGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier Group')
    item_group = models.ForeignKey('erp_core.ItemGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Item Group')
    shipping_city = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shipping City")
    shipping_county = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shipping County")
    shipping_state = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shipping State")
    shipping_zipcode = models.CharField(max_length=255, blank=True, null=True, verbose_name="Shipping Zipcode")
    shipping_country = models.ForeignKey('erp_core.Country', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Shipping Country')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    priority = models.IntegerField(default=0, verbose_name="Priority")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class TaxRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxRule
        fields = '__all__'

class TaxRuleViewSet(viewsets.ModelViewSet):
    queryset = TaxRule.objects.all()
    serializer_class = TaxRuleSerializer

class SalesTaxesandChargesTemplate(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    is_default = models.BooleanField(default=False, verbose_name="Default")
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    taxes = models.JSONField(default=list, blank=True, null=True, verbose_name="Sales Taxes and Charges")
    tax_category = models.ForeignKey('erp_core.TaxCategory', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax Category')

class SalesTaxesandChargesTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTaxesandChargesTemplate
        fields = '__all__'

class SalesTaxesandChargesTemplateViewSet(viewsets.ModelViewSet):
    queryset = SalesTaxesandChargesTemplate.objects.all()
    serializer_class = SalesTaxesandChargesTemplateSerializer

class CostCenterAllocation(BaseDocument):
    main_cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Main Cost Center')
    valid_from = models.DateField(blank=True, null=True, verbose_name="Valid From")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    allocation_percentages = models.JSONField(default=list, blank=True, null=True, verbose_name="Cost Center Allocation Percentages")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class CostCenterAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenterAllocation
        fields = '__all__'

class CostCenterAllocationViewSet(viewsets.ModelViewSet):
    queryset = CostCenterAllocation.objects.all()
    serializer_class = CostCenterAllocationSerializer

class PartyLink(BaseDocument):
    primary_role = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Primary Role')
    secondary_role = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Secondary Role')
    primary_party = models.TextField(blank=True, null=True, verbose_name="Primary Party")
    secondary_party = models.TextField(blank=True, null=True, verbose_name="Secondary Party")

class PartyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyLink
        fields = '__all__'

class PartyLinkViewSet(viewsets.ModelViewSet):
    queryset = PartyLink.objects.all()
    serializer_class = PartyLinkSerializer

class PaymentReconciliationAllocation(BaseDocument):
    invoice_number = models.TextField(blank=True, null=True, verbose_name="Invoice Number")
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Allocated Amount")
    difference_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Difference Account')
    difference_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Difference Amount")
    reference_name = models.TextField(blank=True, null=True, verbose_name="Reference Name")
    is_advance = models.CharField(max_length=255, blank=True, null=True, verbose_name="Is Advance")
    reference_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Reference Type')
    invoice_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Invoice Type')
    unreconciled_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Unreconciled Amount")
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    reference_row = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row")
    currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Currency')
    exchange_rate = models.FloatField(default=0.0, verbose_name="Exchange Rate")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    gain_loss_posting_date = models.DateField(blank=True, null=True, verbose_name="Difference Posting Date")
    debit_or_credit_note_posting_date = models.DateField(blank=True, null=True, verbose_name="Debit / Credit Note Posting Date")

class PaymentReconciliationAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReconciliationAllocation
        fields = '__all__'

class PaymentReconciliationAllocationViewSet(viewsets.ModelViewSet):
    queryset = PaymentReconciliationAllocation.objects.all()
    serializer_class = PaymentReconciliationAllocationSerializer

class BankAccountSubtype(BaseDocument):
    account_subtype = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Subtype")

class BankAccountSubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountSubtype
        fields = '__all__'

class BankAccountSubtypeViewSet(viewsets.ModelViewSet):
    queryset = BankAccountSubtype.objects.all()
    serializer_class = BankAccountSubtypeSerializer

class ChartofAccountsImporter(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    import_file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Attach custom Chart of Accounts file")

class ChartofAccountsImporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartofAccountsImporter
        fields = '__all__'

class ChartofAccountsImporterViewSet(viewsets.ModelViewSet):
    queryset = ChartofAccountsImporter.objects.all()
    serializer_class = ChartofAccountsImporterSerializer

class CampaignItem(BaseDocument):
    campaign = models.ForeignKey('erp_core.UTMCampaign', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campaign')

class CampaignItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignItem
        fields = '__all__'

class CampaignItemViewSet(viewsets.ModelViewSet):
    queryset = CampaignItem.objects.all()
    serializer_class = CampaignItemSerializer

class BankAccountType(BaseDocument):
    account_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Account Type")

class BankAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountType
        fields = '__all__'

class BankAccountTypeViewSet(viewsets.ModelViewSet):
    queryset = BankAccountType.objects.all()
    serializer_class = BankAccountTypeSerializer

class BisectNodes(BaseDocument):
    root = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Root')
    left_child = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Left Child')
    right_child = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Right Child')
    period_from_date = models.DateTimeField(blank=True, null=True, verbose_name="Period_from_date")
    period_to_date = models.DateTimeField(blank=True, null=True, verbose_name="Period To Date")
    difference = models.FloatField(default=0.0, verbose_name="Difference")
    balance_sheet_summary = models.FloatField(default=0.0, verbose_name="Balance Sheet Summary")
    profit_loss_summary = models.FloatField(default=0.0, verbose_name="Profit and Loss Summary")
    generated = models.BooleanField(default=False, verbose_name="Generated")

class BisectNodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BisectNodes
        fields = '__all__'

class BisectNodesViewSet(viewsets.ModelViewSet):
    queryset = BisectNodes.objects.all()
    serializer_class = BisectNodesSerializer

class TaxWithholdingAccount(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')

class TaxWithholdingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxWithholdingAccount
        fields = '__all__'

class TaxWithholdingAccountViewSet(viewsets.ModelViewSet):
    queryset = TaxWithholdingAccount.objects.all()
    serializer_class = TaxWithholdingAccountSerializer

class LoyaltyPointEntryRedemption(BaseDocument):
    sales_invoice = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sales Invoice")
    redemption_date = models.DateField(blank=True, null=True, verbose_name="Redemption Date")
    redeemed_points = models.IntegerField(default=0, verbose_name="Redeemed Points")

class LoyaltyPointEntryRedemptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyPointEntryRedemption
        fields = '__all__'

class LoyaltyPointEntryRedemptionViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyPointEntryRedemption.objects.all()
    serializer_class = LoyaltyPointEntryRedemptionSerializer

class ShareType(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

class ShareTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareType
        fields = '__all__'

class ShareTypeViewSet(viewsets.ModelViewSet):
    queryset = ShareType.objects.all()
    serializer_class = ShareTypeSerializer

class SupplierItem(BaseDocument):
    supplier = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Supplier')

class SupplierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItem
        fields = '__all__'

class SupplierItemViewSet(viewsets.ModelViewSet):
    queryset = SupplierItem.objects.all()
    serializer_class = SupplierItemSerializer

class ProcessDeferredAccounting(BaseDocument):
    type = models.CharField(max_length=255, choices=[('Income', 'Income'), ('Expense', 'Expense')], blank=True, null=True, verbose_name='Type')
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    start_date = models.DateField(blank=True, null=True, verbose_name="Service Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="Service End Date")
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class ProcessDeferredAccountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessDeferredAccounting
        fields = '__all__'

class ProcessDeferredAccountingViewSet(viewsets.ModelViewSet):
    queryset = ProcessDeferredAccounting.objects.all()
    serializer_class = ProcessDeferredAccountingSerializer

class BankClearance(BaseDocument):
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    from_date = models.DateField(blank=True, null=True, verbose_name="From Date")
    to_date = models.DateField(blank=True, null=True, verbose_name="To Date")
    bank_account = models.ForeignKey('erp_core.BankAccount', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Bank Account')
    include_reconciled_entries = models.BooleanField(default=False, verbose_name="Include Reconciled Entries")
    include_pos_transactions = models.BooleanField(default=False, verbose_name="Include POS Transactions")
    payment_entries = models.JSONField(default=list, blank=True, null=True, verbose_name="Payment Entries")

class BankClearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankClearance
        fields = '__all__'

class BankClearanceViewSet(viewsets.ModelViewSet):
    queryset = BankClearance.objects.all()
    serializer_class = BankClearanceSerializer

class CurrencyExchangeSettingsResult(BaseDocument):
    key = models.CharField(max_length=255, blank=True, null=True, verbose_name="Key")

class CurrencyExchangeSettingsResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchangeSettingsResult
        fields = '__all__'

class CurrencyExchangeSettingsResultViewSet(viewsets.ModelViewSet):
    queryset = CurrencyExchangeSettingsResult.objects.all()
    serializer_class = CurrencyExchangeSettingsResultSerializer

class ProcessStatementOfAccountsCustomer(BaseDocument):
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    primary_email = models.TextField(blank=True, null=True, verbose_name="Primary Contact Email")
    billing_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Billing Email")
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Customer Name")

class ProcessStatementOfAccountsCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStatementOfAccountsCustomer
        fields = '__all__'

class ProcessStatementOfAccountsCustomerViewSet(viewsets.ModelViewSet):
    queryset = ProcessStatementOfAccountsCustomer.objects.all()
    serializer_class = ProcessStatementOfAccountsCustomerSerializer

class PricingRuleDetail(BaseDocument):
    pricing_rule = models.ForeignKey('erp_core.PricingRule', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pricing Rule')
    item_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Code")
    margin_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Margin Type")
    rate_or_discount = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rate or Discount")
    child_docname = models.CharField(max_length=255, blank=True, null=True, verbose_name="Child Docname")
    rule_applied = models.BooleanField(default=False, verbose_name="Rule Applied")

class PricingRuleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRuleDetail
        fields = '__all__'

class PricingRuleDetailViewSet(viewsets.ModelViewSet):
    queryset = PricingRuleDetail.objects.all()
    serializer_class = PricingRuleDetailSerializer

class AccountClosingBalance(BaseDocument):
    closing_date = models.DateField(blank=True, null=True, verbose_name="Closing Date")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    debit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount")
    credit = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    debit_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount in Account Currency")
    credit_in_account_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount in Account Currency")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')
    finance_book = models.ForeignKey('erp_core.FinanceBook', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Finance Book')
    period_closing_voucher = models.ForeignKey('erp_core.PeriodClosingVoucher', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Period Closing Voucher')
    is_period_closing_voucher_entry = models.BooleanField(default=False, verbose_name="Is Period Closing Voucher Entry")
    debit_in_reporting_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Debit Amount in Reporting Currency")
    credit_in_reporting_currency = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Credit Amount in Reporting Currency")
    reporting_currency_exchange_rate = models.FloatField(default=0.0, verbose_name="Reporting Currency Exchange Rate")

class AccountClosingBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountClosingBalance
        fields = '__all__'

class AccountClosingBalanceViewSet(viewsets.ModelViewSet):
    queryset = AccountClosingBalance.objects.all()
    serializer_class = AccountClosingBalanceSerializer

class PurchaseTaxesandCharges(BaseDocument):
    category = models.CharField(max_length=255, choices=[('Valuation and Total', 'Valuation and Total'), ('Valuation', 'Valuation'), ('Total', 'Total')], blank=True, null=True, verbose_name='Consider Tax or Charge for')
    add_deduct_tax = models.CharField(max_length=255, choices=[('Add', 'Add'), ('Deduct', 'Deduct')], blank=True, null=True, verbose_name='Add or Deduct')
    charge_type = models.CharField(max_length=255, choices=[('Actual', 'Actual'), ('On Net Total', 'On Net Total'), ('On Previous Row Amount', 'On Previous Row Amount'), ('On Previous Row Total', 'On Previous Row Total'), ('On Item Quantity', 'On Item Quantity')], blank=True, null=True, verbose_name='Type')
    row_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference Row #")
    included_in_print_rate = models.BooleanField(default=False, verbose_name="Is this Tax included in Basic Rate?")
    account_head = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Head')
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    rate = models.FloatField(default=0.0, verbose_name="Tax Rate")
    tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    tax_amount_after_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Tax Amount After Discount Amount")
    total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total")
    base_tax_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount (Company Currency)")
    base_total = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Total (Company Currency)")
    base_tax_amount_after_discount_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Tax Amount After Discount Amount")
    project = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    included_in_paid_amount = models.BooleanField(default=False, verbose_name="Considered In Paid Amount")
    account_currency = models.ForeignKey('erp_core.Currency', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account Currency')
    is_tax_withholding_account = models.BooleanField(default=False, verbose_name="Is Tax Withholding Account")
    net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount")
    base_net_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Net Amount (Company Currency)")
    set_by_item_tax_template = models.BooleanField(default=False, verbose_name="Set by Item Tax Template")
    dont_recompute_tax = models.BooleanField(default=False, verbose_name="Don't Recompute Tax")

class PurchaseTaxesandChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseTaxesandCharges
        fields = '__all__'

class PurchaseTaxesandChargesViewSet(viewsets.ModelViewSet):
    queryset = PurchaseTaxesandCharges.objects.all()
    serializer_class = PurchaseTaxesandChargesSerializer

class FinanceBook(BaseDocument):
    finance_book_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")

class FinanceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceBook
        fields = '__all__'

class FinanceBookViewSet(viewsets.ModelViewSet):
    queryset = FinanceBook.objects.all()
    serializer_class = FinanceBookSerializer

class OpeningInvoiceCreationToolItem(BaseDocument):
    party_type = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Party Type')
    party = models.TextField(blank=True, null=True, verbose_name="Party ID")
    temporary_opening_account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Temporary Opening Account')
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    item_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Item Name")
    outstanding_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Outstanding Amount")
    qty = models.CharField(max_length=255, blank=True, null=True, verbose_name="Quantity")
    cost_center = models.ForeignKey('erp_core.CostCenter', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cost Center')
    invoice_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Invoice Number")
    supplier_invoice_date = models.DateField(blank=True, null=True, verbose_name="Supplier Invoice Date")
    party_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Party Name")

class OpeningInvoiceCreationToolItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningInvoiceCreationToolItem
        fields = '__all__'

class OpeningInvoiceCreationToolItemViewSet(viewsets.ModelViewSet):
    queryset = OpeningInvoiceCreationToolItem.objects.all()
    serializer_class = OpeningInvoiceCreationToolItemSerializer

class POSInvoiceMergeLog(BaseDocument):
    posting_date = models.DateField(blank=True, null=True, verbose_name="Posting Date")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    pos_invoices = models.JSONField(default=list, blank=True, null=True, verbose_name="POS Invoices")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')
    consolidated_invoice = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Consolidated Sales Invoice')
    consolidated_credit_note = models.ForeignKey('erp_core.SalesInvoice', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Consolidated Credit Note')
    pos_closing_entry = models.ForeignKey('erp_core.POSClosingEntry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='POS Closing Entry')
    merge_invoices_based_on = models.CharField(max_length=255, choices=[('Customer', 'Customer'), ('Customer Group', 'Customer Group')], blank=True, null=True, verbose_name='Merge Invoices Based On')
    customer_group = models.ForeignKey('erp_core.CustomerGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer Group')
    posting_time = models.TextField(blank=True, null=True, verbose_name="Posting Time")
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class POSInvoiceMergeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSInvoiceMergeLog
        fields = '__all__'

class POSInvoiceMergeLogViewSet(viewsets.ModelViewSet):
    queryset = POSInvoiceMergeLog.objects.all()
    serializer_class = POSInvoiceMergeLogSerializer

class SalesInvoicePayment(BaseDocument):
    mode_of_payment = models.ForeignKey('erp_core.ModeofPayment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Mode of Payment')
    amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Amount")
    account = models.ForeignKey('erp_core.Account', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Account')
    type = models.TextField(blank=True, null=True, verbose_name="Type")
    base_amount = models.DecimalField(max_digits=18, decimal_places=6, default=0.0, verbose_name="Base Amount (Company Currency)")
    clearance_date = models.DateField(blank=True, null=True, verbose_name="Clearance Date")
    default = models.BooleanField(default=False, verbose_name="Default")
    reference_no = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference No")

class SalesInvoicePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoicePayment
        fields = '__all__'

class SalesInvoicePaymentViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoicePayment.objects.all()
    serializer_class = SalesInvoicePaymentSerializer

class PSOAProject(BaseDocument):
    project_name = models.ForeignKey('erp_core.Project', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')

class PSOAProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSOAProject
        fields = '__all__'

class PSOAProjectViewSet(viewsets.ModelViewSet):
    queryset = PSOAProject.objects.all()
    serializer_class = PSOAProjectSerializer

class LedgerHealthMonitorCompany(BaseDocument):
    company = models.ForeignKey('erp_core.Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Company')

class LedgerHealthMonitorCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerHealthMonitorCompany
        fields = '__all__'

class LedgerHealthMonitorCompanyViewSet(viewsets.ModelViewSet):
    queryset = LedgerHealthMonitorCompany.objects.all()
    serializer_class = LedgerHealthMonitorCompanySerializer
