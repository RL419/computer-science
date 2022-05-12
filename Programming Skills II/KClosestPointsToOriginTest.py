from unittest import TestCase
from KClosestPointsToOrigin import k_closest

class TestKCPTO(TestCase):
    def test_1(self):
        self.assertCountEqual(k_closest([[1,3], [-2,2]], 1), [[-2,2]])
    def test_2(self):
        self.assertCountEqual(k_closest([[3,3],[5,-1],[-2,4]], k = 2), [[3,3],[-2,4]])