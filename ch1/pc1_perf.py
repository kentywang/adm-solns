from ch1.pc1 import threenplusone, threenplusone_recur_bad_memo, threenplusone_recur_good_memo, maxcyclelen, \
    maxcyclelen_bad_memo, maxcyclelen_memo
from profilerv2 import ProfilerV2
from util import asserter


def test_func(fn):
    asserter(lambda: fn(22), 16)


def test_perf(fn):
    with ProfilerV2(fn, var='j', step=lambda j: j + 1000, start=1, count=11, reps=1) as (f, n):
        f(1, n)


test_func(threenplusone)
test_func(threenplusone_recur_bad_memo)
test_func(threenplusone_recur_good_memo)

test_perf(maxcyclelen)
test_perf(maxcyclelen_bad_memo)
test_perf(maxcyclelen_memo)
