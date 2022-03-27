from unittest import TestCase
from NearestPoint import nearest_point

class TestNP(TestCase):
    def test_example(self):
        self.assertEqual(nearest_point(3, 4, [[1,2], [3,1], [2,4], [2,3], [4,4]]), 2)

    def test_same_point(self):
        self.assertEqual(nearest_point(3,4,[[4,4], [3,3] ,[3,4]]), 2)

    def test_no_ans(self):
        self.assertEqual(nearest_point(3,4, [[1,2], [5,6], [7,8]]), -1)