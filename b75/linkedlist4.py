from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        T: O(n)
        S: O(1)

        optimizations left to do:
        n = 1 case : no reversals necessary at all

        47 min solution

        okay, this was a stupid way. I could've never reversed it in the first place. and just did two forward passes)
        """

        def reverse(node):
            count = 0
            prev, curr = None, node

            while curr:
                tmp, curr.next = curr.next, prev
                prev, curr = curr, tmp

                count += 1
            return prev, count

        # reverse to get count, then get head again (stored as curr)
        curr, count = reverse(reverse(head)[0])

        # now we know the length, we can see how many nodes away the nth node from the end is
        m = count - n
        prev = None

        while m != 0:
            prev = curr
            curr = curr.next
            m -= 1

        if prev:
            prev.next = curr.next
        else:
            # 1st node removal case
            head = curr.next

        return head
