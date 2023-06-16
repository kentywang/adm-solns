import math
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
        """
        O(n) time, O(n) space
        """
        result = [0] * (n + 1)
        for i, _ in enumerate(result):
            if i == 0:
                continue
            result[i] = result[self.getLowerIdx(i)] + 1
        return result

    def getLowerIdx(self, x: int) -> int:
        y = math.log2(x)
        y2 = math.floor(y)
        if y == y2:
            return 0
        return x - pow(2, y2)


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
