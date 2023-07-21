import random
import sys
from itertools import pairwise

from ch3.common import bst, btree, BTree, is_bst
from util import asserter


def swap_nodes(tree: BTree, i: int, j: int) -> BTree:
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


def fix_bad_nodes(tree: BTree) -> BTree:
    """
    Brute force, for each node that violates its BFS bounds, try swapping with every other node.
    Each violation takes up to n-1 swaps, where each swap needs another n ops to verify the tree is BTree.
    so O(n*(n-1)*n) = O(n^3) time

    Traverse in DFS order. Keep track of bounds. Find the nodes that violate the bounds and swap their keys.
    Very similar structure to Node.verify_balance() and swap_nodes()

    THIS DOESN'T WORK WITH NODES SWAPPED WITH GRANDPARENTS
    """

    first_bad_node: BTree | None = None
    first_bad_node_parent: BTree | None = None
    second_bad_node: BTree | None = None

    def go(node: BTree, parent: BTree | None, minbound=~sys.maxsize, maxbound=sys.maxsize):
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


def fix_bad_nodes_2(tree: BTree) -> BTree:
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


asserter(lambda: is_bst(btree(20)), False)

a_bst = bst(15)
asserter(lambda: is_bst(a_bst), True)

x = random.randint(1, 15)
while (y := random.randint(1, 15)) == x:
    continue

swap_nodes(a_bst, x, y)
asserter(lambda: is_bst(a_bst), False)

fix_bad_nodes_2(a_bst)
asserter(lambda: is_bst(a_bst), True)
# print(bst(10))
asserter(lambda: is_bst(fix_bad_nodes_2(swap_nodes(bst(15), 12, 13))), True)
asserter(lambda: is_bst(fix_bad_nodes_2(swap_nodes(bst(15), 8, 6))), True)
asserter(lambda: is_bst(fix_bad_nodes_2(swap_nodes(bst(15), 1, 4))), True)
