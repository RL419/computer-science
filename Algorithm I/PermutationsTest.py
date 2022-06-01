from unittest import TestCase
from Permutations import permutations

class TestPermutations(TestCase):
    def test_1(self):
        self.assertEqual(permutations([1,2,3]),[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    
    def test_2(self):
        self.assertEqual(permutations([0,1]),[[0,1],[1,0]])
    
    def test_3(self):
        self.assertEqual(permutations([1]),[[1]])