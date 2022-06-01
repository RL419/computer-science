from unittest import TestCase
from DailyTemperatures import dailyTemp

class TestDT(TestCase):
    def test_1(self):
        self.assertEqual(dailyTemp([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    def test_2(self):
        self.assertEqual(dailyTemp([30,40,50,60]), [1,1,1,0])
    def test_3(self):
        self.assertEqual(dailyTemp([30,60,90]), [1,1,0])