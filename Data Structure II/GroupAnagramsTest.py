from unittest import TestCase
from GroupAnagrams import group


class TestGA(TestCase):
    def test_1(self):
        self.assertEqual(group(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
    def test_2(self):
        self.assertEqual(group([""]), [[""]])
    def test_3(self):
        self.assertEqual(group(["a"]), [["a"]])