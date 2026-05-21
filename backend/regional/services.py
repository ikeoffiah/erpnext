
# Migrated from regional/address_template/setup.py
def set_up_address_templates(*args, **kwargs):
    pass

def get_address_templates(*args, **kwargs):
    pass

def country(*args, **kwargs):
    pass

def get_file_content(*args, **kwargs):
    pass

def update_address_template(*args, **kwargs):
    pass


# Migrated from regional/address_template/test_regional_address_template.py
def ensure_country(*args, **kwargs):
    pass

def test_get_address_templates(*args, **kwargs):
    pass

def test_create_address_template(*args, **kwargs):
    pass

def test_update_address_template(*args, **kwargs):
    pass


# Migrated from regional/turkey/setup.py
def setup(*args, **kwargs):
    pass


# Migrated from regional/italy/setup.py
def setup(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def setup_report(*args, **kwargs):
    pass

def add_permissions(*args, **kwargs):
    pass


# Migrated from regional/italy/utils.py
def update_itemised_tax_data(*args, **kwargs):
    pass

def export_invoices(*args, **kwargs):
    pass

def prepare_invoice(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def download_zip(*args, **kwargs):
    pass

def get_invoice_summary(*args, **kwargs):
    pass

def update_summary_details(*args, **kwargs):
    pass

def append_row_as_charges(*args, **kwargs):
    pass

def sales_invoice_validate(*args, **kwargs):
    pass

def sales_invoice_on_submit(*args, **kwargs):
    pass

def prepare_and_attach_invoice(*args, **kwargs):
    pass

def generate_single_invoice(*args, **kwargs):
    pass

def sales_invoice_on_cancel(*args, **kwargs):
    pass

def get_company_country(*args, **kwargs):
    pass

def get_e_invoice_attachments(*args, **kwargs):
    pass

def validate_address(*args, **kwargs):
    pass

def get_unamended_name(*args, **kwargs):
    pass

def get_progressive_name_and_number(*args, **kwargs):
    pass

def set_state_code(*args, **kwargs):
    pass


# Migrated from regional/australia/setup.py
def setup(*args, **kwargs):
    pass

def update_regional_tax_settings(*args, **kwargs):
    pass


# Migrated from regional/south_africa/setup.py
def setup(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def add_permissions(*args, **kwargs):
    pass


# Migrated from regional/united_arab_emirates/setup.py
def setup(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def add_print_formats(*args, **kwargs):
    pass

def add_custom_roles_for_reports(*args, **kwargs):
    pass

def add_permissions(*args, **kwargs):
    pass


# Migrated from regional/united_arab_emirates/utils.py
def update_itemised_tax_data(*args, **kwargs):
    pass

def determine_if_export(*args, **kwargs):
    pass

def get_account_currency(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def get_tax_accounts(*args, **kwargs):
    pass

def update_grand_total_for_rcm(*args, **kwargs):
    pass

def update_totals(*args, **kwargs):
    pass

def make_regional_gl_entries(*args, **kwargs):
    pass

def make_gl_entry(*args, **kwargs):
    pass

def validate_returns(*args, **kwargs):
    pass


# Migrated from regional/united_states/setup.py
def setup(*args, **kwargs):
    pass

def setup_company_independent_fixtures(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def add_print_formats(*args, **kwargs):
    pass


# Migrated from regional/united_states/test_united_states.py
def test_irs_1099_custom_field(*args, **kwargs):
    pass

def test_irs_1099_report(*args, **kwargs):
    pass

def make_irs_1099_supplier(*args, **kwargs):
    pass

def make_payment_entry_to_irs_1099_supplier(*args, **kwargs):
    pass


# Migrated from regional/report/vat_audit_report/vat_audit_report.py
def execute(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_company_region(*args, **kwargs):
    pass

def get_sa_vat_accounts(*args, **kwargs):
    pass

def get_invoice_data(*args, **kwargs):
    pass

def get_invoice_items(*args, **kwargs):
    pass

def get_items_based_on_tax_rate(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_consolidated_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from regional/report/vat_audit_report/test_vat_audit_report.py
def setUp(*args, **kwargs):
    pass

def test_vat_audit_report(*args, **kwargs):
    pass

def make_company(*args, **kwargs):
    pass

def set_sa_vat_accounts(*args, **kwargs):
    pass

def make_customer(*args, **kwargs):
    pass

def make_supplier(*args, **kwargs):
    pass

def make_item(*args, **kwargs):
    pass

def make_sales_invoices(*args, **kwargs):
    pass

def make_sales_invoices_wrapper(*args, **kwargs):
    pass

def create_purchase_invoices(*args, **kwargs):
    pass


# Migrated from regional/report/electronic_invoice_register/electronic_invoice_register.py
def execute(*args, **kwargs):
    pass


# Migrated from regional/report/irs_1099/irs_1099.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def irs_1099_print(*args, **kwargs):
    pass

def get_payer_address_html(*args, **kwargs):
    pass

def get_street_address_html(*args, **kwargs):
    pass


# Migrated from regional/report/uae_vat_201/uae_vat_201.py
def execute(*args, **kwargs):
    pass

def validate_company_region(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def append_vat_on_sales(*args, **kwargs):
    pass

def standard_rated_expenses_emiratewise(*args, **kwargs):
    pass

def append_emiratewise_expenses(*args, **kwargs):
    pass

def append_vat_on_expenses(*args, **kwargs):
    pass

def append_data(*args, **kwargs):
    pass

def get_total_emiratewise(*args, **kwargs):
    pass

def get_emirates(*args, **kwargs):
    pass

def get_filters(*args, **kwargs):
    pass

def get_reverse_charge_total(*args, **kwargs):
    pass

def get_reverse_charge_tax(*args, **kwargs):
    pass

def get_reverse_charge_recoverable_total(*args, **kwargs):
    pass

def get_reverse_charge_recoverable_tax(*args, **kwargs):
    pass

def get_conditions_join(*args, **kwargs):
    pass

def get_standard_rated_expenses_total(*args, **kwargs):
    pass

def get_standard_rated_expenses_tax(*args, **kwargs):
    pass

def get_tourist_tax_return_total(*args, **kwargs):
    pass

def get_tourist_tax_return_tax(*args, **kwargs):
    pass

def get_zero_rated_total(*args, **kwargs):
    pass

def get_exempt_total(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass


# Migrated from regional/report/uae_vat_201/test_uae_vat_201.py
def setUp(*args, **kwargs):
    pass

def test_validate_company_region(*args, **kwargs):
    pass

def test_uae_vat_201_report(*args, **kwargs):
    pass

def test_uae_vat_201_report_with_foreign_transaction(*args, **kwargs):
    pass

def set_vat_accounts(*args, **kwargs):
    pass

def make_customer(*args, **kwargs):
    pass

def make_supplier(*args, **kwargs):
    pass

def create_warehouse(*args, **kwargs):
    pass

def make_item(*args, **kwargs):
    pass

def make_sales_invoices(*args, **kwargs):
    pass

def make_sales_invoices_wrapper(*args, **kwargs):
    pass

def create_purchase_invoices(*args, **kwargs):
    pass


# Migrated from regional/address_template/setup.py
def set_up_address_templates(*args, **kwargs):
    pass

def get_address_templates(*args, **kwargs):
    pass

def country(*args, **kwargs):
    pass

def get_file_content(*args, **kwargs):
    pass

def update_address_template(*args, **kwargs):
    pass


# Migrated from regional/address_template/test_regional_address_template.py
def ensure_country(*args, **kwargs):
    pass

def test_get_address_templates(*args, **kwargs):
    pass

def test_create_address_template(*args, **kwargs):
    pass

def test_update_address_template(*args, **kwargs):
    pass


# Migrated from regional/turkey/setup.py
def setup(*args, **kwargs):
    pass


# Migrated from regional/italy/setup.py
def setup(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def setup_report(*args, **kwargs):
    pass

def add_permissions(*args, **kwargs):
    pass


# Migrated from regional/italy/utils.py
def update_itemised_tax_data(*args, **kwargs):
    pass

def export_invoices(*args, **kwargs):
    pass

def prepare_invoice(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def download_zip(*args, **kwargs):
    pass

def get_invoice_summary(*args, **kwargs):
    pass

def update_summary_details(*args, **kwargs):
    pass

def append_row_as_charges(*args, **kwargs):
    pass

def sales_invoice_validate(*args, **kwargs):
    pass

def sales_invoice_on_submit(*args, **kwargs):
    pass

def prepare_and_attach_invoice(*args, **kwargs):
    pass

def generate_single_invoice(*args, **kwargs):
    pass

def sales_invoice_on_cancel(*args, **kwargs):
    pass

def get_company_country(*args, **kwargs):
    pass

def get_e_invoice_attachments(*args, **kwargs):
    pass

def validate_address(*args, **kwargs):
    pass

def get_unamended_name(*args, **kwargs):
    pass

def get_progressive_name_and_number(*args, **kwargs):
    pass

def set_state_code(*args, **kwargs):
    pass


# Migrated from regional/australia/setup.py
def setup(*args, **kwargs):
    pass

def update_regional_tax_settings(*args, **kwargs):
    pass


# Migrated from regional/south_africa/setup.py
def setup(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def add_permissions(*args, **kwargs):
    pass


# Migrated from regional/united_arab_emirates/setup.py
def setup(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def add_print_formats(*args, **kwargs):
    pass

def add_custom_roles_for_reports(*args, **kwargs):
    pass

def add_permissions(*args, **kwargs):
    pass


# Migrated from regional/united_arab_emirates/utils.py
def update_itemised_tax_data(*args, **kwargs):
    pass

def determine_if_export(*args, **kwargs):
    pass

def get_account_currency(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def get_tax_accounts(*args, **kwargs):
    pass

def update_grand_total_for_rcm(*args, **kwargs):
    pass

def update_totals(*args, **kwargs):
    pass

def make_regional_gl_entries(*args, **kwargs):
    pass

def make_gl_entry(*args, **kwargs):
    pass

def validate_returns(*args, **kwargs):
    pass


# Migrated from regional/united_states/setup.py
def setup(*args, **kwargs):
    pass

def setup_company_independent_fixtures(*args, **kwargs):
    pass

def make_custom_fields(*args, **kwargs):
    pass

def add_print_formats(*args, **kwargs):
    pass


# Migrated from regional/united_states/test_united_states.py
def test_irs_1099_custom_field(*args, **kwargs):
    pass

def test_irs_1099_report(*args, **kwargs):
    pass

def make_irs_1099_supplier(*args, **kwargs):
    pass

def make_payment_entry_to_irs_1099_supplier(*args, **kwargs):
    pass


# Migrated from regional/report/vat_audit_report/vat_audit_report.py
def execute(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_company_region(*args, **kwargs):
    pass

def get_sa_vat_accounts(*args, **kwargs):
    pass

def get_invoice_data(*args, **kwargs):
    pass

def get_invoice_items(*args, **kwargs):
    pass

def get_items_based_on_tax_rate(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_consolidated_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from regional/report/vat_audit_report/test_vat_audit_report.py
def setUp(*args, **kwargs):
    pass

def test_vat_audit_report(*args, **kwargs):
    pass

def make_company(*args, **kwargs):
    pass

def set_sa_vat_accounts(*args, **kwargs):
    pass

def make_customer(*args, **kwargs):
    pass

def make_supplier(*args, **kwargs):
    pass

def make_item(*args, **kwargs):
    pass

def make_sales_invoices(*args, **kwargs):
    pass

def make_sales_invoices_wrapper(*args, **kwargs):
    pass

def create_purchase_invoices(*args, **kwargs):
    pass


# Migrated from regional/report/electronic_invoice_register/electronic_invoice_register.py
def execute(*args, **kwargs):
    pass


# Migrated from regional/report/irs_1099/irs_1099.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def irs_1099_print(*args, **kwargs):
    pass

def get_payer_address_html(*args, **kwargs):
    pass

def get_street_address_html(*args, **kwargs):
    pass


# Migrated from regional/report/uae_vat_201/uae_vat_201.py
def execute(*args, **kwargs):
    pass

def validate_company_region(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def append_vat_on_sales(*args, **kwargs):
    pass

def standard_rated_expenses_emiratewise(*args, **kwargs):
    pass

def append_emiratewise_expenses(*args, **kwargs):
    pass

def append_vat_on_expenses(*args, **kwargs):
    pass

def append_data(*args, **kwargs):
    pass

def get_total_emiratewise(*args, **kwargs):
    pass

def get_emirates(*args, **kwargs):
    pass

def get_filters(*args, **kwargs):
    pass

def get_reverse_charge_total(*args, **kwargs):
    pass

def get_reverse_charge_tax(*args, **kwargs):
    pass

def get_reverse_charge_recoverable_total(*args, **kwargs):
    pass

def get_reverse_charge_recoverable_tax(*args, **kwargs):
    pass

def get_conditions_join(*args, **kwargs):
    pass

def get_standard_rated_expenses_total(*args, **kwargs):
    pass

def get_standard_rated_expenses_tax(*args, **kwargs):
    pass

def get_tourist_tax_return_total(*args, **kwargs):
    pass

def get_tourist_tax_return_tax(*args, **kwargs):
    pass

def get_zero_rated_total(*args, **kwargs):
    pass

def get_exempt_total(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass


# Migrated from regional/report/uae_vat_201/test_uae_vat_201.py
def setUp(*args, **kwargs):
    pass

def test_validate_company_region(*args, **kwargs):
    pass

def test_uae_vat_201_report(*args, **kwargs):
    pass

def test_uae_vat_201_report_with_foreign_transaction(*args, **kwargs):
    pass

def set_vat_accounts(*args, **kwargs):
    pass

def make_customer(*args, **kwargs):
    pass

def make_supplier(*args, **kwargs):
    pass

def create_warehouse(*args, **kwargs):
    pass

def make_item(*args, **kwargs):
    pass

def make_sales_invoices(*args, **kwargs):
    pass

def make_sales_invoices_wrapper(*args, **kwargs):
    pass

def create_purchase_invoices(*args, **kwargs):
    pass
