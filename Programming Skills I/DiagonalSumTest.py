from unittest import TestCase
from DiagonalSum import diagonal_sum

class TestDS(TestCase):
    def test_example(self):
        self.assertEqual(diagonal_sum([[1,2,3],[4,5,6], [7,8,9]]), 25)
    
    def test_one_element(self):
        self.assertEqual(diagonal_sum([[1]]), 1)
    
    def test_3(self):
        self.assertEqual(diagonal_sum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]), 8)