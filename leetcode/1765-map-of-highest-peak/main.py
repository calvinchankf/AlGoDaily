"""
    1st: multisource BFS
    - noted that:
        1. since BFS can find the shortest path for every landCell, so we dont need to do steps comparison like lc994(rotten oranges)
        2. optimze the time by putting the dir
    
    Time    O(RC)
    Space   O(RC)
    6704 ms, faster than 20.00%
"""


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        grid = isWater

        R, C = len(grid), len(grid[0])
        cache = [C * [2**32] for _ in range(R)]

        q = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    q.append((i, j))
                    cache[i][j] = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(q) > 0:
            i, j = q.pop(0)

            for di, dj in dirs:
                _i = i + di
                _j = j + dj
                if _i < 0 or _i == R or _j < 0 or _j == C or cache[_i][_j] != 2**32:
                    continue
                cache[_i][_j] = cache[i][j] + 1
                q.append((_i, _j))

        return cache
