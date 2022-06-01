from unittest import TestCase
from TwoSumII import twosum

class TestTSII(TestCase):
    def test_1(self):
        self.assertEqual(twosum([2,7,11,15], 9), [1,2])
    
    def test_2(self):
        self.assertEqual(twosum([2,3,4], 6), [1,3])
    
    def test_3(self):
        self.assertEqual(twosum([-1,0], -1), [1,2])