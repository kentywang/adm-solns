from itertools import islice, count, cycle

from ch1.pc2 import totalexchange
from profilerv2 import ProfilerV2
from util import asserter

asserter(lambda: totalexchange([[1, 5, 6]]), [3])
# changed from 11.99 to avoid floating point issue
asserter(lambda: totalexchange([[10, 20, 30], [15, 15.01, 3, 3.01]]), [10, 12.01])

# Varying trip amounts
with ProfilerV2(totalexchange, var='n', start=1000,
                mapper=lambda x: [[1, 2, 3, 4, 5]] + list(islice(cycle([[]]), x))
                ) as (f, n):
    f(n)

# Varying student amounts
with ProfilerV2(totalexchange, var='m', start=1000,
                mapper=lambda x: [list(islice(count(0), x))]
                ) as (f, n):
    f(n)
