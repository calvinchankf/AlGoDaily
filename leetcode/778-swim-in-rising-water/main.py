"""
    1st: binary search + BFS

    Time    O(NN logNN)
    Space   O(1)
    356 ms, faster than 14.26%
"""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        left = 0
        right = 2500
        while left < right:
            mid = (left + right) // 2
            b = self.canSwim(grid, mid)
            if b:
                right = mid
            else:
                left = mid + 1
        return left

    def canSwim(self, grid, mid):
        R = len(grid)
        C = len(grid[0])

        hs = set()
        q = [(0, 0)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] > mid:
                continue
            key = (i, j)
            if key in hs:
                continue
            hs.add(key)

            if i+1 == R and j+1 == C:
                return True

            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return False
