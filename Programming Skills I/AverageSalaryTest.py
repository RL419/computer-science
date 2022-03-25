from unittest import TestCase
from AverageSalary import average_salary

class TestAverageSalary(TestCase):
    def test_default(self):
        self.assertEqual(average_salary([4000, 3000, 1000, 2000]), 2500)
    
    def test_big_list(self):
        self.assertEqual(average_salary([1000, 2000, 3000, 4000, 5000, 6000, 7000]), 4000)