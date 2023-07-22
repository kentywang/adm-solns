from math import floor, log2

from ch3.common import max_depth, unbalanced_bst, BST
from util import asserter


def balanced(tree: BST) -> BST:
    """
    Strat:
    1. convert BST to list (time: O(n), space: O(n))
    2. divide and conquer on list, picking middle element as node, and subcontract subtree populating to recursed function calls
    (time: O(n), space: O(lg n))
    """
    keys = list(tree)

    def build_bst(start, end):
        if start <= end:
            mid = (end + start) // 2
            x = BST(keys[mid])
            x.left = build_bst(start, mid - 1)
            x.right = build_bst(mid + 1, end)
            return x
        else:
            return None

    return build_bst(0, len(keys) - 1)


# Checking unbalanced_bst() builds a lopsided BST as intended.
asserter(lambda: list(unbalanced_bst(5)), [1, 2, 3, 4, 5])
asserter(lambda: max_depth(unbalanced_bst(15)), 15)

# Checking balanced() generates a height-balanced BST as intended.
asserter(lambda: list(balanced(unbalanced_bst(5))), [1, 2, 3, 4, 5])
asserter(lambda: max_depth(balanced(unbalanced_bst(15))), floor(log2(15) + 1))
asserter(lambda: max_depth(balanced(unbalanced_bst(16))), floor(log2(16) + 1))
