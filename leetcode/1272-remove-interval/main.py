"""
    1st: brute-force all cases

    Time    O(N) N: number of intervals
    Space   O(N)
    332 ms, faster than 34.48%
"""


class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for s, e in intervals:
            if e < toBeRemoved[0] or s > toBeRemoved[1]:
                res.append([s, e])
            elif s < toBeRemoved[0] and e > toBeRemoved[1]:
                res.append([s, toBeRemoved[0]])
                res.append([toBeRemoved[1], e])
            elif s < toBeRemoved[0] and e > toBeRemoved[0]:
                res.append([s, toBeRemoved[0]])
            elif s < toBeRemoved[1] and e > toBeRemoved[1]:
                res.append([toBeRemoved[1], e])
        return res
