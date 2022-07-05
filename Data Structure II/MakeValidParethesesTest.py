from unittest import TestCase
from MakeValidParetheses import min_remove_make_valid


class TestMVP(TestCase):
    def test_1(self):
        self.assertEqual(min_remove_make_valid("lee(t(c)o)de)"), "lee(t(c)o)de")

    def test_2(self):
        self.assertEqual(min_remove_make_valid("a)b(c)d"), "ab(c)d")

    def test_3(self):
        self.assertEqual(min_remove_make_valid("))(("), '')

    def test_4(self):
        self.assertEqual(min_remove_make_valid("(lee(t(c)o)de"), "lee(t(c)o)de")

    def test_5(self):
        self.assertEqual(min_remove_make_valid("())()((("), "()()")