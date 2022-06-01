from unittest import TestCase
from LengthOfLastWord import len_of_last_word

class TestLOLW(TestCase):
    def test_1(self):
        self.assertEqual(len_of_last_word("Hello World"), 5)
    def test_2(self):
        self.assertEqual(len_of_last_word("   fly me   to   the moon  "), 4)
    def test_3(self):
        self.assertEqual(len_of_last_word("luffy is still joyboy"), 6)