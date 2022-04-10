from unittest import TestCase
from PascalsTriangle import pascalTriangle

class TestPS(TestCase):
    def test_ex1(self):
        self.assertEqual(pascalTriangle(5), [[1],[1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]])
    
    def test_ex2(self):
        self.assertEqual(pascalTriangle(1), [[1]])