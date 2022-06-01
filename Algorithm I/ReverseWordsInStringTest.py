from unittest import TestCase
from ReverseWordsInString import reverse

class TestReverse(TestCase):
    def test1(self):
        self.assertEqual(reverse("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
    
    def test2(self):
        self.assertEqual(reverse("God Ding"), "doG gniD")
    
    def test(self):
        self.assertEqual(reverse('abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba'), 'abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba')