from unittest import TestCase
from AddtoArrayFormInt import add_to_array_form_int

class TestATAFI(TestCase):
    def test1(self):
        self.assertEqual(add_to_array_form_int([1,2,0,0], 34), [1,2,3,4])
    def test2(self):
        self.assertEqual(add_to_array_form_int([2,7,4], 181), [4,5,5])
    def test3(self):
        self.assertEqual(add_to_array_form_int([2,1,5], 806), [1,0,2,1])