from typing import List


class Solution:
    """
    T: O(lg n)
    S: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return []

        lo = 0
        hi = len(nums) - 1

        # the edge case where it's not rotated
        if nums[lo] < nums[hi]:
            return nums[lo]

        while (mid := (lo + hi) // 2) != lo:
            if nums[lo] > nums[mid]:
                hi = mid
            else:  # b is definitely greater than c, so reduce problem to this area
                lo = mid

        # only 2 elements left, so pick the smaller
        return min(nums[lo], nums[hi])


x = Solution().findMin([11, 13, 15, 17])
print(x)

x = Solution().findMin([3, 4, 5, 1, 2])
print(x)
