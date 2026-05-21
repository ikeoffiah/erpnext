
# Migrated from selling/page/point_of_sale/point_of_sale.py
def search_by_term(*args, **kwargs):
    pass

def __sort(*args, **kwargs):
    pass

def filter_result_items(*args, **kwargs):
    pass

def get_parent_item_group(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def search_for_serial_or_batch_or_barcode_number(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def add_search_fields_condition(*args, **kwargs):
    pass

def get_item_group_condition(*args, **kwargs):
    pass

def item_group_query(*args, **kwargs):
    pass

def check_opening_entry(*args, **kwargs):
    pass

def create_opening_voucher(*args, **kwargs):
    pass

def get_past_order_list(*args, **kwargs):
    pass

def set_customer_info(*args, **kwargs):
    pass

def get_pos_profile_data(*args, **kwargs):
    pass

def add_doctype_to_results(*args, **kwargs):
    pass

def order_results_by_posting_date(*args, **kwargs):
    pass

def get_invoice_filters(*args, **kwargs):
    pass

def get_customer_recent_transactions(*args, **kwargs):
    pass


# Migrated from selling/page/sales_funnel/sales_funnel.py
def validate_filters(*args, **kwargs):
    pass

def get_funnel_data(*args, **kwargs):
    pass

def get_opp_by_utm_source(*args, **kwargs):
    pass

def get_opp_by_utm_campaign(*args, **kwargs):
    pass

def get_opp_by_utm_medium(*args, **kwargs):
    pass

def get_opp_by(*args, **kwargs):
    pass

def get_pipeline_data(*args, **kwargs):
    pass


# Migrated from selling/report/customer_wise_item_price/customer_wise_item_price.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def fetch_item_prices(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_customer_details(*args, **kwargs):
    pass

def get_selling_items(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_transaction_summary/sales_partner_transaction_summary.py
def execute(*args, **kwargs):
    pass

def prepare_columns(*args, **kwargs):
    pass

def extend_report_query(*args, **kwargs):
    pass

def apply_filters(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_transaction_summary/test_sales_partner_transaction_summary.py
def setUp(*args, **kwargs):
    pass

def test_doctype_filters(*args, **kwargs):
    pass

def test_posting_date_column_label(*args, **kwargs):
    pass

def test_sales_order_sp_transaction_summary(*args, **kwargs):
    pass

def test_sales_invoice_sp_transaction_summary(*args, **kwargs):
    pass

def test_delivery_note_sp_transaction_summary(*args, **kwargs):
    pass

def test_pos_invoice_sp_transaction_summary(*args, **kwargs):
    pass

def assert_sales_partner_transaction_summary_report(*args, **kwargs):
    pass

def assert_7pc_commission(*args, **kwargs):
    pass

def assert_5pc_commission_with_multiple_items(*args, **kwargs):
    pass

def assert_doc_with_no_sp(*args, **kwargs):
    pass

def assert_doc_with_posting_date_out_of_range(*args, **kwargs):
    pass

def assert_doc_with_revoked_commission(*args, **kwargs):
    pass

def assert_doc_not_submitted(*args, **kwargs):
    pass

def assert_doc_cancelled(*args, **kwargs):
    pass

def assert_commission(*args, **kwargs):
    pass

def assert_returned_doc(*args, **kwargs):
    pass


# Migrated from selling/report/territory_wise_sales/territory_wise_sales.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_opportunities(*args, **kwargs):
    pass

def get_quotations(*args, **kwargs):
    pass

def get_sales_orders(*args, **kwargs):
    pass

def get_sales_invoice(*args, **kwargs):
    pass

def _get_total(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_target_variance_based_on_item_group/sales_person_target_variance_based_on_item_group.py
def execute(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_target_variance_based_on_item_group/test_sales_person_target_variance_based_on_item_group.py
def setUp(*args, **kwargs):
    pass

def test_achieved_target_and_variance(*args, **kwargs):
    pass

def create_target_distribution(*args, **kwargs):
    pass

def create_sales_target_doc(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_commission_summary/sales_partner_commission_summary.py
def execute(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def _set_date_field_and_label(*args, **kwargs):
    pass

def prepare_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def build_report_query(*args, **kwargs):
    pass

def _build_report_base_query(*args, **kwargs):
    pass

def extend_report_query(*args, **kwargs):
    pass

def _apply_common_filters(*args, **kwargs):
    pass

def apply_filters(*args, **kwargs):
    pass

def make_column(*args, **kwargs):
    pass

def prepare_columns(*args, **kwargs):
    pass

def extend_report_query(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_commission_summary/test_sales_partner_commission_summary.py
def assert_doctype_filters(*args, **kwargs):
    pass

def assert_posting_date_label(*args, **kwargs):
    pass

def create_transactions(*args, **kwargs):
    pass

def transaction_doc_with_7pc_commision(*args, **kwargs):
    pass

def transaction_doc_with_5pc_commission(*args, **kwargs):
    pass

def transaction_doc_with_no_sales_partner(*args, **kwargs):
    pass

def transaction_doc_date_out_of_range_of_filters(*args, **kwargs):
    pass

def transaction_doc_with_revoked_commission(*args, **kwargs):
    pass

def transaction_doc_not_submitted(*args, **kwargs):
    pass

def transaction_doc_cancelled(*args, **kwargs):
    pass

def transaction_doc_returned(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def test_doctype_filters(*args, **kwargs):
    pass

def test_posting_date_column_label(*args, **kwargs):
    pass

def test_sales_order_sp_commission_summary(*args, **kwargs):
    pass

def test_sales_invoice_sp_commission_summary(*args, **kwargs):
    pass

def test_delivery_note_sp_commission_summary(*args, **kwargs):
    pass

def test_pos_invoice_sp_commission_summary(*args, **kwargs):
    pass

def assert_sales_partner_commission_summary_report(*args, **kwargs):
    pass

def assert_7pc_commission(*args, **kwargs):
    pass

def assert_5pc_commission_with_multiple_items(*args, **kwargs):
    pass

def assert_doc_with_no_sp(*args, **kwargs):
    pass

def assert_doc_with_posting_date_out_of_range(*args, **kwargs):
    pass

def assert_doc_with_revoked_commission(*args, **kwargs):
    pass

def assert_doc_not_submitted(*args, **kwargs):
    pass

def assert_doc_cancelled(*args, **kwargs):
    pass

def assert_total_commission(*args, **kwargs):
    pass

def assert_returned_doc(*args, **kwargs):
    pass


# Migrated from selling/report/pending_so_items_for_purchase_request/test_pending_so_items_for_purchase_request.py
def test_result_for_partial_material_request(*args, **kwargs):
    pass

def test_result_for_so_item(*args, **kwargs):
    pass


# Migrated from selling/report/pending_so_items_for_purchase_request/pending_so_items_for_purchase_request.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_items_with_product_bundle(*args, **kwargs):
    pass

def get_packed_items(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_target_variance_based_on_item_group/sales_partner_target_variance_based_on_item_group.py
def execute(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_target_variance_based_on_item_group/item_group_wise_sales_target_variance.py
def get_data_column(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def get_item_group_parent_child_map(*args, **kwargs):
    pass

def get_actual_data(*args, **kwargs):
    pass

def get_parents_data(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_target_variance_based_on_item_group/test_sales_partner_target_variance_based_on_item_group.py
def setUp(*args, **kwargs):
    pass

def test_achieved_target_and_variance_for_partner(*args, **kwargs):
    pass


# Migrated from selling/report/sales_order_analysis/test_sales_order_analysis.py
def create_sales_order(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_delivery_note(*args, **kwargs):
    pass

def test_01_so_to_deliver_and_bill(*args, **kwargs):
    pass

def test_02_so_to_deliver(*args, **kwargs):
    pass

def test_03_so_to_bill(*args, **kwargs):
    pass

def test_04_so_completed(*args, **kwargs):
    pass

def test_05_all_so_status(*args, **kwargs):
    pass

def test_06_so_pending_delivery_with_multiple_delivery_notes(*args, **kwargs):
    pass

def test_07_so_delivered_with_multiple_delivery_notes(*args, **kwargs):
    pass


# Migrated from selling/report/sales_order_analysis/sales_order_analysis.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_so_elapsed_time(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def prepare_chart_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from selling/report/item_wise_sales_history/item_wise_sales_history.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_customer_details(*args, **kwargs):
    pass

def get_item_details(*args, **kwargs):
    pass

def get_sales_order_details(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/address_and_contacts/address_and_contacts.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_party_addresses_and_contact(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def add_blank_columns_for(*args, **kwargs):
    pass

def get_party_group(*args, **kwargs):
    pass

def should_add_party_name(*args, **kwargs):
    pass


# Migrated from selling/report/inactive_customers/inactive_customers.py
def execute(*args, **kwargs):
    pass

def get_sales_details(*args, **kwargs):
    pass

def get_last_sales_amt(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from selling/report/payment_terms_status_for_sales_order/test_payment_terms_status_for_sales_order.py
def create_payment_terms_template(*args, **kwargs):
    pass

def test_01_payment_terms_status(*args, **kwargs):
    pass

def create_exchange_rate(*args, **kwargs):
    pass

def test_02_alternate_currency(*args, **kwargs):
    pass

def test_03_group_filters(*args, **kwargs):
    pass

def test_04_due_date_filter(*args, **kwargs):
    pass


# Migrated from selling/report/payment_terms_status_for_sales_order/payment_terms_status_for_sales_order.py
def get_columns(*args, **kwargs):
    pass

def get_descendants_of(*args, **kwargs):
    pass

def get_customers_or_items(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def build_filter_criterions(*args, **kwargs):
    pass

def get_so_with_invoices(*args, **kwargs):
    pass

def set_payment_terms_statuses(*args, **kwargs):
    pass

def prepare_chart(*args, **kwargs):
    pass

def filter_on_calculated_status(*args, **kwargs):
    pass

def filter_for_immediate_upcoming_term(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from selling/report/customer_acquisition_and_loyalty/customer_acquisition_and_loyalty.py
def execute(*args, **kwargs):
    pass

def get_data_by_time(*args, **kwargs):
    pass

def get_data_by_territory(*args, **kwargs):
    pass

def get_customer_stats(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_wise_transaction_summary/sales_person_wise_transaction_summary.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def get_item_details(*args, **kwargs):
    pass


# Migrated from selling/report/sales_order_trends/sales_order_trends.py
def execute(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_commission_summary/sales_person_commission_summary.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass


# Migrated from selling/report/available_stock_for_packing_items/available_stock_for_packing_items.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_item_details(*args, **kwargs):
    pass

def get_item_warehouse_quantity_map(*args, **kwargs):
    pass


# Migrated from selling/report/customer_credit_balance/customer_credit_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_details(*args, **kwargs):
    pass


# Migrated from selling/report/quotation_trends/quotation_trends.py
def execute(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/lost_quotations/lost_quotations.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass


# Migrated from selling/report/sales_analytics/test_analytics.py
def test_sales_analytics(*args, **kwargs):
    pass

def compare_result_for_customer(*args, **kwargs):
    pass

def compare_result_for_customer_group(*args, **kwargs):
    pass

def compare_result_for_customer_based_on_quantity(*args, **kwargs):
    pass

def create_sales_orders(*args, **kwargs):
    pass


# Migrated from selling/report/sales_analytics/sales_analytics.py
def execute(*args, **kwargs):
    pass

def append_report(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def update_company_list_for_parent_company(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_sales_transactions_based_on_order_type(*args, **kwargs):
    pass

def get_sales_transactions_based_on_customers_or_suppliers(*args, **kwargs):
    pass

def get_sales_transactions_based_on_items(*args, **kwargs):
    pass

def get_sales_transactions_based_on_customer_or_territory_group(*args, **kwargs):
    pass

def get_sales_transactions_based_on_item_group(*args, **kwargs):
    pass

def get_sales_transactions_based_on_project(*args, **kwargs):
    pass

def get_rows(*args, **kwargs):
    pass

def get_rows_by_group(*args, **kwargs):
    pass

def get_periodic_data(*args, **kwargs):
    pass

def get_period(*args, **kwargs):
    pass

def get_period_date_ranges(*args, **kwargs):
    pass

def get_groups(*args, **kwargs):
    pass

def get_teams(*args, **kwargs):
    pass

def get_supplier_parent_child_map(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/territory_target_variance_based_on_item_group/territory_target_variance_based_on_item_group.py
def execute(*args, **kwargs):
    pass


# Migrated from selling/page/point_of_sale/point_of_sale.py
def search_by_term(*args, **kwargs):
    pass

def __sort(*args, **kwargs):
    pass

def filter_result_items(*args, **kwargs):
    pass

def get_parent_item_group(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def search_for_serial_or_batch_or_barcode_number(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def add_search_fields_condition(*args, **kwargs):
    pass

def get_item_group_condition(*args, **kwargs):
    pass

def item_group_query(*args, **kwargs):
    pass

def check_opening_entry(*args, **kwargs):
    pass

def create_opening_voucher(*args, **kwargs):
    pass

def get_past_order_list(*args, **kwargs):
    pass

def set_customer_info(*args, **kwargs):
    pass

def get_pos_profile_data(*args, **kwargs):
    pass

def add_doctype_to_results(*args, **kwargs):
    pass

def order_results_by_posting_date(*args, **kwargs):
    pass

def get_invoice_filters(*args, **kwargs):
    pass

def get_customer_recent_transactions(*args, **kwargs):
    pass


# Migrated from selling/page/sales_funnel/sales_funnel.py
def validate_filters(*args, **kwargs):
    pass

def get_funnel_data(*args, **kwargs):
    pass

def get_opp_by_utm_source(*args, **kwargs):
    pass

def get_opp_by_utm_campaign(*args, **kwargs):
    pass

def get_opp_by_utm_medium(*args, **kwargs):
    pass

def get_opp_by(*args, **kwargs):
    pass

def get_pipeline_data(*args, **kwargs):
    pass


# Migrated from selling/report/customer_wise_item_price/customer_wise_item_price.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def fetch_item_prices(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_customer_details(*args, **kwargs):
    pass

def get_selling_items(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_transaction_summary/sales_partner_transaction_summary.py
def execute(*args, **kwargs):
    pass

def prepare_columns(*args, **kwargs):
    pass

def extend_report_query(*args, **kwargs):
    pass

def apply_filters(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_transaction_summary/test_sales_partner_transaction_summary.py
def setUp(*args, **kwargs):
    pass

def test_doctype_filters(*args, **kwargs):
    pass

def test_posting_date_column_label(*args, **kwargs):
    pass

def test_sales_order_sp_transaction_summary(*args, **kwargs):
    pass

def test_sales_invoice_sp_transaction_summary(*args, **kwargs):
    pass

def test_delivery_note_sp_transaction_summary(*args, **kwargs):
    pass

def test_pos_invoice_sp_transaction_summary(*args, **kwargs):
    pass

def assert_sales_partner_transaction_summary_report(*args, **kwargs):
    pass

def assert_7pc_commission(*args, **kwargs):
    pass

def assert_5pc_commission_with_multiple_items(*args, **kwargs):
    pass

def assert_doc_with_no_sp(*args, **kwargs):
    pass

def assert_doc_with_posting_date_out_of_range(*args, **kwargs):
    pass

def assert_doc_with_revoked_commission(*args, **kwargs):
    pass

def assert_doc_not_submitted(*args, **kwargs):
    pass

def assert_doc_cancelled(*args, **kwargs):
    pass

def assert_commission(*args, **kwargs):
    pass

def assert_returned_doc(*args, **kwargs):
    pass


# Migrated from selling/report/territory_wise_sales/territory_wise_sales.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_opportunities(*args, **kwargs):
    pass

def get_quotations(*args, **kwargs):
    pass

def get_sales_orders(*args, **kwargs):
    pass

def get_sales_invoice(*args, **kwargs):
    pass

def _get_total(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_target_variance_based_on_item_group/sales_person_target_variance_based_on_item_group.py
def execute(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_target_variance_based_on_item_group/test_sales_person_target_variance_based_on_item_group.py
def setUp(*args, **kwargs):
    pass

def test_achieved_target_and_variance(*args, **kwargs):
    pass

def create_target_distribution(*args, **kwargs):
    pass

def create_sales_target_doc(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_commission_summary/sales_partner_commission_summary.py
def execute(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def _set_date_field_and_label(*args, **kwargs):
    pass

def prepare_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def build_report_query(*args, **kwargs):
    pass

def _build_report_base_query(*args, **kwargs):
    pass

def extend_report_query(*args, **kwargs):
    pass

def _apply_common_filters(*args, **kwargs):
    pass

def apply_filters(*args, **kwargs):
    pass

def make_column(*args, **kwargs):
    pass

def prepare_columns(*args, **kwargs):
    pass

def extend_report_query(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_commission_summary/test_sales_partner_commission_summary.py
def assert_doctype_filters(*args, **kwargs):
    pass

def assert_posting_date_label(*args, **kwargs):
    pass

def create_transactions(*args, **kwargs):
    pass

def transaction_doc_with_7pc_commision(*args, **kwargs):
    pass

def transaction_doc_with_5pc_commission(*args, **kwargs):
    pass

def transaction_doc_with_no_sales_partner(*args, **kwargs):
    pass

def transaction_doc_date_out_of_range_of_filters(*args, **kwargs):
    pass

def transaction_doc_with_revoked_commission(*args, **kwargs):
    pass

def transaction_doc_not_submitted(*args, **kwargs):
    pass

def transaction_doc_cancelled(*args, **kwargs):
    pass

def transaction_doc_returned(*args, **kwargs):
    pass

def setUp(*args, **kwargs):
    pass

def test_doctype_filters(*args, **kwargs):
    pass

def test_posting_date_column_label(*args, **kwargs):
    pass

def test_sales_order_sp_commission_summary(*args, **kwargs):
    pass

def test_sales_invoice_sp_commission_summary(*args, **kwargs):
    pass

def test_delivery_note_sp_commission_summary(*args, **kwargs):
    pass

def test_pos_invoice_sp_commission_summary(*args, **kwargs):
    pass

def assert_sales_partner_commission_summary_report(*args, **kwargs):
    pass

def assert_7pc_commission(*args, **kwargs):
    pass

def assert_5pc_commission_with_multiple_items(*args, **kwargs):
    pass

def assert_doc_with_no_sp(*args, **kwargs):
    pass

def assert_doc_with_posting_date_out_of_range(*args, **kwargs):
    pass

def assert_doc_with_revoked_commission(*args, **kwargs):
    pass

def assert_doc_not_submitted(*args, **kwargs):
    pass

def assert_doc_cancelled(*args, **kwargs):
    pass

def assert_total_commission(*args, **kwargs):
    pass

def assert_returned_doc(*args, **kwargs):
    pass


# Migrated from selling/report/pending_so_items_for_purchase_request/test_pending_so_items_for_purchase_request.py
def test_result_for_partial_material_request(*args, **kwargs):
    pass

def test_result_for_so_item(*args, **kwargs):
    pass


# Migrated from selling/report/pending_so_items_for_purchase_request/pending_so_items_for_purchase_request.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_items_with_product_bundle(*args, **kwargs):
    pass

def get_packed_items(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_target_variance_based_on_item_group/sales_partner_target_variance_based_on_item_group.py
def execute(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_target_variance_based_on_item_group/item_group_wise_sales_target_variance.py
def get_data_column(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def get_item_group_parent_child_map(*args, **kwargs):
    pass

def get_actual_data(*args, **kwargs):
    pass

def get_parents_data(*args, **kwargs):
    pass


# Migrated from selling/report/sales_partner_target_variance_based_on_item_group/test_sales_partner_target_variance_based_on_item_group.py
def setUp(*args, **kwargs):
    pass

def test_achieved_target_and_variance_for_partner(*args, **kwargs):
    pass


# Migrated from selling/report/sales_order_analysis/test_sales_order_analysis.py
def create_sales_order(*args, **kwargs):
    pass

def create_sales_invoice(*args, **kwargs):
    pass

def create_delivery_note(*args, **kwargs):
    pass

def test_01_so_to_deliver_and_bill(*args, **kwargs):
    pass

def test_02_so_to_deliver(*args, **kwargs):
    pass

def test_03_so_to_bill(*args, **kwargs):
    pass

def test_04_so_completed(*args, **kwargs):
    pass

def test_05_all_so_status(*args, **kwargs):
    pass

def test_06_so_pending_delivery_with_multiple_delivery_notes(*args, **kwargs):
    pass

def test_07_so_delivered_with_multiple_delivery_notes(*args, **kwargs):
    pass


# Migrated from selling/report/sales_order_analysis/sales_order_analysis.py
def execute(*args, **kwargs):
    pass

def validate_filters(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_so_elapsed_time(*args, **kwargs):
    pass

def prepare_data(*args, **kwargs):
    pass

def prepare_chart_data(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from selling/report/item_wise_sales_history/item_wise_sales_history.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_customer_details(*args, **kwargs):
    pass

def get_item_details(*args, **kwargs):
    pass

def get_sales_order_details(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/address_and_contacts/address_and_contacts.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_party_addresses_and_contact(*args, **kwargs):
    pass

def get_party_details(*args, **kwargs):
    pass

def add_blank_columns_for(*args, **kwargs):
    pass

def get_party_group(*args, **kwargs):
    pass

def should_add_party_name(*args, **kwargs):
    pass


# Migrated from selling/report/inactive_customers/inactive_customers.py
def execute(*args, **kwargs):
    pass

def get_sales_details(*args, **kwargs):
    pass

def get_last_sales_amt(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass


# Migrated from selling/report/payment_terms_status_for_sales_order/test_payment_terms_status_for_sales_order.py
def create_payment_terms_template(*args, **kwargs):
    pass

def test_01_payment_terms_status(*args, **kwargs):
    pass

def create_exchange_rate(*args, **kwargs):
    pass

def test_02_alternate_currency(*args, **kwargs):
    pass

def test_03_group_filters(*args, **kwargs):
    pass

def test_04_due_date_filter(*args, **kwargs):
    pass


# Migrated from selling/report/payment_terms_status_for_sales_order/payment_terms_status_for_sales_order.py
def get_columns(*args, **kwargs):
    pass

def get_descendants_of(*args, **kwargs):
    pass

def get_customers_or_items(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def build_filter_criterions(*args, **kwargs):
    pass

def get_so_with_invoices(*args, **kwargs):
    pass

def set_payment_terms_statuses(*args, **kwargs):
    pass

def prepare_chart(*args, **kwargs):
    pass

def filter_on_calculated_status(*args, **kwargs):
    pass

def filter_for_immediate_upcoming_term(*args, **kwargs):
    pass

def execute(*args, **kwargs):
    pass


# Migrated from selling/report/customer_acquisition_and_loyalty/customer_acquisition_and_loyalty.py
def execute(*args, **kwargs):
    pass

def get_data_by_time(*args, **kwargs):
    pass

def get_data_by_territory(*args, **kwargs):
    pass

def get_customer_stats(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_wise_transaction_summary/sales_person_wise_transaction_summary.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass

def get_items(*args, **kwargs):
    pass

def get_item_details(*args, **kwargs):
    pass


# Migrated from selling/report/sales_order_trends/sales_order_trends.py
def execute(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/sales_person_commission_summary/sales_person_commission_summary.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_entries(*args, **kwargs):
    pass

def get_conditions(*args, **kwargs):
    pass


# Migrated from selling/report/available_stock_for_packing_items/available_stock_for_packing_items.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_item_details(*args, **kwargs):
    pass

def get_item_warehouse_quantity_map(*args, **kwargs):
    pass


# Migrated from selling/report/customer_credit_balance/customer_credit_balance.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_details(*args, **kwargs):
    pass


# Migrated from selling/report/quotation_trends/quotation_trends.py
def execute(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/lost_quotations/lost_quotations.py
def execute(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass


# Migrated from selling/report/sales_analytics/test_analytics.py
def test_sales_analytics(*args, **kwargs):
    pass

def compare_result_for_customer(*args, **kwargs):
    pass

def compare_result_for_customer_group(*args, **kwargs):
    pass

def compare_result_for_customer_based_on_quantity(*args, **kwargs):
    pass

def create_sales_orders(*args, **kwargs):
    pass


# Migrated from selling/report/sales_analytics/sales_analytics.py
def execute(*args, **kwargs):
    pass

def append_report(*args, **kwargs):
    pass

def __init__(*args, **kwargs):
    pass

def update_company_list_for_parent_company(*args, **kwargs):
    pass

def run(*args, **kwargs):
    pass

def get_columns(*args, **kwargs):
    pass

def get_data(*args, **kwargs):
    pass

def get_sales_transactions_based_on_order_type(*args, **kwargs):
    pass

def get_sales_transactions_based_on_customers_or_suppliers(*args, **kwargs):
    pass

def get_sales_transactions_based_on_items(*args, **kwargs):
    pass

def get_sales_transactions_based_on_customer_or_territory_group(*args, **kwargs):
    pass

def get_sales_transactions_based_on_item_group(*args, **kwargs):
    pass

def get_sales_transactions_based_on_project(*args, **kwargs):
    pass

def get_rows(*args, **kwargs):
    pass

def get_rows_by_group(*args, **kwargs):
    pass

def get_periodic_data(*args, **kwargs):
    pass

def get_period(*args, **kwargs):
    pass

def get_period_date_ranges(*args, **kwargs):
    pass

def get_groups(*args, **kwargs):
    pass

def get_teams(*args, **kwargs):
    pass

def get_supplier_parent_child_map(*args, **kwargs):
    pass

def get_chart_data(*args, **kwargs):
    pass


# Migrated from selling/report/territory_target_variance_based_on_item_group/territory_target_variance_based_on_item_group.py
def execute(*args, **kwargs):
    pass
