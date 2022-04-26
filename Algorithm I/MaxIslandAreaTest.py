from unittest import TestCase
from MaxIslandArea import area_of_island

class TestIA(TestCase):
    def test_1(self):
        self.assertEqual(area_of_island([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]), 6)
    
    def test_2(self):
        self.assertEqual(area_of_island([[0,0,0,0,0,0,0,0]]), 0)