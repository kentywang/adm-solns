"""
Planning    14:56 - 15:35 (39 min)
Coding      15:35 - 15:48, 16:01 - 16:13 (25 min)
Fixing      16:13 - 16:35 (22 min)

Observations:
- given [1,99], we should return 0 w[0]/w of the time, and 1 w[1]/w of the time
- we'll need to store the sum w, also the weights themselves
- need to translate a fraction into a index value from 0 to w-1
- randrange(0,1) gives us a number from 0 to 1
- if we mult that by len - 1, we'll get random number from 0 to len - 1.
    - if len - 1 == 3, range is 0.0 to 3.0. We can round that to nearest int to get an index.
- need to map values from 0.0-1.0 to 0-sum (or the converse)
- once you have the map, use it to know which index the rand decimal lands in.

1. produce mapping of rand range to index, using weights [time O(n), space O(n)]
- not needed if we just use weights as range
- could do binary search to find right index, if it were sorted
2. convert rand value to index, using sth like getIndexFromDecimal(i, ranges) [want O(1) time, easily O(n)]

.5 * 189 =               94.5
[90, 10, 89] => [[0,90),[90,100), [100,189)]

[[0,1.0)]

[]1,3]
1/.25 .75

      .05
[0.01, .1, .2, .3, .4, 1.0]
            ^
Cases:
- n = 1 e.g. [5]
- [1, 10, 89] => sum = 100, so ranges are

Option 1: pickIndex is O(lg n)
- initialization takes O(n) to convert weights to range from 0.0 - 1.0, then O(n lg n) time to sort
    - make something like this: [0,0.01), [0.01, 0.1), [0.1,1)
- generate random number, throw into binary search to find proper index to return

"""
import random
from collections import Counter
from itertools import accumulate, pairwise, chain
from typing import List


#
#
# class Solution:
#     def __init__(self, w: List[int]):
#         total = sum(w)
#         acc = 0
#         # a list of decimals representing the upper bound (exclusive) for mapping random numbers to indices
#         self.mapping = [None] * len(w)
#
#         for i, weight in enumerate(w):
#             prob = weight / total
#             self.mapping[i] = (acc, prob + acc)
#             acc += prob
#
#     def pickIndex(self) -> int:
#
#         rand_num = random.random()
#
#         lo = 0
#         hi = len(self.mapping) - 1
#
#         while lo <= hi:
#             mid = (hi + lo) // 2
#             a, b = self.mapping[mid]
#             if a <= rand_num < b:
#                 return mid
#             if rand_num < a:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#

class Solution:

    def __init__(self, w: List[int]):
        # init prefix sum
        self.prefix_sum = list(pairwise(chain([0], accumulate(w))))
        # find rng multiplier
        self.multiplier = self.prefix_sum[-1][1]

    def pickIndex(self) -> int:
        # get randnum
        # apply mutliplier
        r = self.multiplier * random.random()
        # find lowest value in prefix sum above the multiplied rng [O(n lg n)]
        # return its index
        lo = 0
        hi = len(self.prefix_sum) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.prefix_sum[mid][0] <= r < self.prefix_sum[mid][1]:
                return mid
            elif r >= self.prefix_sum[mid][1]:
                lo = mid + 1
            else:
                hi = mid - 1

        """
        could do it this way too:
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        """


# -------------------------------->


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 4, 5])
c = Counter(obj.pickIndex() for _ in range(1000))
print(c)
