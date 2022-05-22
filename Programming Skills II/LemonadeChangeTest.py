from unittest import TestCase
from LemonadeChange import change

class TestLC(TestCase):
    def test_1(self):
        self.assertEqual(change([5,5,5,10,20]), True)
    def test_2(self):
        self.assertEqual(change([5,5,10,10,20]), False)