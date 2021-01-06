"""
    dynamic programming: recursion + hashtable

    Time    O(N * 9) there are 9 digits (not 10 because 5 has zero cells to go)
    Space   O(N * 9)
    2464 ms, faster than 23.51%
"""


class Solution:
    def knightDialer(self, n: int) -> int:
        m = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        cache = {}
        total = 0
        for i in range(10):
            total += self.dfs(i, n-1, m, cache)
            total %= (10**9 + 7)
        return total

    def dfs(self, d, n, m, cache):
        if n == 0:
            return 1

        key = (d, n)
        if key in cache:
            return cache[key]

        total = 0
        cands = m[d]
        for c in cands:
            total += self.dfs(c, n-1, m, cache)
        cache[key] = total % (10**9 + 7)
        return cache[key]
