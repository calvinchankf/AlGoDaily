from typing import List
import sys

"""
    1st: dynamic programming, recursion + hashtable
    - similar to lc813, lc1043
    - 

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


"""
    2nd:
    - optimize 1st approach with suffix sum and use start index instead of array slicing

    Time    O(M * N^2)
    Space   O(MN)
    7508 ms, faster than 5.66%
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        suffixSums = len(nums) * [0]
        sfs = 0
        for i in range(len(nums)-1, -1, -1):
            sfs += nums[i]
            suffixSums[i] = sfs

        return self.dfs(nums, 0, m, {}, suffixSums)

    def dfs(self, nums, start, m, ht, suffixSums):
        if m == 1:
            return suffixSums[start]
        key = (start, m)
        if key in ht:
            return ht[key]

        pfs = 0
        res = sys.maxsize
        for i in range(start, len(nums) - 1):
            pfs += nums[i]
            temp = self.dfs(nums, i+1, m - 1, ht, suffixSums)
            cur = max(pfs, temp)
            res = min(res, cur)
        ht[key] = res
        return res
