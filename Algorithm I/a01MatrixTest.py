from unittest import TestCase
from a01Matrix import distance_to_0

class Test01(TestCase):
    def test_1(self):
        self.assertEqual(distance_to_0([[0,0,0],[0,1,0],[0,0,0]]), [[0,0,0],[0,1,0],[0,0,0]])
    
    def test_2(self):
        self.assertEqual(distance_to_0([[0,0,0],[0,1,0],[1,1,1]]), [[0,0,0],[0,1,0],[1,2,1]])