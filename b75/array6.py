# 238. Product of Array Except Self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n

        res = []

        if zeros > 1:
            for n in nums:
                res.append(0)

        elif zeros == 1:
            for n in nums:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for n in nums:
                res.append(prod * (n ** -1))

        return res


x = Solution().productExceptSelf([1, 2, 3, 4])
print(x)

x = Solution().productExceptSelf([-1, 1, 0, -3, 3])
print(x)
