from unittest import TestCase
from SpiralMatrix import spiralOrder

class TestSM(TestCase):
    def test_1(self):
        self.assertEqual(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
    def test_2(self):
        self.assertEqual(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])