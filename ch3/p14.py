from ch3.common import BST, bst, check_sorted, DLL
from util import asserter


def merge(a: BST, b: BST) -> DLL:
    """
    Iterate thru each BST, then walk thru both lists simulanteously to perform merge.

    Time: O(m+n)
    Space: O(1) (not including return value)
    """

    def add_to_tail_and_advance(val, hd, tl, iterat):
        new_node = DLL([val])
        if tl:
            tl.link_node(new_node)
        else:
            hd = new_node
        return hd, new_node, next(iterat, None)

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


print(list(merge(bst(5), bst(5))))

asserter(lambda: check_sorted(DLL([1])), True)
asserter(lambda: check_sorted(DLL([1, 2])), True)
asserter(lambda: check_sorted(DLL([2, 1])), False)
asserter(lambda: check_sorted(DLL([1, 2, 3, 4, 5])), True)
asserter(lambda: check_sorted(DLL([1, 2, 3, 4, 4])), True)
asserter(lambda: check_sorted(DLL([1, 2, 3, 5, 4])), False)
asserter(lambda: DLL([1]), DLL([1]))
asserter(lambda: list(DLL([1, 2, 3, 4])), [1, 2, 3, 4])
asserter(lambda: check_sorted(merge(bst(1), bst(1))), True)
asserter(lambda: check_sorted(merge(bst(15), bst(15))), True)
asserter(lambda: check_sorted(merge(bst(50), bst(50))), True)
