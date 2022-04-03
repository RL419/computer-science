from unittest import TestCase
from FindDifference import find_difference

class TestFD(TestCase):
    def test_long_string(self):
        self.assertEqual(find_difference('abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjjkkkkkkkkkkk','abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjjkkkkkkkkkkkz'), 'z')

    def test_empty_s(self):
        self.assertEqual(find_difference('', 'y'), 'y')