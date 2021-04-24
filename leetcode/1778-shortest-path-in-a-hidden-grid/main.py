"""
    1st: DFS + BFS
    - assume the current location is at (0, 0)
    - DFS to get all the cells location
    - BFS to find the shortest path from (0, 0) to destination

    Time    O(RC)
    Space   O(RC)
    6240 ms, faster than 100.00% 
"""

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> bool:
#
#
#    def isTarget(self) -> None:
#
#


class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        dirs = {
            'U': (-1, 0),
            'D': (1, 0),
            'R': (0, -1),
            'L': (0, 1)
        }
        counterDirs = {
            'U': 'D',
            'D': 'U',
            'R': 'L',
            'L': 'R'
        }

        isValid = {}
        isValid[(0, 0)] = master.isTarget()

        # dfs
        def dfs(i, j):
            for d in dirs:
                di, dj = dirs[d]
                _i, _j = i + di, j + dj
                if (_i, _j) not in isValid and master.canMove(d):
                    master.move(d)
                    isValid[(_i, _j)] = master.isTarget()
                    dfs(_i, _j)
                    master.move(counterDirs[d])
        dfs(0, 0)

        # bfs
        q = [(0, 0, 0)]
        seen = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if isValid[(i, j)]:
                return steps
            if (i, j) in seen:
                continue
            seen.add((i, j))
            for d in dirs:
                di, dj = dirs[d]
                _i, _j = i + di, j + dj
                if (_i, _j) in isValid:
                    q.append((_i, _j, steps+1))
        return -1
