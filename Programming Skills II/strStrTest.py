from unittest import TestCase
from strStr import strStr

class TestSS(TestCase):
    def test_1(self):
        self.assertEqual(strStr('hello', 'll'), 2)

    def test_2(self):
        self.assertEqual(strStr('aaaaa','bba'), -1)
    
    def test_3(self):
        self.assertEqual(strStr('stonk', ''), 0)