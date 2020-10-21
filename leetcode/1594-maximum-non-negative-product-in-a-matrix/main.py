import sys

"""
    1st: dynamic programming
    - combination of lc62 and lc152

    Time    O(RC)
    Space   O(RC)
    64 ms, faster than 100.00%
"""


class Solution(object):
    def maxProductPath(self, grid):
        R, C = len(grid), len(grid[0])
        res = -1

        mindp = []
        for _ in range(R):
            temp = []
            for _ in range(C):
                temp.append(sys.maxsize)
            mindp.append(temp)

        maxdp = []
        for _ in range(R):
            temp = []
            for _ in range(C):
                temp.append(-sys.maxsize)
            maxdp.append(temp)

        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    mindp[i][j] = grid[i][j]
                    maxdp[i][j] = grid[i][j]
                elif i == 0:
                    mindp[i][j] = mindp[i][j-1] * grid[i][j]
                    maxdp[i][j] = maxdp[i][j-1] * grid[i][j]
                elif j == 0:
                    mindp[i][j] = mindp[i-1][j] * grid[i][j]
                    maxdp[i][j] = maxdp[i-1][j] * grid[i][j]
                else:
                    if grid[i][j] > 0:
                        mindp[i][j] = min(
                            grid[i][j] * mindp[i-1][j],
                            grid[i][j] * mindp[i][j-1]
                        )
                        maxdp[i][j] = max(
                            grid[i][j] * maxdp[i-1][j],
                            grid[i][j] * maxdp[i][j-1]
                        )
                    else:
                        mindp[i][j] = min(
                            grid[i][j] * maxdp[i-1][j],
                            grid[i][j] * maxdp[i][j-1]
                        )
                        maxdp[i][j] = max(
                            grid[i][j] * mindp[i-1][j],
                            grid[i][j] * mindp[i][j-1]
                        )

        res = max(mindp[-1][-1], maxdp[-1][-1])
        if res < 0:
            return -1
        return res % (10**9+7)


s = Solution()

a = [[-1, -2, -3],
     [-2, -3, -3],
     [-3, -3, -2]]
print(s.maxProductPath(a))

a = [[1, -2, 1],
     [1, -2, 1],
     [3, -4, 1]]
print(s.maxProductPath(a))

a = [[1, 3],
     [0, -4]]
print(s.maxProductPath(a))

a = [[1, 4, 4, 0],
     [-2, 0, 0, 1],
     [1, -1, 1, 1]]
print(s.maxProductPath(a))

a = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]
print(s.maxProductPath(a))

a = [[2, 2, -2, 0, 3, -3, 1, 3, 2, 0], [-4, 4, 3, -4, -4, -1, -2, 4, -3, 1], [-3, 1, 2, 3, 0, 0, 4, -1, -1, -1], [3, -4, -4, -3, -4, 1, 3, 1, 4, 3], [-1, -4, 2, 1, 3, 0, -4, -1, 4, -2],
     [0, 4, 2, 3, 2, -1, -1, 1, 0, -1], [-2, 2, 2, 2, 2, -3, -1, 0, -3, 3], [-1, -1, -2, -2, -3, -4, 1, -1, 3, -3], [2, 2, 3, 2, -2, -2, 1, 3, -1, 1], [2, 1, 2, 4, -1, -3, -3, 2, 2, 4]]
print(s.maxProductPath(a))
