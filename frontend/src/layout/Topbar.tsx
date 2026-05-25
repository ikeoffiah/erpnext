import { useLocation } from 'react-router-dom';
import './Topbar.css';

const TITLES: Record<string, string> = {
  '/': 'Dashboard',
  '/banking/banks': 'Banking — Banks',
  '/banking/accounts': 'Banking — Bank Accounts',
  '/banking/reconciliation': 'Banking — Reconciliation',
  '/banking/statement-import': 'Banking — Statement Import',
  '/accounting/chart': 'Accounting — Chart of Accounts',
  '/accounting/journal': 'Accounting — Journal Entries',
  '/accounting/payments': 'Accounting — Payment Entry',
  '/accounting/reports': 'Accounting — Financial Reports',
  '/sales/customers': 'Sales — Customers',
  '/sales/quotations': 'Sales — Quotations',
  '/sales/orders': 'Sales — Orders',
  '/sales/invoices': 'Sales — Invoices',
  '/sales/delivery-notes': 'Sales — Delivery Notes',
  '/purchase/suppliers': 'Purchase — Suppliers',
  '/purchase/orders': 'Purchase — Orders',
  '/purchase/invoices': 'Purchase — Invoices',
  '/purchase/receipts': 'Purchase — Receipts',
  '/inventory/items': 'Inventory — Items',
  '/inventory/warehouses': 'Inventory — Warehouses',
  '/inventory/ledger': 'Inventory — Stock Ledger',
  '/inventory/reports': 'Inventory — Reports',
  '/manufacturing/bom': 'Manufacturing — Bill of Materials',
  '/manufacturing/work-orders': 'Manufacturing — Work Orders',
  '/manufacturing/production': 'Manufacturing — Production Plan',
  '/hr/employees': 'HR — Employees',
  '/hr/attendance': 'HR — Attendance',
  '/hr/leaves': 'HR — Leave Management',
  '/hr/payroll': 'HR — Payroll',
  '/crm/leads': 'CRM — Leads',
  '/crm/opportunities': 'CRM — Opportunities',
  '/crm/contacts': 'CRM — Contacts',
  '/projects/list': 'Projects — Project List',
  '/projects/tasks': 'Projects — Tasks',
  '/projects/timesheets': 'Projects — Timesheets',
  '/assets/list': 'Assets — Asset List',
  '/assets/depreciation': 'Assets — Depreciation',
  '/support/issues': 'Support — Issues',
  '/support/sla': 'Support — Service Level Agreements',
  '/settings': 'Settings',
};

export default function Topbar() {
  const { pathname } = useLocation();
  const title = TITLES[pathname] ?? 'ERPNext';

  return (
    <header className="topbar">
      <span className="topbar__title">{title}</span>
      <div className="topbar__right">
        <span className="topbar__username">Admin</span>
        <div className="topbar__avatar">A</div>
      </div>
    </header>
  );
}
