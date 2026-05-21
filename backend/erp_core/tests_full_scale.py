from django.test import TestCase
from accounts.models import Account
from setup.models import Company, Currency
from selling.models import Customer
from stock.models import Item, Warehouse, UOM

class FullScaleE2ETest(TestCase):
    def test_complete_setup_flow(self):
        # 1. Setup Base Data
        currency = Currency.objects.create(name="USD")
        uom = UOM.objects.create(name="Nos")

        # 2. Create Company
        company = Company.objects.create(
            name="Global Corp",
            company_name="Global Corp",
            default_currency=currency
        )

        # 3. Create Warehouse
        warehouse = Warehouse.objects.create(
            name="Main Store - GC",
            warehouse_name="Main Store",
            company=company
        )

        # 4. Create Item
        item = Item.objects.create(
            name="ITM-001",
            item_code="ITM-001",
            item_name="Test Product",
            stock_uom=uom,
            is_stock_item=True
        )

        # 5. Create Customer
        customer = Customer.objects.create(
            name="CUST-001",
            customer_name="John Doe",
            customer_type="Individual"
        )

        # 6. Verify Relationships
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Warehouse.objects.get(name="Main Store - GC").company.name, "Global Corp")
        print("Backend Full Scale E2E Test Passed: Models from different apps are interconnected.")
