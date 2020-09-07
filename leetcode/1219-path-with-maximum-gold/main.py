from typing import List

"""
    1st: backtracking
    - recursively traverse the matrix with dfs
    - to avoid redundant visiting:
        1. temporary put the candidate into the hashtable
        2. remove the candidate after the exploration
        This technique is known as backtacking
    - similar to lc51, 52

    Time    O(RRCC)
    Space   O(RC)
    1724 ms, faster than 41.22%
"""


class Solution(object):
    def getMaximumGold(self, grid):
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                ht = {}
                self.dfs(grid, i, j, ht, 0)
        return self.res

    def dfs(self, grid, i, j, ht, gold):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return
        if grid[i][j] == 0:
            return
        key = (i, j)
        if key in ht:
            return
        ht[key] = True

        gold += grid[i][j]
        self.res = max(self.res, gold)

        self.dfs(grid, i-1, j, ht, gold)
        self.dfs(grid, i+1, j, ht, gold)
        self.dfs(grid, i, j-1, ht, gold)
        self.dfs(grid, i, j+1, ht, gold)

        del ht[key]
        return


s = Solution()

a = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(s.getMaximumGold(a))

a = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(s.getMaximumGold(a))
