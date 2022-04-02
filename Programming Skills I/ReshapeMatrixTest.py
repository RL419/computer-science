from unittest import TestCase
from ReshapeMatrix import reshape

class TestReshape(TestCase):
    def test_example(self):
        self.assertEqual(reshape([[1,2],[3,4]],1,4), [[1,2,3,4]])
    
    def test_no_sol(self):
        self.assertEqual(reshape([[1,2,3],[4,5,6],[7,8,9]],2,4), [[1,2,3],[4,5,6],[7,8,9]]) 