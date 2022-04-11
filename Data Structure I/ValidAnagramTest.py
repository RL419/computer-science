from unittest import TestCase
from ValidAnagram import valid_anagram

class TestVA(TestCase):
    def test_ex1(self):
        self.assertEqual(valid_anagram('anagram', 'nagaram'), True)
    
    def test_ex2(self):
        self.assertEqual(valid_anagram('rat', 'car'), False)
    
    def test_idk1(self):
        self.assertEqual(valid_anagram('sstonk', 'stonk'), False)

    def test_idk2(self):
        self.assertEqual(valid_anagram('stonk', 'stonks'), False)
    
    def test_stupid(self):
        self.assertEqual(valid_anagram('ab', 'a'), False)