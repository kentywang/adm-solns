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

    Time: O(2(m+n)) (one iteration to get list for each BST, another to merge)
    Space: O(mn) (not including return value)

    Theoretical optimal: O(m+n)
    Space: O(1) (not including return value)
    """
    ia, ib = iter(a), iter(b)
    result = []

    na = next(ia, None)
    nb = next(ib, None)
    while na is not None or nb is not None:
        if na is None:
            result.append(nb)
            nb = next(ib, None)
        elif nb is None:
            result.append(na)
            na = next(ia, None)
        elif na <= nb:
            result.append(na)
            na = next(ia, None)
        else:
            result.append(nb)
            nb = next(ib, None)

    return DLLNode(result)


asserter(lambda: check_sorted(DLLNode([1])), True)
asserter(lambda: check_sorted(DLLNode([1, 2])), True)
asserter(lambda: check_sorted(DLLNode([2, 1])), False)
asserter(lambda: check_sorted(DLLNode([1, 2, 3, 4, 5])), True)
asserter(lambda: check_sorted(DLLNode([1, 2, 3, 4, 4])), True)
asserter(lambda: check_sorted(DLLNode([1, 2, 3, 5, 4])), False)
asserter(lambda: DLLNode([1]), DLLNode([1]))
asserter(lambda: list(DLLNode([1, 2, 3, 4])), [1, 2, 3, 4])
# print(list(merge(bst(5), bst(5))))
asserter(lambda: check_sorted(merge(bst(1), bst(1))), True)
asserter(lambda: check_sorted(merge(bst(15), bst(15))), True)
asserter(lambda: check_sorted(merge(bst(50), bst(50))), True)
