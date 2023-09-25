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

    def threeSumV3(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            # skip dupes in 1st position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                # skip dupes in 2nd position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return res


x = Solution().threeSumV3([-1, 0, 1, 2, -1, -4])
x = Solution().threeSumV3([0, 0, 0, 0])
print(x)
