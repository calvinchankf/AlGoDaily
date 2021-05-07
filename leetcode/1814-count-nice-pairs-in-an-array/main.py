from collections import *

"""
    1st: hashtable + math
    
    - a pair is nice if  
        a + rev(b) == b + rev(a)
        a - rev(a) == b - rev(b)
    - it is a two-sum problem

    Time    O(N)
    Space   O(N)
    972 ms, faster than 9.25%
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ht = Counter()
        res = 0
        for i in range(len(nums)):
            key = nums[i] - self.rev(nums[i])
            if key in ht:
                res += ht[key]
                res %= 10**9 + 7
            ht[key] += 1
        return res

    def rev(self, num):
        res = 0
        while num > 0:
            res = 10*res + num % 10
            num //= 10
        return res
