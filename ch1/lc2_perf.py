from random import randint

from ch1.lc2 import ListNode, rotate_right_v1, rotate_right_v2
from profiler import Profiler
from profilerv2 import ProfilerV2
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
        with Profiler(rotate_right_v1, head, k) as f:
            for _ in range(1000):
                f()

        with Profiler(rotate_right_v2, head, k) as f:
            for _ in range(1000):
                f()


def test_perf2():
    with ProfilerV2(rotate_right_v1, var='n', start=500, reps=1000, mapper=make_list, clone=False) as (f, n):
        f(n, 500)

    with ProfilerV2(rotate_right_v1, var='k', start=1000, reps=1000) as (f, k):
        f(make_list(100), k)

    with ProfilerV2(rotate_right_v2, var='n', start=30, reps=1000, mapper=make_list, clone=False) as (f, n):
        f(n, 500)

    with ProfilerV2(rotate_right_v2, var='k', start=100000, reps=1000) as (f, k):
        f(make_list(100), k)


test_func()
# test_perf()
test_perf2()

# rotate_right_v1: O(n) space, O(n+k) time
# rotate_right_v2: O(1) space, O(n) time
