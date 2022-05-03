from unittest import TestCase
from PowerOf2 import power_of_2

class TestPO2(TestCase):
    def test_1(self):
        self.assertEqual(power_of_2(1), True)
    
    def test_2(self):
        self.assertEqual(power_of_2(16), True)
    
    def test_3(self):
        self.assertEqual(power_of_2(3), False)
    
    def test_4(self):
        self.assertEqual(power_of_2(536870912), True)