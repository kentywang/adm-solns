# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
"""
Planning:   21:11 - 21:29   (18m)
Coding + fixing: - 21:55    (26m)

Observations:
- recursion will let us handle this generally
- have a fixed length of 50 array, where each index corresponds to a depth. Element is the current value at that depth. We can combine mix them even if they are on different lists because of distributive property of multiplication ab + ac = a(b + c)
- for each item we either have a num or a list, if list we recurse down and pass it the depth (O(d) space)
- after iterating, mult the value of each element in array with its index. Sum the products.

Time: O(n)
Space: O(d)

Cases:
- [9]
- [[[7]], 1, [4, 6]] => 1*1 + 10*2 + 7*3 = 42
"""
from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depthvals = [0] * 50

        def recurse(nested, d):
            for i in range(len(nested)):
                if nested[i].isInteger():
                    depthvals[d] += nested[i].getInteger()
                else:
                    recurse(nested[i].getList(), d + 1)

        recurse(nestedList, 0)

        return sum(v * (i + 1) for i, v in enumerate(depthvals))


# ---------------------------------------
"""
21:12 - 21:19 (7m)
Time: O(n)
Space: O(d)
"""


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def recurse(depth, arr):
            ans = 0
            i = 0
            while i < len(arr):
                if arr[i].isInteger():
                    ans += depth * arr[i].getInteger()
                else:
                    ans += recurse(depth + 1, arr[i].getList())
                i += 1
            return ans

        return recurse(1, nestedList)
