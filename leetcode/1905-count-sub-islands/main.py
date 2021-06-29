"""
    1st: BFS + hashtable
    - mark grid1 islands with some IDs
    - see if every island in grid2 has to the same island ID

    Time    O(RC)
    Space   O(RC)
    5024 ms, faster than 50.00%
"""


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R, C = len(grid1), len(grid1[0])
        mapping = []
        for i in range(R):
            mapping.append(C * [-1])
        curId = 0
        seen = set()
        for i in range(R):
            for j in range(C):
                if grid1[i][j] == 0 or (i, j) in seen:
                    continue
                self.markIsland(grid1, i, j, mapping, seen, curId)
                curId += 1
        count = 0
        seen = set()
        for i in range(R):
            for j in range(C):
                if grid2[i][j] == 0 or (i, j) in seen:
                    continue
                b = self.checkIfOneIsland(grid2, i, j, mapping, seen)
                if b:
                    count += 1
        return count

    def markIsland(self, grid, x, y, mapping, seen, curId):
        R, C = len(grid), len(grid[0])
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] == 0:
                continue

            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            mapping[i][j] = curId

            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))

    def checkIfOneIsland(self, grid, x, y, mapping, seen):
        R, C = len(grid), len(grid[0])
        islandIds = set()
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] == 0:
                continue

            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            islandIds.add(mapping[i][j])

            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return len(islandIds) == 1 and list(islandIds)[0] != -1
