import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';

interface SubLink { label: string; to: string; }
interface NavGroup {
  icon: string;
  label: string;
  subLinks?: SubLink[];
  to?: string;
}

const NAV: NavGroup[] = [
  { icon: '🏠', label: 'Dashboard', to: '/' },
  {
    icon: '🏦', label: 'Banking',
    subLinks: [
      { label: 'Banks', to: '/banking/banks' },
      { label: 'Bank Accounts', to: '/banking/accounts' },
      { label: 'Reconciliation', to: '/banking/reconciliation' },
      { label: 'Statement Import', to: '/banking/statement-import' },
    ],
  },
  {
    icon: '📊', label: 'Accounting',
    subLinks: [
      { label: 'Chart of Accounts', to: '/accounting/chart' },
      { label: 'Journal Entries', to: '/accounting/journal' },
      { label: 'Payment Entry', to: '/accounting/payments' },
      { label: 'Financial Reports', to: '/accounting/reports' },
    ],
  },
  {
    icon: '🛒', label: 'Sales',
    subLinks: [
      { label: 'Customers', to: '/sales/customers' },
      { label: 'Quotations', to: '/sales/quotations' },
      { label: 'Sales Orders', to: '/sales/orders' },
      { label: 'Sales Invoices', to: '/sales/invoices' },
      { label: 'Delivery Notes', to: '/sales/delivery-notes' },
    ],
  },
  {
    icon: '📦', label: 'Purchase',
    subLinks: [
      { label: 'Suppliers', to: '/purchase/suppliers' },
      { label: 'Purchase Orders', to: '/purchase/orders' },
      { label: 'Purchase Invoices', to: '/purchase/invoices' },
      { label: 'Purchase Receipts', to: '/purchase/receipts' },
    ],
  },
  {
    icon: '🏭', label: 'Inventory',
    subLinks: [
      { label: 'Items', to: '/inventory/items' },
      { label: 'Warehouses', to: '/inventory/warehouses' },
      { label: 'Stock Ledger', to: '/inventory/ledger' },
      { label: 'Stock Reports', to: '/inventory/reports' },
    ],
  },
  {
    icon: '⚙️', label: 'Manufacturing',
    subLinks: [
      { label: 'Bill of Materials', to: '/manufacturing/bom' },
      { label: 'Work Orders', to: '/manufacturing/work-orders' },
      { label: 'Production Plan', to: '/manufacturing/production' },
    ],
  },
  {
    icon: '👥', label: 'HR & Payroll',
    subLinks: [
      { label: 'Employees', to: '/hr/employees' },
      { label: 'Attendance', to: '/hr/attendance' },
      { label: 'Leave Management', to: '/hr/leaves' },
      { label: 'Payroll', to: '/hr/payroll' },
    ],
  },
  {
    icon: '🤝', label: 'CRM',
    subLinks: [
      { label: 'Leads', to: '/crm/leads' },
      { label: 'Opportunities', to: '/crm/opportunities' },
      { label: 'Contacts', to: '/crm/contacts' },
    ],
  },
  {
    icon: '📋', label: 'Projects',
    subLinks: [
      { label: 'Projects', to: '/projects/list' },
      { label: 'Tasks', to: '/projects/tasks' },
      { label: 'Timesheets', to: '/projects/timesheets' },
    ],
  },
  {
    icon: '🏗️', label: 'Assets',
    subLinks: [
      { label: 'Asset List', to: '/assets/list' },
      { label: 'Depreciation', to: '/assets/depreciation' },
    ],
  },
  {
    icon: '🎧', label: 'Support',
    subLinks: [
      { label: 'Issues', to: '/support/issues' },
      { label: 'Service Level', to: '/support/sla' },
    ],
  },
  { icon: '⚙️', label: 'Settings', to: '/settings' },
];

export default function Sidebar() {
  const [openGroups, setOpenGroups] = useState<string[]>(['Banking']);

  const toggleGroup = (label: string) => {
    setOpenGroups((prev) =>
      prev.includes(label) ? prev.filter((l) => l !== label) : [...prev, label]
    );
  };

  return (
    <aside className="sidebar">
      <div className="sidebar__brand">
        <div className="sidebar__logo">E</div>
        <span className="sidebar__brand-name">ERPNext</span>
      </div>

      <nav className="sidebar__nav">
        {NAV.map((item) => {
          if (item.to) {
            return (
              <NavLink
                key={item.label}
                to={item.to}
                end={item.to === '/'}
                className={({ isActive }) =>
                  `sidebar__link${isActive ? ' active' : ''}`
                }
              >
                <span className="sidebar__icon">{item.icon}</span>
                {item.label}
              </NavLink>
            );
          }

          const isOpen = openGroups.includes(item.label);
          return (
            <div key={item.label} className="sidebar__group">
              <button
                className={`sidebar__group-toggle${isOpen ? ' open' : ''}`}
                onClick={() => toggleGroup(item.label)}
              >
                <span className="sidebar__icon">{item.icon}</span>
                {item.label}
                <span className="sidebar__chevron">▶</span>
              </button>
              {isOpen && (
                <div className="sidebar__sub-links">
                  {item.subLinks!.map((sub) => (
                    <NavLink
                      key={sub.to}
                      to={sub.to}
                      className={({ isActive }) =>
                        `sidebar__sub-link${isActive ? ' active' : ''}`
                      }
                    >
                      {sub.label}
                    </NavLink>
                  ))}
                </div>
              )}
            </div>
          );
        })}
      </nav>
    </aside>
  );
}
