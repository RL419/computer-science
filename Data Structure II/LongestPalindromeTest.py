from unittest import TestCase
from LongestPalindrome import longestPalindrome


class TestLP(TestCase):
    def test_1(self):
        self.assertEqual(longestPalindrome("abccccdd"), 7)
    def test_2(self):
        self.assertEqual(longestPalindrome('a'), 1)