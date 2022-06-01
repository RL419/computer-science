from unittest import TestCase
from CanBeObtainedByRotation import if_obtainable

class TestCBO(TestCase):
    def test_1(self):
        self.assertEqual(if_obtainable(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]), True)
    def test_2(self):
        self.assertEqual(if_obtainable(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]), False)
    def test_3(self):
        self.assertEqual(if_obtainable([[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]), True)