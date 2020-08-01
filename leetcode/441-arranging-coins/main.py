"""
    1st: binary search
    
    Time    O(logN)
    Space   O(1)
    44 ms, faster than 62.68%
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if n >= total:
                left = mid + 1
            else:
                right = mid
        return left - 1
