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
