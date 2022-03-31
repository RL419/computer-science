from unittest import TestCase
from MaxWealth import max_wealth

class TestMW(TestCase):
    def test_example(self):
        self.assertEqual(max_wealth([[1,2,3], [3,2,1]]), 6)