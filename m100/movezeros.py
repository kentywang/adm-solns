def moveZerosToEnd(arr):
    p1, p2 = 0, 0

    while p1 < len(arr):

        while arr[p1] != 0:
            p1 += 1
            p2 = max(p1, p2)
            if p1 == len(arr):
                return arr
        # at this point, p1 is at a 0

        while arr[p2] == 0:
            p2 += 1
            if p2 == len(arr):
                return arr

        # p2 is now at a non 0, so swap
        arr[p1], arr[p2] = arr[p2], arr[p1]

    return arr


print(moveZerosToEnd([1, 0, 5, 6, 0, 10, 0]))


# Online, excellent
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
