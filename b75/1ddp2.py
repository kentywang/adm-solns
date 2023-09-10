# 198. House Robber
from typing import List

from util import asserter


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Each dp cell represents the max money possible if considering up to that house.
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        # dp will be offset by +1 to make room for extra beginning 0 cell
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])  # first arg is if we rob, second is if we pass

        return dp[-1]


asserter(lambda: Solution().rob([2, 7, 9, 3, 1]), 12)
asserter(lambda: Solution().rob([1]), 1)
