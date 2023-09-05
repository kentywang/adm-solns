# 141. Linked List Cycle
from typing import Optional

from util import asserter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Brute force:
Hash each node, store it. Compare against it during iteration.

Time: O(n)
Space: O(n)

Better soln:
Double pointers, one iterates twice per loop. Guaranteed to eventually land on the same node.
By the time the slower pointer reaches the end, the faster should've passed it if there was a loop.

Time: O(n)
Space: O(1)
"""


class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if not head:
    #         return False
    #
    #     hashset = set()
    #
    #     while head:
    #         if head in hashset:
    #             return True
    #
    #         hashset.add(head)
    #         head = head.next
    #
    #     return False
    #
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # special case 1: n = 0
        # special case 2: n = 1
        if not head or not head.next:
            return False

        # offset starting positions of ptrs so that our check doesn't erroneously report a loop immediately.
        # faster ptr starts first so no collisions happen until/if we enter loop
        p1 = head
        p2 = head.next

        # p2 should terminate first if non-loop, so no need to check p1 termination
        while p2 and p2.next:
            if p1 is p2:
                return True

            p1 = p1.next
            p2 = p2.next

            if not p2.next:
                return False

            p2 = p2.next

        return False


asserter(lambda: Solution().hasCycle(None), False)
asserter(lambda: Solution().hasCycle(ListNode(1)), False)

x = ListNode(1)
x.next = x
asserter(lambda: Solution().hasCycle(x), True)

y = ListNode(1)
y.next = ListNode(2)
asserter(lambda: Solution().hasCycle(y), False)
y.next.next = y
asserter(lambda: Solution().hasCycle(y), True)
