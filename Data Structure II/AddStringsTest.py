from unittest import TestCase
from AddStrings import add_string


class TestAS(TestCase):
    def test_1(self):
        self.assertEqual(add_string('11', '123'), '134')
    def test_2(self):
        self.assertEqual(add_string('456', '77'), '533')
    def test_3(self):
        self.assertEqual(add_string('0', '0'), '0')