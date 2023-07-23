import random
import sys
from collections import deque
from enum import Enum


class Side(Enum):
    LEFT = 1
    RIGHT = 2


class BTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __iter__(self):
        self.check_next = [self]
        return self

    def __next__(self):
        while self.check_next:
            x = self.check_next.pop()
            if isinstance(x, int):
                return x
            else:
                if x.right:
                    self.check_next.append(x.right)
                self.check_next.append(x.key)
                if x.left:
                    self.check_next.append(x.left)
        else:
            raise StopIteration

    def to_list(self) -> list:
        """
        Different than __iter__ and __next__ methods, because this returns a list of nodes, not ints.
        """
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
        return '  '.join(f'{e}' for i, e in enumerate(list(self)))


class BST(BTree):
    def insert(self, val):
        curr = self
        while curr:
            if val == curr.key:
                raise ValueError("No duplicates allowed in BST")
            elif val > curr.key:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = BST(val)
                    break
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BST(val)
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
                else:
                    parent.left = None
            elif self.left and not self.right:  # 1 child
                self.key = self.left.key
                self.left = None
            elif self.right and not self.left:  # 1 child
                self.key = self.right.key
                self.right = None
            elif self.left and self.right:  # 2 children
                succ = self.right.minimum()
                self.key = succ
                self.right.delete(succ, self, Side.RIGHT)
        else:
            raise ValueError("Value not in BST.")

    def minimum(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.key

    def maximum(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.key


def btree(ct: int) -> BTree:
    """
    helper fn to generate tree with a given number of nodes (non-BST)
    """
    arr = deque()
    root = BTree(random.randint(0, 1000))
    ct -= 1

    arr.append(root)
    while arr and ct > 0:
        curr = arr.popleft()
        curr.left = BTree(random.randint(0, 1000))
        ct -= 1
        if ct > 0:
            curr.right = BTree(random.randint(0, 1000))
            ct -= 1

        arr.append(curr.left)
        arr.append(curr.right)

    return root


def max_depth(tree: BTree) -> int:
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


def bst(ct: int) -> BST:
    try:
        curr_ct = ct
        arbitrary_lower_bound_for_generated_vals = ~sys.maxsize // 1000000000000000
        arbitrary_upper_bound_for_generated_vals = sys.maxsize // 1000000000000000
        arr = deque()
        bounds = (None, None)
        root = BST(100)
        curr_ct -= 1

        arr.append((root, bounds))
        while arr and curr_ct > 0:
            curr, (minbound, maxbound) = arr.popleft()
            left_node_bounds = (minbound if not minbound else minbound + 1, curr.key - 1)

            left_key = random.randint(left_node_bounds[0] or arbitrary_lower_bound_for_generated_vals,
                                      left_node_bounds[1])
            curr.left = BST(left_key)
            curr_ct -= 1
            arr.append((curr.left, left_node_bounds))

            if curr_ct > 0:
                right_node_bounds = (curr.key + 1, maxbound if not maxbound else maxbound - 1)
                right_key = random.randint(right_node_bounds[0],
                                           right_node_bounds[1] or arbitrary_upper_bound_for_generated_vals)
                curr.right = BST(right_key)
                curr_ct -= 1
                arr.append((curr.right, right_node_bounds))

        return root
    except ValueError:  # retry when rand range is bad due to unfortunately close keys generated
        return bst(ct)


def is_bst(tree: BTree) -> bool:
    def go(node: BTree, minbound=~sys.maxsize, maxbound=sys.maxsize) -> bool:
        if minbound < node.key < maxbound:
            left_ok = True if not node.left else go(node.left, minbound, node.key)
            right_ok = True if not node.right else go(node.right, node.key, maxbound)
            return left_ok and right_ok
        else:
            return False

    return go(tree)


class DLL:
    def __init__(self, vals: list[any], previous=None):
        self.value = vals[0]
        self.prev = previous
        self.next = DLL(vals[1:], self) if len(vals) > 1 else None

    def link_node(self, next_node):
        self.next = next_node
        next_node.prev = self

    def __eq__(self, other):
        return all([
            self.value == other.value,
            self.prev == other.prev,
            self.next == other.next
        ])

    def __iter__(self):
        self.curr = self
        return self

    def __next__(self):
        if self.curr:
            result = self.curr.value
            self.curr = self.curr.next
            return result
        else:
            raise StopIteration


def check_sorted(n: DLL) -> bool:
    prev = None
    curr = n

    while curr:
        if prev and prev.value > curr.value:
            return False
        else:
            prev = curr
            curr = curr.next

    return True


def unbalanced_bst(ct: int) -> BST:
    curr_ct = 1
    curr, root = None, None
    while curr_ct <= ct:
        x = BST(curr_ct)
        if root is None:
            root = x
        if curr:
            curr.right = x
        curr = x
        curr_ct += 1
    return root
