"""
    Time    O(N)
    Space   O(1)
    108 ms, faster than 100.00%
"""


class Solution(object):
    def diagonalSum(self, mat):
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i]
        for i in range(n):
            res += mat[i][n-i-1]
        if n % 2 == 1:
            half = n//2
            res -= mat[half][half]
        return res
