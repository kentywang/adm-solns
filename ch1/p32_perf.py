# 9/30 6:45 - 9:00
from operator import floordiv
from random import randint, choice

from ch1.p32 import intdiv
from profiler import Profiler
from util import red, reset_color


for n in map(int, [1e5, 2e5, 4e5]):
    print(f'{red}n: {n}{reset_color}')

    with Profiler(floordiv) as f:
        for _ in range(100):
            f(randint(-n, n), choice(list(set(range(-n, n + 1)) - {0})))

    with Profiler(intdiv) as f:
        for _ in range(100):
            f(randint(-n, n), choice(list(set(range(-n, n + 1)) - {0})))

# Analysis
# Mine runs at same time complexity O(n) as the builtin,
# but mine does it at O(1) space complexity instead of O(n).
