from unittest import TestCase
from EvaluateRPN import evaluate

class TestRPN(TestCase):
    def test_1(self):
        self.assertEqual(evaluate(["2","1","+","3","*"]), 9)

    def test_2(self):
        self.assertEqual(evaluate(["4","13","5","/","+"]), 6)

    def test_3(self):
        self.assertEqual(evaluate(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)