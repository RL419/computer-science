from unittest import TestCase
from BuyAndSellStock import stonks

class TestStonk(TestCase):
    def test_ex1(self):
        self.assertEqual(stonks([7,1,5,3,6,4]), 5)

    def test_ex(self):
        self.assertEqual(stonks([7,6,4,3,1]), 0)
    
    def test_edge1(self):
        self.assertEqual(stonks([2,4,1]), 2)
    
    def test_edge2(self):
        self.assertEqual(stonks([1]), 0)
    
    def test_stupid(self):
        self.assertEqual(stonks([3,2,6,5,0,3]), 4)