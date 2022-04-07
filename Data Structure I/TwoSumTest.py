from unittest import TestCase
from TwoSum import two_sum

class TestTS(TestCase):
    def test_negative(self):
        self.assertEqual(two_sum([-2,-9,-7,10,69,73], 60), [1, 4])
    
    def test_ex(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [0,1])
    
    def test_ex2(self):
        self.assertEqual(two_sum([3,2,4], 6), [1,2])