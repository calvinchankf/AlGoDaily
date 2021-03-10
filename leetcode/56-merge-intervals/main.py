"""
    1st approach: sort
    - similar to lc56, 452, 616, 758
    1. sort the intervals by start time
    2. iterate the intervals and compare the cur interval start time with the last interval end time

    Time    O(NlogN)
    Space   O(N)
    80 ms, faster than 91.82%
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort()
        res = []
        for s, e in intervals:
            if len(res) > 0 and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res


a = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(a))
