from unittest import TestCase
from NonOverlappingIntervals import no_overlap


class TestOverlap(TestCase):
    def test_1(self):
        self.assertEqual(no_overlap([[1,2],[2,3],[3,4],[1,3]]), 1)
    def test_2(self):
        self.assertEqual(no_overlap([[1,2],[1,2],[1,2]]), 2)
    def test_3(self):
        self.assertEqual(no_overlap([[1,2],[2,3]]), 0)