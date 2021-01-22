"""
    1st: dynamic programming (recursion + hashtable)

    Time    O(AS)
    Space   O(AS)
    944 ms, faster than 29.46%
"""


class Solution:
    def numWays(self, steps: int, N: int) -> int:
        return self.dfs(steps, N, 0, {})

    def dfs(self, remain, N, i, cache):
        if i < 0 or i == N:
            return 0
        if remain == 0:
            if i == 0:
                return 1
            return 0
        key = (remain, i)
        if key in cache:
            return cache[key]
        left = self.dfs(remain-1, N, i-1, cache)
        right = self.dfs(remain-1, N, i+1, cache)
        stay = self.dfs(remain-1, N, i, cache)
        total = left + right + stay
        cache[key] = total % (10**9 + 7)
        return cache[key]
