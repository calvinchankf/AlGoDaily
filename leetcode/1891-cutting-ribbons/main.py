"""
    1st: binary search
    
    Time    O(32N)
    Space   O(1)
    3680 ms, faster than 100.00% 
"""


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 1
        right = 2**32
        while left < right:
            mid = (left + right)//2
            count = self.countRibbons(ribbons, mid)
            if count >= k:
                left = mid + 1
            else:
                right = mid
        return right - 1

    def countRibbons(self, ribbons, L):
        res = 0
        for i in range(len(ribbons)):
            res += ribbons[i] // L
        return res
