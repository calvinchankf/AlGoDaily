"""
    1st: sort, dp
    - similar to lc84, 85
    e.g.
    [
        [1, 0, 1, 1]
        [1, 0, 1, 0]
        [0, 1, 1, 0]
    ]
    transform to
    [
        [1, 0, 1, 1]
        [2, 0, 2, 0]
        [0, 1, 3, 0]
    ]
    Then we sort every row,
    [
        [1, 1, 1, 0]
        [2, 2, 0, 0]
        [3, 1, 0, 0]
    ]
    For every cell, area = matrix[i][j] * (j+1)

    ref:
    - https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020682/Java-or-6ms-or-easy-understanding-with-comments-and-images

    Time    O(RC + RClogC)
    Space   O(1)
    1044 ms, faster than 95.10%
"""


class Solution(object):
    def largestSubmatrix(self, matrix):
        R, C = len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] = matrix[i-1][j] + 1
        res = 0
        for i in range(R):
            matrix[i].sort(reverse=True)
            for j in range(C):
                res = max(res, matrix[i][j] * (j+1))
        return res
