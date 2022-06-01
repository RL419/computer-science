from unittest import TestCase
from AddBinary import add_binary

class TestAB(TestCase):
    def test_1(self):
        self.assertEqual(add_binary('11', '1'), '100')
    def test_2(self):
        self.assertEqual(add_binary('1010', '1011'), '10101')