import sys
from itertools import islice
from random import randint

from profilerv2 import ProfilerV2
from util import asserter


def selsort(s):
    """
    O(1) space, unbelievably
    - range() runs to completion, but should be O(1) since it isn't captured in a list
    - islice doesn't make intermediate list
    - enumerate makes an iterator of O(1) space
    - min() on the enumerate will work piecemeal I think, so no intermediate list either
    """
    n = len(s)
    if n < 2:
        return s
    for i in range(n):
        # compare values, but only care about index afterwards
        j, _ = min(enumerate(islice(s, i, sys.maxsize), i), key=lambda x: x[1])
        s[i], s[j] = s[j], s[i]
    return s


def selsortv2(s):
    """
    O(1) space
    """
    n = len(s)
    if n < 2:
        return s
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if s[j] < s[m]:
                m = j
        s[m], s[i] = s[i], s[m]
    return s


def insort(s):
    """
    O(1) space
    """
    n = len(s)
    if n < 2:
        return s
    for i in range(1, n):
        for j in reversed(range(i + 1)):
            if s[j - 1] > s[j]:
                s[j - 1], s[j] = s[j], s[j - 1]
            else:  # terminate early once we've slotted it in the sorted place
                break
    return s


def test_perf(*fns):
    for fn in fns:
        ls = [4, 2, 1, 3, 1]
        expected = sorted(ls)
        asserter(lambda: fn(ls), expected)

        with ProfilerV2(fn, start=500, mapper=lambda n: [randint(0, 100) for _ in range(n)]) as (f, n):
            f(n)


test_perf(selsort, selsortv2, insort)

# selsort
# n: 500                4 KiB               13866 µs
# n: 1000               0 KiB  (0.0x)       53853 µs  (3.88x)
# n: 2000               0 KiB              212470 µs  (3.95x)
# n: 4000               0 KiB              848582 µs  (3.99x)
# selsortv2
# n: 500                0 KiB                6838 µs
# n: 1000               0 KiB               28246 µs  (4.13x)
# n: 2000               0 KiB              111385 µs  (3.94x)
# n: 4000               0 KiB              457888 µs  (4.11x)
# insort
# n: 500                0 KiB               11275 µs
# n: 1000               0 KiB               46694 µs  (4.14x)
# n: 2000               0 KiB              211071 µs  (4.52x)
# n: 4000               0 KiB              814888 µs  (3.86x)
