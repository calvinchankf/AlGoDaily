"""
    1st approach:
	1. sort the intervals by start time
	2. prepare a temporary array for nonoverlapping intervals
	3. when the current interval follows(behind and not overlap) the temp array last item, append to the temp array
	4. when the current interval overlaps but shorter than the temp array last item, replace the temp array last item, res++
	5. when the current interval overlaps with the previous interval, res++

    corner case: [[1,10], [2,3], [3,4], [4,5], [5,6], [7,8]]
    we should just remove the [1, 10]

	Time		O(nlogn)    built-in sort
	Space		O(n)		the temporary array
    56 ms, faster than 84.29%
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        def cmpter(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cmpter)

        res = 0
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s >= merged[-1][1]:
                merged.append([s, e])
            else:
                # if the current interval overlaps but is shorter than the merged[-1], replace merged[-1][1] with the shorter end
                if e < merged[-1][1]:
                    merged[-1][1] = e
                res += 1
        return res


"""
    2nd: activity selection
    - similar to 435, 646
    - sort by end time
    - update the count & curEnd greedily

    Time    O(NlogN)
    Space   O(1)
    92 ms, faster than 8.49%
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        legitCount = 0
        curEnd = -sys.maxsize
        for s, e in intervals:
            if s >= curEnd:
                curEnd = e
                legitCount += 1
        return len(intervals) - legitCount
