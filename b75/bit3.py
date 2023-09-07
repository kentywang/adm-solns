# 190. Reverse Bits
from util import asserter

"""
Time: O(1) (32 passes)
Space: O(1) (max is 32 bits)
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            val = n & 1  # mask everything but first digit
            res = (res << 1) | val  # add it to res, shifting everything left to make room for it
            n >>= 1  # make way for next digit

        return res


asserter(lambda: Solution().reverseBits(43261596), 964176192)
asserter(lambda: Solution().reverseBits(4294967293), 3221225471)
π
