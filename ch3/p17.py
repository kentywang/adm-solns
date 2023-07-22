from ch3.common import bst, unbalanced_bst, BST
from util import asserter


def is_balanced(tree: BST) -> bool:
    """
    Time: O(n) (DFS)
    Space: O(lg n)
    """

    def go(node, height):
        min_l, max_l = go(node.left, height + 1) if node.left else (height, height)
        min_r, max_r = go(node.right, height + 1) if node.right else (height, height)
        return min(min_l, min_r), max(max_l, max_r)

    min_depth, max_depth = go(tree, 1)
    return max_depth - min_depth <= 1


asserter(lambda: is_balanced(bst(1)), True)
asserter(lambda: is_balanced(bst(2)), True)
asserter(lambda: is_balanced(bst(3)), True)
asserter(lambda: is_balanced(bst(4)), True)
asserter(lambda: is_balanced(bst(30)), True)
asserter(lambda: is_balanced(unbalanced_bst(1)), True)
asserter(lambda: is_balanced(unbalanced_bst(2)), True)
asserter(lambda: is_balanced(unbalanced_bst(3)), False)
asserter(lambda: is_balanced(unbalanced_bst(10)), False)
