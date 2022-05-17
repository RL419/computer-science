from unittest import TestCase
from SubArrProductLTK import yes

class TestYes(TestCase):
    def test_1(self):
        self.assertEqual(yes([10,5,2,6], 100), 8)
    def test_2(self):
        self.assertEqual(yes([1,2,3],0), 0)