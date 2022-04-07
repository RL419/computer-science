from unittest import TestCase
from MaximumSubarray import max_subarr

class TestMS(TestCase):
    def test_ex1(self):
        self.assertEqual(max_subarr([-2,1,-3,4,-1,2,1,-5,4]), 6)
    
    def test_ex2(self):
        self.assertEqual(max_subarr([1]), 1)
    
    def test_ex3(self):
        self.assertEqual(max_subarr([5,4,-1,7,8]), 23)