# 9/1/22 8:30
# v1: 11:00
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
    pass
