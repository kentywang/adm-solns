# 9/1/22 8:30
# v1: 11:00
# v2: 9/2 11:59π
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Custom class
class DoublyListNode(ListNode):
    def __init__(self, val=0, prev=None, next=None):
        super().__init__(val, next)
        self.prev = prev


def rotate_right_v1(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    O(n) space, O(n+k) time
    """
    # both these conditions necessary for below code not to trip an exception
    # their speeding up the computation is just a side effect
    if not head:
        return None
    if not head.next:
        return head

    curr = head
    dhead = dcurr = DoublyListNode(curr.val)
    while curr.next:
        curr = curr.next
        dcurr.next = DoublyListNode(val=curr.val, prev=dcurr)
        dcurr = dcurr.next
    dtail = dcurr

    for _ in range(k):
        # order matters here
        dtail.prev.next, dtail.next, dhead.prev = None, dhead, dtail
        dhead, dhead.prev, dtail = dtail, None, dtail.prev

    # rebuild new singly node
    dcurr = dhead
    nhead = ncurr = ListNode(dcurr.val)
    while dcurr.next:
        dcurr = dcurr.next
        ncurr.next = ListNode(dcurr.val)
        ncurr = ncurr.next
    return nhead


def rotate_right_v2(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Notice only 3 operations for call of any n or k.
        - Set list[-1] node to point to list[0]
        - Set head to list[-k]
        - Unset list[-k-1]'s .next pointer

    To reduce operations further, notice:
        - When k > n, we can set k := k - n for the same result

    O(1) space, O(n) time
    """

    def ll_len(listnode):
        length = 0
        while listnode:
            length += 1
            listnode = listnode.next
        return length

    if not head:
        return head

    n = ll_len(head)
    k %= n

    if k == 0:
        return head

    # get tail, l[-k] (newhead) and l[-k-1] (newtail)
    curr = head
    i = 0
    while i < n:
        if i == n - k - 1:  # Notice when using offsets (k) with list lengths, we don't need to factor in 0-indexing
            newtail = curr
            newhead = curr.next
        if i == n - 1:
            tail = curr
        curr = curr.next
        i += 1

    tail.next = head  # link tail to head (makes a ring)
    newtail.next = None  # sever a connection to form a new tail (returns it to a finite list)
    return newhead  # return front end of that new list
