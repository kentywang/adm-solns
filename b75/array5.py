import collections
from functools import total_ordering
from typing import List

from misc.datastructs import Heap


@total_ordering
class NumberFrequency:
    def __init__(self, num, freq):
        self.number = num
        self.frequency = freq

    def _is_valid_operand(self, other):
        return (hasattr(other, "number") and
                hasattr(other, "frequency"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.frequency == other.frequency

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.frequency < other.frequency


# [(1,1), (2,5), (3,1), (4,4), (5,8)]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        h = Heap()

        for n, f in ct.items():
            h.push(NumberFrequency(num=n, freq=f))

        return list(h.pop().number for _ in range(k))


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([3, 0, 1, 0], 2))
print(1)
