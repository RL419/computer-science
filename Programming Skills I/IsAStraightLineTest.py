from unittest import TestCase
from IsAStraightLine import is_a_straight_line

class TestSL(TestCase):
    def test_example(self):
        self.assertEqual(is_a_straight_line([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)

    def test_no_slope(self):
        self.assertEqual(is_a_straight_line([[0,1], [0,2], [0,3], [0,4]]), True)
    
    def test_false(self):
        self.assertEqual(is_a_straight_line([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)