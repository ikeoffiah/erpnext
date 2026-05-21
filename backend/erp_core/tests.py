from django.test import TestCase, Client
import json

class RPCTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_rpc_resolution(self):
        # Test a standard erpnext method resolution
        response = self.client.post(
            '/api/rpc/?method=erpnext.accounts.doctype.bank_transaction.bank_transaction.unreconcile',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('accounts.services.unreconcile', data['resolved_to'])

    def test_rpc_whitelist(self):
        # Test a non-whitelisted app
        response = self.client.post(
            '/api/rpc/?method=erpnext.malicious_app.func',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 403)
