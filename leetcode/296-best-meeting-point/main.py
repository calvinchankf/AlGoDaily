import sys
from typing import List 

"""
    1st approach: bfs + hashtable
    - similar to lc317
    - for each person, bfs to count the distance on the distance board
    
    Time    O(RRCC)
    Space   O(RRCC)
    LTE 56 / 57 test cases passed.
"""


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        R, C = len(grid), len(grid[0])
        dists = []
        for _ in range(R):
            dists.append(C * [0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dists)
        res = sys.maxsize
        for i in range(R):
            for j in range(C):
                res = min(res, dists[i][j])
        if res == sys.maxsize:
            return -1
        return res
    
    def bfs(self, grid, x, y, dists):
        q = [(x, y, 0)]
        seen = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            dists[i][j] += steps
            q.append((i-1, j, steps + 1))
            q.append((i+1, j, steps + 1))
            q.append((i, j-1, steps + 1))
            q.append((i, j+1, steps + 1))

s = Solution()

a = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
print(s.minTotalDistance(a))

a = [
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
print(s.minTotalDistance(a))

a = [[1,1]]
print(s.minTotalDistance(a))

print("-----")


"""
    2nd: math
    - the best point to meet on a line is the median of all the ones on a line
    - so the best point to meet on a grid where
        - i is the median of the rows
        - j is the median of the cols

    e.g. grid = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    
    Only care about the positions of ones:
    rows = [0, 0, 2]
    cols = [0, 4, 2] => [0, 2, 4]
    therefore,
        median of rows = 0
        median of cols = 2
    which is the coordinate (x, y) of the best meeting point


    ref:
    - https://leetcode.com/problems/best-meeting-point/solution/

    Time    O(RClogRC)
    Space   O(N)
    44 ms, faster than 96.88%
"""
class Solution(object):
    def minTotalDistance(self, grid):
        R, C = len(grid), len(grid[0])
        rows = []
        cols = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        median_row = rows[len(rows)//2]
        median_col = cols[len(cols)//2]
        return self.minDistance1D(rows, median_row) + self.minDistance1D(cols, median_col)
    
    def minDistance1D(self, points, median):
        d = 0
        for p in points:
            d += abs(p - median)
        return d

s = Solution()

a = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
print(s.minTotalDistance(a))

a = [
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
print(s.minTotalDistance(a))

a = [[1,1]]
print(s.minTotalDistance(a))