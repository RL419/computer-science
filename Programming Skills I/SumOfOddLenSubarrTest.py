from unittest import TestCase
from SumOfOddLenSubarr import odd_len_subarray

class TestSOOLS(TestCase):
    def test_example1(self):
        self.assertEqual(odd_len_subarray([1,4,2,5,3]), 58)

    def test_example2(self):
        self.assertEqual(odd_len_subarray([1,2]), 3)
    
    def test_example3(self):
        self.assertEqual(odd_len_subarray([10,11,12]), 66)