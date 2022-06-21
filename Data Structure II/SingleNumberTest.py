from unittest import TestCase
from SingleNumber import singleNumber


class TestSN(TestCase):
    def test_1(self):
        self.assertEqual(singleNumber([2,2,1]), 1)
    
    def test_2(self):
        self.assertEqual(singleNumber([4,1,2,1,2]), 4)
    
    def test_3(self):
        self.assertEqual(singleNumber([1]), 1)