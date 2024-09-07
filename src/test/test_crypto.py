import unittest
from crypto_price_service.app import app

class TestCryptoPriceService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_price(self):
        response = self.app.get('/price')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'price', response.data)
        self.assertIn(b'1000 USD', response.data)

if __name__ == '__main__':
    unittest.main()