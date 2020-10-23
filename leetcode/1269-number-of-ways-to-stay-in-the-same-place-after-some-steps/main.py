"""
    1st: dynamic programming (recursion + hashtable)

    Time    O(AS)
    Space   O(AS)
    944 ms, faster than 29.46%
"""
class Solution(object):
    def numWays(self, steps, arrLen):
        return self.dfs(steps, arrLen, 0, {})
        
    def dfs(self, steps, arrLen, n, ht):
        if n < 0 or n == arrLen:
            return 0
        if steps == 0:
            if n == 0:
                return 1
            return 0
        key = (steps, n)
        if key in ht:
            return ht[key]
        left = self.dfs(steps-1, arrLen, n-1, ht)
        stay = self.dfs(steps-1, arrLen, n, ht)
        right = self.dfs(steps-1, arrLen, n+1, ht)
        ht[key] = (left + stay + right) % (10**9+7)
        return ht[key]