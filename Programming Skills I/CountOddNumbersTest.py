from unittest import TestCase
from CountOddNumbers import con

class TestCountOddNumbers(TestCase):
    def test_example(self):
        self.assertEqual(con(3,7), 3)
    
    def test_big_range(self):
        self.assertEqual(con(1,1000), 500)

    def test_same_lh(self):
        self.assertEqual(con(2,2), 0)