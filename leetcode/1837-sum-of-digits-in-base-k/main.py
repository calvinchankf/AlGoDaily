"""
    1st: math

    Time    O(logN / logK)
    Space   O(1)
    28 ms, faster than 100.00%
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n > 0:
            res += n % k
            n //= k
        return res
