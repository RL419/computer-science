from unittest import TestCase
from PlusOne import plus_1

class TestP1(TestCase):
    def test_1(self):
        self.assertEqual(plus_1([1,2,3]), [1,2,4])

    def test_2(self):
        self.assertEqual(plus_1([4,3,2,1]), [4,3,2,2])

    def test_3(self):
        self.assertEqual(plus_1([9]), [1,0])

    def test_4(self):
        self.assertEqual(plus_1([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]), [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])