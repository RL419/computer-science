from unittest import TestCase
from RansomNote import canConstruct

class TestC(TestCase):
    def test_ex1(self):
        self.assertEqual(canConstruct('a', 'b'), False)

    def test_ex2(self):
        self.assertEqual(canConstruct('aa', 'ab'), False)
    
    def test_ex3(self):
        self.assertEqual(canConstruct('aa', 'aab'), True)