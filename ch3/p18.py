from ch3.common import is_bst, BST, Side
from util import asserter

# First, let's implement insert, min/max, and delete in O(lg n) for a BST
x = BST(100)
x.insert(98)
x.insert(102)
x.insert(97)
x.insert(99)
x.insert(101)
x.insert(103)
# print(list(x))
asserter(lambda: is_bst(x), True)
asserter(lambda: len(list(x)), 7)
asserter(lambda: 100 in list(x), True)
asserter(lambda: x.minimum(), list(x)[0])
asserter(lambda: x.maximum(), list(x)[-1])
x.delete(100)  # test deleting root w/ 2 children
x.delete(98)  # test deleting nonroot w/ 2 children
x.delete(102)  # test deleting nonroot w/ 1 child
asserter(lambda: 100 in list(x), False)
asserter(lambda: 98 in list(x), False)
asserter(lambda: 102 in list(x), False)
asserter(lambda: len(list(x)), 4)


# print(list(x))

# Now let's subclass it to implement O(1) succ/pred, mixing in DLL-like props "prev" and "next"
# to store references to each successor.
# No need to change read methods such as minimum() and maximum()
class BST2(BST):
    def __init__(self, key):
        super().__init__(key)
        self.prev = None
        self.next = None

    def predecessor(self):
        return self.prev

    def successor(self):
        return self.next

    def insert(self, val):
        curr = self
        while curr:
            if val == curr.key:
                raise ValueError("No duplicates allowed in BST")
            elif val > curr.key:
                if curr.right:
                    curr = curr.right
                else:
                    new_node = BST2(val)
                    curr.right = new_node

                    new_node.next = curr.next  # need to always set the refs on both sides
                    if new_node.next:
                        new_node.next.prev = new_node

                    new_node.prev = curr
                    curr.next = new_node

                    break
            else:
                if curr.left:
                    curr = curr.left
                else:
                    new_node = BST2(val)
                    curr.left = new_node

                    new_node.prev = curr.prev
                    if new_node.prev:
                        new_node.prev.next = new_node

                    new_node.next = curr
                    curr.prev = new_node

                    break
        return self

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
                    parent.right = None
                    parent.next = self.next  # parent's succ/pred pointers need to also update
                    self.next.prev = parent
                else:
                    parent.left = None
                    parent.prev = self.prev  # parent's succ/pred pointers need to also update
                    self.prev.next = parent
            elif self.left and not self.right:  # 1 child on the left, just replace curr node with that child
                self.key = self.left.key

                # we just need to clear the refs to the current node by joining its refs with each other
                self.next.prev = self.prev.next
                self.prev.next = self.next.prev

                self.left = None
            elif self.right and not self.left:  # 1 child on the right, just replace curr node with that child
                self.key = self.right.key

                # we just need to clear the refs to the current node by joining its refs with each other
                self.next.prev = self.prev.next
                self.prev.next = self.next.prev

                self.right = None
            elif self.left and self.right:  # 2 children
                succ = self.right.minimum()
                self.key = succ
                self.right.delete(succ, self, Side.RIGHT)
        else:
            raise ValueError("Value not in BST.")


y = BST2(100)
y.insert(98)
y.insert(102)
y.insert(97)
y.insert(99)
y.insert(101)
y.insert(103)
asserter(lambda: is_bst(y), True)
asserter(lambda: len(list(y)), 7)
asserter(lambda: 100 in list(y), True)
asserter(lambda: y.minimum(), list(y)[0])
asserter(lambda: y.maximum(), list(y)[-1])
asserter(lambda: y.successor().key, 101)
asserter(lambda: y.predecessor().key, 99)
y.delete(100)  # test deleting root w/ 2 children
y.delete(98)  # test deleting nonroot w/ 2 children
y.delete(102)  # test deleting nonroot w/ 1 child
asserter(lambda: 100 in list(y), False)
asserter(lambda: 98 in list(y), False)
asserter(lambda: 102 in list(y), False)
asserter(lambda: len(list(y)), 4)
asserter(lambda: y.successor().key, 103)
asserter(lambda: y.left.predecessor().key, 97)
asserter(lambda: y.left.left.predecessor(), None)
asserter(lambda: y.left.left.successor().key, 99)
