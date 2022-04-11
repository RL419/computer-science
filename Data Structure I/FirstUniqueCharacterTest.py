from unittest import TestCase
from FirstUniqueCharacter import unique_char

class TestFUC(TestCase):
    def test_ex1(self):
        self.assertEqual(unique_char('leetcode'), 0)

    def test_ex2(self):
        self.assertEqual(unique_char('loveleetcode'), 2)
    
    def test_ex(self):
        self.assertEqual(unique_char('aabb'), -1)