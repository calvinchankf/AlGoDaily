"""
    1st approach: BFS + hashset
    - on each cell, BFS to traverse in 9 directions
    - use a hashset to avoid redundant visit

    Time    O(n^2)
    Space   O(n)
    1000 ms, faster than 14.14%
"""


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        ht = {}
        R, C = len(grid), len(grid[0])
        q = [(0, 0, 1)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue

            if grid[i][j] != 0:
                continue

            if i+1 == R and j+1 == C:
                return steps

            key = (i, j)
            if key in ht:
                continue
            ht[key] = True

            dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                    (1, 0), (1, -1), (0, -1), (-1, -1)]
            for di, dj in dirs:
                q.append((i+di, j+dj, steps+1))

        return -1
