# 128. Longest Consecutive Sequence
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = {}

        for n in nums:
            longest[n] = 0

        def check_prev(n):
            if n - 1 in longest:
                if longest[n - 1] == 0:
                    check_prev(n - 1)

                longest[n] = longest[n - 1] + 1
            else:
                longest[n] = 1

        for n, length in longest.items():
            check_prev(n)

        return max(longest.values()) if longest else 0


x = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(x)

x = Solution().longestConsecutive([1, 3, 5, 8, 7, 2, 4, 6])
print(x)
