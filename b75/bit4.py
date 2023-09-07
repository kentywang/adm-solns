# 268. Missing Number
from typing import List

"""
n numbers from [0, n] means they sum to 1+2+...+n. Diff that with actual sum to find the missing number.

Time: O(n)
Space: O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # We won't lose any data by floor dividing because n * (n+1) is always even. This just is for casting it to int.
        ev = n * (n + 1) // 2
        av = sum(nums)  # O(n)
        return ev - av


Solution().missingNumber([3, 0, 1])
