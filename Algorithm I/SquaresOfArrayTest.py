from unittest import TestCase
from SquaresOfArray import squares

class TestSquares(TestCase):
    def test_1(self):
        self.assertEqual(squares([-4,-1,0,3,10]), [0,1,9,16,100])
    
    def test_2(self):
        self.assertEqual(squares([-7,-3,2,3,11]), [4,9,9,49,121])