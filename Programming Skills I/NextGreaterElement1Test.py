from unittest import TestCase
from NextGreaterElement1 import next_greater_element

class TestNGE(TestCase):
    def test_example(self):
        self.assertEqual(next_greater_element([4,1,2], [1,3,4,2]),[-1,3,-1])