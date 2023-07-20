from ch3.p13 import BSTNode, bst
from util import asserter


class DLLNode:
    def __init__(self, vals: list[int], previous=None):
        self.value = vals[0]
        self.prev = previous
        self.next = DLLNode(vals[1:], self) if len(vals) > 1 else None

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


def check_sorted(n: DLLNode) -> bool:
    prev = None
    curr = n

    while curr:
        if prev and prev.value > curr.value:
            return False
        else:
            prev = curr
            curr = curr.next

    return True


def merge(a: BSTNode, b: BSTNode) -> DLLNode:
    """
    Iterate thru each BST, then walk thru both lists simulanteously to perform merge.

    Time: O(m+n)
    Space: O(1) (not including return value)
    """

    def add_to_tail_and_advance(val, hd, tl, iterat):
        x = DLLNode([val])
        if tl:
            tl.next = x
            x.prev = tl
        else:
            hd = x
        return hd, x, next(iterat, None)

    head = None
    tail = None
    ia, ib = iter(a), iter(b)
    na = next(ia, None)
    nb = next(ib, None)

    while na is not None or nb is not None:
        if na is None:
            head, tail, nb = add_to_tail_and_advance(nb, head, tail, ib)
        elif nb is None:
            head, tail, na = add_to_tail_and_advance(na, head, tail, ia)
        elif na <= nb:
            head, tail, na = add_to_tail_and_advance(na, head, tail, ia)
        else:
            head, tail, nb = add_to_tail_and_advance(nb, head, tail, ib)

    return head


# print(list(merge(bst(5), bst(5))))

asserter(lambda: check_sorted(DLLNode([1])), True)
asserter(lambda: check_sorted(DLLNode([1, 2])), True)
asserter(lambda: check_sorted(DLLNode([2, 1])), False)
asserter(lambda: check_sorted(DLLNode([1, 2, 3, 4, 5])), True)
asserter(lambda: check_sorted(DLLNode([1, 2, 3, 4, 4])), True)
asserter(lambda: check_sorted(DLLNode([1, 2, 3, 5, 4])), False)
asserter(lambda: DLLNode([1]), DLLNode([1]))
asserter(lambda: list(DLLNode([1, 2, 3, 4])), [1, 2, 3, 4])
asserter(lambda: check_sorted(merge(bst(1), bst(1))), True)
asserter(lambda: check_sorted(merge(bst(15), bst(15))), True)
asserter(lambda: check_sorted(merge(bst(50), bst(50))), True)
