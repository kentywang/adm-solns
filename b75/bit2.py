# 338. Counting Bits
from typing import List

from profilerv2 import ProfilerV2
from util import asserter

"""
x     :     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
lg(x) :     -  0  1     2           3                       4
f(x)  :     0  1  1  2  1  2  2  3  1  2  2  3  2  3  3  4  1
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


dummy = Solution()
asserter(lambda: dummy.countBits(0), [0])
asserter(lambda: dummy.countBits(1), [0, 1])
asserter(lambda: dummy.countBits(2), [0, 1, 1])
asserter(lambda: dummy.countBits(3), [0, 1, 1, 2])
asserter(lambda: dummy.countBits(5), [0, 1, 1, 2, 1, 2])
asserter(lambda: dummy.countBits(7), [0, 1, 1, 2, 1, 2, 2, 3])
asserter(lambda: dummy.countBits(8), [0, 1, 1, 2, 1, 2, 2, 3, 1])

with ProfilerV2(dummy.countBits, var='n', start=1, step=(lambda x: x * 10), count=5, reps=10) as (f, n):
    f(n)
