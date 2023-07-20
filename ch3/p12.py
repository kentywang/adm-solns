"""

Since spec is to have O(n) time with n nodes, we just need to iterate to each node no more than once and track the
depth of each node, and return the max of recorded depths. With DFS (or BFS I think), space usage will be O(lg n).

"""
import random
from collections import deque

from profilerv2 import ProfilerV2
from util import asserter


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def tree(ct: int) -> Node:
    """
    helper fn to generate tree with a given number of nodes
    """
    arr = deque()
    root = Node(random.randint(0, 1000))
    ct -= 1

    arr.append(root)
    while arr and ct > 0:
        curr = arr.popleft()
        curr.left = Node(random.randint(0, 1000))
        ct -= 1
        if ct > 0:
            curr.right = Node(random.randint(0, 1000))
            ct -= 1

        arr.append(curr.left)
        arr.append(curr.right)

    return root


def max_depth(tree: Node) -> int:
    """
    simple DFS.

    Time: O(n)
    Space: O(lg n)
    """

    def go(t, h):
        if not t.left and not t.right:
            return h

        max_l, max_r = 0, 0
        if t.left:
            max_l = go(t.left, h + 1)
        if t.right:
            max_r = go(t.right, h + 1)
        return max(max_l, max_r)

    return go(tree, 1)


asserter(lambda: max_depth(tree(1)), 1)
asserter(lambda: max_depth(tree(2)), 2)
asserter(lambda: max_depth(tree(3)), 2)
asserter(lambda: max_depth(tree(4)), 3)
asserter(lambda: max_depth(tree(7)), 3)
asserter(lambda: max_depth(tree(8)), 4)
asserter(lambda: max_depth(tree(15)), 4)
asserter(lambda: max_depth(tree(31)), 5)

with ProfilerV2(max_depth, var='n', start=1000, count=6, reps=1000, mapper=tree, clone=False) as (f, n):
    f(n)
