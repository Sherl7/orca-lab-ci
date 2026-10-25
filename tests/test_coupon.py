import unittest
from orders import apply_coupon

class CouponTests(unittest.TestCase):
    def test_save10_basic(self):
        self.assertEqual(apply_coupon(100_000, "SAVE10"), 90_000)

    def test_save10_just_below_cap(self):
        # 10% is 49_999.9: floor gives 450_000, round gives 449_999 (spec doesn't say)
        self.assertIn(apply_coupon(499_999, "SAVE10"), (449_999, 450_000))

    def test_save10_at_cap(self):
        self.assertEqual(apply_coupon(500_000, "SAVE10"), 450_000)

    def test_save10_just_above_cap(self):
        self.assertEqual(apply_coupon(500_001, "SAVE10"), 450_001)

    def test_save10_capped(self):
        self.assertEqual(apply_coupon(1_000_000, "SAVE10"), 950_000)

    def test_invalid_codes_no_discount(self):
        for code in (None, "", "save10", "OTHER"):
            with self.subTest(code=code):
                self.assertEqual(apply_coupon(100_000, code), 100_000)

    def test_zero_subtotal(self):
        self.assertEqual(apply_coupon(0, "SAVE10"), 0)
        self.assertEqual(apply_coupon(0, "OTHER"), 0)

    def test_negative_subtotal_save10(self):
        with self.assertRaises(ValueError):
            apply_coupon(-1, "SAVE10")

    def test_negative_subtotal_other_code(self):
        with self.assertRaises(ValueError):
            apply_coupon(-1, "OTHER")

    def test_returns_int(self):
        self.assertIsInstance(apply_coupon(100_000, "SAVE10"), int)
        self.assertIsInstance(apply_coupon(100_001, "SAVE10"), int)
        self.assertIsInstance(apply_coupon(100_000, "OTHER"), int)
