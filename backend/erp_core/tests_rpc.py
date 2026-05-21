from django.test import TestCase, Client
import json
from erp_core.models import BaseDocument

class RPCE2ETest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_rpc_flow(self):
        # Call a function that should exist in the accounts app
        response = self.client.post(
            '/api/rpc/?method=erpnext.accounts.doctype.bank_transaction.bank_transaction.get_item_details',
            data=json.dumps({'test': 'data'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        res_data = response.json()
        self.assertEqual(res_data['status'], 'success')
        self.assertIn('accounts.services.get_item_details', res_data['resolved_to'])

    def test_rpc_invalid_app(self):
        response = self.client.post(
            '/api/rpc/?method=erpnext.non_existent_app.func',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 403)
