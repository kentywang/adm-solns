import sys
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        T: O(k * 500k)
        S: O(k)
        """
        dummyhead = ListNode(val=0)
        prev = dummyhead

        while any(lists):
            # dummy values, will be overridden
            smallest = ListNode(val=sys.maxsize)
            i = -1

            for j, p in enumerate(lists):
                if p is not None and p.val < smallest.val:
                    smallest = p
                    i = j

            prev.next = smallest
            prev = smallest
            lists[i] = smallest.next  # increment pointer (of node we just appended to result) to next LL node

        return dummyhead.next


x = Solution().mergeKLists([
    ListNode(val=1, next=ListNode(val=3)),
    ListNode(val=2),
    None
])
