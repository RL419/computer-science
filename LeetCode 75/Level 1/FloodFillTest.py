from unittest import TestCase
from FloodFill import flood_fill

class TestFF(TestCase):
    def test_1(self):
        self.assertEqual(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])
    
    def test_2(self):
        self.assertEqual(flood_fill([[0,0,0],[0,0,0]], 0, 0, 2), [[2,2,2],[2,2,2]])