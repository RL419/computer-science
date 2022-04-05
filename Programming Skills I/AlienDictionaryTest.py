from unittest import TestCase
from AlienDictionary import alien_dict

class TestAD(TestCase):
    def test_ex1(self):
        self.assertEqual(alien_dict(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
    
    def test_ex2(self):
        self.assertEqual(alien_dict(["word","world","row"], "worldabcefghijkmnpqstuvxyz"), False)
    
    def test_ex3(self):
        self.assertEqual(alien_dict(["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False)