from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        best = 0

        while i < j:

            left = height[i]
            right = height[j]

            best = max(best, (j - i) * min(left, right))

            if left <= right:
                i += 1
            if left >= right:
                j -= 1

        return best


print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))
