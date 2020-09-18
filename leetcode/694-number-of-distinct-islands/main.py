from typing import List

"""
    2nd: BFS + hashing
    - if 2 islands have the same shape, their nodes traversal order must be the same
    - so we can record the traversal direction as a hash, and use a hashtable to deduplicate the islands

    Time    O(RC)
    Space   O(RC)
    340 ms, faster than 26.24%
"""


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = set()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    code = self.bfs(grid, i, j, seen)
                    res.add(code)
        return len(res)

    def bfs(self, grid, x, y, seen):
        code = ''
        q = [(x, y, '#')]
        while len(q) > 0:
            i, j, c = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if grid[i][j] == 0:
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            code += c
            q.append((i-1, j, c+'u'))
            q.append((i+1, j, c+'d'))
            q.append((i, j-1, c+'l'))
            q.append((i, j+1, c+'r'))
        return code
