from typing import List

"""
    2nd: BFS + hashing
    - if 2 islands have the same shape, their nodes traversal order must be the same
    - so we can record the traversal direction as a hash, and use a hashtable to deduplicate the islands

    Time    O(RC)
    Space   O(RC)
    228 ms, faster than 61.82%
"""


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        R, C = len(grid), len(grid[0])
        res = set()
        seen = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i, j) not in seen:
                    pattern = self.bfs(grid, i, j, seen)
                    res.add(pattern)
        return len(res)

    def bfs(self, grid, x, y, seen):
        R, C = len(grid), len(grid[0])
        q = [(x, y)]
        pattern = []
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] != 1:
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            pattern.append((i-x, j-y))
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return tuple(pattern)
