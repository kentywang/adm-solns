import random
import sys
from collections import deque
from itertools import pairwise

from util import asserter


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def verify_balance(self) -> bool:
        def go(node: Node, minbound=~sys.maxsize, maxbound=sys.maxsize) -> bool:
            if minbound < node.key < maxbound:
                left_ok = True if not node.left else go(node.left, minbound, node.key)
                right_ok = True if not node.right else go(node.right, node.key, maxbound)
                return left_ok and right_ok
            else:
                return False

        return go(self)

    def to_list(self) -> list:
        arr = []

        def go(node):
            if node.left:
                go(node.left)
            arr.append(node)
            if node.right:
                go(node.right)

        go(self)

        return arr

    def __repr__(self) -> str:
        return '\n'.join(f'{i + 1} : {e.key}' for i, e in enumerate(self.to_list()))


def nonbst(ct: int) -> Node:
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


def bst(ct: int) -> Node:
    arbitrary_lower_bound_for_generated_vals = ~sys.maxsize // 1000000000000000
    arbitrary_upper_bound_for_generated_vals = sys.maxsize // 1000000000000000
    arr = deque()
    bounds = (None, None)
    root = Node(100)
    ct -= 1

    arr.append((root, bounds))
    while arr and ct > 0:
        curr, (minbound, maxbound) = arr.popleft()
        left_node_bounds = (minbound if not minbound else minbound + 1, curr.key - 1)

        left_key = random.randint(left_node_bounds[0] or arbitrary_lower_bound_for_generated_vals, left_node_bounds[1])
        curr.left = Node(left_key)
        ct -= 1
        arr.append((curr.left, left_node_bounds))

        if ct > 0:
            right_node_bounds = (curr.key + 1, maxbound if not maxbound else maxbound - 1)
            right_key = random.randint(right_node_bounds[0],
                                       right_node_bounds[1] or arbitrary_upper_bound_for_generated_vals)
            curr.right = Node(right_key)
            ct -= 1
            arr.append((curr.right, right_node_bounds))

    return root


def swap_nodes(tree: Node, i: int, j: int) -> Node:
    """
    :param tree:
    :param i: ith node in tree to swap, with nodes in sorted order
    :param j: jth node in tree, with nodes in sorted order
    :return:
    """
    a, b = tree, tree

    def go(curr, n):
        """
        Iterate thru tree using in-order traversal.
        Keep track of count of nodes traversed so far.
        Save the node when reaching the ith or jth node.
        """
        nonlocal a
        nonlocal b

        # left ==============
        if curr.left:
            n = go(curr.left, n)

        # current ==============
        if n == i:
            a = curr
        elif n == j:
            b = curr

        n += 1  # increment, pass on to next call

        # right ==============
        if curr.right:
            n = go(curr.right, n)

        # return ==============
        return n

    go(tree, 1)
    b.key, a.key = a.key, b.key
    return tree


def fix_bad_nodes(tree: Node) -> Node:
    """
    Brute force, for each node that violates its BFS bounds, try swapping with every other node.
    Each violation takes up to n-1 swaps, where each swap needs another n ops to verify the tree is BST.
    so O(n*(n-1)*n) = O(n^3) time

    Traverse in DFS order. Keep track of bounds. Find the nodes that violate the bounds and swap their keys.
    Very similar structure to Node.verify_balance() and swap_nodes()

    THIS DOESN'T WORK WITH NODES SWAPPED WITH GRANDPARENTS
    """

    first_bad_node: Node | None = None
    first_bad_node_parent: Node | None = None
    second_bad_node: Node | None = None

    def go(node: Node, parent: Node | None, minbound=~sys.maxsize, maxbound=sys.maxsize):
        nonlocal first_bad_node
        nonlocal first_bad_node_parent
        nonlocal second_bad_node

        if minbound < node.key < maxbound:
            if node.left:
                go(node.left, node, minbound, node.key)
            if node.right:
                go(node.right, node, node.key, maxbound)
        else:
            print('bad node!', minbound, node.key, maxbound)
            if first_bad_node:  # one bad node was already found, so this is the 2nd one
                second_bad_node = node
            else:  # save parent ref too
                first_bad_node, first_bad_node_parent = node, parent

    go(tree, None)
    if second_bad_node:
        first_bad_node.key, second_bad_node.key = second_bad_node.key, first_bad_node.key
    else:  # when no second bad node found, it's because the parent is the second bad node (which we checked already)
        first_bad_node.key, first_bad_node_parent.key = first_bad_node_parent.key, first_bad_node.key

    return tree


def fix_bad_nodes_2(tree: Node) -> Node:
    """
    When two nodes swap in a monotonically increasing sequence, the one node (the smaller) will be identified first
    when it will be preceded by a smaller value, a violation of the order. The smaller node can be identified when
    another violation occurs, but this time the node (the smaller one) will be successor.

    If only one violation occurs in the entire sequence, it reveales that it's those two nodes that are the involved in swap.
    """
    violation_1 = None
    violation_2 = None

    for a, b in pairwise(tree.to_list()):
        if a.key > b.key:
            if not violation_1:
                violation_1 = a, b
            else:
                violation_2 = a, b

    if not violation_2:
        violation_1[0].key, violation_1[1].key = violation_1[1].key, violation_1[0].key
    else:
        violation_1[0].key, violation_2[1].key = violation_2[1].key, violation_1[0].key

    return tree


nonbst = nonbst(20)
asserter(lambda: nonbst.verify_balance(), False)

a_bst = bst(15)
asserter(lambda: a_bst.verify_balance(), True)

x = random.randint(1, 15)
while (y := random.randint(1, 15)) == x:
    continue

swap_nodes(a_bst, x, y)
asserter(lambda: a_bst.verify_balance(), False)

fix_bad_nodes_2(a_bst)
asserter(lambda: a_bst.verify_balance(), True)

asserter(lambda: fix_bad_nodes_2(swap_nodes(bst(15), 12, 13)).verify_balance(), True)
asserter(lambda: fix_bad_nodes_2(swap_nodes(bst(15), 8, 6)).verify_balance(), True)
asserter(lambda: fix_bad_nodes_2(swap_nodes(bst(15), 1, 4)).verify_balance(), True)
