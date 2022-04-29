from unittest import TestCase
from RottingOranges import rotting_oranges

class TestRO(TestCase):
    def test_1(self):
        self.assertEqual(rotting_oranges([[2,1,1],[1,1,0],[0,1,1]]), 4)
    
    def test_2(self):
        self.assertEqual(rotting_oranges([[0,2]]), 0)
    
    def test_3(self):
        self.assertEqual(rotting_oranges([[2,1,1],[0,1,1],[1,0,1]]),-1)