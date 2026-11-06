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