from unittest import TestCase
from NextGreaterElementII import next_greater_element

class TestNGE2(TestCase):
    def test_1(self):
        self.assertEqual(next_greater_element([1,2,1]), [2,-1,2])
    def test_2(self):
        self.assertEqual(next_greater_element([1,2,3,4,3]), [2,3,4,-1,4])
    def test_3(self):
        self.assertEqual(next_greater_element([9,8,7,6,5,4,3,2,1]),[-1,9,9,9,9,9,9,9,9])