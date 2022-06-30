from unittest import TestCase
from RepeatedDNASequence import find


class TestDNA(TestCase):
    def test_1(self):
        self.assertEqual(find("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC","CCCCCAAAAA"])

    def test_2(self):
        self.assertEqual(find("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])