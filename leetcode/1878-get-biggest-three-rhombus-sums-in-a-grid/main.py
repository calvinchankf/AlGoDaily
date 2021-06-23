from heapq import *

"""
    1st: math + min heap
    - at every point, the rhombus boundary is calculated by
        e.g. coordinate = (x, y), radius = 3

        consider the deltas, there are 4 possiblies
        0, 3 => (0, -3), (0, 3)
        1, 2 => (1, 2), (-1, 2), (1, -2), (-1, -2)
        2, 1 => (2, 1), (-2, 1), (2, -1), (-2, -1)
        3, 0 => (-3, 0), (3, 0)
    - use a maxheap to pop the smaller rhombusSums, so only the larger rhombusSums remain
    
    Time    O(RRCC)
    Space   O(RRCC)
    3584 ms, faster than 12.01%
"""


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        self.maxheap = []
        self.seen = set()
        for i in range(R):
            for j in range(C):
                self.processRhombusSum(grid, i, j)
        res = [x for x in self.maxheap]
        return sorted(res, reverse=True)

    def processRhombusSum(self, grid, i, j):
        R, C = len(grid), len(grid[0])
        maxRadius = min(R, C)
        for r in range(maxRadius):
            if i-r < 0 or i+r == R or j-r < 0 or j+r == C:
                break
            cands = set()
            for d in range(r+1):
                x = i + d
                y = j + r-d
                cands.add((x, y))
                x = i - d
                y = j + r-d
                cands.add((x, y))
                x = i + d
                y = j - (r-d)
                cands.add((x, y))
                x = i - d
                y = j - (r-d)
                cands.add((x, y))
            total = 0
            for x, y in cands:
                total += grid[x][y]
            if total in self.seen:
                continue
            self.seen.add(total)
            heappush(self.maxheap, total)
            if len(self.maxheap) > 3:
                heappop(self.maxheap)
