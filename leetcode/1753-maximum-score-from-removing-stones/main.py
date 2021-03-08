from heapq import *

"""
    1st: heap

    Time    O(Nlog3) N:a+b+c
    Space   O(3)
    600 ms, faster than 33.33%
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        maxheap = [-a, -b, -c]
        heapify(maxheap)
        count = 0
        while len(maxheap) >= 2:
            a = heappop(maxheap)
            b = heappop(maxheap)
            count += 1
            a += 1
            b += 1
            if a < 0:
                heappush(maxheap, a)
            if b < 0:
                heappush(maxheap, b)
        return count
