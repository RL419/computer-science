from unittest import TestCase
from GoalParserInterpretation import interpret

class TestGPI(TestCase):
    def test_example1(self):
        self.assertEqual(interpret('G()(al)'), 'Goal')
    
    def test_example2(self):
        self.assertEqual(interpret('G()()()()(al)'), 'Gooooal')
    
    def test_example3(self):
        self.assertEqual(interpret('(al)G(al)()()G'), 'alGalooG')