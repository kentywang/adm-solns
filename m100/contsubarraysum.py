"""
20m?
11:25 - 11:46 (n^2 soln, no work)

Observations:
- for range (i, j), the sum is (prefix sum to i-1) + (suffix sum to j+1)
- if we can't find a better heuristic, do brute force pairing [O(n^2)] and check
    each pair for validity using above technique [O(1)]
- Time: O(n^2)
- Space: O(2n)
"""


# [23, 2, 4, 6, 7]
# 23 25 29 35 42
# 5  1  5

class Solution:
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     prefix = list(accumulate(nums))
    #     suffix = list(reversed(list(accumulate(list(reversed(nums))))))  # TODO: optimize
    #     total = prefix[-1]

    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             a = prefix[i-1] if i - 1 >= 0 else 0
    #             b = suffix[j+1] if j + 1 < len(nums) else 0
    #             range_sum = total - a - b
    #             if (range_sum / k).is_integer():
    #                 return True
    #     return False
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        acc = 0
        mods = {
            0: -1}  # we don't want to have it 0:0 else if first element mods to 0, then false positive. We want a distance of two
        for i, n in enumerate(nums):
            acc += n
            element = acc % k
            if element in mods and i - mods[element] >= 2:
                return True
            if element not in mods:
                mods[element] = i
        return False
