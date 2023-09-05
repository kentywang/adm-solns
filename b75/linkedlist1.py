# 206. Reverse Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Brute force:
    Iterate through LL, building a stack. Then LIFO the stack to generate a new LL.
    Time: O(n) (2 passes of n)
    Space: O(n) (stack, and also return LL)

    Recursive:
    Time: O(n) (1 pass, actually maybe 2 passes since we have to return from the recursion and do more work)
    Space: O(n) (just call stack; otherwise we're just manipulating the refs within the original LL, so no space cost from that)

    Verdict: Somewhat tricky. Thought the solution was inelegant until I realized I didn't need to duplicate any code between the
    outer and the inner functions.

    EDIT: There's another way to do this iteratively, building a new LL tail-first as we touch each node, accomplishing
    the same as the recursive but with O(1) space, since it's also just doing pointer manipulation. (See reverseListV2)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Some validation here allows just to treat the LL going forward as always having a head
        if head is None or head.next is None:
            return head

        def inner(h: ListNode) -> (ListNode, ListNode):
            if h.next is None:
                return h, h

            inner_rest_head, inner_rest_tail = inner(h.next)
            h.next = None
            inner_rest_tail.next = h

            return inner_rest_head, inner_rest_tail.next

        return inner(head)[0]

    def reverseListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        while head:
            rest = head.next  # save the ref to the rest of the LL
            head.next = result  # unhook the head from the LL, put on 2nd LL that we're building
            result = head  # assign result to the head of that 2nd LL now
            head = rest  # iterate to next node on the original LL
        return result


# Not sure why these aren't passing
# asserter(lambda: Solution().reverseList(None), None)
# asserter(lambda: Solution().reverseList(ListNode(1)), ListNode(1))
# asserter(lambda: Solution().reverseList(ListNode(1, ListNode(2))), ListNode(2, ListNode(1)))
# asserter(lambda: Solution().reverseList(ListNode(1, ListNode(2, ListNode(3)))), ListNode(3, ListNode(2, ListNode(1))))

x = Solution().reverseListV2(ListNode(1))
xx = Solution().reverseListV2(ListNode(1, ListNode(2)))
xxx = Solution().reverseListV2(ListNode(1, ListNode(2, ListNode(3))))
xxxx = 'EOF'
