from typing import Any

from util import asserter


class Node:
    def __init__(self, key: Any, nxt=None):
        self.key = key
        self.next = nxt

    def __eq__(self, other):
        return self.key == other.key and self.next == other.next


# [1,*]->[2,*]->[3,X]
def reverse_ll(ll: Node) -> Node:  # Same object, so technically needn't return anything
    """
    Build up queue O(n) long, with call stack on each subsequent node.
    After built up, dequeue to place first time in last node, 2nd item in penultimate node, etc.

    Time: O(n)
    Space: O(n) (call stack, also queue)

    There's a way to do this in O(1) space, I just don't know it yet.
    """

    def traverse(node: Node | None):
        if node:
            q.append(node.key)
            traverse(node.next)
            node.key = q.pop(0)  # get foremost element in list, to put in current node

    q = []
    traverse(ll)

    return ll


ll = Node(1, Node(2, Node(3)))
asserter(lambda: reverse_ll(Node(1)), Node(1))
asserter(lambda: reverse_ll(Node(1, Node(2))), Node(2, Node(1)))
asserter(lambda: reverse_ll(ll), Node(3, Node(2, Node(1))))
