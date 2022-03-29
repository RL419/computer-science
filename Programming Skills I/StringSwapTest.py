from unittest import TestCase
from StringSwap import are_almost_equal

class TestSS(TestCase):
    def test_example(self):
        self.assertEqual(are_almost_equal('bank', 'kanb'), True)
    
    def test_3(self):
        self.assertEqual(are_almost_equal('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwzxy'), False)
    
    def test_no(self):
        self.assertEqual(are_almost_equal('attack', 'defend'), False)