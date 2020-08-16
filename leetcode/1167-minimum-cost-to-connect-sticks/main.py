import heapq

"""
    1st: heap

    Time    O(NlogN)
    Space   O(1)
    800 ms, faster than 82.10%
"""


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        res = 0
        pq = sticks[:]
        heapq.heapify(pq)
        while len(pq) > 1:
            a = heapq.heappop(pq)
            b = heapq.heappop(pq)
            c = a + b
            res += c
            heapq.heappush(pq, c)
        return res
