import sys

"""
    1st approach: bfs 
    - need a 2D array. for each cell, calculate the distance from 2s
    - after bfs, if there is still an 1 which the distance is not calculated, return -1

    Time    O(kRC) k=number of rotten oranges in the beginning
    Space   O(RC)
    64 ms, faster than 19.36%
"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        R, C = len(grid), len(grid[0])
        dist = [C * [sys.maxsize] for _ in range(R)]
        q = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] == 0:
                continue
            if steps >= dist[i][j]:
                continue
            dist[i][j] = steps
            q.append((i-1, j, steps + 1))
            q.append((i+1, j, steps + 1))
            q.append((i, j-1, steps + 1))
            q.append((i, j+1, steps + 1))

        res = 0
        for i in range(R):
            for j in range(C):
                if dist[i][j] == sys.maxsize:
                    if grid[i][j] == 1:
                        return -1
                else:
                    res = max(res, dist[i][j])
        return res
