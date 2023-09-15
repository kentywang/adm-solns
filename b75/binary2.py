from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2

        while target not in {nums[lo], nums[mid], nums[hi]}:
            if mid == lo:
                return -1

            a = nums[lo]
            b = nums[mid]
            c = nums[hi]

            # no pivot case
            if a <= b <= c:
                if target <= b:
                    hi = mid
                else:
                    lo = mid

            # left unsorted
            elif a >= b:
                if b <= target <= c:
                    lo = mid
                else:
                    hi = mid

            # right unsorted (b > c)
            else:
                if a <= target <= b:
                    hi = mid
                else:
                    lo = mid

            mid = (lo + hi) // 2

        if nums[lo] == target:
            return lo
        if nums[mid] == target:
            return mid
        return hi


x = Solution().search([1, 3], 2)
