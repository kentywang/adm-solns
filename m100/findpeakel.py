"""
Planning    ???
Coding  8:37 - 8:47 (10m)
One timer!
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        # invariant: lo is incrementing, hi is decrementing
        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] < nums[mid + 1]:  # incrementing, so choose right half
                lo = mid + 1
            else:  # decrementing, so choose left half
                hi = mid
        return lo
# ------------------ 1 2 {3 4}   l=3 h=3 m=2,3
