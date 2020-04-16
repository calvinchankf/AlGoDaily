from typing import List
from math import ceil, sqrt

"""
    1st: factorization
    - get the factors of num+1 and num+2
    - compare and return the result

    Time    O(2 * sqrt(N))
    Space   O(4)
    192 ms, faster than 72.42%
"""


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a, b = self.getFactors(num + 1)
        c, d = self.getFactors(num + 2)
        if abs(a - b) < abs(c - d):
            return [a, b]
        return [c, d]

    def getFactors(self, n: int) -> List[int]:
        root = ceil(sqrt(n))
        for i in range(root+1, 0, -1):
            if n % i == 0:
                return [i, n//i]


s = Solution()
# print(s.getFactors(124))
# print(s.getFactors(125))

# print(s.getFactors(1000))
# print(s.getFactors(1001))

print(s.closestDivisors(8))
print(s.closestDivisors(123))
print(s.closestDivisors(999))
print(s.closestDivisors(8876543567))
