"""
    1st: dynamic programming
    - use prefixSums for cols and rols as caches to calculate squareSums

    Time    O(RC + RC*min(RC))
    Space   O(RC)
    5564 ms, faster than 10.37%
"""


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        horizontalSums = [(C+1) * [0] for _ in range(R+1)]
        verticalSums = [(R+1) * [0] for _ in range(C+1)]
        for i in range(R):
            for j in range(C):
                horizontalSums[i+1][j+1] = horizontalSums[i+1][j] + grid[i][j]
                verticalSums[j+1][i+1] = verticalSums[j+1][i] + grid[i][j]
        res = 0
        for i in range(1, R+1):
            for j in range(1, C+1):
                subRes = self.getSubLarget(
                    grid, i, j, horizontalSums, verticalSums)
                res = max(res, subRes)
        return res

    def getSubLarget(self, grid, i, j, horizontalSums, verticalSums):
        R, C = len(grid), len(grid[0])
        k = 0
        res = 0
        while i+k <= R and j+k <= C:
            sumSet = set()
            for d in range(k+1):
                sumSet.add(horizontalSums[i+d][j+k] - horizontalSums[i+d][j-1])
            for d in range(k+1):
                sumSet.add(verticalSums[j+d][i+k] - verticalSums[j+d][i-1])
            dialog1, dialog2 = 0, 0
            for d in range(k+1):
                dialog1 += grid[i+d-1][j+d-1]
                dialog2 += grid[i+d-1][j+k-d-1]
            sumSet.add(dialog1)
            sumSet.add(dialog2)
            k += 1
            if len(sumSet) == 1:
                res = max(res, k)
        return res
