import sys
from typing import List

"""
    0th: brute force recursion

    Time    O(N!)
    LTE 22 / 44 test cases passed.
"""


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.res = sys.maxsize
        self.dfs(workers, bikes, 0)
        return self.res

    def dfs(self, workers, bikes, total):
        if len(workers) == 0:
            self.res = min(self.res, total)
            return
        x0, y0 = workers[0]
        for i in range(len(bikes)):
            x1, y1 = bikes[i]
            dist = abs(x0 - x1) + abs(y0-y1)
            self.dfs(workers[1:], bikes[:i] + bikes[i+1:], total + dist)


"""
    1st: dynamic programming (recursion + hashtable)

    Time    O(BBW) BW: hashtable, B: iteration in recursion
    Space   O(BW)
    128 ms, faster than 55.06%
"""


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        return self.dfs(workers, bikes, [], {})

    def dfs(self, workers, bikes, selectedBikes, ht):
        if len(workers) == 0:
            return 0

        key = (len(workers), tuple(sorted(selectedBikes)))
        if key in ht:
            return ht[key]
        minDist = sys.maxsize

        x0, y0 = workers[0]
        for i in range(len(bikes)):
            if i in selectedBikes:
                continue
            x1, y1 = bikes[i]
            dist = abs(x0 - x1) + abs(y0-y1)
            temp = self.dfs(workers[1:], bikes, selectedBikes + [i], ht) + dist
            minDist = min(minDist, temp)

        ht[key] = minDist
        return ht[key]
