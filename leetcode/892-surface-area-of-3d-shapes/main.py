"""
    1st: math
    - for every non-zero box
        - calculate the area of the top and bottom
        - calculate the area of 4 vertical sides
    
    Time    O(RC)
    Space   O(1)
    68 ms, faster than 87.10%
"""


class Solution(object):
    def surfaceArea(self, grid):
        R, C = len(grid), len(grid[0])
        area = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    continue
                # top, bottom
                area += 2
                # 4 sides
                for di, dj in dirs:
                    _i = i + di
                    _j = j + dj
                    if _i < 0 or _i == R or _j < 0 or _j == C:
                        area += grid[i][j]
                    elif grid[i][j] > grid[_i][_j]:
                        area += grid[i][j] - grid[_i][_j]
        return area
