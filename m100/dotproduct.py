"""
Planning:   16:49 - 17:08 (19m)
Coding:     - 17:16 (8m)
One timer!

Observations:
- only need to calculate product where on indices of A and B where both indices are nonzero

Options:
- Brute force: store size n list for A, B. Iterate and multiply each.
    Time: O(n), Space: O(n)
- Theoretical best:
    Time: O(min(j,k)) where j = nonzeros in A, k = nonzeroes in b, Space: O(j + k)
- Hash map (with a list of nonzero elements): We can quickly iterate through all indices and compare them against another hash map. If j = nonzeros in A, k = nonzeroes in b, we can check existence in min(j, k), where
each check is followed up by a multiplication and accumulation
    Time: like the theoretical best

Sandbox:
--------------------

nums    1, 0, 0, 2, 3   =>  1, '2z', 2, 3       Compaction (harder to calculate subsequent indices for dot prod)
i       0  1  2  3  4       {0:1, 3:2, 4:3}     Hash map without 0s

-------------------
Cases:
- [1], [0] => {0:1}, {} => no mults, 0
- [0], [0] => {}, {} => ''

If only one is sparse, i.e.
[1,0,0,...,5,0,...,2]
[1,3,4,2,4,2,3,4,5,1]
our data struct picks it to iterate on instead of the other, so we don't have to do as many hash set checks.
"""
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Time: O(n)
        Space: O(k)
        """
        self.c = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.c[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        # a will be smaller or equal in size to b
        a, b = (self.c, vec.c) if len(self.c) <= len(vec.c) else (vec.c, self.c)

        acc = 0
        for i in a:
            if i in b:
                acc += (a[i] * b[i])

        return acc
# ------------------------------------->
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
