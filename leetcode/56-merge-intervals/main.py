"""
    1st approach: sort
    1. sort the intervals by start time
    2. iterate the intervals and compare the cur interval start time with the last interval end time

    Time    O(nlogn)
    Space   O(n)
    84 ms, faster than 87.62%
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append(intervals[i])
        return res


a = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(a))

print("-----")

"""
    2nd approach: sort by comparator
    1. sort the intervals by start time and order by end time
    2. iterate the intervals and compare the cur interval start time with the last interval end time

    Time    O(nlogn)
    Space   O(n)
    92 ms, faster than 14.93%
    30apr2019
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        def cmpter(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cmpter)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append(intervals[i])
        return res
