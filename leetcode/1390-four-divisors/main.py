from typing import List
from math import ceil, sqrt

"""
    1st: faster brute force
    - for each number, get all of its factors
    - sum of factors of len(factors) == 4

    Time    O(N * sqrt(N))
    Space   O(N * 4) <- the worse case: all the numbers have 4 factors
    1004 ms, faster than 46.16%
"""


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        candidates = []
        for num in nums:
            factors = self.getFactors(num)
            if len(factors) == 4:
                candidates += factors
        return sum(candidates)

    def getFactors(self, n: int) -> List[int]:
        res = set()
        root = ceil(sqrt(n))
        for i in range(1, root+1):
            if n % i == 0:
                res.add(i)
                res.add(n//i)
        return list(res)


s = Solution()

print(s.getFactors(4))
print(s.getFactors(7))
print(s.getFactors(21))
print(s.getFactors(49))
print(s.getFactors(50))

a = [21, 4, 7]
print(s.sumFourDivisors(a))

a = [21, 4, 7, 50, 77]
print(s.sumFourDivisors(a))
