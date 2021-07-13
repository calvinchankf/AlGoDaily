"""
    1st: dynamic programming(recursion + hashtable)

    Time    O(5N)
    Space   O(5N)
    1012 ms, faster than 17.65%
"""


class Solution(object):
    def countVowelPermutation(self, n):
        return self.dfs(n, -1, {})

    def dfs(self, n, vowelIdx, cache):
        if n == 0:
            return 1
        key = (n, vowelIdx)
        if key in cache:
            return cache[key]
        count = 0
        if vowelIdx == -1:
            count += self.dfs(n-1, 0, cache)
            count += self.dfs(n-1, 1, cache)
            count += self.dfs(n-1, 2, cache)
            count += self.dfs(n-1, 3, cache)
            count += self.dfs(n-1, 4, cache)
        elif vowelIdx == 0:
            count += self.dfs(n-1, 1, cache)
        elif vowelIdx == 1:
            count += self.dfs(n-1, 0, cache)
            count += self.dfs(n-1, 2, cache)
        elif vowelIdx == 2:
            count += self.dfs(n-1, 0, cache)
            count += self.dfs(n-1, 1, cache)
            count += self.dfs(n-1, 3, cache)
            count += self.dfs(n-1, 4, cache)
        elif vowelIdx == 3:
            count += self.dfs(n-1, 2, cache)
            count += self.dfs(n-1, 4, cache)
        elif vowelIdx == 4:
            count += self.dfs(n-1, 0, cache)
        count %= 10**9 + 7
        cache[key] = count
        return count


"""
    2nd: elegant implementation, learned from others

    Time    O(N)
    Space   O(5)
    200 ms, faster than 72.99%
"""


class Solution(object):
    def countVowelPermutation(self, n):
        a = e = i = o = u = 1
        for _ in range(n-1):
            a, e, i, o, u = e, a+i, a+e+o+u, i+u, a
        return (a+e+i+o+u) % (10**9+7)
