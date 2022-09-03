from random import randint

from ch1.lc1 import daily_temperatures_v1, daily_temperatures_v2, daily_temperatures_lc
from profiler import Profiler
from util import reset_color, red


def test_perf():
    for n in [10000, 20000, 40000, 80000]:
        temps = list(randint(0, 100) for _ in range(n))
        print(f'{red}n: {n}{reset_color}')

        with Profiler(daily_temperatures_v1, temps) as f:
            v1 = f()
        with Profiler(daily_temperatures_v2, temps) as f:
            v2 = f()
        with Profiler(daily_temperatures_lc, temps) as f:
            v3 = f()

        assert v1 == v2 == v3

test_func()
test_perf()

# v1: O(1) space, O(n^2) time
# v2: O(1) space, O(n^2) time
# lc: O(1) space, O(n) time
