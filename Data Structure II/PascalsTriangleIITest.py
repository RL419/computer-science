from unittest import TestCase
from PascalsTriangleII import triangle


class TestPascal(TestCase):
    def test_1(self):
        self.assertEqual(triangle(3), [1,3,3,1])
    def test_2(self):
        self.assertEqual(triangle(0), [1])
    def test_3(self):
        self.assertEqual(triangle(1), [1,1])