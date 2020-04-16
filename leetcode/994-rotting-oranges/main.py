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

        dist = []
        q = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(sys.maxsize)
                if grid[i][j] == 2:
                    q.append((i, j, 0))
            dist.append(temp)

        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if grid[i][j] != 1 and grid[i][j] != 2:
                continue
            if steps < dist[i][j]:
                dist[i][j] = steps
                q.append((i-1, j, steps+1))
                q.append((i+1, j, steps+1))
                q.append((i, j-1, steps+1))
                q.append((i, j+1, steps+1))

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if dist[i][j] == sys.maxsize:
                        return -1
                    res = max(res, dist[i][j])
        return res
