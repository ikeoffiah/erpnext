from django.test import TestCase
from accounts.models import Account
from setup.models import Company, Currency

class EndToEndBackendTest(TestCase):
    def test_company_and_account_creation(self):
        # Create a currency
        currency = Currency.objects.create(name="USD")

        # Create a company
        company = Company.objects.create(
            name="Test Company",
            company_name="Test Company",
            default_currency=currency
        )

        # Create an account
        account = Account.objects.create(
            name="Cash - TC",
            account_name="Cash",
            company=company,
            is_group=False,
            root_type="Asset",
            report_type="Balance Sheet"
        )

        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.first().company.name, "Test Company")
