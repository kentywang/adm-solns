from typing import List

"""
Planning/research on Quickselect
21:30 - 22:40 (70m)
Coding - 23:48 (68m)

Verdict: Couldn't even pass LC's tests because Lomuto doesn't handle duplicates well (even if I randomize the pivot index). Still learn a bunch though.

Observations:
Time            : space
- O(k log n)    : O(n)      with n-sized heap (trivial)
- O(n log k)    : O(k)      with k-sized heap
- O(n)          : O(1)      using quickselect

"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def lomuto_partition(x, y):
            """
            returns index of partition
            """
            pivot = nums[y]  # pick right most val as pivot
            i = x  # left pointer, kept on the leftmost value bigger than the pivot, only advances after a swap
            for j in range(x, y):  # right pointer
                if nums[j] <= pivot:  # found a value at j to put in the left partition, so swap with i
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            # finally, swap pivot val with val where i ends up
            nums[i], nums[y] = nums[y], nums[i]
            return i

        n = len(nums)
        k = n - k  # converts problem to kth smallest element from this point on
        lo = 0
        hi = n - 1

        while True:
            pividx = lomuto_partition(lo, hi)
            if k == pividx:
                return nums[pividx]
            if k < pividx:
                hi = pividx - 1
            else:
                lo = pividx + 1


print(Solution().findKthLargest([5, 2, 7, 3, 1, 9, 4, 6, 8, 0], 9))
