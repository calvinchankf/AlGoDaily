"""
    1st: sort
    - similar to other interval problems lc252, 253, 495, 616, 759

    Time    O(NlogN)
    Space   O(N)
    96 ms, faster than 29.72%
"""


class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        def cmpter(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cmpter)
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] == merged[-1][0]:
                if cur[1] >= merged[-1][1]:
                    merged.pop()
                    merged.append(cur)
            elif cur[0] > merged[-1][0]:
                if cur[1] > merged[-1][1]:
                    merged.append(cur)
        return len(merged)

"""
    2nd: sort
    - but by descending end time

    Time    O(NlogN)
    Space   O(N)
    92 ms, faster than 50.86%
"""
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        def cmpter(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            return a[0] - b[0]
        intervals.sort(cmp=cmpter)
        mergeds = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < mergeds[-1][1]:
                if e > mergeds[-1][1]:
                    mergeds.append([s, e])
            else:
                mergeds.append([s, e])
        return len(mergeds)