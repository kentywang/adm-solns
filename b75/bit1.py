# 191. Number of 1 Bits
from util import asserter

"""
Time: O(lg n) (when n is decimal. if n is binary, then O(n))
Space: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            digit = n & 1  # mask everything but first digit
            count += digit
            n >>= 1  # this won't reverse sign, because we aren't doing unsigned right shift (>>>)
        return count


asserter(lambda: Solution().hammingWeight(11), 3)  # ...1011
asserter(lambda: Solution().hammingWeight(128), 1)  # ...10000000
asserter(lambda: Solution().hammingWeight(4294967293), 31)  # ...11111111111111111111111111111101
