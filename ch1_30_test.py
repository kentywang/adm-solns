from unittest import TestCase

from ch1_30 import nearest_neighbor, closest_pair
from random import randint

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

    def test_perf(self):
        def randgridsz(sz):
            return [(randint(-sz, sz), randint(-sz, sz)) for _ in range(0, sz)]

        for n in [50, 100, 200]:
            g = randgridsz(n)
            with self.subTest(input):
                print(f'\033[0;31mn: {n}\033[0m')
                print(nearest_neighbor(g)[1])
                print(closest_pair(g)[1])

# Results
# n: 100
# nearest_neighbor: 4 KiB, 3 ms
# 2023.768245164767
# closest_pair: 4272 KiB, 356 ms
# 2039.4096178628715
# n: 200
# nearest_neighbor: 4 KiB, 15 ms
# 5663.23900541345
# closest_pair: 11704 KiB, 2821 ms
# 4814.492834218646
# n: 400
# nearest_neighbor: 0 KiB, 65 ms
# 15298.839718985993
# closest_pair: 48964 KiB, 23200 ms
# 14352.34495753338

# Analysis
# Closest pair returns slightly better results at the cost of much more time and space usage.
# I'll pass on coming up with my own heuristic, seeing as it already took a while to implement these two.
