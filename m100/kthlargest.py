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


# 9:20 - 9:52 (32m)
# k=1 => 6
# k=2 => 5
# k=3,4,5 => 4
# [3,2,1,4,5,4,6,4]
#        ^
#                 ^
""" 
             k
        [1,2,3]
slow         ^
fast       ^
piv          ^
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def lomuto_partition(i, j):
            piv = j
            slow = i
            for fast in range(i, j):
                # <= :: makes pivot the largest of its val
                # < :: makes pivot smallest of its val
                if nums[fast] <= nums[piv]:
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                    slow += 1
            nums[piv], nums[slow] = nums[slow], nums[piv]
            return slow

        i = 0
        j = len(nums) - 1
        k = len(nums) - k  # reverse the k, make k = 0 mean smallest el
        while i < j:
            piv = lomuto_partition(i, j)
            if piv == k:
                break
            if piv > k:
                j = piv - 1
            elif piv < k:
                i = piv + 1

        return nums[k]


# -----------------------------> k = 3 - 1 = 2     , piv = 0


# 9:55 - 10:01 (6m)
from heapq import heapify, heappop

"""
[-6,3,2,1,5,6,4], k = 2

Time: O(n + k lg n)
Space: O(n)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-1 * x for x in nums]
        heapify(pq)

        while k:
            res = heappop(pq)
            k -= 1

        return -1 * res


print(Solution().findKthLargest([5, 2, 7, 3, 1, 9, 4, 6, 8, 0], 9))
