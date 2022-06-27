from unittest import TestCase
from TripletSubsequence import triplet


class TestTriplet(TestCase):
    def test_1(self):
        self.assertEqual(triplet([1,2,3,4,5]), True)
    def test_2(self):
        self.assertEqual(triplet([5,4,3,2,1]), False)
    def test_3(self):
        self.assertEqual(triplet([2,1,5,0,4,6]), True)