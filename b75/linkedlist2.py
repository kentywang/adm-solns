# 21. Merge Two Sorted Lists
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Theoretical optimal:

Time: O(min(n, m))
Space: O(1) (just pointer manip, no new data)

Plan: simultaneous iteration on both LLs. Put the smaller element on the buildup, and iterate once on the LL of the smaller element.
If both elements are the same, put both on and iterate on both. 
If one is empty, the built-up LL is hooked up to the remainder of the leftover LL.

EDIT: Seems this could be simplified if we used one dummy node to attach elements to. That way, we don't need branching
logic for the initial head element case. 
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        result = None
        result_tail = result

        while list1 and list2:
            x, y = list1.next, list2.next  # save refs to the rest of the LLs

            if list1.val <= list2.val:
                if not result:
                    result = list1  # empty result, so set it to this once and forever
                else:
                    result_tail.next = list1
                list1.next = None  # sever ref to rest of LL
                result_tail = list1  # update result_tail with latest change
                list1 = x  # iterate on smaller element's LL
            else:
                if not result:
                    result = list2  # empty result, so set it to this once and forever
                else:
                    result_tail.next = list2
                list2.next = None  # sever ref to rest of LL
                result_tail = list2  # update result_tail with latest change
                list2 = y  # iterate on smaller element's LL

        # if we run out of one LL, paste the remaining LL to result_tail
        if not list1: result_tail.next = list2
        if not list2: result_tail.next = list1

        return result
