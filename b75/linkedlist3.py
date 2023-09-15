"""
- fetch takes O(n) time, O(1) space if TCRO or iterative
- fetch can be O(1) time, O(n) space if we keep refs on a stack
"""
from typing import Optional

"""
Trickier than I expected.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        while curr:
            last = stack.pop()

            if last == curr or last == curr.next:
                last.next = None
                break

            subsequent = curr.next
            curr.next = last
            last.next = subsequent

            curr = subsequent

        return head


x = Solution().reorderList(ListNode(1))
x = Solution().reorderList(ListNode(1, ListNode(2)))
x = Solution().reorderList(ListNode(1, ListNode(2, ListNode(3))))
x = Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
