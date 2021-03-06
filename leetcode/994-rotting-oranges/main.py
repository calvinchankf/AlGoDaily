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
        caches = [C * [2**32] for _ in range(R)]
        # put rotten oranges into a queue
        q = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        # BFS
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] == 0:
                continue
            if steps >= caches[i][j]:
                continue
            caches[i][j] = steps
            q.append((i-1, j, steps + 1))
            q.append((i+1, j, steps + 1))
            q.append((i, j-1, steps + 1))
            q.append((i, j+1, steps + 1))
        # find the max distance + checking
        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if caches[i][j] == 2**32:
                        return -1
                    res = max(res, caches[i][j])
        return res
