from random import randint

from ch1.p30 import nearest_neighbor, closest_pair
from profiler import Profiler


def test_perf():
    def randgridsz(sz):
        return [(randint(-sz, sz), randint(-sz, sz)) for _ in range(0, sz)]

    results = []

    for n in [50, 100, 200]:
        g = randgridsz(n)
        print(f'\033[0;31mn: {n}\033[0m')

        with Profiler(nearest_neighbor, g) as f:
            nn = f()[1]
        with Profiler(closest_pair, g) as f:
            cp = f()[1]

        results.append((int(nn), int(cp)))

    print(results)


test_perf()

# Analysis
# Closest pair returns usually slightly better results to nearest neighbor at the cost of much more time and
# space usage. I'll pass on coming up with my own heuristic, seeing as it already took a while to implement these two.

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