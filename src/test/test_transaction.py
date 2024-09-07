import unittest
from transaction_service.app import app

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_transaction(self):
        response = self.app.post('/transaction')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Transaction Created', response.data)

if __name__ == '__main__':
    unittest.main()