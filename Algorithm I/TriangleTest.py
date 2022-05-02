from unittest import TestCase
from Triangle import min_total

class TestTriangle(TestCase):
    def test_1(self):
        self.assertEqual(min_total([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
    
    def test_2(self):
        self.assertEqual(min_total([[-10]]), -10)