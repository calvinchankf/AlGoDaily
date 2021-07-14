from heapq import *

"""
    1st: math + min heap
    - calculate the arrival time
    - kill the monsters one by one until a monster reaches me

    Time    O(NlogN)
    Space   O(N)
    904 ms, faster than 14.29% 
"""


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        pq = []
        n = len(dist)
        for i in range(n):
            arrivalTime = dist[i] / speed[i]
            heappush(pq, arrivalTime)
        res = 0
        curTime = 0
        while len(pq) > 0 and heappop(pq) > curTime:
            res += 1
            curTime += 1
        return res
