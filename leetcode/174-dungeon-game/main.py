import sys

"""
    classic: dynamic programming

    ref:
    - https://leetcode.com/articles/dungeon-game
    - https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-9-lines-O(mn)-top-down-explained
    - https://leetcode.com/problems/dungeon-game/discuss/464716/Diego's-Understandable-Explanations-C%2B%2B

    Time    O(RC)
    Space   O(RC)
    48 ms, faster than 98.54%
"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0]*(c+1) for _ in range(r+1)]

        dp[r-1][c], dp[r][c-1] = 1, 1
        for i in range(r-1):
            dp[i][c] = sys.maxsize
        for j in range(c-1):
            dp[r][j] = sys.maxsize

        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                minFromRightOrBottom = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(minFromRightOrBottom - dungeon[i][j], 1)

        return dp[0][0]


s = Solution()

a = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
print(s.calculateMinimumHP(a))

a = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -500]
]
print(s.calculateMinimumHP(a))

a = [
    [-3, 5]
]
print(s.calculateMinimumHP(a))

a = [
    [0, 5],
    [-2, -3],
]
print(s.calculateMinimumHP(a))

a = [
    [-2, -3, 3, -4],
    [-5, -10, 1, -4],
    [10, 30, -5, 5],
    [10, 30, -5, -6],
]
print(s.calculateMinimumHP(a))
