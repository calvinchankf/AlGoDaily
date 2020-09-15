from typing import List
from sys import maxsize
"""
    0th: brute force

    Time    O(2^N) try all subsets
    Space   O(2^N)
    LTE: 7 / 32 test cases passed.
"""


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.res = maxsize
        self.dfs(jobDifficulty, d, 0)
        if self.res == maxsize:
            return -1
        return self.res

    def dfs(self, nums, K, total):
        if K == 0 and len(nums) == 0:
            self.res = min(self.res, total)
        curMax = 0
        for i in range(len(nums)):
            curMax = max(curMax, nums[i])
            self.dfs(nums[i+1:], K-1, total + curMax)


"""
    1st: dynamic programming(recursion + hashtable)
    - similar to lc410, 1043, 1335
    - instead of calculating the max(subarray) from the top, we can do it from the bottom of the recursion
    - sub problem = min(
                        max(nums[:i]), 
                        max(nums[i:])
                    )

    Time    O(NNK)
    Space   O(N)
    2152 ms, faster than 25.61%
"""


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ht = {}
        res = self.dfs(jobDifficulty, d, ht)
        if res == maxsize:
            return -1
        return res

    def dfs(self, nums, K, ht):
        if K == 1:
            if len(nums) == 0:
                return maxsize
            return max(nums)
        key = (len(nums), K)
        if key in ht:
            return ht[key]
        # sub problem: find the minimum sum from all the a + b pairs
        res = maxsize
        a = 0
        for i in range(len(nums)):
            a = max(a, nums[i])
            b = self.dfs(nums[i+1:], K-1, ht)
            if a + b < res:
                res = a + b
        ht[key] = res
        return res
