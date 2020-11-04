"""
    1st: backtracking

    Time    worst O(4^N) -> O(4 * 3^N)
    Space   O(N)
    56 ms, faster than 53.28%
"""


class Solution(object):
    def uniquePathsIII(self, grid):
        self.res = 0
        start = [-1, -1]
        dest = [-1, -1]
        k = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 2:
                    dest = [i, j]
                elif grid[i][j] == 0:
                    k += 1
        self.dfs(grid, start[0], start[1], dest, k, {})
        return self.res

    def dfs(self, grid, i, j, dest, k, ht):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return

        if i == dest[0] and j == dest[1]:
            if len(ht) - 1 == k:
                self.res += 1
            return

        if grid[i][j] == -1:
            return

        key = (i, j)
        if key in ht:
            return
        ht[key] = True

        self.dfs(grid, i-1, j, dest, k, ht)
        self.dfs(grid, i+1, j, dest, k, ht)
        self.dfs(grid, i, j-1, dest, k, ht)
        self.dfs(grid, i, j+1, dest, k, ht)

        del ht[key]
