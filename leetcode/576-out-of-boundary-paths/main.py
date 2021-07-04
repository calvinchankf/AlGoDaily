"""
    1st: brute force BFS

    Time    O(4^N)
    LTE     12 / 94 test cases passed.
"""


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        q = [(i, j, 0)]
        res = 0
        while len(q) > 0:
            _i, _j, steps = q.pop(0)
            if steps > N:
                continue
            if _i < 0 or _i == m or _j < 0 or _j == n:
                res += 1
                continue
            q.append((_i-1, _j, steps+1))
            q.append((_i+1, _j, steps+1))
            q.append((_i, _j-1, steps+1))
            q.append((_i, _j+1, steps+1))
        return res


"""
    2nd: dynamic programming(recursion + hashtable)

    Time        O(mnN)
    Space       O(mnN)
    128 ms, faster than 70.21%
"""


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        return self.dfs(m, n, N, i, j, {})

    def dfs(self, m, n, N, i, j, cache):
        if N < 0:
            return 0
        if i < 0 or i == m or j < 0 or j == n:
            return 1
        key = (i, j, N)
        if key in cache:
            return cache[key]
        total = 0
        total += self.dfs(m, n, N-1, i-1, j, cache)
        total += self.dfs(m, n, N-1, i+1, j, cache)
        total += self.dfs(m, n, N-1, i, j-1, cache)
        total += self.dfs(m, n, N-1, i, j+1, cache)
        total %= 10**9 + 7
        cache[key] = total
        return total
