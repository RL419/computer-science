from unittest import TestCase
from SpiralMatrixII import generate

class TestSM(TestCase):
    def test_1(self):
        self.assertEqual(generate(3), [[1,2,3],[8,9,4],[7,6,5]])
    def test_2(self):
        self.assertEqual(generate(1), [[1]])