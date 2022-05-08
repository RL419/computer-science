from unittest import TestCase
from MultiplyStrings import multiply_str

class Test_MS(TestCase):
    def test_1(self):
        self.assertEqual(multiply_str('2','3'), '6')
    def test_2(self):
        self.assertEqual(multiply_str('123', '456'), '56088')
    def test_3(self):
        self.assertEqual(multiply_str('9999999999999999', '0'), '0')
    def test_4(self):
        self.assertEqual(multiply_str('10', '10'), '100')