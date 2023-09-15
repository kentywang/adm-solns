from typing import List


class Solution:
    def threeSumV1(self, nums: List[int]) -> List[List[int]]:
        def twosum(xs, n):
            for j, x in enumerate(xs):
                for y in range(j + 1, len(xs)):
                    if x + xs[y] + n == 0:
                        res.add(tuple(sorted([x, xs[y], n])))

        res = set()

        for i, n in enumerate(nums):
            # O(n) timespace
            rest_of_nums = nums[:i] + nums[i + 1:]
            twosum(rest_of_nums, n)

        return list(list(r) for r in res)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(val, idx):
            hashmap = {}
            for i, n in enumerate(nums):
                if i == idx:
                    continue

                tgt = (n + val) * -1
                if tgt in hashmap:
                    res.add(tuple(sorted([val, n, tgt])))

                hashmap[n] = i

        res = set()
        for i, n in enumerate(nums):
            twosum(n, i)

        return list(list(r) for r in res)


x = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(x)
