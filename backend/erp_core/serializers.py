from rest_framework import serializers
from .models import (
    # Banking
    Bank, BankAccount, BankStatementImportLog,
    
    # CRM & Sales
    Customer, Lead, Opportunity, Quotation, SalesOrder, SalesInvoice,
    
    # Purchase & Inventory
    Supplier, Item, PurchaseOrder, PurchaseInvoice,
    
    # HR & Payroll
    Employee, Attendance, LeaveApplication, SalarySlip,
    
    # Manufacturing & Projects
    BOM, WorkOrder, ProductionPlan, Project, Task, Timesheet,
    
    # Assets & Support
    Asset, AssetDepreciationSchedule, Issue, ServiceLevelAgreement
)

# =====================================================================
# BATCH 1 SERIALIZERS
# =====================================================================

# Banking Serializers
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class BankStatementImportLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatementImportLog
        fields = '__all__'

# CRM & Sales Serializers
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'

class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = '__all__'

# Purchase & Inventory Serializers
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'

# =====================================================================
# BATCH 2 SERIALIZERS
# =====================================================================

# HR & Payroll Serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = '__all__'

class SalarySlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalarySlip
        fields = '__all__'

# Manufacturing & Projects Serializers
class BOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM
        fields = '__all__'

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'

class ProductionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionPlan
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'

# Assets & Support Serializers
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetDepreciationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetDepreciationSchedule
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class ServiceLevelAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLevelAgreement
        fields = '__all__'
