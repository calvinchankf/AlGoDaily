
from heapq import *

"""
    1st: heap

    Time    O(NlogN)
    Space   O(N)
    596ms beat 10.77%
"""


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minheap = []
        res = 0
        speedSum = 0
        A = []
        for i in range(n):
            A.append((efficiency[i], speed[i]))
        A.sort(reverse=1)
        for e, s in A:
            heappush(minheap, s)
            speedSum += s
            if len(minheap) > k:
                speedSum -= heappop(minheap)
            res = max(res, speedSum * e)
        return res % (10**9 + 7)
