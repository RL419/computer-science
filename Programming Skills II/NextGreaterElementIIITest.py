from unittest import TestCase
from NextGreaterElementIII import next_greater_element3

class TestNGE3(TestCase):
    def test_1(self):
        self.assertEqual(next_greater_element3(12), 21)
    def test_2(self):
        self.assertEqual(next_greater_element3(21), -1)
    def test_3(self):
        self.assertEqual(next_greater_element3(999999999999), -1)
    def test_4(self):
        self.assertEqual(next_greater_element3(1234), 1243)