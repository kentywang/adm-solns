# 55. Jump Game
from functools import cache
from typing import List


class Solution:
    """
    Time (caching): O(min(length of nums, value of nums))
    Time (no cache): O(value of nums ** length of nums)
    Space: O(length of nums)
    """

    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        @cache
        def greedy(i):
            if i >= end:
                return True
            return any(
                greedy(i + dist) for dist in range(nums[i], 0, -1))  # start from highest dist

        return greedy(0)
