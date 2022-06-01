from unittest import TestCase
from HouseRobber import rob

class TestHR(TestCase):
    def test_(self):
        self.assertEqual(rob([1,2,3,1]), 4)
    
    def test_2(self):
        self.assertEqual(rob([2,7,9,3,1]), 12)