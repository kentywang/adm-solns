"""

Since spec is to have O(n) time with n nodes, we just need to iterate to each node no more than once and track the
depth of each node, and return the max of recorded depths. With DFS (or BFS I think), space usage will be O(lg n).

"""

from ch3.common import btree, max_depth
from profilerv2 import ProfilerV2
from util import asserter

asserter(lambda: max_depth(btree(1)), 1)
asserter(lambda: max_depth(btree(2)), 2)
asserter(lambda: max_depth(btree(3)), 2)
asserter(lambda: max_depth(btree(4)), 3)
asserter(lambda: max_depth(btree(7)), 3)
asserter(lambda: max_depth(btree(8)), 4)
asserter(lambda: max_depth(btree(15)), 4)
asserter(lambda: max_depth(btree(31)), 5)

with ProfilerV2(max_depth, var='n', start=1000, count=6, reps=1000, mapper=btree, clone=False) as (f, n):
    f(n)
