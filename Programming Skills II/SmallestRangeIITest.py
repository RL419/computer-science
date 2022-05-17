from unittest import TestCase
from SmallestRangeII import small_range

class TestSR2(TestCase):
    def test_1(self):
        self.assertEqual(small_range([1],0), 0)
    def test_2(self):
        self.assertEqual(small_range([0,10], 2), 6)
    def test_3(self):
        self.assertEqual(small_range([1,3,6], 3), 3)