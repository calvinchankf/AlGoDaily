import sys


"""
    1st: dynamic programming, recursive bottom up + memoization
    - basically traverse all the paths, add up the values from the bottom
    - cache the running sum(from the bottom) to avoid redundant calculation

    Time    O(RC)
    Space   O(RC)
    160 ms, faster than 9.52%
"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.ht = {}
        cost = sys.maxsize
        for j in range(len(A[0])):
            cost = min(cost, self.dfs(A, 0, j))
        return cost

    def dfs(self, A, i, j):
        if i + 1 == len(A):
            return A[i][j]
        if (i, j) in self.ht:
            return self.ht[(i, j)]

        a, b, c = sys.maxsize, sys.maxsize, sys.maxsize

        if j - 1 >= 0:
            a = self.dfs(A, i+1, j-1) + A[i][j]

        b = self.dfs(A, i+1, j) + A[i][j]

        if j + 1 < len(A[0]):
            c = self.dfs(A, i+1, j+1) + A[i][j]

        cost = min(a, b, c)
        self.ht[(i, j)] = cost
        return cost


"""
    2nd: dynamic programming, bottom up
    - storing the minimum running sum from bottom of the matrix
    Time    O(RC)
    Space   O(RC)
    100 ms, faster than 62.54%
"""


class Solution(object):

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)-2, -1, -1):
            for j in range(len(A[0])):
                best = A[i+1][j]
                if j - 1 >= 0:
                    best = min(best, A[i+1][j-1])
                if j + 1 < len(A[0]):
                    best = min(best, A[i+1][j+1])
                A[i][j] += best
        res = sys.maxsize
        for j in range(len(A[0])):
            res = min(res, A[0][j])
        return res
