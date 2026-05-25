import { Link } from 'react-router-dom';
import './Dashboard.css';

const MODULES = [
  { icon: '🏦', label: 'Banking', desc: 'Banks, accounts & reconciliation', to: '/banking/banks', color: 'hsl(221,83%,60%)' },
  { icon: '📊', label: 'Accounting', desc: 'Chart of accounts, journal entries', to: '/accounting/chart', color: 'hsl(142,71%,45%)' },
  { icon: '🛒', label: 'Sales', desc: 'Quotations, orders & invoices', to: '/sales/customers', color: 'hsl(38,92%,50%)' },
  { icon: '📦', label: 'Purchase', desc: 'Suppliers, POs & receipts', to: '/purchase/suppliers', color: 'hsl(290,70%,60%)' },
  { icon: '🏭', label: 'Inventory', desc: 'Items, warehouses & stock', to: '/inventory/items', color: 'hsl(200,80%,50%)' },
  { icon: '⚙️', label: 'Manufacturing', desc: 'BOMs, work orders & production', to: '/manufacturing/bom', color: 'hsl(0,72%,58%)' },
  { icon: '👥', label: 'HR & Payroll', desc: 'Employees, leaves & payroll', to: '/hr/employees', color: 'hsl(170,70%,45%)' },
  { icon: '🤝', label: 'CRM', desc: 'Leads, opportunities & contacts', to: '/crm/leads', color: 'hsl(30,90%,55%)' },
  { icon: '📋', label: 'Projects', desc: 'Projects, tasks & timesheets', to: '/projects/list', color: 'hsl(250,70%,65%)' },
  { icon: '🏗️', label: 'Assets', desc: 'Asset tracking & depreciation', to: '/assets/list', color: 'hsl(15,80%,55%)' },
  { icon: '🎧', label: 'Support', desc: 'Issues & service levels', to: '/support/issues', color: 'hsl(195,85%,45%)' },
  { icon: '⚙️', label: 'Settings', desc: 'Company & system settings', to: '/settings', color: 'hsl(0,0%,55%)' },
];

export default function Dashboard() {
  return (
    <div className="dashboard">
      <div className="dashboard__header">
        <h1 className="dashboard__title">Welcome back, Admin 👋</h1>
        <p className="dashboard__subtitle">Here's an overview of your ERP modules</p>
      </div>
      <div className="dashboard__grid">
        {MODULES.map((m) => (
          <Link key={m.to} to={m.to} className="dashboard__card">
            <span className="dashboard__icon" style={{ background: m.color + '22', color: m.color }}>
              {m.icon}
            </span>
            <div>
              <h3 className="dashboard__card-title">{m.label}</h3>
              <p className="dashboard__card-desc">{m.desc}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
