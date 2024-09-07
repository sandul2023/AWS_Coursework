import unittest
from account_service.app import app

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_account(self):
        response = self.app.get('/account/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username', response.data)
        self.assertIn(b'testuser', response.data)
        self.assertIn(b'Active', response.data)

if __name__ == '__main__':
    unittest.main()