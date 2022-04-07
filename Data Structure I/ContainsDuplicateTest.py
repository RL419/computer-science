from unittest import TestCase
from ContainsDuplicate import contains_duplicate

class TestCD(TestCase):
    def test_ex1(self):
        self.assertEqual(contains_duplicate([1,2,3,1]), True)
    
    def test_ex2(self):
        self.assertEqual(contains_duplicate([1,2,3,4]), False)
    
    def test_ex3(self):
        self.assertEqual(contains_duplicate([1,1,1,3,3,4,3,2,4,2]), True)