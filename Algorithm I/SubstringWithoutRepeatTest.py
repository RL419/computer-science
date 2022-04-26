from unittest import TestCase
from SubstringWithoutRepeat import length

class TestSSWR(TestCase):
    def test_1(self):
        self.assertEqual(length('abcabcbb'), 3)
    
    def test_2(self):
        self.assertEqual(length('bbbbbbbbbbbbbbbbbbbbbbb'), 1)
    
    def test_3(self):
        self.assertEqual(length('stonks'), 5)