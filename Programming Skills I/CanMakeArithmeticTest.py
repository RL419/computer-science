from unittest import TestCase
from CanMakeArithmetic import can_make_arithmetic

class TestCMA(TestCase):
    def test_example(self):
        self.assertEqual(can_make_arithmetic([1,2,3]), True)
    
    def test_negative(self):
        self.assertEqual(can_make_arithmetic([i for i in range(-10000, -1, 2)]), True)
    
    def test_large_list(self):
        self.assertEqual(can_make_arithmetic([i for i in range(-10000, 10000, 5)]), True)
    
    def test_false(self):
        self.assertEqual(can_make_arithmetic([1,2,3,5,7,9,11,12]), False)