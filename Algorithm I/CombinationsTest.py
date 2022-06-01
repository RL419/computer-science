from unittest import TestCase
from Combinations import function

class TestC(TestCase):
    def test_1(self):
        self.assertCountEqual(function(4,2), [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
])
    
    def test_2(self):
        self.assertCountEqual(function(1,1), [[1]])

    # def test_3(self):
    #     self.assertEqual(function(), )