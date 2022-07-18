from unittest import TestCase
from BinarySearch import binary_search

class TestBS(TestCase):
    def test_1(self):
        self.assertEqual(binary_search([-1,0,3,5,9,12], 9), 4)
    
    def test_2(self):
        self.assertEqual(binary_search([-1,0,3,5,9,12], 2), -1)
    
    def test_big(self):
        self.assertEqual(binary_search([i for i in range(100)], 99), 99)