from re import L
from unittest import TestCase
from LetterCasePermutation import letter_case

class TestLCP(TestCase):
    def test_1(self):
        self.assertEqual(letter_case('a1b2'), ["a1b2","a1B2","A1b2","A1B2"])
    
    def test_2(self):
        self.assertEqual(letter_case('3z4'), ["3z4","3Z4"])