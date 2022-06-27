from unittest import TestCase
from WordPattern import word_pattern

class TestWP(TestCase):
    def test_1(self):
        self.assertEqual(word_pattern('abba', "dog cat cat dog"), True)
    def test_2(self):
        self.assertEqual(word_pattern("abba", "dog cat cat fish"), False)
    def test_3(self):
        self.assertEqual(word_pattern(pattern = "aaaa", s = "dog cat cat dog"), False)
    def test_4(self):
        self.assertEqual(word_pattern('abba', 'dog dog dog dog'), False)