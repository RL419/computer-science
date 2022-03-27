from unittest import TestCase
from LargestPerimeter import largest_perimeter

class TestLP(TestCase):
    def test_example(self):
        self.assertEqual(largest_perimeter([1,1,2]), 0)
    
    def test_large_list(self):
        self.assertEqual(largest_perimeter([10, 5, 5, 4, 3, 2, 1]), 14)