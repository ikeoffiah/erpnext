from rest_framework import viewsets
from .models import (
    Bank, BankAccount, BankStatementImportLog,
    Customer, Lead, Opportunity, Quotation, SalesOrder, SalesInvoice,
    Supplier, Item, PurchaseOrder, PurchaseInvoice,
    Employee, Attendance, LeaveApplication, SalarySlip,
    BOM, WorkOrder, ProductionPlan, Project, Task, Timesheet,
    Asset, AssetDepreciationSchedule, Issue, ServiceLevelAgreement
)
from .serializers import (
    BankSerializer, BankAccountSerializer, BankStatementImportLogSerializer,
    CustomerSerializer, LeadSerializer, OpportunitySerializer, QuotationSerializer, SalesOrderSerializer, SalesInvoiceSerializer,
    SupplierSerializer, ItemSerializer, PurchaseOrderSerializer, PurchaseInvoiceSerializer,
    EmployeeSerializer, AttendanceSerializer, LeaveApplicationSerializer, SalarySlipSerializer,
    BOMSerializer, WorkOrderSerializer, ProductionPlanSerializer, ProjectSerializer, TaskSerializer, TimesheetSerializer,
    AssetSerializer, AssetDepreciationScheduleSerializer, IssueSerializer, ServiceLevelAgreementSerializer
)

# =====================================================================
# BATCH 1 VIEWSETS
# =====================================================================

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class BankStatementImportLogViewSet(viewsets.ModelViewSet):
    queryset = BankStatementImportLog.objects.all()
    serializer_class = BankStatementImportLogSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer

# =====================================================================
# BATCH 2 VIEWSETS
# =====================================================================

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

class SalarySlipViewSet(viewsets.ModelViewSet):
    queryset = SalarySlip.objects.all()
    serializer_class = SalarySlipSerializer

class BOMViewSet(viewsets.ModelViewSet):
    queryset = BOM.objects.all()
    serializer_class = BOMSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class ProductionPlanViewSet(viewsets.ModelViewSet):
    queryset = ProductionPlan.objects.all()
    serializer_class = ProductionPlanSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetDepreciationScheduleViewSet(viewsets.ModelViewSet):
    queryset = AssetDepreciationSchedule.objects.all()
    serializer_class = AssetDepreciationScheduleSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ServiceLevelAgreementViewSet(viewsets.ModelViewSet):
    queryset = ServiceLevelAgreement.objects.all()
    serializer_class = ServiceLevelAgreementSerializer
