from unittest import TestCase
from DecryptString import freqAlphabets

class TestDS(TestCase):
    def test_example(self):
        self.assertEqual(freqAlphabets('10#11#12'), 'jkab')
    
    def test_example1(self):
        self.assertEqual(freqAlphabets('1326#'), 'acz')
    
    def test_long(self):
        self.assertEqual(freqAlphabets('123456789876543212345678987654321'), 'abcdefghihgfedcbabcdefghihgfedcba')