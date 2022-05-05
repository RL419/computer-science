from unittest import TestCase
from MonotonicArray import monotonic

class TestMonotonic(TestCase):
    def test_1(self):
        self.assertEqual(monotonic([1,2,2,3]), True)
    
    def test_2(self):
        self.assertEqual(monotonic([6,5,4,4]), True)

    def test_3(self):
        self.assertEqual(monotonic([1,3,2]), False)