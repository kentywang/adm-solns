# 217. Contains Duplicate

class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
