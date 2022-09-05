from itertools import count, islice

from ch1.hr3 import hackerlandRadioTransmitters_dp, hackerlandRadioTransmitters_dp_memo, \
    hackerlandRadioTransmitters_dp_builtin_cache, hackerlandRadioTransmitters_hr
from profilerv2 import ProfilerV2
from util import asserter


def test_func(fn):
    asserter(lambda: fn([1], 2), 1)
    asserter(lambda: fn([1, 5], 2), 2)
    asserter(lambda: fn([1, 5, 9], 5), 1)
    asserter(lambda: fn([1, 3, 5, 6], 2), 2)
    asserter(lambda: fn([1, 2, 3, 5, 9], 1), 3)
    asserter(lambda: fn([7, 2, 4, 6, 5, 9, 12, 11], 2), 3)


def test_perf(fn):
    test_func(fn)  # Sanity check before benchmarking

    inflist = count(0)

    with ProfilerV2(
            fn,
            start=3,
            mapper=lambda x: list(islice(inflist, x)),
    ) as (f, n):
        f(n, 10)

    # Only used to verify that k doesn't matter
    # with ProfilerV2(fn, var='k', start=25) as (f, n):
    #     f(list(islice(inflist, 25)), 5)


test_perf(hackerlandRadioTransmitters_dp)
test_perf(hackerlandRadioTransmitters_dp_memo)
test_perf(hackerlandRadioTransmitters_dp_builtin_cache)
test_perf(hackerlandRadioTransmitters_hr)
