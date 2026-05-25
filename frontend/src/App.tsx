import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './layout/Layout';
import Dashboard from './pages/Dashboard';

// Banking
import BanksPage from './pages/banking/BanksPage';
import BankAccountsPage from './pages/banking/BankAccountsPage';
import ReconciliationPage from './pages/banking/ReconciliationPage';
import StatementImportPage from './pages/banking/StatementImportPage';

// Accounting
import ChartOfAccountsPage from './pages/accounting/ChartOfAccountsPage';
import JournalEntriesPage from './pages/accounting/JournalEntriesPage';
import PaymentsPage from './pages/accounting/PaymentsPage';
import FinancialReportsPage from './pages/accounting/FinancialReportsPage';

// Sales
import CustomersPage from './pages/sales/CustomersPage';
import QuotationsPage from './pages/sales/QuotationsPage';
import SalesOrdersPage from './pages/sales/SalesOrdersPage';
import SalesInvoicesPage from './pages/sales/SalesInvoicesPage';
import DeliveryNotesPage from './pages/sales/DeliveryNotesPage';

// Purchase
import SuppliersPage from './pages/purchase/SuppliersPage';
import PurchaseOrdersPage from './pages/purchase/PurchaseOrdersPage';
import PurchaseInvoicesPage from './pages/purchase/PurchaseInvoicesPage';
import PurchaseReceiptsPage from './pages/purchase/PurchaseReceiptsPage';

// Inventory
import ItemsPage from './pages/inventory/ItemsPage';
import WarehousesPage from './pages/inventory/WarehousesPage';
import StockLedgerPage from './pages/inventory/StockLedgerPage';
import StockReportsPage from './pages/inventory/StockReportsPage';

// Manufacturing
import BOMPage from './pages/manufacturing/BOMPage';
import WorkOrdersPage from './pages/manufacturing/WorkOrdersPage';
import ProductionPlanPage from './pages/manufacturing/ProductionPlanPage';

// HR
import EmployeesPage from './pages/hr/EmployeesPage';
import AttendancePage from './pages/hr/AttendancePage';
import LeavesPage from './pages/hr/LeavesPage';
import PayrollPage from './pages/hr/PayrollPage';

// CRM
import LeadsPage from './pages/crm/LeadsPage';
import OpportunitiesPage from './pages/crm/OpportunitiesPage';
import ContactsPage from './pages/crm/ContactsPage';

// Projects
import ProjectsListPage from './pages/projects/ProjectsListPage';
import TasksPage from './pages/projects/TasksPage';
import TimesheetsPage from './pages/projects/TimesheetsPage';

// Assets
import AssetListPage from './pages/assets/AssetListPage';
import DepreciationPage from './pages/assets/DepreciationPage';

// Support
import IssuesPage from './pages/support/IssuesPage';
import SLAPage from './pages/support/SLAPage';

// Settings
import SettingsPage from './pages/SettingsPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />

          {/* Banking */}
          <Route path="banking/banks" element={<BanksPage />} />
          <Route path="banking/accounts" element={<BankAccountsPage />} />
          <Route path="banking/reconciliation" element={<ReconciliationPage />} />
          <Route path="banking/statement-import" element={<StatementImportPage />} />

          {/* Accounting */}
          <Route path="accounting/chart" element={<ChartOfAccountsPage />} />
          <Route path="accounting/journal" element={<JournalEntriesPage />} />
          <Route path="accounting/payments" element={<PaymentsPage />} />
          <Route path="accounting/reports" element={<FinancialReportsPage />} />

          {/* Sales */}
          <Route path="sales/customers" element={<CustomersPage />} />
          <Route path="sales/quotations" element={<QuotationsPage />} />
          <Route path="sales/orders" element={<SalesOrdersPage />} />
          <Route path="sales/invoices" element={<SalesInvoicesPage />} />
          <Route path="sales/delivery-notes" element={<DeliveryNotesPage />} />

          {/* Purchase */}
          <Route path="purchase/suppliers" element={<SuppliersPage />} />
          <Route path="purchase/orders" element={<PurchaseOrdersPage />} />
          <Route path="purchase/invoices" element={<PurchaseInvoicesPage />} />
          <Route path="purchase/receipts" element={<PurchaseReceiptsPage />} />

          {/* Inventory */}
          <Route path="inventory/items" element={<ItemsPage />} />
          <Route path="inventory/warehouses" element={<WarehousesPage />} />
          <Route path="inventory/ledger" element={<StockLedgerPage />} />
          <Route path="inventory/reports" element={<StockReportsPage />} />

          {/* Manufacturing */}
          <Route path="manufacturing/bom" element={<BOMPage />} />
          <Route path="manufacturing/work-orders" element={<WorkOrdersPage />} />
          <Route path="manufacturing/production" element={<ProductionPlanPage />} />

          {/* HR */}
          <Route path="hr/employees" element={<EmployeesPage />} />
          <Route path="hr/attendance" element={<AttendancePage />} />
          <Route path="hr/leaves" element={<LeavesPage />} />
          <Route path="hr/payroll" element={<PayrollPage />} />

          {/* CRM */}
          <Route path="crm/leads" element={<LeadsPage />} />
          <Route path="crm/opportunities" element={<OpportunitiesPage />} />
          <Route path="crm/contacts" element={<ContactsPage />} />

          {/* Projects */}
          <Route path="projects/list" element={<ProjectsListPage />} />
          <Route path="projects/tasks" element={<TasksPage />} />
          <Route path="projects/timesheets" element={<TimesheetsPage />} />

          {/* Assets */}
          <Route path="assets/list" element={<AssetListPage />} />
          <Route path="assets/depreciation" element={<DepreciationPage />} />

          {/* Support */}
          <Route path="support/issues" element={<IssuesPage />} />
          <Route path="support/sla" element={<SLAPage />} />

          {/* Settings */}
          <Route path="settings" element={<SettingsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
