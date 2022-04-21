from unittest import TestCase
from SearchInsertPos import insertpos

class TestIP(TestCase):
    def test_1(self):
        self.assertEqual(insertpos([1,3,5,6], 5), 2)
    
    def test_2(self):
        self.assertEqual(insertpos([1,3,5,6], 2), 1)
    
    def test_3(self):
        self.assertEqual(insertpos([1,3,5,6], 7), 4)
    
    def test_4(self):
        self.assertEqual(insertpos([n for n in range(100)], -1), 0)