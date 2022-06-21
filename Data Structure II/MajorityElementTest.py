from unittest import TestCase
from MajorityElement import majorityElement

class TestME(TestCase):
    def test_1(self):
        self.assertEqual(majorityElement([3,2,3]), 3)
    def test_2(self):
        self.assertEqual(majorityElement([2,2,1,1,1,2,2]), 2)