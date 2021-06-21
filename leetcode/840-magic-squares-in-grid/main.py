"""
    1st approach: brute force checking
    - for every cell within (M-2, N-2), get the sums from the rows, cols and diagonals and check if they equal

    Time    O(10RC)
    Space   O(9) -> O(1)
    28 ms, faster than 58.18%
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0
        res = 0
        for i in range(1, R-1):
            for j in range(1, C-1):
                res += self.isMagicGrid(grid, i, j)
        return res

    def isMagicGrid(self, grid, i, j):
        # check if from 1 to 9
        digits = set()
        for _i in range(i-1, i+2):
            for _j in range(j-1, j+2):
                if 0 < grid[_i][_j] < 10:
                    digits.add(grid[_i][_j])
        if len(digits) != 9:
            return 0
        diag1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
        diag2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
        row1 = grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]
        row2 = grid[i-1][j] + grid[i][j] + grid[i+1][j]
        row3 = grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]
        col1 = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
        col2 = grid[i][j-1] + grid[i][j] + grid[i][j+1]
        col3 = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
        s = set([diag1, diag2, row1, row2, row3, col1, col2, col3])
        return 1 if len(s) == 1 else 0
