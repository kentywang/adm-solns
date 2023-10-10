"""
11:00 - 11:26 (26m)
One timer

Time: O(n)
Space: O(n)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        while curr:
            clone = Node(curr.val, next=curr.next)
            curr.next = clone
            curr = clone.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        orig = head
        clone = head.next
        clonehead = clone

        while orig:
            orig.next = orig.next.next
            if clone.next:
                clone.next = clone.next.next
            orig = orig.next
            clone = clone.next

        return clonehead
