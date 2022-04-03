from unittest import TestCase
from MergeString import merge_string

class TestMS(TestCase):
    def test_example1(self):
        self.assertEqual(merge_string('abc', 'pqr'), 'apbqcr')

    def test_example2(self):
        self.assertEqual(merge_string('ab', 'pqrs'), 'apbqrs')
    
    def test_example3(self):
        self.assertEqual(merge_string('abcd', 'pq'), 'apbqcd')