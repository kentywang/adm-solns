from ch3.common import BST, Side
from util import asserter

"""
Parent knows how many members each child (including child itself) has.

For delete(), if parent is asked to delete 5th smallest element and left child has 2 elements and right child has 4,
it knows it is the 3th smallest, so it tells right subtree to delete its 2nd smallest node.
Each level's call also should update its own respective member count to account for the deletion.

For insert(), every time we descend, we increment the member count on the parent for the respective side,
since we know they'll be increasing that side's count.

For member(), that's just a search, nothing special needs to be done with regards to updating member count.
"""


class BST3(BST):
    def __init__(self, key):
        super().__init__(key)
        self.ct_right = 0
        self.ct_left = 0

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
                    curr.right = BST3(val)
                    break
            else:
                curr.ct_left += 1
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BST3(val)
                    break
        return self

    def member(self, val) -> bool:
        if val == self.key:
            return True
        if val < self.key:
            if self.left:
                return self.left.member(val)
            else:
                return False
        else:
            if self.right:
                return self.right.member(val)
            else:
                return False

    def delete_position(self, position: int, root=None) -> int:
        """
        Weakness: client must call on root of tree. If not, won't properly delete.
        """
        if not root:
            root = self
        own_pos = self.ct_left + 1
        if position == own_pos:
            save = self.key
            # This will start from the top, in order to get the correct parent pointer set.
            # Method will still remain O(lg n), just adding a second pass.
            root.delete(self.key)
            return save
        if position <= self.ct_left:
            self.ct_left -= 1
            return self.left.delete_position(position, root=root)
        if own_pos < position <= own_pos + self.ct_right:
            self.ct_right -= 1
            return self.right.delete_position(position - own_pos, root=root)
        else:
            raise ValueError(f'Position {position} does not exist on BST.')

    def delete(self, val, parent=None, last_side=None):
        if val < self.key and self.left:
            self.left.delete(val, self, Side.LEFT)
        elif val > self.key and self.right:
            self.right.delete(val, self, Side.RIGHT)
        elif self.key == val:
            if not self.left and not self.right:  # leaf
                if not parent:
                    raise ValueError("This BST implementation does not support empty BSTs.")
                if last_side == Side.RIGHT:
                    parent.ct_right = 0
                    parent.right = None
                else:
                    parent.ct_left = 0
                    parent.left = None
            elif self.left and not self.right:  # 1 child
                self.key = self.left.key
                self.ct_left = self.left.ct_left  # just transplant the counts from child to self
                self.ct_right = self.left.ct_right
                self.left = None
            elif self.right and not self.left:  # 1 child
                self.key = self.right.key
                self.ct_left = self.right.ct_left
                self.ct_right = self.right.ct_right
                self.right = None
            elif self.left and self.right:  # 2 children
                succ = self.right.minimum()
                self.key = succ
                self.ct_right -= 1
                self.right.delete(succ, self, Side.RIGHT)
        else:
            raise ValueError("Value not in BST.")


x = BST3(4)
x.insert(2)
x.insert(6)
x.insert(1)
x.insert(3)
x.insert(5)
x.insert(7)
asserter(lambda: x.delete_position(4), 4)  # test deleting root w/ 2 children
asserter(lambda: x.delete_position(2), 2)  # test deleting nonroot w/ 2 children
asserter(lambda: x.delete_position(4), 6)  # test deleting nonroot w/ 1 child
asserter(lambda: x.member(4), False)
asserter(lambda: x.member(7), True)
