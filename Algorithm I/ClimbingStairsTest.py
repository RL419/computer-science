from unittest import TestCase
from ClimbingStairs import climbStairs

class TestCS(TestCase):
    def test_1(self):
        self.assertEqual(climbStairs(2), 2)

    def test_2(self):
        self.assertEqual(climbStairs(3), 3)