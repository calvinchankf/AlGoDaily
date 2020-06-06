from typing import List
import sys

"""
    1st: dynamic programming, recursion + hashtable
    - similar to lc813, lc1043  

    LTE 
    26 / 27 test cases passed.
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.dfs(nums, m, {})

    def dfs(self, nums, m, ht):
        if m == 1:
            return sum(nums)
        n = len(nums)
        key = (n, m)
        if key in ht:
            return ht[key]

        pfs = 0
        res = sys.maxsize
        for i in range(len(nums) - 1):
            pfs += nums[i]
            temp = self.dfs(nums[i+1:], m - 1, ht)
            cur = max(pfs, temp)
            res = min(res, cur)
        ht[key] = res
        return res
