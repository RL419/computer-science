from unittest import TestCase
from SortBy1Bits import sortbybit

class TestSort(TestCase):
    def test_ex1(self):
        self.assertEqual(sortbybit([0,1,2,3,4,5,6,7,8]), [0,1,2,4,8,3,5,6,7])
    
    def test_ex2(self):
        self.assertEqual(sortbybit([1024,512,256,128,64,32,16,8,4,2,1]), [1,2,4,8,16,32,64,128,256,512,1024])