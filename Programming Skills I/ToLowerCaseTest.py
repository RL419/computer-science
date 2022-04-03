from unittest import TestCase
from ToLowerCase import to_lower_case

class TestTLC(TestCase):
    def test_both_case(self):
        self.assertEqual(to_lower_case('UwU'), 'uwu')