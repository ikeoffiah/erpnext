from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from erp_core import views as erp_views

router = DefaultRouter()

# =====================================================================
# BATCH 1 ROUTERS
# =====================================================================

# Banking
router.register(r'bank', erp_views.BankViewSet, basename='bank')
router.register(r'bank-account', erp_views.BankAccountViewSet, basename='bankaccount')
router.register(r'bank-statement-import-log', erp_views.BankStatementImportLogViewSet, basename='bankstatementimportlog')

# CRM & Sales
router.register(r'customer', erp_views.CustomerViewSet, basename='customer')
router.register(r'lead', erp_views.LeadViewSet, basename='lead')
router.register(r'opportunity', erp_views.OpportunityViewSet, basename='opportunity')
router.register(r'quotation', erp_views.QuotationViewSet, basename='quotation')
router.register(r'sales-order', erp_views.SalesOrderViewSet, basename='salesorder')
router.register(r'sales-invoice', erp_views.SalesInvoiceViewSet, basename='salesinvoice')

# Purchase & Inventory
router.register(r'supplier', erp_views.SupplierViewSet, basename='supplier')
router.register(r'item', erp_views.ItemViewSet, basename='item')
router.register(r'purchase-order', erp_views.PurchaseOrderViewSet, basename='purchaseorder')
router.register(r'purchase-invoice', erp_views.PurchaseInvoiceViewSet, basename='purchaseinvoice')

# =====================================================================
# BATCH 2 ROUTERS
# =====================================================================

# HR & Payroll
router.register(r'employee', erp_views.EmployeeViewSet, basename='employee')
router.register(r'attendance', erp_views.AttendanceViewSet, basename='attendance')
router.register(r'leave-application', erp_views.LeaveApplicationViewSet, basename='leaveapplication')
router.register(r'salary-slip', erp_views.SalarySlipViewSet, basename='salaryslip')

# Manufacturing & Projects
router.register(r'bom', erp_views.BOMViewSet, basename='bom')
router.register(r'work-order', erp_views.WorkOrderViewSet, basename='workorder')
router.register(r'production-plan', erp_views.ProductionPlanViewSet, basename='productionplan')
router.register(r'project', erp_views.ProjectViewSet, basename='project')
router.register(r'task', erp_views.TaskViewSet, basename='task')
router.register(r'timesheet', erp_views.TimesheetViewSet, basename='timesheet')

# Assets & Support
router.register(r'asset', erp_views.AssetViewSet, basename='asset')
router.register(r'asset-depreciation', erp_views.AssetDepreciationScheduleViewSet, basename='assetdepreciation')
router.register(r'issue', erp_views.IssueViewSet, basename='issue')
router.register(r'sla', erp_views.ServiceLevelAgreementViewSet, basename='sla')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
