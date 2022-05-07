from SubstringPattern import substring
from unittest import TestCase

class TestSSP(TestCase):
    def test_1(self):
        self.assertEqual(substring('abab'), True)

    def test_2(self):
        self.assertEqual(substring('abba'), False)

    def test_3(self):
        self.assertEqual(substring('abcdaabcda'), True)

