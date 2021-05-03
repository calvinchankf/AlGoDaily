"""
    1st: knapsack, recursion + hashtable
    - this is a classic knapsack problem

    Time    O(SMN)
    Space   O(SMN)
    2652 ms, faster than 86.34%
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        weights = []
        for s in strs:
            zeros, ones = 0, 0
            for c in s:
                if c == '0':
                    zeros += 1
                elif c == '1':
                    ones += 1
            weights.append((zeros, ones))
        return self.dfs(weights, 0, m, n, {})

    def dfs(self, weights, idx, m, n, cache):
        if m == 0 and n == 0:
            return 0
        if idx == len(weights):
            return 0

        # DP
        key = (idx, m, n)
        if key in cache:
            return cache[key]

        # get the count of zeros and ones of the current str
        zeros, ones = weights[idx]

        # consider the current str if we have enough quota
        if zeros <= m and ones <= n:
            selected = 1 + self.dfs(weights, idx + 1,
                                    m - zeros, n - ones, cache)
            notSelected = self.dfs(weights, idx + 1, m, n, cache)
            cache[key] = max(selected, notSelected)
        else:
            cache[key] = self.dfs(weights, idx + 1, m, n, cache)

        return cache[key]
