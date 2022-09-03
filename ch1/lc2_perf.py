from random import randint

from ch1.lc2 import ListNode, rotate_right_v1, rotate_right_v2
from profiler import Profiler
from util import red, reset_color, yellow


def make_list(length):
    head = curr = ListNode(0)
    for i in range(1, length):
        curr.next = ListNode(i)
        curr = curr.next
    return head


def test_func():
    for f in [rotate_right_v1, rotate_right_v2]:
        # [0]
        head = make_list(0)
        assert f(head, 0).val == 0
        assert f(head, 1).val == 0

        # [0, 1, 2, 3, 4]
        head = make_list(5)
        assert f(head, 0).val == 0
        assert f(head, 1).val == 4


def test_perf():
    lists = []
    for n in [1000, 2000, 4000]:
        head = make_list(n)
        lists.append((head, n))

    for linkedlist, n in lists:
        orig_head = linkedlist

        print(f'{red}n: {n}{reset_color}')
        # Varying n, keeping k constant
        with Profiler(rotate_right_v1) as f:
            for _ in range(1000):
                f(linkedlist, randint(0, 1000))

        assert orig_head == linkedlist

        with Profiler(rotate_right_v2) as f:
            for _ in range(1000):
                f(linkedlist, randint(0, 1000))

    head = make_list(500)

    for k in [2000, 4000, 8000]:
        print(f'{yellow}k: {k}{reset_color}')
        # Varying k, keeping n constant
        with Profiler(rotate_right_v1) as f:
            for _ in range(1000):
                f(head, k)

        with Profiler(rotate_right_v2) as f:
            for _ in range(1000):
                f(head, k)


test_func()
test_perf()

# rotate_right_v1: O(n) space, O(n+k) time
# rotate_right_v1: O(1) space, O(n) time

# TODO setup profiler to also print n count and include more variables for multivariable O(n).
# Also show factor increase compared to previous run

# Ideal output:

# rotate_right_v1:
#   n: 2000
#     3000ms           2000 KiB
#   n: 4000
#     6000ms  (2x)     3000 KiB   (1.5x)
#   n: 8000
#     11000ms (1.9x)   4000 KiB   (1.25x)

#   k: 2000
#     3000ms           2000 KiB
#   k: 4000
#     6000ms  (2x)     3000 KiB   (1.5x)
#   k: 8000
#     11000ms (1.9x)   4000 KiB   (1.25x)

# rotate_right_v2:
#   n: 2000
#     3000ms           2000 KiB
#   n: 4000
#     6000ms  (2x)     3000 KiB   (1.5x)
#   n: 8000
#     11000ms (1.9x)   4000 KiB   (1.25x)

#   k: 2000
#     3000ms           2000 KiB
#   k: 4000
#     6000ms  (2x)     3000 KiB   (1.5x)
#   k: 8000
#     11000ms (1.9x)   4000 KiB   (1.25x)
