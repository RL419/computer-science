from unittest import TestCase
from MergeIntervals import merge

class TestMI(TestCase):
    def test_1(self):
        self.assertEqual(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
    def test_2(self):
        self.assertEqual(merge([[1,4],[4,5]]), [[1,5]])