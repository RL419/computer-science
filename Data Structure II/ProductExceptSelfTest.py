from unittest import TestCase
from ProductExceptSelf import except_self


class TestP(TestCase):
    def test_1(self):
        self.assertEqual(except_self([1,2,3,4]), [24,12,8,6])
    def test_2(self):
        self.assertEqual(except_self([-1,1,0,-3,3]), [0,0,9,0,0])