from unittest import TestCase
from HappyNumber import happy_number

class TestHappyNumber(TestCase):
    def test_example(self):
        self.assertEqual(happy_number(19), True)

    def test_loop(self):
        self.assertEqual(happy_number(116), False)