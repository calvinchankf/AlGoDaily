"""
    1st: BFS
    - find the starting point
    - find pizzas and put them in a hashset
    - BFS

    Time    O(RC)
    Space   O(RC)
    640 ms, faster than 100.00%
"""


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        startI, startJ = -1, -1
        targets = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '*':
                    startI, startJ = i, j
                if grid[i][j] == '#':
                    targets.add((i, j))
        if startI == -1 or startJ == -1 or len(targets) == 0:
            return -1
        q = [(startI, startJ, 0)]
        seen = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            key = (i, j)
            if key in targets:
                return steps
            if grid[i][j] == 'X':
                continue
            if key in seen:
                continue
            seen.add(key)
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))
        return -1
