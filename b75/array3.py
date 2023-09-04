# 1. Two Sum

from util import asserter


class Solution:
    def twoSumV2(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O(n)
        Space: O(n)

        Verdict: Wow, much simpler than my binary search approach, also faster too. So when in doubt, hash it, I guess.
        """
        tbl = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in tbl:
                return [tbl[diff], i]
            else:
                tbl[n] = i

    """
    Time: O(n lg n)
    Space: O(n) (since we need to maintain sorted version)

    Verdict: More complicated to implement than I expected, because of the need to exclude one element from the
    binary search and also maintain the original indices of the list.
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # O(n log n)
        dictionary = \
            sorted(
                ({"index": i, "number": n} for i, n in enumerate(nums)),
                key=lambda x: x["number"])
        sorted_nums = list(d["number"] for d in dictionary)

        # another O(n log n)
        for i, n in enumerate(dictionary):
            res = self.binary_search(sorted_nums, i, target - n["number"])
            if res != -1:
                a = dictionary[i]["index"]
                b = dictionary[res]["index"]
                return [a, b] if a <= b else [b, a]

    def binary_search(self, nums, skip, val):
        """
        finds the idx of the value in the array, or returns -1 if nonexistent

        Time: O(lg n)
        Space: O(1)
        """
        l = len(nums)
        start = 0 if skip != 0 else 1
        end = l - 1 if skip != l - 1 else l - 2

        while end >= start:
            mid = (end + start) // 2
            if mid == skip:
                mid += 1

            if val == nums[mid]:
                return mid
            if val > nums[mid]:
                start = mid + 1 if skip != mid + 1 else mid + 2
            else:
                end = mid - 1 if skip != mid - 1 else mid - 2

        return -1


asserter(lambda: Solution().twoSumV2([2, 7, 11, 15], 9), [0, 1])
asserter(lambda: Solution().twoSumV2([3, 2, 4], 6), [1, 2])
asserter(lambda: Solution().twoSumV2([3, 3], 6), [0, 1])
asserter(lambda: Solution().twoSumV2([1, 2, 3, 3, 10], 6), [2, 3])
asserter(lambda: Solution().twoSumV2([-1, -2, -3, -4, -5], -8), [2, 4])
