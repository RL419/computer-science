from unittest import TestCase
from MergeSortedArray import merge_sorted_arr

class TestMSA(TestCase):
    def test_ex1(self):
        nums1 = [1,2,3,0,0,0]
        merge_sorted_arr(nums1, 3, [2,5,6], 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])
    
    def test_ex2(self):
        nums1 = [1]
        merge_sorted_arr(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])
    
    def test_ex3(self):
        nums1 = [0]
        merge_sorted_arr(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])