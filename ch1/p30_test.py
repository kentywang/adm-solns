from unittest import TestCase

from ch1.p30 import nearest_neighbor, closest_pair

graph1 = [(0, 0), (0, 1), (0, -2), (0, 5), (0, -10), (0, 21)]  # shortest is 31 * 2 = 62
graph2 = [(-3, 0), (-3, 1), (0, 0), (0, 1), (3, 0), (3, 1)]  # shortest is 6 + 6 + 1 + 1 = 14


class P30(TestCase):

    def test_func(self):
        # graph1: expect 1 + 3 + 7 + 15 + 31 + 21 = 78
        # graph2: expect 9 + sqrt(37) = 15.1
        for given, expected in zip([graph1, graph2], [78, 15.1]):
            with self.subTest(given):
                self.assertAlmostEqual(nearest_neighbor(given)[1], expected, places=1)

        # graph1: expect 62
        # graph2: expect 15.1
        for given, expected in zip([graph1, graph2], [62, 15.1]):
            with self.subTest(given):
                self.assertAlmostEqual(closest_pair(given)[1], expected, places=1)
