from unittest import TestCase
from AllAnagramsInString import find_anagram


class TestAA(TestCase):
    def test_1(self):
        self.assertEqual(find_anagram("cbaebabacd", p = "abc"), [0,6])
    def test_2(self):
        self.assertEqual(find_anagram("abab", p = "ab"), [0,1,2])