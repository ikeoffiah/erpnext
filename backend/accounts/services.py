
# Migrated from accounts/test_party.py
def test_get_default_price_list_should_return_none_for_invalid_group(*args, **kwargs):
    pass


# Migrated from accounts/general_ledger.py
def make_gl_entries(*args, **kwargs):
    pass

def make_acc_dimensions_offsetting_entry(*args, **kwargs):
    pass

def get_accounting_dimensions_for_offsetting_entry(*args, **kwargs):
    pass

def validate_disabled_accounts(*args, **kwargs):
    pass

def validate_accounting_period(*args, **kwargs):
    pass

def process_gl_map(*args, **kwargs):
    pass

def distribute_gl_based_on_cost_center_allocation(*args, **kwargs):
    pass

def get_cost_center_allocation_data(*args, **kwargs):
    pass

def merge_similar_entries(*args, **kwargs):
    pass

def get_merge_properties(*args, **kwargs):
    pass

def get_merge_key(*args, **kwargs):
    pass

def check_if_in_list(*args, **kwargs):
    pass

def toggle_debit_credit_if_negative(*args, **kwargs):
    pass

def save_entries(*args, **kwargs):
    pass

def make_entry(*args, **kwargs):
    pass

def validate_cwip_accounts(*args, **kwargs):
    pass

def process_debit_credit_difference(*args, **kwargs):
    pass

def get_debit_credit_difference(*args, **kwargs):
    pass

def get_debit_credit_allowance(*args, **kwargs):
    pass

def raise_debit_credit_not_equal_error(*args, **kwargs):
    pass

def has_opening_entries(*args, **kwargs):
    pass

def make_round_off_gle(*args, **kwargs):
    pass

def update_accounting_dimensions(*args, **kwargs):
    pass

def get_round_off_account_and_cost_center(*args, **kwargs):
    pass

def make_reverse_gl_entries(*args, **kwargs):
    pass

def check_freezing_date(*args, **kwargs):
    pass

def validate_against_pcv(*args, **kwargs):
    pass

def set_as_cancel(*args, **kwargs):
    pass

def validate_allowed_dimensions(*args, **kwargs):
    pass


# Migrated from accounts/utils.py
def get_fiscal_year(*args, **kwargs):
    pass

def get_fiscal_years(*args, **kwargs):
    pass

def _get_fiscal_years(*args, **kwargs):
    pass

def get_fiscal_year_filter_field(*args, **kwargs):
    pass

def validate_fiscal_year(*args, **kwargs):
    pass

def get_balance_on(*args, **kwargs):
    pass

def get_count_on(*args, **kwargs):
    pass

def add_ac(*args, **kwargs):
    pass

def add_cc(*args, **kwargs):
    pass

def _build_dimensions_dict_for_exc_gain_loss(*args, **kwargs):
    pass

def reconcile_against_document(*args, **kwargs):
    pass

def check_if_advance_entry_modified(*args, **kwargs):
    pass

def validate_allocated_amount(*args, **kwargs):
    pass

def update_reference_in_journal_entry(*args, **kwargs):
    pass

def update_reference_in_payment_entry(*args, **kwargs):
    pass

def get_reconciliation_effect_date(*args, **kwargs):
    pass

def cancel_exchange_gain_loss_journal(*args, **kwargs):
    pass

def delete_exchange_gain_loss_journal(*args, **kwargs):
    pass

def get_linked_exchange_gain_loss_journal(*args, **kwargs):
    pass

def cancel_common_party_journal(*args, **kwargs):
    pass

def update_accounting_ledgers_after_reference_removal(*args, **kwargs):
    pass

def remove_ref_from_advance_section(*args, **kwargs):
    pass

def unlink_ref_doc_from_payment_entries(*args, **kwargs):
    pass

def remove_ref_doc_link_from_jv(*args, **kwargs):
    pass

def convert_to_list(*args, **kwargs):
    pass

def remove_ref_doc_link_from_pe(*args, **kwargs):
    pass

def get_company_default(*args, **kwargs):
    pass

def fix_total_debit_credit(*args, **kwargs):
    pass

def get_currency_precision(*args, **kwargs):
    pass

def get_fraction_units(*args, **kwargs):
    pass

def get_zero_cutoff(*args, **kwargs):
    pass

def get_held_invoices(*args, **kwargs):
    pass

def get_outstanding_invoices(*args, **kwargs):
    pass

def get_account_name(*args, **kwargs):
    pass

def get_companies(*args, **kwargs):
    pass

def get_children(*args, **kwargs):
    pass

def get_account_balances(*args, **kwargs):
    pass

def get_account_balances_coa(*args, **kwargs):
    pass

def create_payment_gateway_account(*args, **kwargs):
    pass

def update_cost_center(*args, **kwargs):
    pass

def validate_field_number(*args, **kwargs):
    pass

def get_autoname_with_number(*args, **kwargs):
    pass

def parse_naming_series_variable(*args, **kwargs):
    pass

def get_coa(*args, **kwargs):
    pass

def update_gl_entries_after(*args, **kwargs):
    pass

def repost_gle_for_stock_vouchers(*args, **kwargs):
    pass

def _delete_pl_entries(*args, **kwargs):
    pass

def _delete_adv_pl_entries(*args, **kwargs):
    pass

def _delete_gl_entries(*args, **kwargs):
    pass

def _delete_accounting_ledger_entries(*args, **kwargs):
    pass

def sort_stock_vouchers_by_posting_date(*args, **kwargs):
    pass

def get_future_stock_vouchers(*args, **kwargs):
    pass

def get_voucherwise_gl_entries(*args, **kwargs):
    pass

def compare_existing_and_expected_gle(*args, **kwargs):
    pass

def get_stock_accounts(*args, **kwargs):
    pass

def get_stock_and_account_balance(*args, **kwargs):
    pass

def get_journal_entry(*args, **kwargs):
    pass

def check_and_delete_linked_reports(*args, **kwargs):
    pass

def create_err_and_its_journals(*args, **kwargs):
    pass

def _auto_create_exchange_rate_revaluation_for(*args, **kwargs):
    pass

def auto_create_exchange_rate_revaluation_daily(*args, **kwargs):
    pass

def auto_create_exchange_rate_revaluation_weekly(*args, **kwargs):
    pass

def auto_create_exchange_rate_revaluation_monthly(*args, **kwargs):
    pass

def get_payment_ledger_entries(*args, **kwargs):
    pass

def get_account_type(*args, **kwargs):
    pass

def get_advance_ledger_entry(*args, **kwargs):
    pass

def create_payment_ledger_entry(*args, **kwargs):
    pass

def update_voucher_outstanding(*args, **kwargs):
    pass

def delink_original_entry(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def reset(*args, **kwargs):
    pass

def query_for_outstanding(*args, **kwargs):
    pass

def get_voucher_outstandings(*args, **kwargs):
    pass

def create_gain_loss_journal(*args, **kwargs):
    pass

def get_party_types_from_account_type(*args, **kwargs):
    pass

def get_advance_payment_doctypes(*args, **kwargs):
    pass

def run_ledger_health_checks(*args, **kwargs):
    pass

def sync_auto_reconcile_config(*args, **kwargs):
    pass

def get_link_fields_grouped_by_option(*args, **kwargs):
    pass

def build_qb_match_conditions(*args, **kwargs):
    pass

def is_immutable_ledger_enabled(*args, **kwargs):
    pass

def pre_submit_validation(*args, **kwargs):
    pass

def _run_pre_submit_checks(*args, **kwargs):
    pass

def _check_prev_docstatus(*args, **kwargs):
    pass

def _check_credit_limit_warn(*args, **kwargs):
    pass

def _check_packed_qty_warn(*args, **kwargs):
    pass


# Migrated from accounts/party.py
def get_party_details(*args, **kwargs):
    pass

def _get_party_details(*args, **kwargs):
    pass

def set_address_details(*args, **kwargs):
    pass

def get_regional_address_details(*args, **kwargs):
    pass

def complete_contact_details(*args, **kwargs):
    pass

def set_contact_details(*args, **kwargs):
    pass

def set_other_values(*args, **kwargs):
    pass

def get_default_price_list(*args, **kwargs):
    pass

def set_price_list(*args, **kwargs):
    pass

def set_account_and_due_date(*args, **kwargs):
    pass

def get_party_account(*args, **kwargs):
    pass

def get_party_advance_account(*args, **kwargs):
    pass

def get_party_bank_account(*args, **kwargs):
    pass

def get_party_account_currency(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def get_party_gle_currency(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def get_party_gle_account(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def validate_party_gle_currency(*args, **kwargs):
    pass

def validate_party_accounts(*args, **kwargs):
    pass

def get_due_date(*args, **kwargs):
    pass

def get_due_date_from_template(*args, **kwargs):
    pass

def validate_due_date(*args, **kwargs):
    pass

def validate_due_date_with_template(*args, **kwargs):
    pass

def get_address_tax_category(*args, **kwargs):
    pass

def set_taxes(*args, **kwargs):
    pass

def get_payment_terms_template(*args, **kwargs):
    pass

def validate_party_frozen_disabled(*args, **kwargs):
    pass

def validate_account_party_type(*args, **kwargs):
    pass

def get_dashboard_info(*args, **kwargs):
    pass

def get_party_shipping_address(*args, **kwargs):
    pass

def get_partywise_advanced_payment_amount(*args, **kwargs):
    pass

def get_default_contact(*args, **kwargs):
    pass

def add_party_account(*args, **kwargs):
    pass

def render_address(*args, **kwargs):
    pass

def validate_party_currency_before_merging(*args, **kwargs):
    pass


# Migrated from accounts/deferred_revenue.py
def validate_service_stop_date(*args, **kwargs):
    pass

def build_conditions(*args, **kwargs):
    pass

def convert_deferred_expense_to_expense(*args, **kwargs):
    pass

def convert_deferred_revenue_to_income(*args, **kwargs):
    pass

def get_booking_dates(*args, **kwargs):
    pass

def calculate_monthly_amount(*args, **kwargs):
    pass

def calculate_amount(*args, **kwargs):
    pass

def get_already_booked_amount(*args, **kwargs):
    pass

def book_deferred_income_or_expense(*args, **kwargs):
    pass

def _book_deferred_revenue_or_expense(*args, **kwargs):
    pass

def process_deferred_accounting(*args, **kwargs):
    pass

def make_gl_entries(*args, **kwargs):
    pass

def send_mail(*args, **kwargs):
    pass

def book_revenue_via_journal_entry(*args, **kwargs):
    pass

def get_deferred_booking_accounts(*args, **kwargs):
    pass


# Migrated from accounts/test/test_reports.py
def test_execute_all_accounts_reports(*args, **kwargs):
    pass


# Migrated from accounts/test/test_utils.py
def test_get_party_shipping_address(*args, **kwargs):
    pass

def test_get_party_shipping_address2(*args, **kwargs):
    pass

def test_get_voucher_wise_gl_entry(*args, **kwargs):
    pass

def test_stock_voucher_sorting(*args, **kwargs):
    pass

def test_update_reference_in_payment_entry(*args, **kwargs):
    pass

def test_naming_series_variable_parsing(*args, **kwargs):
    pass

def test_get_zero_cutoff(*args, **kwargs):
    pass


# Migrated from accounts/test/test_pre_submit_validation.py
def _get_orange_warnings(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def _make_si(*args, **kwargs):
    pass

def test_warns_when_amount_exceeds_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_amount_within_credit_limit(*args, **kwargs):
    pass

def test_no_warning_for_return_invoices(*args, **kwargs):
    pass

def test_no_warning_when_customer_has_no_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_all_items_linked_to_so_or_dn(*args, **kwargs):
    pass

def _make_so(*args, **kwargs):
    pass

def test_warns_on_first_save_when_limit_exceeded(*args, **kwargs):
    pass

def test_warns_when_amount_exceeds_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_amount_within_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_bypass_is_set(*args, **kwargs):
    pass

def _make_dn(*args, **kwargs):
    pass

def test_bypass_false_warns_for_existing_draft(*args, **kwargs):
    pass

def test_bypass_false_no_warning_when_under_limit(*args, **kwargs):
    pass

def test_bypass_false_no_warning_when_all_items_linked_to_so(*args, **kwargs):
    pass

def test_bypass_false_partial_link_warns_proportionally(*args, **kwargs):
    pass

def test_bypass_true_warns_on_first_save_new_doc(*args, **kwargs):
    pass

def test_bypass_true_no_warning_when_all_items_billed(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def _make_dn(*args, **kwargs):
    pass

def test_no_warning_for_new_doc(*args, **kwargs):
    pass

def test_warns_when_packed_qty_mismatches(*args, **kwargs):
    pass

def test_no_warning_when_packed_qty_matches(*args, **kwargs):
    pass


# Migrated from accounts/test/accounts_mixin.py
def create_customer(*args, **kwargs):
    pass

def create_supplier(*args, **kwargs):
    pass

def create_item(*args, **kwargs):
    pass

def create_company(*args, **kwargs):
    pass

def enable_advance_as_liability(*args, **kwargs):
    pass

def disable_advance_as_liability(*args, **kwargs):
    pass

def identify_default_warehouses(*args, **kwargs):
    pass

def create_usd_receivable_account(*args, **kwargs):
    pass

def create_usd_payable_account(*args, **kwargs):
    pass

def clear_old_entries(*args, **kwargs):
    pass


# Migrated from accounts/notification/notification_for_new_fiscal_year/notification_for_new_fiscal_year.py
def get_context(*args, **kwargs):
    pass


# Migrated from accounts/custom/address.py
def validate(*args, **kwargs):
    pass

def link_address(*args, **kwargs):
    pass

def update_company_address(*args, **kwargs):
    pass

def validate_reference(*args, **kwargs):
    pass

def on_update(*args, **kwargs):
    pass

def get_shipping_address(*args, **kwargs):
    pass


# Migrated from accounts/dashboard_chart_source/account_balance_timeline/account_balance_timeline.py
def get(*args, **kwargs):
    pass

def build_result(*args, **kwargs):
    pass

def get_gl_entries(*args, **kwargs):
    pass

def get_dates_from_timegrain(*args, **kwargs):
    pass


# Migrated from accounts/report/financial_statements.py
def get_period_list(*args, **kwargs):
    pass

def get_fiscal_year_data(*args, **kwargs):
    pass

def validate_fiscal_year(*args, **kwargs):
    pass

def validate_dates(*args, **kwargs):
    pass

def get_months(*args, **kwargs):
    pass

def get_label(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_appropriate_currency(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def filter_out_zero_value_rows(*args, **kwargs):
    pass

def get_all_parents(*args, **kwargs):
    pass

def add_total_row(*args, **kwargs):
    pass

def get_accounts(*args, **kwargs):
    pass

def filter_accounts(*args, **kwargs):
    pass

def add_to_list(*args, **kwargs):
    pass

def sort_accounts(*args, **kwargs):
    pass

def compare_accounts(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass

def get_accounting_entries(*args, **kwargs):
    pass

def get_account_filter_query(*args, **kwargs):
    pass

def apply_additional_conditions(*args, **kwargs):
    pass

def get_cost_centers_with_children(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_filtered_list_for_consolidated_report(*args, **kwargs):
    pass

def compute_growth_view_data(*args, **kwargs):
    pass

def compute_margin_view_data(*args, **kwargs):
    pass


# Migrated from accounts/report/utils.py
def get_currency(*args, **kwargs):
    pass

def convert(*args, **kwargs):
    pass

def get_rate_as_at(*args, **kwargs):
    pass

def convert_to_presentation_currency(*args, **kwargs):
    pass

def get_appropriate_company(*args, **kwargs):
    pass

def get_invoiced_item_gross_margin(*args, **kwargs):
    pass

def get_query_columns(*args, **kwargs):
    pass

def get_values_for_columns(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def get_taxes_query(*args, **kwargs):
    pass

def get_journal_entries(*args, **kwargs):
    pass

def get_payment_entries(*args, **kwargs):
    pass

def apply_common_conditions(*args, **kwargs):
    pass

def get_advance_taxes_and_charges(*args, **kwargs):
    pass

def filter_invoices_based_on_dimensions(*args, **kwargs):
    pass

def get_opening_row(*args, **kwargs):
    pass


# Migrated from accounts/report/non_billed_report.py
def get_ordered_to_be_billed_data(*args, **kwargs):
    pass

def get_project_field(*args, **kwargs):
    pass


# Migrated from accounts/report/gross_profit/test_gross_profit.py
def setUp(*args, **kwargs):
    pass

def create_company(*args, **kwargs):
    pass

def create_item(*args, **kwargs):
    pass

def create_bundle(*args, **kwargs):
    pass

def create_customer(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_delivery_note(*args, **kwargs):
    pass

def clear_old_entries(*args, **kwargs):
    pass

def test_invoice_without_only_delivery_note(*args, **kwargs):
    pass

def test_bundled_delivery_note_with_different_warehouses(*args, **kwargs):
    pass

def test_order_connected_dn_and_inv(*args, **kwargs):
    pass

def test_crnote_against_invoice_with_multiple_instances_of_same_item(*args, **kwargs):
    pass

def test_standalone_cr_notes(*args, **kwargs):
    pass

def test_different_rates_in_si_and_dn(*args, **kwargs):
    pass

def test_valuation_rate_without_previous_sle(*args, **kwargs):
    pass

def test_gross_profit_groupby_invoices(*args, **kwargs):
    pass

def test_profit_for_later_period_return(*args, **kwargs):
    pass

def test_sales_person_wise_gross_profit(*args, **kwargs):
    pass

def test_drop_ship(*args, **kwargs):
    pass

def make_sales_person(*args, **kwargs):
    pass


# Migrated from accounts/report/gross_profit/gross_profit.py
def execute(*args, **kwargs):
    pass

def get_data_when_grouped_by_invoice(*args, **kwargs):
    pass

def get_data_when_not_grouped_by_invoice(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_column_names(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def process(*args, **kwargs):
    pass

def update_return_invoices(*args, **kwargs):
    pass

def get_average_rate_based_on_group_by(*args, **kwargs):
    pass

def set_average_based_on_payment_term_portion(*args, **kwargs):
    pass

def is_not_invoice_row(*args, **kwargs):
    pass

def set_average_rate(*args, **kwargs):
    pass

def set_average_gross_profit(*args, **kwargs):
    pass

def get_returned_invoice_items(*args, **kwargs):
    pass

def skip_row(*args, **kwargs):
    pass

def get_buying_amount_from_product_bundle(*args, **kwargs):
    pass

def calculate_buying_amount_from_sle(*args, **kwargs):
    pass

def get_buying_amount(*args, **kwargs):
    pass

def get_buying_amount_from_so_dn(*args, **kwargs):
    pass

def get_average_buying_rate(*args, **kwargs):
    pass

def get_last_purchase_rate(*args, **kwargs):
    pass

def load_invoice_items(*args, **kwargs):
    pass

def prepare_invoice_query(*args, **kwargs):
    pass

def apply_common_filters(*args, **kwargs):
    pass

def prepare_vouchers_to_ignore(*args, **kwargs):
    pass

def get_delivery_notes(*args, **kwargs):
    pass

def group_items_by_invoice(*args, **kwargs):
    pass

def get_invoice_row(*args, **kwargs):
    pass

def get_bundle_item_row(*args, **kwargs):
    pass

def get_stock_ledger_entries(*args, **kwargs):
    pass

def load_product_bundle(*args, **kwargs):
    pass

def load_non_stock_items(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable/test_accounts_receivable.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_payment_entry(*args, **kwargs):
    pass

def create_credit_note(*args, **kwargs):
    pass

def test_pos_receivable(*args, **kwargs):
    pass

def test_accounts_receivable_with_payment(*args, **kwargs):
    pass

def test_accounts_receivable_without_payment(*args, **kwargs):
    pass

def test_allow_multi_currency_invoices_against_single_party_account(*args, **kwargs):
    pass

def test_accounts_receivable_with_partial_payment(*args, **kwargs):
    pass

def test_cr_note_flag_to_update_self(*args, **kwargs):
    pass

def test_payment_againt_po_in_receivable_report(*args, **kwargs):
    pass

def test_exchange_revaluation_for_party(*args, **kwargs):
    pass

def test_payment_against_credit_note(*args, **kwargs):
    pass

def test_group_by_party(*args, **kwargs):
    pass

def test_future_payments(*args, **kwargs):
    pass

def test_sales_person(*args, **kwargs):
    pass

def test_cost_center_filter(*args, **kwargs):
    pass

def test_customer_group_filter(*args, **kwargs):
    pass

def test_multi_customer_group_filter(*args, **kwargs):
    pass

def test_party_account_filter(*args, **kwargs):
    pass

def test_usd_customer_filter(*args, **kwargs):
    pass

def test_multi_select_party_filter(*args, **kwargs):
    pass

def test_report_output_if_party_is_missing(*args, **kwargs):
    pass

def test_future_payments_on_foreign_currency(*args, **kwargs):
    pass

def test_accounts_receivable_output_for_minor_outstanding(*args, **kwargs):
    pass

def test_cost_center_on_report_output(*args, **kwargs):
    pass

def test_payment_terms_template_filters(*args, **kwargs):
    pass

def test_project_filter(*args, **kwargs):
    pass

def test_project_on_report_output(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable/accounts_receivable.py
def execute(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def set_defaults(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def fetch_ple_in_buffered_cursor(*args, **kwargs):
    pass

def fetch_ple_in_unbuffered_cursor(*args, **kwargs):
    pass

def build_voucher_dict(*args, **kwargs):
    pass

def init_voucher_balance(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def init_subtotal_row(*args, **kwargs):
    pass

def get_currency_fields(*args, **kwargs):
    pass

def get_voucher_balance(*args, **kwargs):
    pass

def update_voucher_balance(*args, **kwargs):
    pass

def update_sub_total_row(*args, **kwargs):
    pass

def append_subtotal_row(*args, **kwargs):
    pass

def build_data(*args, **kwargs):
    pass

def append_row(*args, **kwargs):
    pass

def set_invoice_details(*args, **kwargs):
    pass

def set_delivery_notes(*args, **kwargs):
    pass

def build_delivery_note_map(*args, **kwargs):
    pass

def get_invoice_details(*args, **kwargs):
    pass

def set_party_details(*args, **kwargs):
    pass

def allocate_outstanding_based_on_payment_terms(*args, **kwargs):
    pass

def get_payment_terms(*args, **kwargs):
    pass

def append_payment_term(*args, **kwargs):
    pass

def allocate_closing_to_term(*args, **kwargs):
    pass

def allocate_extra_payments_or_credits(*args, **kwargs):
    pass

def get_future_payments(*args, **kwargs):
    pass

def get_future_payments_from_payment_entry(*args, **kwargs):
    pass

def get_future_payments_from_journal_entry(*args, **kwargs):
    pass

def allocate_future_payments(*args, **kwargs):
    pass

def get_return_entries(*args, **kwargs):
    pass

def set_ageing(*args, **kwargs):
    pass

def get_ageing_data(*args, **kwargs):
    pass

def prepare_ple_query(*args, **kwargs):
    pass

def get_sales_invoices_or_customers_based_on_sales_person(*args, **kwargs):
    pass

def prepare_conditions(*args, **kwargs):
    pass

def get_cost_center_conditions(*args, **kwargs):
    pass

def add_common_filters(*args, **kwargs):
    pass

def add_customer_filters(*args, **kwargs):
    pass

def exclude_employee_transaction(*args, **kwargs):
    pass

def add_supplier_filters(*args, **kwargs):
    pass

def add_payment_term_template_filters(*args, **kwargs):
    pass

def get_hierarchical_filters(*args, **kwargs):
    pass

def add_accounting_dimensions_filters(*args, **kwargs):
    pass

def is_invoice(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def add_column(*args, **kwargs):
    pass

def setup_ageing_columns(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass

def get_exchange_rate_revaluations(*args, **kwargs):
    pass

def get_party_group_with_children(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_sales_register/item_wise_sales_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_income_account(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def apply_conditions(*args, **kwargs):
    pass

def apply_order_by_conditions(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def get_delivery_notes_against_sales_order(*args, **kwargs):
    pass

def get_grand_total(*args, **kwargs):
    pass

def get_tax_accounts(*args, **kwargs):
    pass

def get_tax_details_query(*args, **kwargs):
    pass

def add_total_row(*args, **kwargs):
    pass

def get_display_value(*args, **kwargs):
    pass

def get_group_by_and_display_fields(*args, **kwargs):
    pass

def add_sub_total_row(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_sales_register/test_item_wise_sales_register.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def test_basic_report_output(*args, **kwargs):
    pass

def test_grouped_report_handles_different_tax_descriptions(*args, **kwargs):
    pass


# Migrated from accounts/report/inactive_sales_items/inactive_sales_items.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_sales_details(*args, **kwargs):
    pass

def get_territories(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass


# Migrated from accounts/report/billed_items_to_be_received/billed_items_to_be_received.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_report_filters(*args, **kwargs):
    pass

def get_report_fields(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_payment_summary/sales_payment_summary.py
def execute(*args, **kwargs):
    pass

def get_pos_columns(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_pos_sales_payment_data(*args, **kwargs):
    pass

def get_sales_payment_data(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_pos_invoice_data(*args, **kwargs):
    pass

def get_sales_invoice_data(*args, **kwargs):
    pass

def get_mode_of_payments(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def get_mode_of_payment_details(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_payment_summary/test_sales_payment_summary.py
def test_get_mode_of_payments(*args, **kwargs):
    pass

def test_get_mode_of_payments_details(*args, **kwargs):
    pass

def get_filters(*args, **kwargs):
    pass

def create_sales_invoice_record(*args, **kwargs):
    pass


# Migrated from accounts/report/voucher_wise_balance/voucher_wise_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def apply_filters(*args, **kwargs):
    pass


# Migrated from accounts/report/general_and_payment_ledger_comparison/general_and_payment_ledger_comparison.py
def __init__(*args, **kwargs):
    pass

def get_accounts(*args, **kwargs):
    pass

def generate_filters(*args, **kwargs):
    pass

def get_gle(*args, **kwargs):
    pass

def get_ple(*args, **kwargs):
    pass

def compare(*args, **kwargs):
    pass

def generate_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/general_and_payment_ledger_comparison/test_general_and_payment_ledger_comparison.py
def setUp(*args, **kwargs):
    pass

def cleanup(*args, **kwargs):
    pass

def test_01_basic_report_functionality(*args, **kwargs):
    pass


# Migrated from accounts/report/share_ledger/share_ledger.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_all_transfers(*args, **kwargs):
    pass


# Migrated from accounts/report/supplier_ledger_summary/supplier_ledger_summary.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/supplier_ledger_summary/test_supplier_ledger_summary.py
def setUp(*args, **kwargs):
    pass

def create_purchase_invoice(*args, **kwargs):
    pass

def test_basic_supplier_ledger_summary(*args, **kwargs):
    pass

def test_supplier_ledger_summary_with_filters(*args, **kwargs):
    pass


# Migrated from accounts/report/share_balance/share_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_all_shares(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_purchase_register/item_wise_purchase_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def apply_conditions(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def get_aii_accounts(*args, **kwargs):
    pass

def get_purchase_receipts_against_purchase_order(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_purchase_register/test_item_wise_purchase_register.py
def setUp(*args, **kwargs):
    pass

def create_purchase_invoice(*args, **kwargs):
    pass

def test_basic_report_output(*args, **kwargs):
    pass


# Migrated from accounts/report/budget_variance_report/budget_variance_report.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_budget_records(*args, **kwargs):
    pass

def build_budget_map(*args, **kwargs):
    pass

def get_actual_transactions(*args, **kwargs):
    pass

def get_budget_distributions(*args, **kwargs):
    pass

def get_months_in_range(*args, **kwargs):
    pass

def build_report_data(*args, **kwargs):
    pass

def get_periods(*args, **kwargs):
    pass

def get_months_between(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_fiscal_years(*args, **kwargs):
    pass

def get_budget_dimensions(*args, **kwargs):
    pass

def validate_budget_dimensions(*args, **kwargs):
    pass

def build_comparison_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/balance_sheet/balance_sheet.py
def execute(*args, **kwargs):
    pass

def get_provisional_profit_loss(*args, **kwargs):
    pass

def check_opening_balance(*args, **kwargs):
    pass

def get_report_summary(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/balance_sheet/test_balance_sheet.py
def test_balance_sheet(*args, **kwargs):
    pass

def make_journal_entry(*args, **kwargs):
    pass

def create_account(*args, **kwargs):
    pass


# Migrated from accounts/report/trial_balance/test_trial_balance.py
def setUp(*args, **kwargs):
    pass

def test_offsetting_entries_for_accounting_dimensions(*args, **kwargs):
    pass


# Migrated from accounts/report/trial_balance/trial_balance.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_opening_balances(*args, **kwargs):
    pass

def get_rootwise_opening_balances(*args, **kwargs):
    pass

def get_opening_balance(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def calculate_total_row(*args, **kwargs):
    pass

def sum_value_fields(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def prepare_opening_closing(*args, **kwargs):
    pass

def hide_group_accounts(*args, **kwargs):
    pass


# Migrated from accounts/report/payment_ledger/payment_ledger.py
def __init__(*args, **kwargs):
    pass

def init_voucher_dict(*args, **kwargs):
    pass

def build_data(*args, **kwargs):
    pass

def build_conditions(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/payment_ledger/test_payment_ledger.py
def setUp(*args, **kwargs):
    pass

def cleanup(*args, **kwargs):
    pass

def create_company(*args, **kwargs):
    pass

def test_unpaid_invoice_outstanding(*args, **kwargs):
    pass


# Migrated from accounts/report/consolidated_financial_statement/consolidated_financial_statement.py
def execute(*args, **kwargs):
    pass

def get_balance_sheet_data(*args, **kwargs):
    pass

def prepare_companywise_opening_balance(*args, **kwargs):
    pass

def get_opening_balance(*args, **kwargs):
    pass

def get_root_account_name(*args, **kwargs):
    pass

def get_profit_loss_data(*args, **kwargs):
    pass

def get_income_expense_data(*args, **kwargs):
    pass

def get_cash_flow_data(*args, **kwargs):
    pass

def get_account_type_based_data(*args, **kwargs):
    pass

def get_company_columns(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_company_currency(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def get_account_heads(*args, **kwargs):
    pass

def update_parent_account_names(*args, **kwargs):
    pass

def get_companies(*args, **kwargs):
    pass

def get_subsidiary_companies(*args, **kwargs):
    pass

def get_accounts(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass

def get_account_details(*args, **kwargs):
    pass

def validate_entries(*args, **kwargs):
    pass

def get_additional_conditions(*args, **kwargs):
    pass

def add_total_row(*args, **kwargs):
    pass

def filter_accounts(*args, **kwargs):
    pass

def add_to_list(*args, **kwargs):
    pass


# Migrated from accounts/report/calculated_discount_mismatch/calculated_discount_mismatch.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_transactions_with_discount_percentage(*args, **kwargs):
    pass


# Migrated from accounts/report/dimension_wise_accounts_balance_report/dimension_wise_accounts_balance_report.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass

def format_gl_entries(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def get_condition(*args, **kwargs):
    pass

def get_dimensions(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/general_ledger/general_ledger.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def validate_party(*args, **kwargs):
    pass

def set_account_currency(*args, **kwargs):
    pass

def get_result(*args, **kwargs):
    pass

def get_gl_entries(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_party_name_map(*args, **kwargs):
    pass

def get_accounts_with_children(*args, **kwargs):
    pass

def set_bill_no(*args, **kwargs):
    pass

def get_translated_labels_for_totals(*args, **kwargs):
    pass

def wrap_in_quotes(*args, **kwargs):
    pass

def get_data_with_opening_closing(*args, **kwargs):
    pass

def add_total_to_data(*args, **kwargs):
    pass

def get_totals_dict(*args, **kwargs):
    pass

def get_group_by_field(*args, **kwargs):
    pass

def initialize_gle_map(*args, **kwargs):
    pass

def get_accountwise_gle(*args, **kwargs):
    pass

def update_value_in_dict(*args, **kwargs):
    pass

def get_account_type_map(*args, **kwargs):
    pass

def get_result_as_list(*args, **kwargs):
    pass

def get_supplier_invoice_details(*args, **kwargs):
    pass

def get_balance(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/general_ledger/test_general_ledger.py
def setUp(*args, **kwargs):
    pass

def clear_old_entries(*args, **kwargs):
    pass

def test_foreign_account_balance_after_exchange_rate_revaluation(*args, **kwargs):
    pass

def test_ignore_exchange_rate_journals_filter(*args, **kwargs):
    pass

def test_ignore_cr_dr_notes_filter(*args, **kwargs):
    pass


# Migrated from accounts/report/trial_balance_for_party/trial_balance_for_party.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_opening_balances(*args, **kwargs):
    pass

def get_balances_within_period(*args, **kwargs):
    pass

def toggle_debit_credit(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def is_party_name_visible(*args, **kwargs):
    pass


# Migrated from accounts/report/asset_depreciation_ledger/asset_depreciation_ledger.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_assets_details(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/invalid_ledger_entries/invalid_ledger_entries.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def identify_cancelled_vouchers(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def build_query_filters(*args, **kwargs):
    pass

def get_active_vouchers_for_period(*args, **kwargs):
    pass


# Migrated from accounts/report/asset_depreciations_and_balances/asset_depreciations_and_balances.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_group_by_asset_category_data(*args, **kwargs):
    pass

def get_asset_categories_for_grouped_by_category(*args, **kwargs):
    pass

def get_assets_for_grouped_by_category(*args, **kwargs):
    pass

def get_asset_value_adjustment_map_by_category(*args, **kwargs):
    pass

def get_group_by_asset_data(*args, **kwargs):
    pass

def get_asset_details_for_grouped_by_category(*args, **kwargs):
    pass

def get_assets_for_grouped_by_asset(*args, **kwargs):
    pass

def get_asset_value_adjustment_map(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/custom_financial_statement/custom_financial_statement.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/customer_ledger_summary/customer_ledger_summary.py
def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def update_hierarchical_filters(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def get_party_conditions(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_gl_entries(*args, **kwargs):
    pass

def prepare_conditions(*args, **kwargs):
    pass

def get_return_invoices(*args, **kwargs):
    pass

def get_party_adjustment_amounts(*args, **kwargs):
    pass

def get_children(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/customer_ledger_summary/test_customer_ledger_summary.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_payment_entry(*args, **kwargs):
    pass

def create_credit_note(*args, **kwargs):
    pass

def test_ledger_summary_basic_output(*args, **kwargs):
    pass

def test_summary_with_return_and_payment(*args, **kwargs):
    pass

def test_customer_ledger_ignore_cr_dr_filter(*args, **kwargs):
    pass

def test_journal_voucher_against_return_invoice(*args, **kwargs):
    pass


# Migrated from accounts/report/profitability_analysis/profitability_analysis.py
def execute(*args, **kwargs):
    pass

def get_accounts_data(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass


# Migrated from accounts/report/purchase_invoice_trends/purchase_invoice_trends.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/delivered_items_to_be_billed/delivered_items_to_be_billed.py
def execute(*args, **kwargs):
    pass

def get_column(*args, **kwargs):
    pass

def get_args(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable_summary/accounts_receivable_summary.py
def execute(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_party_total(*args, **kwargs):
    pass

def init_party_total(*args, **kwargs):
    pass

def set_party_details(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_gl_balance(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable_summary/test_accounts_receivable_summary.py
def setUp(*args, **kwargs):
    pass

def test_01_receivable_summary_output(*args, **kwargs):
    pass

def test_02_various_filters_and_output(*args, **kwargs):
    pass


# Migrated from accounts/report/tax_withholding_details/tax_withholding_details.py
def __init__(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def build_rows(*args, **kwargs):
    pass

def get_entries_query(*args, **kwargs):
    pass

def fetch_party_details(*args, **kwargs):
    pass

def get_party_query(*args, **kwargs):
    pass

def fetch_additional_doc_info(*args, **kwargs):
    pass

def get_doc_info_query(*args, **kwargs):
    pass

def get_purchase_invoice_fields(*args, **kwargs):
    pass

def get_sales_invoice_fields(*args, **kwargs):
    pass

def get_payment_entry_fields(*args, **kwargs):
    pass

def get_journal_entry_fields(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/tax_withholding_details/test_tax_withholding_details.py
def setUp(*args, **kwargs):
    pass

def test_tax_withholding_for_customers(*args, **kwargs):
    pass

def test_single_account_for_multiple_categories(*args, **kwargs):
    pass

def test_date_filters_in_multiple_tax_withholding_rules(*args, **kwargs):
    pass

def check_expected_values(*args, **kwargs):
    pass

def create_tax_category(*args, **kwargs):
    pass

def create_tcs_payment_entry(*args, **kwargs):
    pass

def create_tcs_journal_entry(*args, **kwargs):
    pass


# Migrated from accounts/report/cash_flow/cash_flow.py
def execute(*args, **kwargs):
    pass

def get_cash_flow_accounts(*args, **kwargs):
    pass

def get_account_type_based_data(*args, **kwargs):
    pass

def get_account_type_based_gl_data(*args, **kwargs):
    pass

def get_start_date(*args, **kwargs):
    pass

def add_total_row_account(*args, **kwargs):
    pass

def show_opening_and_closing_balance(*args, **kwargs):
    pass

def get_opening_balance(*args, **kwargs):
    pass

def get_net_income(*args, **kwargs):
    pass

def get_opening_range_using_fiscal_year(*args, **kwargs):
    pass

def get_report_summary(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/payment_period_based_on_invoice_date/payment_period_based_on_invoice_date.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_invoice_posting_date_map(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_payable_summary/accounts_payable_summary.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/pos_register/pos_register.py
def execute(*args, **kwargs):
    pass

def get_pos_entries(*args, **kwargs):
    pass

def concat_mode_of_payments(*args, **kwargs):
    pass

def add_subtotal_row(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_group_by_field(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/deferred_revenue_and_expense/test_deferred_revenue_and_expense.py
def clear_old_entries(*args, **kwargs):
    pass

def setup_deferred_accounts_and_items(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def test_deferred_revenue(*args, **kwargs):
    pass

def test_deferred_expense(*args, **kwargs):
    pass

def test_zero_months(*args, **kwargs):
    pass

def test_zero_amount(*args, **kwargs):
    pass


# Migrated from accounts/report/deferred_revenue_and_expense/deferred_revenue_and_expense.py
def __init__(*args, **kwargs):
    pass

def report_data(*args, **kwargs):
    pass

def get_amount(*args, **kwargs):
    pass

def get_item_total(*args, **kwargs):
    pass

def calculate_amount(*args, **kwargs):
    pass

def calculate_monthly_amount(*args, **kwargs):
    pass

def calculate_days_amount(*args, **kwargs):
    pass

def make_dummy_gle(*args, **kwargs):
    pass

def simulate_future_posting(*args, **kwargs):
    pass

def calculate_item_revenue_expense_for_period(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def calculate_invoice_revenue_expense_for_period(*args, **kwargs):
    pass

def estimate_future(*args, **kwargs):
    pass

def report_data(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def get_period_list(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def estimate_future(*args, **kwargs):
    pass

def calculate_revenue_and_expense(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def generate_report_data(*args, **kwargs):
    pass

def prepare_chart(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/tds_computation_summary/tds_computation_summary.py
def validate_filters(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def group_rows(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_invoice_trends/sales_invoice_trends.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/profit_and_loss_statement/test_profit_and_loss_statement.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def get_fiscal_year(*args, **kwargs):
    pass

def get_report_filters(*args, **kwargs):
    pass

def test_profit_and_loss_output_and_summary(*args, **kwargs):
    pass

def test_p_and_l_export(*args, **kwargs):
    pass

def test_accumulate_filter(*args, **kwargs):
    pass


# Migrated from accounts/report/profit_and_loss_statement/profit_and_loss_statement.py
def execute(*args, **kwargs):
    pass

def get_report_summary(*args, **kwargs):
    pass

def get_net_profit_loss(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/gross_and_net_profit_report/gross_and_net_profit_report.py
def execute(*args, **kwargs):
    pass

def get_revenue(*args, **kwargs):
    pass

def remove_parent_with_no_child(*args, **kwargs):
    pass

def adjust_account_totals(*args, **kwargs):
    pass

def set_total(*args, **kwargs):
    pass

def get_profit(*args, **kwargs):
    pass

def get_net_profit(*args, **kwargs):
    pass


# Migrated from accounts/report/financial_ratios/financial_ratios.py
def execute(*args, **kwargs):
    pass

def setup_filters(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_ratios_data(*args, **kwargs):
    pass

def get_gl_data(*args, **kwargs):
    pass

def add_liquidity_ratios(*args, **kwargs):
    pass

def add_solvency_ratios(*args, **kwargs):
    pass

def add_turnover_ratios(*args, **kwargs):
    pass

def update_balances(*args, **kwargs):
    pass

def avg_ratio_balance(*args, **kwargs):
    pass

def calculate_ratio(*args, **kwargs):
    pass


# Migrated from accounts/report/received_items_to_be_billed/received_items_to_be_billed.py
def execute(*args, **kwargs):
    pass

def get_column(*args, **kwargs):
    pass

def get_args(*args, **kwargs):
    pass


# Migrated from accounts/report/bank_clearance_summary/bank_clearance_summary.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_entries_for_bank_clearance_summary(*args, **kwargs):
    pass


# Migrated from accounts/report/consolidated_trial_balance/consolidated_trial_balance.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def validate_companies(*args, **kwargs):
    pass

def sort_companies(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_company_wise_tb_data(*args, **kwargs):
    pass

def prepare_companywise_tb_data(*args, **kwargs):
    pass

def calculate_foreign_currency_translation_reserve(*args, **kwargs):
    pass

def get_fctr_root_row_index(*args, **kwargs):
    pass

def consolidate_trial_balance_data(*args, **kwargs):
    pass

def get_reporting_currency(*args, **kwargs):
    pass

def consolidate_gle_data(*args, **kwargs):
    pass

def update_to_presentation_currency(*args, **kwargs):
    pass

def prepare_opening_closing_for_ctb(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/consolidated_trial_balance/test_consolidated_trial_balance.py
def setUp(*args, **kwargs):
    pass

def test_single_company_report(*args, **kwargs):
    pass

def test_child_company_report_with_same_default_currency_as_parent_company(*args, **kwargs):
    pass

def test_child_company_with_different_default_currency_from_parent_company(*args, **kwargs):
    pass

def create_journal_entry(*args, **kwargs):
    pass


# Migrated from accounts/report/cheques_and_deposits_incorrectly_cleared/cheques_and_deposits_incorrectly_cleared.py
def execute(*args, **kwargs):
    pass

def build_payment_entry_dict(*args, **kwargs):
    pass

def build_journal_entry_dict(*args, **kwargs):
    pass

def build_data(*args, **kwargs):
    pass

def get_amounts_not_reflected_in_system_for_bank_reconciliation_statement(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/account_balance/test_account_balance.py
def test_account_balance(*args, **kwargs):
    pass

def make_sales_invoice(*args, **kwargs):
    pass


# Migrated from accounts/report/account_balance/account_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass


# Migrated from accounts/report/bank_reconciliation_statement/bank_reconciliation_statement.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_entries_for_bank_reconciliation_statement(*args, **kwargs):
    pass

def get_journal_entries(*args, **kwargs):
    pass

def get_payment_entries(*args, **kwargs):
    pass

def get_purchase_invoices(*args, **kwargs):
    pass

def get_pos_entries(*args, **kwargs):
    pass

def get_amounts_not_reflected_in_system(*args, **kwargs):
    pass

def get_amounts_not_reflected_in_system_for_bank_reconciliation_statement(*args, **kwargs):
    pass

def get_balance_row(*args, **kwargs):
    pass


# Migrated from accounts/report/bank_reconciliation_statement/test_bank_reconciliation_statement.py
def test_loan_entries_in_bank_reco_statement(*args, **kwargs):
    pass


# Migrated from accounts/report/purchase_register/test_purchase_register.py
def test_purchase_register(*args, **kwargs):
    pass

def test_purchase_register_ignores_tax_rows_from_other_doctype(*args, **kwargs):
    pass

def test_purchase_register_ledger_view(*args, **kwargs):
    pass

def make_purchase_invoice(*args, **kwargs):
    pass

def create_purchase_invoice_with_taxes(*args, **kwargs):
    pass

def make_payment_entry(*args, **kwargs):
    pass


# Migrated from accounts/report/purchase_register/purchase_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_account_columns(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_payments(*args, **kwargs):
    pass

def get_invoice_expense_map(*args, **kwargs):
    pass

def get_internal_invoice_map(*args, **kwargs):
    pass

def get_invoice_tax_map(*args, **kwargs):
    pass

def get_invoice_po_pr_map(*args, **kwargs):
    pass

def get_account_details(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_register/sales_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_account_columns(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_payments(*args, **kwargs):
    pass

def get_invoice_income_map(*args, **kwargs):
    pass

def get_internal_invoice_map(*args, **kwargs):
    pass

def get_invoice_tax_map(*args, **kwargs):
    pass

def get_invoice_so_dn_map(*args, **kwargs):
    pass

def get_invoice_cc_wh_map(*args, **kwargs):
    pass

def get_mode_of_payments(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_register/test_sales_register.py
def setUp(*args, **kwargs):
    pass

def create_child_cost_center(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def test_basic_report_output(*args, **kwargs):
    pass

def test_sales_register_ignores_tax_rows_from_other_doctype(*args, **kwargs):
    pass

def test_journal_with_cost_center_filter(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_payable/test_accounts_payable.py
def setUp(*args, **kwargs):
    pass

def test_accounts_payable_for_foreign_currency_supplier(*args, **kwargs):
    pass

def create_purchase_invoice(*args, **kwargs):
    pass

def test_payment_terms_template_filters(*args, **kwargs):
    pass

def test_project_filter(*args, **kwargs):
    pass

def test_project_on_report_output(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_payable/accounts_payable.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/test_party.py
def test_get_default_price_list_should_return_none_for_invalid_group(*args, **kwargs):
    pass


# Migrated from accounts/general_ledger.py
def make_gl_entries(*args, **kwargs):
    pass

def make_acc_dimensions_offsetting_entry(*args, **kwargs):
    pass

def get_accounting_dimensions_for_offsetting_entry(*args, **kwargs):
    pass

def validate_disabled_accounts(*args, **kwargs):
    pass

def validate_accounting_period(*args, **kwargs):
    pass

def process_gl_map(*args, **kwargs):
    pass

def distribute_gl_based_on_cost_center_allocation(*args, **kwargs):
    pass

def get_cost_center_allocation_data(*args, **kwargs):
    pass

def merge_similar_entries(*args, **kwargs):
    pass

def get_merge_properties(*args, **kwargs):
    pass

def get_merge_key(*args, **kwargs):
    pass

def check_if_in_list(*args, **kwargs):
    pass

def toggle_debit_credit_if_negative(*args, **kwargs):
    pass

def save_entries(*args, **kwargs):
    pass

def make_entry(*args, **kwargs):
    pass

def validate_cwip_accounts(*args, **kwargs):
    pass

def process_debit_credit_difference(*args, **kwargs):
    pass

def get_debit_credit_difference(*args, **kwargs):
    pass

def get_debit_credit_allowance(*args, **kwargs):
    pass

def raise_debit_credit_not_equal_error(*args, **kwargs):
    pass

def has_opening_entries(*args, **kwargs):
    pass

def make_round_off_gle(*args, **kwargs):
    pass

def update_accounting_dimensions(*args, **kwargs):
    pass

def get_round_off_account_and_cost_center(*args, **kwargs):
    pass

def make_reverse_gl_entries(*args, **kwargs):
    pass

def check_freezing_date(*args, **kwargs):
    pass

def validate_against_pcv(*args, **kwargs):
    pass

def set_as_cancel(*args, **kwargs):
    pass

def validate_allowed_dimensions(*args, **kwargs):
    pass


# Migrated from accounts/utils.py
def get_fiscal_year(*args, **kwargs):
    pass

def get_fiscal_years(*args, **kwargs):
    pass

def _get_fiscal_years(*args, **kwargs):
    pass

def get_fiscal_year_filter_field(*args, **kwargs):
    pass

def validate_fiscal_year(*args, **kwargs):
    pass

def get_balance_on(*args, **kwargs):
    pass

def get_count_on(*args, **kwargs):
    pass

def add_ac(*args, **kwargs):
    pass

def add_cc(*args, **kwargs):
    pass

def _build_dimensions_dict_for_exc_gain_loss(*args, **kwargs):
    pass

def reconcile_against_document(*args, **kwargs):
    pass

def check_if_advance_entry_modified(*args, **kwargs):
    pass

def validate_allocated_amount(*args, **kwargs):
    pass

def update_reference_in_journal_entry(*args, **kwargs):
    pass

def update_reference_in_payment_entry(*args, **kwargs):
    pass

def get_reconciliation_effect_date(*args, **kwargs):
    pass

def cancel_exchange_gain_loss_journal(*args, **kwargs):
    pass

def delete_exchange_gain_loss_journal(*args, **kwargs):
    pass

def get_linked_exchange_gain_loss_journal(*args, **kwargs):
    pass

def cancel_common_party_journal(*args, **kwargs):
    pass

def update_accounting_ledgers_after_reference_removal(*args, **kwargs):
    pass

def remove_ref_from_advance_section(*args, **kwargs):
    pass

def unlink_ref_doc_from_payment_entries(*args, **kwargs):
    pass

def remove_ref_doc_link_from_jv(*args, **kwargs):
    pass

def convert_to_list(*args, **kwargs):
    pass

def remove_ref_doc_link_from_pe(*args, **kwargs):
    pass

def get_company_default(*args, **kwargs):
    pass

def fix_total_debit_credit(*args, **kwargs):
    pass

def get_currency_precision(*args, **kwargs):
    pass

def get_fraction_units(*args, **kwargs):
    pass

def get_zero_cutoff(*args, **kwargs):
    pass

def get_held_invoices(*args, **kwargs):
    pass

def get_outstanding_invoices(*args, **kwargs):
    pass

def get_account_name(*args, **kwargs):
    pass

def get_companies(*args, **kwargs):
    pass

def get_children(*args, **kwargs):
    pass

def get_account_balances(*args, **kwargs):
    pass

def get_account_balances_coa(*args, **kwargs):
    pass

def create_payment_gateway_account(*args, **kwargs):
    pass

def update_cost_center(*args, **kwargs):
    pass

def validate_field_number(*args, **kwargs):
    pass

def get_autoname_with_number(*args, **kwargs):
    pass

def parse_naming_series_variable(*args, **kwargs):
    pass

def get_coa(*args, **kwargs):
    pass

def update_gl_entries_after(*args, **kwargs):
    pass

def repost_gle_for_stock_vouchers(*args, **kwargs):
    pass

def _delete_pl_entries(*args, **kwargs):
    pass

def _delete_adv_pl_entries(*args, **kwargs):
    pass

def _delete_gl_entries(*args, **kwargs):
    pass

def _delete_accounting_ledger_entries(*args, **kwargs):
    pass

def sort_stock_vouchers_by_posting_date(*args, **kwargs):
    pass

def get_future_stock_vouchers(*args, **kwargs):
    pass

def get_voucherwise_gl_entries(*args, **kwargs):
    pass

def compare_existing_and_expected_gle(*args, **kwargs):
    pass

def get_stock_accounts(*args, **kwargs):
    pass

def get_stock_and_account_balance(*args, **kwargs):
    pass

def get_journal_entry(*args, **kwargs):
    pass

def check_and_delete_linked_reports(*args, **kwargs):
    pass

def create_err_and_its_journals(*args, **kwargs):
    pass

def _auto_create_exchange_rate_revaluation_for(*args, **kwargs):
    pass

def auto_create_exchange_rate_revaluation_daily(*args, **kwargs):
    pass

def auto_create_exchange_rate_revaluation_weekly(*args, **kwargs):
    pass

def auto_create_exchange_rate_revaluation_monthly(*args, **kwargs):
    pass

def get_payment_ledger_entries(*args, **kwargs):
    pass

def get_account_type(*args, **kwargs):
    pass

def get_advance_ledger_entry(*args, **kwargs):
    pass

def create_payment_ledger_entry(*args, **kwargs):
    pass

def update_voucher_outstanding(*args, **kwargs):
    pass

def delink_original_entry(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def reset(*args, **kwargs):
    pass

def query_for_outstanding(*args, **kwargs):
    pass

def get_voucher_outstandings(*args, **kwargs):
    pass

def create_gain_loss_journal(*args, **kwargs):
    pass

def get_party_types_from_account_type(*args, **kwargs):
    pass

def get_advance_payment_doctypes(*args, **kwargs):
    pass

def run_ledger_health_checks(*args, **kwargs):
    pass

def sync_auto_reconcile_config(*args, **kwargs):
    pass

def get_link_fields_grouped_by_option(*args, **kwargs):
    pass

def build_qb_match_conditions(*args, **kwargs):
    pass

def is_immutable_ledger_enabled(*args, **kwargs):
    pass

def pre_submit_validation(*args, **kwargs):
    pass

def _run_pre_submit_checks(*args, **kwargs):
    pass

def _check_prev_docstatus(*args, **kwargs):
    pass

def _check_credit_limit_warn(*args, **kwargs):
    pass

def _check_packed_qty_warn(*args, **kwargs):
    pass


# Migrated from accounts/party.py
def get_party_details(*args, **kwargs):
    pass

def _get_party_details(*args, **kwargs):
    pass

def set_address_details(*args, **kwargs):
    pass

def get_regional_address_details(*args, **kwargs):
    pass

def complete_contact_details(*args, **kwargs):
    pass

def set_contact_details(*args, **kwargs):
    pass

def set_other_values(*args, **kwargs):
    pass

def get_default_price_list(*args, **kwargs):
    pass

def set_price_list(*args, **kwargs):
    pass

def set_account_and_due_date(*args, **kwargs):
    pass

def get_party_account(*args, **kwargs):
    pass

def get_party_advance_account(*args, **kwargs):
    pass

def get_party_bank_account(*args, **kwargs):
    pass

def get_party_account_currency(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def get_party_gle_currency(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def get_party_gle_account(*args, **kwargs):
    pass

def generator(*args, **kwargs):
    pass

def validate_party_gle_currency(*args, **kwargs):
    pass

def validate_party_accounts(*args, **kwargs):
    pass

def get_due_date(*args, **kwargs):
    pass

def get_due_date_from_template(*args, **kwargs):
    pass

def validate_due_date(*args, **kwargs):
    pass

def validate_due_date_with_template(*args, **kwargs):
    pass

def get_address_tax_category(*args, **kwargs):
    pass

def set_taxes(*args, **kwargs):
    pass

def get_payment_terms_template(*args, **kwargs):
    pass

def validate_party_frozen_disabled(*args, **kwargs):
    pass

def validate_account_party_type(*args, **kwargs):
    pass

def get_dashboard_info(*args, **kwargs):
    pass

def get_party_shipping_address(*args, **kwargs):
    pass

def get_partywise_advanced_payment_amount(*args, **kwargs):
    pass

def get_default_contact(*args, **kwargs):
    pass

def add_party_account(*args, **kwargs):
    pass

def render_address(*args, **kwargs):
    pass

def validate_party_currency_before_merging(*args, **kwargs):
    pass


# Migrated from accounts/deferred_revenue.py
def validate_service_stop_date(*args, **kwargs):
    pass

def build_conditions(*args, **kwargs):
    pass

def convert_deferred_expense_to_expense(*args, **kwargs):
    pass

def convert_deferred_revenue_to_income(*args, **kwargs):
    pass

def get_booking_dates(*args, **kwargs):
    pass

def calculate_monthly_amount(*args, **kwargs):
    pass

def calculate_amount(*args, **kwargs):
    pass

def get_already_booked_amount(*args, **kwargs):
    pass

def book_deferred_income_or_expense(*args, **kwargs):
    pass

def _book_deferred_revenue_or_expense(*args, **kwargs):
    pass

def process_deferred_accounting(*args, **kwargs):
    pass

def make_gl_entries(*args, **kwargs):
    pass

def send_mail(*args, **kwargs):
    pass

def book_revenue_via_journal_entry(*args, **kwargs):
    pass

def get_deferred_booking_accounts(*args, **kwargs):
    pass


# Migrated from accounts/test/test_reports.py
def test_execute_all_accounts_reports(*args, **kwargs):
    pass


# Migrated from accounts/test/test_utils.py
def test_get_party_shipping_address(*args, **kwargs):
    pass

def test_get_party_shipping_address2(*args, **kwargs):
    pass

def test_get_voucher_wise_gl_entry(*args, **kwargs):
    pass

def test_stock_voucher_sorting(*args, **kwargs):
    pass

def test_update_reference_in_payment_entry(*args, **kwargs):
    pass

def test_naming_series_variable_parsing(*args, **kwargs):
    pass

def test_get_zero_cutoff(*args, **kwargs):
    pass


# Migrated from accounts/test/test_pre_submit_validation.py
def _get_orange_warnings(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def _make_si(*args, **kwargs):
    pass

def test_warns_when_amount_exceeds_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_amount_within_credit_limit(*args, **kwargs):
    pass

def test_no_warning_for_return_invoices(*args, **kwargs):
    pass

def test_no_warning_when_customer_has_no_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_all_items_linked_to_so_or_dn(*args, **kwargs):
    pass

def _make_so(*args, **kwargs):
    pass

def test_warns_on_first_save_when_limit_exceeded(*args, **kwargs):
    pass

def test_warns_when_amount_exceeds_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_amount_within_credit_limit(*args, **kwargs):
    pass

def test_no_warning_when_bypass_is_set(*args, **kwargs):
    pass

def _make_dn(*args, **kwargs):
    pass

def test_bypass_false_warns_for_existing_draft(*args, **kwargs):
    pass

def test_bypass_false_no_warning_when_under_limit(*args, **kwargs):
    pass

def test_bypass_false_no_warning_when_all_items_linked_to_so(*args, **kwargs):
    pass

def test_bypass_false_partial_link_warns_proportionally(*args, **kwargs):
    pass

def test_bypass_true_warns_on_first_save_new_doc(*args, **kwargs):
    pass

def test_bypass_true_no_warning_when_all_items_billed(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def _make_dn(*args, **kwargs):
    pass

def test_no_warning_for_new_doc(*args, **kwargs):
    pass

def test_warns_when_packed_qty_mismatches(*args, **kwargs):
    pass

def test_no_warning_when_packed_qty_matches(*args, **kwargs):
    pass


# Migrated from accounts/test/accounts_mixin.py
def create_customer(*args, **kwargs):
    pass

def create_supplier(*args, **kwargs):
    pass

def create_item(*args, **kwargs):
    pass

def create_company(*args, **kwargs):
    pass

def enable_advance_as_liability(*args, **kwargs):
    pass

def disable_advance_as_liability(*args, **kwargs):
    pass

def identify_default_warehouses(*args, **kwargs):
    pass

def create_usd_receivable_account(*args, **kwargs):
    pass

def create_usd_payable_account(*args, **kwargs):
    pass

def clear_old_entries(*args, **kwargs):
    pass


# Migrated from accounts/notification/notification_for_new_fiscal_year/notification_for_new_fiscal_year.py
def get_context(*args, **kwargs):
    pass


# Migrated from accounts/custom/address.py
def validate(*args, **kwargs):
    pass

def link_address(*args, **kwargs):
    pass

def update_company_address(*args, **kwargs):
    pass

def validate_reference(*args, **kwargs):
    pass

def on_update(*args, **kwargs):
    pass

def get_shipping_address(*args, **kwargs):
    pass


# Migrated from accounts/dashboard_chart_source/account_balance_timeline/account_balance_timeline.py
def get(*args, **kwargs):
    pass

def build_result(*args, **kwargs):
    pass

def get_gl_entries(*args, **kwargs):
    pass

def get_dates_from_timegrain(*args, **kwargs):
    pass


# Migrated from accounts/report/financial_statements.py
def get_period_list(*args, **kwargs):
    pass

def get_fiscal_year_data(*args, **kwargs):
    pass

def validate_fiscal_year(*args, **kwargs):
    pass

def validate_dates(*args, **kwargs):
    pass

def get_months(*args, **kwargs):
    pass

def get_label(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_appropriate_currency(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def filter_out_zero_value_rows(*args, **kwargs):
    pass

def get_all_parents(*args, **kwargs):
    pass

def add_total_row(*args, **kwargs):
    pass

def get_accounts(*args, **kwargs):
    pass

def filter_accounts(*args, **kwargs):
    pass

def add_to_list(*args, **kwargs):
    pass

def sort_accounts(*args, **kwargs):
    pass

def compare_accounts(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass

def get_accounting_entries(*args, **kwargs):
    pass

def get_account_filter_query(*args, **kwargs):
    pass

def apply_additional_conditions(*args, **kwargs):
    pass

def get_cost_centers_with_children(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_filtered_list_for_consolidated_report(*args, **kwargs):
    pass

def compute_growth_view_data(*args, **kwargs):
    pass

def compute_margin_view_data(*args, **kwargs):
    pass


# Migrated from accounts/report/utils.py
def get_currency(*args, **kwargs):
    pass

def convert(*args, **kwargs):
    pass

def get_rate_as_at(*args, **kwargs):
    pass

def convert_to_presentation_currency(*args, **kwargs):
    pass

def get_appropriate_company(*args, **kwargs):
    pass

def get_invoiced_item_gross_margin(*args, **kwargs):
    pass

def get_query_columns(*args, **kwargs):
    pass

def get_values_for_columns(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def get_taxes_query(*args, **kwargs):
    pass

def get_journal_entries(*args, **kwargs):
    pass

def get_payment_entries(*args, **kwargs):
    pass

def apply_common_conditions(*args, **kwargs):
    pass

def get_advance_taxes_and_charges(*args, **kwargs):
    pass

def filter_invoices_based_on_dimensions(*args, **kwargs):
    pass

def get_opening_row(*args, **kwargs):
    pass


# Migrated from accounts/report/non_billed_report.py
def get_ordered_to_be_billed_data(*args, **kwargs):
    pass

def get_project_field(*args, **kwargs):
    pass


# Migrated from accounts/report/gross_profit/test_gross_profit.py
def setUp(*args, **kwargs):
    pass

def create_company(*args, **kwargs):
    pass

def create_item(*args, **kwargs):
    pass

def create_bundle(*args, **kwargs):
    pass

def create_customer(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_delivery_note(*args, **kwargs):
    pass

def clear_old_entries(*args, **kwargs):
    pass

def test_invoice_without_only_delivery_note(*args, **kwargs):
    pass

def test_bundled_delivery_note_with_different_warehouses(*args, **kwargs):
    pass

def test_order_connected_dn_and_inv(*args, **kwargs):
    pass

def test_crnote_against_invoice_with_multiple_instances_of_same_item(*args, **kwargs):
    pass

def test_standalone_cr_notes(*args, **kwargs):
    pass

def test_different_rates_in_si_and_dn(*args, **kwargs):
    pass

def test_valuation_rate_without_previous_sle(*args, **kwargs):
    pass

def test_gross_profit_groupby_invoices(*args, **kwargs):
    pass

def test_profit_for_later_period_return(*args, **kwargs):
    pass

def test_sales_person_wise_gross_profit(*args, **kwargs):
    pass

def test_drop_ship(*args, **kwargs):
    pass

def make_sales_person(*args, **kwargs):
    pass


# Migrated from accounts/report/gross_profit/gross_profit.py
def execute(*args, **kwargs):
    pass

def get_data_when_grouped_by_invoice(*args, **kwargs):
    pass

def get_data_when_not_grouped_by_invoice(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_column_names(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def process(*args, **kwargs):
    pass

def update_return_invoices(*args, **kwargs):
    pass

def get_average_rate_based_on_group_by(*args, **kwargs):
    pass

def set_average_based_on_payment_term_portion(*args, **kwargs):
    pass

def is_not_invoice_row(*args, **kwargs):
    pass

def set_average_rate(*args, **kwargs):
    pass

def set_average_gross_profit(*args, **kwargs):
    pass

def get_returned_invoice_items(*args, **kwargs):
    pass

def skip_row(*args, **kwargs):
    pass

def get_buying_amount_from_product_bundle(*args, **kwargs):
    pass

def calculate_buying_amount_from_sle(*args, **kwargs):
    pass

def get_buying_amount(*args, **kwargs):
    pass

def get_buying_amount_from_so_dn(*args, **kwargs):
    pass

def get_average_buying_rate(*args, **kwargs):
    pass

def get_last_purchase_rate(*args, **kwargs):
    pass

def load_invoice_items(*args, **kwargs):
    pass

def prepare_invoice_query(*args, **kwargs):
    pass

def apply_common_filters(*args, **kwargs):
    pass

def prepare_vouchers_to_ignore(*args, **kwargs):
    pass

def get_delivery_notes(*args, **kwargs):
    pass

def group_items_by_invoice(*args, **kwargs):
    pass

def get_invoice_row(*args, **kwargs):
    pass

def get_bundle_item_row(*args, **kwargs):
    pass

def get_stock_ledger_entries(*args, **kwargs):
    pass

def load_product_bundle(*args, **kwargs):
    pass

def load_non_stock_items(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable/test_accounts_receivable.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_payment_entry(*args, **kwargs):
    pass

def create_credit_note(*args, **kwargs):
    pass

def test_pos_receivable(*args, **kwargs):
    pass

def test_accounts_receivable_with_payment(*args, **kwargs):
    pass

def test_accounts_receivable_without_payment(*args, **kwargs):
    pass

def test_allow_multi_currency_invoices_against_single_party_account(*args, **kwargs):
    pass

def test_accounts_receivable_with_partial_payment(*args, **kwargs):
    pass

def test_cr_note_flag_to_update_self(*args, **kwargs):
    pass

def test_payment_againt_po_in_receivable_report(*args, **kwargs):
    pass

def test_exchange_revaluation_for_party(*args, **kwargs):
    pass

def test_payment_against_credit_note(*args, **kwargs):
    pass

def test_group_by_party(*args, **kwargs):
    pass

def test_future_payments(*args, **kwargs):
    pass

def test_sales_person(*args, **kwargs):
    pass

def test_cost_center_filter(*args, **kwargs):
    pass

def test_customer_group_filter(*args, **kwargs):
    pass

def test_multi_customer_group_filter(*args, **kwargs):
    pass

def test_party_account_filter(*args, **kwargs):
    pass

def test_usd_customer_filter(*args, **kwargs):
    pass

def test_multi_select_party_filter(*args, **kwargs):
    pass

def test_report_output_if_party_is_missing(*args, **kwargs):
    pass

def test_future_payments_on_foreign_currency(*args, **kwargs):
    pass

def test_accounts_receivable_output_for_minor_outstanding(*args, **kwargs):
    pass

def test_cost_center_on_report_output(*args, **kwargs):
    pass

def test_payment_terms_template_filters(*args, **kwargs):
    pass

def test_project_filter(*args, **kwargs):
    pass

def test_project_on_report_output(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable/accounts_receivable.py
def execute(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def set_defaults(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def fetch_ple_in_buffered_cursor(*args, **kwargs):
    pass

def fetch_ple_in_unbuffered_cursor(*args, **kwargs):
    pass

def build_voucher_dict(*args, **kwargs):
    pass

def init_voucher_balance(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def init_subtotal_row(*args, **kwargs):
    pass

def get_currency_fields(*args, **kwargs):
    pass

def get_voucher_balance(*args, **kwargs):
    pass

def update_voucher_balance(*args, **kwargs):
    pass

def update_sub_total_row(*args, **kwargs):
    pass

def append_subtotal_row(*args, **kwargs):
    pass

def build_data(*args, **kwargs):
    pass

def append_row(*args, **kwargs):
    pass

def set_invoice_details(*args, **kwargs):
    pass

def set_delivery_notes(*args, **kwargs):
    pass

def build_delivery_note_map(*args, **kwargs):
    pass

def get_invoice_details(*args, **kwargs):
    pass

def set_party_details(*args, **kwargs):
    pass

def allocate_outstanding_based_on_payment_terms(*args, **kwargs):
    pass

def get_payment_terms(*args, **kwargs):
    pass

def append_payment_term(*args, **kwargs):
    pass

def allocate_closing_to_term(*args, **kwargs):
    pass

def allocate_extra_payments_or_credits(*args, **kwargs):
    pass

def get_future_payments(*args, **kwargs):
    pass

def get_future_payments_from_payment_entry(*args, **kwargs):
    pass

def get_future_payments_from_journal_entry(*args, **kwargs):
    pass

def allocate_future_payments(*args, **kwargs):
    pass

def get_return_entries(*args, **kwargs):
    pass

def set_ageing(*args, **kwargs):
    pass

def get_ageing_data(*args, **kwargs):
    pass

def prepare_ple_query(*args, **kwargs):
    pass

def get_sales_invoices_or_customers_based_on_sales_person(*args, **kwargs):
    pass

def prepare_conditions(*args, **kwargs):
    pass

def get_cost_center_conditions(*args, **kwargs):
    pass

def add_common_filters(*args, **kwargs):
    pass

def add_customer_filters(*args, **kwargs):
    pass

def exclude_employee_transaction(*args, **kwargs):
    pass

def add_supplier_filters(*args, **kwargs):
    pass

def add_payment_term_template_filters(*args, **kwargs):
    pass

def get_hierarchical_filters(*args, **kwargs):
    pass

def add_accounting_dimensions_filters(*args, **kwargs):
    pass

def is_invoice(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def add_column(*args, **kwargs):
    pass

def setup_ageing_columns(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass

def get_exchange_rate_revaluations(*args, **kwargs):
    pass

def get_party_group_with_children(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_sales_register/item_wise_sales_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_income_account(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def apply_conditions(*args, **kwargs):
    pass

def apply_order_by_conditions(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def get_delivery_notes_against_sales_order(*args, **kwargs):
    pass

def get_grand_total(*args, **kwargs):
    pass

def get_tax_accounts(*args, **kwargs):
    pass

def get_tax_details_query(*args, **kwargs):
    pass

def add_total_row(*args, **kwargs):
    pass

def get_display_value(*args, **kwargs):
    pass

def get_group_by_and_display_fields(*args, **kwargs):
    pass

def add_sub_total_row(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_sales_register/test_item_wise_sales_register.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def test_basic_report_output(*args, **kwargs):
    pass

def test_grouped_report_handles_different_tax_descriptions(*args, **kwargs):
    pass


# Migrated from accounts/report/inactive_sales_items/inactive_sales_items.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_sales_details(*args, **kwargs):
    pass

def get_territories(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass


# Migrated from accounts/report/billed_items_to_be_received/billed_items_to_be_received.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_report_filters(*args, **kwargs):
    pass

def get_report_fields(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_payment_summary/sales_payment_summary.py
def execute(*args, **kwargs):
    pass

def get_pos_columns(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_pos_sales_payment_data(*args, **kwargs):
    pass

def get_sales_payment_data(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_pos_invoice_data(*args, **kwargs):
    pass

def get_sales_invoice_data(*args, **kwargs):
    pass

def get_mode_of_payments(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def get_mode_of_payment_details(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_payment_summary/test_sales_payment_summary.py
def test_get_mode_of_payments(*args, **kwargs):
    pass

def test_get_mode_of_payments_details(*args, **kwargs):
    pass

def get_filters(*args, **kwargs):
    pass

def create_sales_invoice_record(*args, **kwargs):
    pass


# Migrated from accounts/report/voucher_wise_balance/voucher_wise_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def apply_filters(*args, **kwargs):
    pass


# Migrated from accounts/report/general_and_payment_ledger_comparison/general_and_payment_ledger_comparison.py
def __init__(*args, **kwargs):
    pass

def get_accounts(*args, **kwargs):
    pass

def generate_filters(*args, **kwargs):
    pass

def get_gle(*args, **kwargs):
    pass

def get_ple(*args, **kwargs):
    pass

def compare(*args, **kwargs):
    pass

def generate_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/general_and_payment_ledger_comparison/test_general_and_payment_ledger_comparison.py
def setUp(*args, **kwargs):
    pass

def cleanup(*args, **kwargs):
    pass

def test_01_basic_report_functionality(*args, **kwargs):
    pass


# Migrated from accounts/report/share_ledger/share_ledger.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_all_transfers(*args, **kwargs):
    pass


# Migrated from accounts/report/supplier_ledger_summary/supplier_ledger_summary.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/supplier_ledger_summary/test_supplier_ledger_summary.py
def setUp(*args, **kwargs):
    pass

def create_purchase_invoice(*args, **kwargs):
    pass

def test_basic_supplier_ledger_summary(*args, **kwargs):
    pass

def test_supplier_ledger_summary_with_filters(*args, **kwargs):
    pass


# Migrated from accounts/report/share_balance/share_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_all_shares(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_purchase_register/item_wise_purchase_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def apply_conditions(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def get_aii_accounts(*args, **kwargs):
    pass

def get_purchase_receipts_against_purchase_order(*args, **kwargs):
    pass


# Migrated from accounts/report/item_wise_purchase_register/test_item_wise_purchase_register.py
def setUp(*args, **kwargs):
    pass

def create_purchase_invoice(*args, **kwargs):
    pass

def test_basic_report_output(*args, **kwargs):
    pass


# Migrated from accounts/report/budget_variance_report/budget_variance_report.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_budget_records(*args, **kwargs):
    pass

def build_budget_map(*args, **kwargs):
    pass

def get_actual_transactions(*args, **kwargs):
    pass

def get_budget_distributions(*args, **kwargs):
    pass

def get_months_in_range(*args, **kwargs):
    pass

def build_report_data(*args, **kwargs):
    pass

def get_periods(*args, **kwargs):
    pass

def get_months_between(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_fiscal_years(*args, **kwargs):
    pass

def get_budget_dimensions(*args, **kwargs):
    pass

def validate_budget_dimensions(*args, **kwargs):
    pass

def build_comparison_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/balance_sheet/balance_sheet.py
def execute(*args, **kwargs):
    pass

def get_provisional_profit_loss(*args, **kwargs):
    pass

def check_opening_balance(*args, **kwargs):
    pass

def get_report_summary(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/balance_sheet/test_balance_sheet.py
def test_balance_sheet(*args, **kwargs):
    pass

def make_journal_entry(*args, **kwargs):
    pass

def create_account(*args, **kwargs):
    pass


# Migrated from accounts/report/trial_balance/test_trial_balance.py
def setUp(*args, **kwargs):
    pass

def test_offsetting_entries_for_accounting_dimensions(*args, **kwargs):
    pass


# Migrated from accounts/report/trial_balance/trial_balance.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_opening_balances(*args, **kwargs):
    pass

def get_rootwise_opening_balances(*args, **kwargs):
    pass

def get_opening_balance(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def calculate_total_row(*args, **kwargs):
    pass

def sum_value_fields(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def prepare_opening_closing(*args, **kwargs):
    pass

def hide_group_accounts(*args, **kwargs):
    pass


# Migrated from accounts/report/payment_ledger/payment_ledger.py
def __init__(*args, **kwargs):
    pass

def init_voucher_dict(*args, **kwargs):
    pass

def build_data(*args, **kwargs):
    pass

def build_conditions(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/payment_ledger/test_payment_ledger.py
def setUp(*args, **kwargs):
    pass

def cleanup(*args, **kwargs):
    pass

def create_company(*args, **kwargs):
    pass

def test_unpaid_invoice_outstanding(*args, **kwargs):
    pass


# Migrated from accounts/report/consolidated_financial_statement/consolidated_financial_statement.py
def execute(*args, **kwargs):
    pass

def get_balance_sheet_data(*args, **kwargs):
    pass

def prepare_companywise_opening_balance(*args, **kwargs):
    pass

def get_opening_balance(*args, **kwargs):
    pass

def get_root_account_name(*args, **kwargs):
    pass

def get_profit_loss_data(*args, **kwargs):
    pass

def get_income_expense_data(*args, **kwargs):
    pass

def get_cash_flow_data(*args, **kwargs):
    pass

def get_account_type_based_data(*args, **kwargs):
    pass

def get_company_columns(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_company_currency(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def get_account_heads(*args, **kwargs):
    pass

def update_parent_account_names(*args, **kwargs):
    pass

def get_companies(*args, **kwargs):
    pass

def get_subsidiary_companies(*args, **kwargs):
    pass

def get_accounts(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass

def get_account_details(*args, **kwargs):
    pass

def validate_entries(*args, **kwargs):
    pass

def get_additional_conditions(*args, **kwargs):
    pass

def add_total_row(*args, **kwargs):
    pass

def filter_accounts(*args, **kwargs):
    pass

def add_to_list(*args, **kwargs):
    pass


# Migrated from accounts/report/calculated_discount_mismatch/calculated_discount_mismatch.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_transactions_with_discount_percentage(*args, **kwargs):
    pass


# Migrated from accounts/report/dimension_wise_accounts_balance_report/dimension_wise_accounts_balance_report.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass

def format_gl_entries(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def get_condition(*args, **kwargs):
    pass

def get_dimensions(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/general_ledger/general_ledger.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def validate_party(*args, **kwargs):
    pass

def set_account_currency(*args, **kwargs):
    pass

def get_result(*args, **kwargs):
    pass

def get_gl_entries(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_party_name_map(*args, **kwargs):
    pass

def get_accounts_with_children(*args, **kwargs):
    pass

def set_bill_no(*args, **kwargs):
    pass

def get_translated_labels_for_totals(*args, **kwargs):
    pass

def wrap_in_quotes(*args, **kwargs):
    pass

def get_data_with_opening_closing(*args, **kwargs):
    pass

def add_total_to_data(*args, **kwargs):
    pass

def get_totals_dict(*args, **kwargs):
    pass

def get_group_by_field(*args, **kwargs):
    pass

def initialize_gle_map(*args, **kwargs):
    pass

def get_accountwise_gle(*args, **kwargs):
    pass

def update_value_in_dict(*args, **kwargs):
    pass

def get_account_type_map(*args, **kwargs):
    pass

def get_result_as_list(*args, **kwargs):
    pass

def get_supplier_invoice_details(*args, **kwargs):
    pass

def get_balance(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/general_ledger/test_general_ledger.py
def setUp(*args, **kwargs):
    pass

def clear_old_entries(*args, **kwargs):
    pass

def test_foreign_account_balance_after_exchange_rate_revaluation(*args, **kwargs):
    pass

def test_ignore_exchange_rate_journals_filter(*args, **kwargs):
    pass

def test_ignore_cr_dr_notes_filter(*args, **kwargs):
    pass


# Migrated from accounts/report/trial_balance_for_party/trial_balance_for_party.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_opening_balances(*args, **kwargs):
    pass

def get_balances_within_period(*args, **kwargs):
    pass

def toggle_debit_credit(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def is_party_name_visible(*args, **kwargs):
    pass


# Migrated from accounts/report/asset_depreciation_ledger/asset_depreciation_ledger.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_assets_details(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/invalid_ledger_entries/invalid_ledger_entries.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def identify_cancelled_vouchers(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def build_query_filters(*args, **kwargs):
    pass

def get_active_vouchers_for_period(*args, **kwargs):
    pass


# Migrated from accounts/report/asset_depreciations_and_balances/asset_depreciations_and_balances.py
def execute(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_group_by_asset_category_data(*args, **kwargs):
    pass

def get_asset_categories_for_grouped_by_category(*args, **kwargs):
    pass

def get_assets_for_grouped_by_category(*args, **kwargs):
    pass

def get_asset_value_adjustment_map_by_category(*args, **kwargs):
    pass

def get_group_by_asset_data(*args, **kwargs):
    pass

def get_asset_details_for_grouped_by_category(*args, **kwargs):
    pass

def get_assets_for_grouped_by_asset(*args, **kwargs):
    pass

def get_asset_value_adjustment_map(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/custom_financial_statement/custom_financial_statement.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/customer_ledger_summary/customer_ledger_summary.py
def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def update_hierarchical_filters(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def get_party_conditions(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_gl_entries(*args, **kwargs):
    pass

def prepare_conditions(*args, **kwargs):
    pass

def get_return_invoices(*args, **kwargs):
    pass

def get_party_adjustment_amounts(*args, **kwargs):
    pass

def get_children(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/customer_ledger_summary/test_customer_ledger_summary.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_payment_entry(*args, **kwargs):
    pass

def create_credit_note(*args, **kwargs):
    pass

def test_ledger_summary_basic_output(*args, **kwargs):
    pass

def test_summary_with_return_and_payment(*args, **kwargs):
    pass

def test_customer_ledger_ignore_cr_dr_filter(*args, **kwargs):
    pass

def test_journal_voucher_against_return_invoice(*args, **kwargs):
    pass


# Migrated from accounts/report/profitability_analysis/profitability_analysis.py
def execute(*args, **kwargs):
    pass

def get_accounts_data(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def calculate_values(*args, **kwargs):
    pass

def accumulate_values_into_parents(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def set_gl_entries_by_account(*args, **kwargs):
    pass


# Migrated from accounts/report/purchase_invoice_trends/purchase_invoice_trends.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/delivered_items_to_be_billed/delivered_items_to_be_billed.py
def execute(*args, **kwargs):
    pass

def get_column(*args, **kwargs):
    pass

def get_args(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable_summary/accounts_receivable_summary.py
def execute(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_party_total(*args, **kwargs):
    pass

def init_party_total(*args, **kwargs):
    pass

def set_party_details(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_gl_balance(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_receivable_summary/test_accounts_receivable_summary.py
def setUp(*args, **kwargs):
    pass

def test_01_receivable_summary_output(*args, **kwargs):
    pass

def test_02_various_filters_and_output(*args, **kwargs):
    pass


# Migrated from accounts/report/tax_withholding_details/tax_withholding_details.py
def __init__(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def build_rows(*args, **kwargs):
    pass

def get_entries_query(*args, **kwargs):
    pass

def fetch_party_details(*args, **kwargs):
    pass

def get_party_query(*args, **kwargs):
    pass

def fetch_additional_doc_info(*args, **kwargs):
    pass

def get_doc_info_query(*args, **kwargs):
    pass

def get_purchase_invoice_fields(*args, **kwargs):
    pass

def get_sales_invoice_fields(*args, **kwargs):
    pass

def get_payment_entry_fields(*args, **kwargs):
    pass

def get_journal_entry_fields(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/tax_withholding_details/test_tax_withholding_details.py
def setUp(*args, **kwargs):
    pass

def test_tax_withholding_for_customers(*args, **kwargs):
    pass

def test_single_account_for_multiple_categories(*args, **kwargs):
    pass

def test_date_filters_in_multiple_tax_withholding_rules(*args, **kwargs):
    pass

def check_expected_values(*args, **kwargs):
    pass

def create_tax_category(*args, **kwargs):
    pass

def create_tcs_payment_entry(*args, **kwargs):
    pass

def create_tcs_journal_entry(*args, **kwargs):
    pass


# Migrated from accounts/report/cash_flow/cash_flow.py
def execute(*args, **kwargs):
    pass

def get_cash_flow_accounts(*args, **kwargs):
    pass

def get_account_type_based_data(*args, **kwargs):
    pass

def get_account_type_based_gl_data(*args, **kwargs):
    pass

def get_start_date(*args, **kwargs):
    pass

def add_total_row_account(*args, **kwargs):
    pass

def show_opening_and_closing_balance(*args, **kwargs):
    pass

def get_opening_balance(*args, **kwargs):
    pass

def get_net_income(*args, **kwargs):
    pass

def get_opening_range_using_fiscal_year(*args, **kwargs):
    pass

def get_report_summary(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/payment_period_based_on_invoice_date/payment_period_based_on_invoice_date.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_invoice_posting_date_map(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_payable_summary/accounts_payable_summary.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/pos_register/pos_register.py
def execute(*args, **kwargs):
    pass

def get_pos_entries(*args, **kwargs):
    pass

def concat_mode_of_payments(*args, **kwargs):
    pass

def add_subtotal_row(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_group_by_field(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/deferred_revenue_and_expense/test_deferred_revenue_and_expense.py
def clear_old_entries(*args, **kwargs):
    pass

def setup_deferred_accounts_and_items(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def test_deferred_revenue(*args, **kwargs):
    pass

def test_deferred_expense(*args, **kwargs):
    pass

def test_zero_months(*args, **kwargs):
    pass

def test_zero_amount(*args, **kwargs):
    pass


# Migrated from accounts/report/deferred_revenue_and_expense/deferred_revenue_and_expense.py
def __init__(*args, **kwargs):
    pass

def report_data(*args, **kwargs):
    pass

def get_amount(*args, **kwargs):
    pass

def get_item_total(*args, **kwargs):
    pass

def calculate_amount(*args, **kwargs):
    pass

def calculate_monthly_amount(*args, **kwargs):
    pass

def calculate_days_amount(*args, **kwargs):
    pass

def make_dummy_gle(*args, **kwargs):
    pass

def simulate_future_posting(*args, **kwargs):
    pass

def calculate_item_revenue_expense_for_period(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def calculate_invoice_revenue_expense_for_period(*args, **kwargs):
    pass

def estimate_future(*args, **kwargs):
    pass

def report_data(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def get_period_list(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def estimate_future(*args, **kwargs):
    pass

def calculate_revenue_and_expense(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def generate_report_data(*args, **kwargs):
    pass

def prepare_chart(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/tds_computation_summary/tds_computation_summary.py
def validate_filters(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def group_rows(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_invoice_trends/sales_invoice_trends.py
def execute(*args, **kwargs):
    pass


# Migrated from accounts/report/profit_and_loss_statement/test_profit_and_loss_statement.py
def setUp(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def get_fiscal_year(*args, **kwargs):
    pass

def get_report_filters(*args, **kwargs):
    pass

def test_profit_and_loss_output_and_summary(*args, **kwargs):
    pass

def test_p_and_l_export(*args, **kwargs):
    pass

def test_accumulate_filter(*args, **kwargs):
    pass


# Migrated from accounts/report/profit_and_loss_statement/profit_and_loss_statement.py
def execute(*args, **kwargs):
    pass

def get_report_summary(*args, **kwargs):
    pass

def get_net_profit_loss(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from accounts/report/gross_and_net_profit_report/gross_and_net_profit_report.py
def execute(*args, **kwargs):
    pass

def get_revenue(*args, **kwargs):
    pass

def remove_parent_with_no_child(*args, **kwargs):
    pass

def adjust_account_totals(*args, **kwargs):
    pass

def set_total(*args, **kwargs):
    pass

def get_profit(*args, **kwargs):
    pass

def get_net_profit(*args, **kwargs):
    pass


# Migrated from accounts/report/financial_ratios/financial_ratios.py
def execute(*args, **kwargs):
    pass

def setup_filters(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_ratios_data(*args, **kwargs):
    pass

def get_gl_data(*args, **kwargs):
    pass

def add_liquidity_ratios(*args, **kwargs):
    pass

def add_solvency_ratios(*args, **kwargs):
    pass

def add_turnover_ratios(*args, **kwargs):
    pass

def update_balances(*args, **kwargs):
    pass

def avg_ratio_balance(*args, **kwargs):
    pass

def calculate_ratio(*args, **kwargs):
    pass


# Migrated from accounts/report/received_items_to_be_billed/received_items_to_be_billed.py
def execute(*args, **kwargs):
    pass

def get_column(*args, **kwargs):
    pass

def get_args(*args, **kwargs):
    pass


# Migrated from accounts/report/bank_clearance_summary/bank_clearance_summary.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_entries_for_bank_clearance_summary(*args, **kwargs):
    pass


# Migrated from accounts/report/consolidated_trial_balance/consolidated_trial_balance.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def validate_companies(*args, **kwargs):
    pass

def sort_companies(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_company_wise_tb_data(*args, **kwargs):
    pass

def prepare_companywise_tb_data(*args, **kwargs):
    pass

def calculate_foreign_currency_translation_reserve(*args, **kwargs):
    pass

def get_fctr_root_row_index(*args, **kwargs):
    pass

def consolidate_trial_balance_data(*args, **kwargs):
    pass

def get_reporting_currency(*args, **kwargs):
    pass

def consolidate_gle_data(*args, **kwargs):
    pass

def update_to_presentation_currency(*args, **kwargs):
    pass

def prepare_opening_closing_for_ctb(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/consolidated_trial_balance/test_consolidated_trial_balance.py
def setUp(*args, **kwargs):
    pass

def test_single_company_report(*args, **kwargs):
    pass

def test_child_company_report_with_same_default_currency_as_parent_company(*args, **kwargs):
    pass

def test_child_company_with_different_default_currency_from_parent_company(*args, **kwargs):
    pass

def create_journal_entry(*args, **kwargs):
    pass


# Migrated from accounts/report/cheques_and_deposits_incorrectly_cleared/cheques_and_deposits_incorrectly_cleared.py
def execute(*args, **kwargs):
    pass

def build_payment_entry_dict(*args, **kwargs):
    pass

def build_journal_entry_dict(*args, **kwargs):
    pass

def build_data(*args, **kwargs):
    pass

def get_amounts_not_reflected_in_system_for_bank_reconciliation_statement(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from accounts/report/account_balance/test_account_balance.py
def test_account_balance(*args, **kwargs):
    pass

def make_sales_invoice(*args, **kwargs):
    pass


# Migrated from accounts/report/account_balance/account_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass


# Migrated from accounts/report/bank_reconciliation_statement/bank_reconciliation_statement.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_entries_for_bank_reconciliation_statement(*args, **kwargs):
    pass

def get_journal_entries(*args, **kwargs):
    pass

def get_payment_entries(*args, **kwargs):
    pass

def get_purchase_invoices(*args, **kwargs):
    pass

def get_pos_entries(*args, **kwargs):
    pass

def get_amounts_not_reflected_in_system(*args, **kwargs):
    pass

def get_amounts_not_reflected_in_system_for_bank_reconciliation_statement(*args, **kwargs):
    pass

def get_balance_row(*args, **kwargs):
    pass


# Migrated from accounts/report/bank_reconciliation_statement/test_bank_reconciliation_statement.py
def test_loan_entries_in_bank_reco_statement(*args, **kwargs):
    pass


# Migrated from accounts/report/purchase_register/test_purchase_register.py
def test_purchase_register(*args, **kwargs):
    pass

def test_purchase_register_ignores_tax_rows_from_other_doctype(*args, **kwargs):
    pass

def test_purchase_register_ledger_view(*args, **kwargs):
    pass

def make_purchase_invoice(*args, **kwargs):
    pass

def create_purchase_invoice_with_taxes(*args, **kwargs):
    pass

def make_payment_entry(*args, **kwargs):
    pass


# Migrated from accounts/report/purchase_register/purchase_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_account_columns(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_payments(*args, **kwargs):
    pass

def get_invoice_expense_map(*args, **kwargs):
    pass

def get_internal_invoice_map(*args, **kwargs):
    pass

def get_invoice_tax_map(*args, **kwargs):
    pass

def get_invoice_po_pr_map(*args, **kwargs):
    pass

def get_account_details(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_register/sales_register.py
def execute(*args, **kwargs):
    pass

def _execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_account_columns(*args, **kwargs):
    pass

def get_invoices(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_payments(*args, **kwargs):
    pass

def get_invoice_income_map(*args, **kwargs):
    pass

def get_internal_invoice_map(*args, **kwargs):
    pass

def get_invoice_tax_map(*args, **kwargs):
    pass

def get_invoice_so_dn_map(*args, **kwargs):
    pass

def get_invoice_cc_wh_map(*args, **kwargs):
    pass

def get_mode_of_payments(*args, **kwargs):
    pass


# Migrated from accounts/report/sales_register/test_sales_register.py
def setUp(*args, **kwargs):
    pass

def create_child_cost_center(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def test_basic_report_output(*args, **kwargs):
    pass

def test_sales_register_ignores_tax_rows_from_other_doctype(*args, **kwargs):
    pass

def test_journal_with_cost_center_filter(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_payable/test_accounts_payable.py
def setUp(*args, **kwargs):
    pass

def test_accounts_payable_for_foreign_currency_supplier(*args, **kwargs):
    pass

def create_purchase_invoice(*args, **kwargs):
    pass

def test_payment_terms_template_filters(*args, **kwargs):
    pass

def test_project_filter(*args, **kwargs):
    pass

def test_project_on_report_output(*args, **kwargs):
    pass


# Migrated from accounts/report/accounts_payable/accounts_payable.py
def execute(*args, **kwargs):
    pass
