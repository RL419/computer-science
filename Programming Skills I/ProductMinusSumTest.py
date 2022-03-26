from ProductMinusSum import prosum
from unittest import TestCase

class TestProsum(TestCase):
    def test_zero(self):
        self.assertEqual(prosum(0), 0)
    
    def test_large_num(self):
        self.assertEqual(prosum(1234567890987654321234567890987654321), -sum([int(x) for x in str(1234567890987654321234567890987654321)]))