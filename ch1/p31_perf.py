from ch1.p31 import gen_tix_v1, gen_tix_v2
from profiler import Profiler
from util import reset_color, red


def test_perf():
    results = []

    for n in [4, 5, 6]:
        arg = {"numpool": n, "slots": 3, "win_thresh": 2}
        print(f'{red}n: {n}{reset_color}')

        with Profiler(gen_tix_v1) as f:
            v1 = f(**arg)
        with Profiler(gen_tix_v2) as f:
            v2 = f(**arg)

        results.append((len(v1), len(v2)))

    print(results)


test_perf()

# Analysis
# Random selection heuristic offer worser results, and takes much longer as
# the number pool increases. Consider adding a smarter way of picking new
# tickets.

# Results
# n: 4
# gen_tix_v1: 4 KiB, 0 ms
# gen_tix_v2: 0 KiB, 0 ms
# n: 5
# gen_tix_v1: 588 KiB, 12 ms
# gen_tix_v2: 0 KiB, 0 ms
# n: 6
# gen_tix_v1: 834532 KiB, 2044 ms
# gen_tix_v2: too long