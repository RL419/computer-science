from unittest import TestCase
from Search2DMatrix import search

class TestS2D(TestCase):
    def test_ex1(self):
        self.assertEqual(search([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3), True)
    
    def test_ex2(self):
        self.assertEqual(search([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 13), False)