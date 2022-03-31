from unittest import TestCase
from MoveZeros import move_zeros

class TestMZ(TestCase):
    def test_example(self):
        n = [0,1,0,3,12]
        move_zeros(n)
        self.assertEqual(n, [1,3,12,0,0])

    def test_large_list(self):
        n = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2]
        move_zeros(n)
        self.assertEqual(n, [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])