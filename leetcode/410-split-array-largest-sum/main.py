from typing import List
import sys

"""
    1st: dynamic programming, recursion + hashtable
    - similar to lc813, 1043, 1335

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
    - similar to lc813, 1043, 1335
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
            sfs = self.dfs(nums, i+1, m - 1, ht, suffixSums)
            cur = max(pfs, sfs)
            res = min(res, cur)
        ht[key] = res
        return res


"""
    3rd: bottom up iteration
    - similar to lc813, 1043, 1335
    - tbh, it is hard to transform the recursive approach into this approach....

    ref:
    - https://www.youtube.com/watch?v=Cpy4T_rVuPk

    Time    O(M * N^2)
    Space   O(MN)
    5856 ms, faster than 18.00%
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        preffixSums = (n+1) * [0]
        for i in range(n):
            preffixSums[i+1] = preffixSums[i] + nums[i]

        dp = []
        for i in range(n + 1):
            dp.append((m + 1) * [sys.maxsize])

        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    cur = max(dp[k][j-1], preffixSums[i] - preffixSums[k])
                    dp[i][j] = min(dp[i][j], cur)

        return dp[-1][-1]
