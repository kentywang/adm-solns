"""
0:04 - 0:31 (27m)

Edges:
- √ should insert at start of node
- √ should insert at end
- √ just one other node
- same val throughout LL
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newnode = Node(insertVal)

        # n = 0
        if not head:
            newnode.next = newnode
            return newnode

        # n = 1
        if head.next == head:
            head.next = newnode
            newnode.next = head
            return head

        pred, succ = head, head.next
        while pred.val <= succ.val:
            pred, succ = succ, succ.next
            # below condition checks if we've traveresed the entire
            # LL without successfully finding a high or low
            # by seeing if we've looped back to the start
            if pred == head:
                newnode.next = succ
                pred.next = newnode
                return head

        # predecessor is now bigger that successor, meaning
        # successor is the loop start and smallest element

        # insert if it's an extremity
        if insertVal <= succ.val or pred.val <= insertVal:
            newnode.next = succ
            pred.next = newnode
            return head

        # if it's somewher in the middle, traverse until it fits
        while not (pred.val <= insertVal <= succ.val):
            pred, succ = succ, succ.next

        newnode.next = succ
        pred.next = newnode
        return head
