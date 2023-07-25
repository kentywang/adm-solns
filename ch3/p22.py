"""
A self-balancing BST (without support for deletes) seems to just need an insert operation that tracks the size of its
left and right subtrees, so that when an insert may increase the size difference of the two subtrees to more than 1, the
insert instead calls up the predecessor/successor to current node (decide which by drawing from the more populous subtree)
and takes the current node's spot. The current node's value is inserted in the smaller subtree, thereby reversing the size
differences, such that the new element can be inserted without increasing the difference between the trees.

Can't just keep track of height (instead of size) because we need median.

The above method actually may work too well in that median may be a O(1) op. If we relax the requirement that insert
keeps the tree balanced, we can instead just rely on memberships counts to figure out which side to recurse down to find
the middle number.
So this is essentially a reduction to the delete() call in problem 20, but without the deletion.

E.g. the median of a tree with 6 members on the left subtree and 3 on the right is the 5th and 6th smallest elements. Get
those and you'll have the median when you average them.
"""
import math

from ch3.p20 import BST3
from util import asserter


class BST4(BST3):
    def get_position(self, position) -> int:
        """
        Get node at nth position's key. Time: O(lg n)
        """
        own_pos = self.ct_left + 1
        if position == own_pos:
            return self.key
        if position <= self.ct_left:
            return self.left.get_position(position)
        if own_pos < position <= own_pos + self.ct_right:
            return self.right.get_position(position - own_pos)
        else:
            raise ValueError(f'Position {position} does not exist on BST.')

    def median(self) -> float:
        ct_total = self.ct_left + 1 + self.ct_right
        if ct_total % 2:  # odd
            return self.get_position(math.ceil(ct_total / 2))
        # even
        return (self.get_position(ct_total / 2) + self.get_position(ct_total / 2 + 1)) / 2

    # Just changing the new instance types to BST4
    def insert(self, val):
        curr = self
        while curr:
            if val == curr.key:
                raise ValueError("No duplicates allowed in BST")
            elif val > curr.key:
                curr.ct_right += 1
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = BST4(val)
                    break
            else:
                curr.ct_left += 1
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BST4(val)
                    break
        return self


x = BST4(4)
x.insert(2)
x.insert(6)
x.insert(1)
x.insert(3)
x.insert(5)
x.insert(7)
asserter(lambda: x.median(), 4)  # root is 4
x.delete_position(4)
asserter(lambda: x.median(), 4)  # medians are 3, 5
x.delete_position(2)
asserter(lambda: x.median(), 5)
x.delete_position(4)
asserter(lambda: x.median(), 4)  # root is 5
x.delete_position(1)
x.delete_position(1)
asserter(lambda: x.median(), 6)  # root is 5
