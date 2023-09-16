import sys
from queue import PriorityQueue
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        T: O(kn)
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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Note: this is Python2 code
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


x = Solution().mergeKLists([
    ListNode(val=1, next=ListNode(val=3)),
    ListNode(val=2),
    None
])
