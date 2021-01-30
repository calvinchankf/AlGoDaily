"""
    1st approach: classic dynamic programming approach
    - similar to lc1277

    ref:
    - https://www.youtube.com/watch?v=NYeVhmWsWec

    Time  O(r*c)
    Space O(r*c)
    160 ms, faster than 93.75%
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        R, C = len(matrix), len(matrix[0])
        dp = []
        for i in range(R):
            dp.append(C * [0])

        res = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == '1':
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i-1][j-1],
                            dp[i-1][j],
                            dp[i][j-1]
                        ) + 1
                    res = max(res, dp[i][j])
        return res**res


a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(Solution().maximalSquare(a))

a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "0", "0"],
]
print(Solution().maximalSquare(a))
