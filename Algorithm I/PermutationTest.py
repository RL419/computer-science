from unittest import TestCase
from Permutation import permutations

class TestPermutatiton(TestCase):
    def test_1(self):
        self.assertEqual(permutations('ab', 'eidbaooo'), True)
    
    def test_2(self):
        self.assertEqual(permutations('ab', 'eidboaoo'), False)
    
    def test_3(self):
        self.assertEqual(permutations('yes', 'eyes'), True)