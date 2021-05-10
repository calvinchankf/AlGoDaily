from heapq import *

"""
    1st: DFS + dijkstra
    - run a DFS to get all the cells' cost
    - run a dijkstra to find the cheapest path to destination

    Time    O((E + V) x logV)
    Space   O(V)
    1568 ms, faster than 100.00%
"""

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> int:
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

        if master.isTarget():
            return 0

        grid = {}
        grid[(0, 0)] = 0
        self.dest = None

        # dfs
        def dfs(i, j):
            for d in dirs:
                di, dj = dirs[d]
                _i, _j = i + di, j + dj
                if (_i, _j) not in grid and master.canMove(d):
                    grid[(_i, _j)] = master.move(d)
                    if master.isTarget() == True:
                        self.dest = (_i, _j)
                    dfs(_i, _j)
                    master.move(counterDirs[d])
        dfs(0, 0)

        if self.dest == None:
            return -1

        # dijkstra
        minheap = [(0, 0, 0)]
        best = {}
        while len(minheap) > 0:
            cost, i, j = heappop(minheap)
            key = (i, j)
            if key in best and cost >= best[key]:
                continue
            best[key] = cost
            for d in dirs:
                di, dj = dirs[d]
                _i, _j = i + di, j + dj
                if (_i, _j) in grid:
                    heappush(minheap, (cost + grid[(_i, _j)], _i, _j))
        return best[self.dest]
