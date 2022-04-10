from unittest import TestCase
from IntersectionOf2Arrays import intersect

class TestIO2A(TestCase):
    def test_ex1(self):
        self.assertEqual(intersect(nums1 = [1,2,2,1], nums2 = [2,2]), [2,2])
    
    def test_ex2(self):
        self.assertEqual(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]), [4,9] or [9,4])