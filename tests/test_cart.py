import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa
        for i in range(20):
            cart.add_dvd(DigitalVideoDisc(f"Title {i}"))
        
        # Thêm đĩa thứ 21, kỳ vọng trả về False
        result = cart.add_dvd(DigitalVideoDisc("21st DVD"))
        self.assertFalse(result)

    def test_discount_calculation(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD")
        dvd.cost = 100.0
        cart.add_dvd(dvd)
        
        # Test 1: 100 -> giảm 20% = 80
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        
        # Test 2: percent 150 -> ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)