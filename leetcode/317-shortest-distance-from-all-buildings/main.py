import sys

"""
    1st approach: BFS + hastable
    - similar to lc286: walls and gates
    - on each cell
        - sum up all the steps from each buildings
        - record the number of buildings which can access this cell
    - find the min

    Time    O(kRRCC) k: number of buildings
    Space   O(2RC)
    1112 ms, faster than 24.56%
"""


class Solution(object):
    def shortestDistance(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        R, C = len(grid), len(grid[0])
        dists = []
        visitCounts = []
        for _ in range(R):
            dists.append(C * [0])
            visitCounts.append(C * [0])
        buildingCount = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    buildingCount += 1
                    self.bfs(grid, i, j, dists, visitCounts)
        res = sys.maxsize
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0 and visitCounts[i][j] == buildingCount:
                    res = min(res, dists[i][j])
        if res == sys.maxsize:
            return -1
        return res
    
    def bfs(self, grid, x, y, dists, visitCounts):
        q = [(x, y, 0)]
        seen = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if (i == x and j == y) or (grid[i][j] != 1 and grid[i][j] != 2):
                dists[i][j] += steps
                visitCounts[i][j] += 1
                q.append((i-1, j, steps + 1))
                q.append((i+1, j, steps + 1))
                q.append((i, j-1, steps + 1))
                q.append((i, j+1, steps + 1))


a = [
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
print(Solution().shortestDistance(a))

a = [
    [0, 2, 1],
    [1, 0, 2],
    [0, 1, 0],
]
print(Solution().shortestDistance(a))
