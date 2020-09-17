from typing import List


"""
    1st approach: binary search + merge intervals
    1. upper bound binary search the intervals to insert the new interval
    2. merge the intervals

    Time    O(logn + n) => O(n)
    Space   O(n) result
    64 ms, faster than 77.77%
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        # insert the new interval into the right position
        upperIdx = self.bsearch(intervals, newInterval)
        intervals.insert(upperIdx, newInterval)
        # merge the intervals
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])
        return merged

    def bsearch(self, intervals, target):
        left = 0
        right = len(intervals)
        while left < right:
            mid = (left + right)//2
            if target[0] >= intervals[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right

    # upper bound binary search
    def bsearch(self, intervals, target):
        left = 0
        right = len(intervals)
        while left < right:
            mid = (left + right)/2
            if target[0] >= intervals[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))

print("---")


"""
    2nd: insert + sort + merge intervals

    Time    O(NlogN)
    Space   O(N)
    104 ms, faster than 28.81%
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])
        return merged
