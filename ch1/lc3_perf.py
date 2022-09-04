from itertools import cycle, islice

from ch1.lc3 import wiggle_sort_v1, is_valid, wiggle_sort_v2, wiggle_sort_lc1
from profilerv2 import ProfilerV2


def test_func():
    """
    Some basic sanity checks before running perfomance tests.
    """

    def cases(fn):
        empty = []
        case1 = [1]
        case2 = [2, 3]
        case3 = [2, 1, 1]
        casen = [1, 5, 1, 1, 6, 4]
        case_proving_cant_just_swap_adjacents_sequentially = [1, 2, 3, 2, 1]  # expect [2,3,1,2,1]
        tricky = [4, 5, 5, 6]

        fn(empty)
        assert is_valid(empty)
        fn(case1)
        assert is_valid(case1)
        fn(case2)
        assert is_valid(case2)
        fn(case3)
        assert is_valid(case3)
        fn(casen)
        assert is_valid(casen)
        assert casen != [1, 5, 1, 1, 6, 4]
        fn(case_proving_cant_just_swap_adjacents_sequentially)
        assert is_valid(case_proving_cant_just_swap_adjacents_sequentially)
        assert case_proving_cant_just_swap_adjacents_sequentially != [1, 2, 3, 2, 1]
        fn(tricky)
        assert is_valid(tricky)

    cases(wiggle_sort_v1)
    cases(wiggle_sort_v2)
    cases(wiggle_sort_lc1)


def test_perf():
    c = cycle([1, 1, 1, 2, 2, 2])

    with ProfilerV2(wiggle_sort_v1, var='n', start=1, reps=1, mapper=lambda x: list(islice(c, x))) as (f, n):
        f(n)
    with ProfilerV2(wiggle_sort_v2, var='n', start=500, reps=500, mapper=lambda x: list(islice(c, x))) as (f, n):
        f(n)
    with ProfilerV2(wiggle_sort_lc1, var='n', start=500, reps=500, mapper=lambda x: list(islice(c, x))) as (f, n):
        f(n)


test_func()
test_perf()
