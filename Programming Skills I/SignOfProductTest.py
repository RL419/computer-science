from unittest import TestCase
from SignOfProduct import sign_of_product

class TestSOP(TestCase):
    def test_zero(self):
        self.assertEqual(sign_of_product([1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]), 0)
    
    def test_all_positive(self):
        self.assertEqual(sign_of_product([100, 22,69,96,73,45,25,10,7,9,14,73,1,27,84,47,36]), 1)
    
    def test_even_negative(self):
        self.assertEqual(sign_of_product([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]), 1)

    def test_odd_negative(self):
        self.assertEqual(sign_of_product([-1,-2,-3,-4,-5,-6,-7,-8,-9]), -1)

    def test_long_list(self):
        self.assertEqual(sign_of_product([i for i in range(1, 101)]), 1)

    def test_long_list2(self):
        l = [i for i in range(1, 101)]
        l.append(-1)
        self.assertEqual(sign_of_product(l), -1)