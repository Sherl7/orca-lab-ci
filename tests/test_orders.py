import unittest
from orders import shipping_fee

class ShippingTests(unittest.TestCase):
    def test_below_threshold(self):
        self.assertEqual(shipping_fee(299_999), 30_000)

    def test_at_threshold(self):
        self.assertEqual(shipping_fee(300_000), 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            shipping_fee(-1)
