from unittest import TestCase
from ValidParentheses import is_valid

class TestVP(TestCase):
    def test_1(self):
        self.assertEqual(is_valid('((())]'), False)
    
    def test_2(self):
        self.assertEqual(is_valid('()[]{}'), True)
    
    def test_3(self):
        self.assertEqual(is_valid('([{[]}])'), True)