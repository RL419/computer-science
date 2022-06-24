from unittest import TestCase
from Search2DMatrixII import search_matrix

class Test2D(TestCase):
    def test_1(self):
        self.assertEqual(search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), True)
    def test_2(self):
        self.assertEqual(search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20), False)