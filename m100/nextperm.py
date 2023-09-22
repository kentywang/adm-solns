"""
Planning    8:54 - 9:27 (33m)
Coding      ??? - 10:07 (30m?)
Debug       - 10:32     (25m) tricky because of 2ndary comparison by index when I did min()

Option:
- RTL pointer
- if strictly decreasing since prev, swap immediately those two vals
- if incrementing
    - if reach end and still incrementing, reverse entire array [O(n) : O(1)]
    - if find decrement while incrementing, find the next largest number to the decrement
        number in the range (using binary search), swap with it, then reverse the array
- invariant:
    -

Examples:
[1] => no incr/decr; return self [corner case]
[2, 3] => decr; swap immediately to [3,2]
[2, 2] => no decr; reverse array (or do nothing)
[2, 3, 2, 2, 1] => decr at index 0; find largest (3), swap to [3, 2, 2, 2, 1], then reverse the explored range
"""

"""
Planning    8:54 - 9:27 (33m)
Coding      ??? - 10:07 (30m?)
Debug       - 10:32     (25m) tricky because of 2ndary comparison by index when I did min()

Option:
- RTL pointer
- if strictly decreasing since prev, swap immediately those two vals
- if incrementing
    - if reach end and still incrementing, reverse entire array [O(n) : O(1)]
    - if find decrement while incrementing, find the next largest number to the decrement
        number in the range (using binary search), swap with it, then reverse the array
- invariant:
    - 

Examples:
[1] => no incr/decr; return self [corner case]
[2, 3] => decr; swap immediately to [3,2]
[2, 2] => no decr; reverse array (or do nothing)
[2, 3, 2, 2, 1] => decr at index 0; find largest (3), swap to [3, 2, 2, 2, 1], then reverse the explored range
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1:
            return nums

        def reverseFrom(idx):
            lo = idx
            hi = n - 1
            while lo < hi:
                nums[hi], nums[lo] = nums[lo], nums[hi]
                lo += 1
                hi -= 1

        def findSuccessor(x):
            """
            replace with binary search for better perf
            """
            j = n - 1
            while nums[j] <= x:
                j -= 1
            return j

        # -------------------------------- [1, 2] 1, 1     (1, 0)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            # reached the lexological end of this entire sequence, so reverse it
            reverseFrom(i + 1)
            return

        # else condition is that nums[i] < nums[i + 1]
        j = findSuccessor(nums[i])
        nums[i], nums[j] = nums[j], nums[i]
        reverseFrom(i + 1)
        return
