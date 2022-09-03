from random import randint

from ch1.lc2 import ListNode, rotate_right_v1#, rotate_right_v2
from profiler import Profiler
from util import red, reset_color


def test_perf():
    lists = []
    for n in [1000, 2000, 4000, 8000]:
        head = curr = ListNode(0)
        for i in range(1, n):
            curr.next = ListNode(i)
            curr = curr.next
        lists.append((head, n))

    for linkedlist, n in lists:
        print(f'{red}n: {n}{reset_color}')
        # Varying n, keeping k constant
        with Profiler(rotate_right_v1) as f:
            for _ in range(100):
                f(linkedlist, randint(0, 1000))

    for k in [10000, 20000, 40000]:
        print(f'{red}k: {k}{reset_color}')
        # Varying k, keeping n constant
        with Profiler(rotate_right_v1) as f:
            for _ in range(100):
                f(lists[0][0], k)


test_perf()

# rotate_right_v1: O(n) space, O(n+k) time

# TODO setup profiler to also print n count and include more variables for multivariable O(n).
# Also show factor increase compared to previous run
