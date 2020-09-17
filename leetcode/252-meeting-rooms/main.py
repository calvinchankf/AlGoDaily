"""
    1st approach
    - sort the array, compare the item[i].start and item[i-1].end
    
    Time	    O(nlogn)
    Space	    O(1)
    76 ms, faster than 39.42%
"""


class Solution(object):
    def canAttendMeetings(self, intervals):
        def cptr(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cptr)

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            prevStart, prevEnd = intervals[i-1]
            if curStart < prevEnd:
                return False
        return True
