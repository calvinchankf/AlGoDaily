from heapq import *

"""
    1st: max heap
    - i was given this question in the online test amazon in Nov2020
    
    idea:
    - the increase from 1/2 to 2/3 is 50% -> 66.6% = +16.6%
    - the increase from 3/6 to 4/7 is 50% -> 57.1% = +7.1%
    - so we can use a maxheap to keep popping the most significant increase(of a review) and add it to total, stop when we consumed all the extraStudents

    Time    O(NlogN)
    Space   O(N)
    2660 ms, faster than 100.00%
"""


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        total = 0
        maxheap = []
        for p, t in classes:
            ratio = p / t
            _ratio = (p + 1) / (t + 1)
            _increase = _ratio - ratio
            total += ratio
            heappush(maxheap, (-_increase, p+1, t+1))

        count = 0
        while count < extraStudents:
            count += 1
            increase, p, t = heappop(maxheap)
            total += -increase  # negative here since we use maxheap
            ratio = p / t
            _ratio = (p + 1) / (t + 1)
            _increase = _ratio - ratio
            heappush(maxheap, (-_increase, p+1, t+1))

        return total / n
