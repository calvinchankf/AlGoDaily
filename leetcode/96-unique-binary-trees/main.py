"""
    Classic DP: Catalan Number
	- https://www.youtube.com/watch?v=YDf982Lb84o
    - https://www.youtube.com/watch?v=GgP75HAvrlY

    f(0) = 1
	f(1) = 1
	f(2) = f(1) + f(1)
	f(3) = f(2) + f(1)f(1) + f(2)
	f(4) = f(3) + f(1)f(2) + f(2)f(1) + f(3)
	f(5) = f(4) + f(1)f(3) + f(2)f(2) + f(3)f(1) + f(4)
	f(6) = f(5) + f(1)f(4) + f(2)f(3) + f(3)f(2) + f(4)f(1) + f(5)

	Time 	O(n^2) for each number, we need to iterate through the previous items and sum up the results
	Space	O(n)
	64 ms, faster than 59.42%
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        ht = {}
        ht[0] = 1
        ht[1] = 1
        return self.dfs(n, ht)

    def dfs(self, k, ht):
        if k in ht:
            return ht[k]
        total = 0
        for i in range(k):
            total += self.dfs(i, ht) * self.dfs(k-i-1, ht)
        ht[k] = total
        return ht[k]


"""
    2nd: same logic in iterative way
    28 ms, faster than 71.55%
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        ht = [0]*(n+1)
        ht[0] = 1
        ht[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                ht[i] += ht[j] * ht[i-j-1]
        return ht[n]
