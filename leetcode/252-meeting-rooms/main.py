"""
    1st approach
    - sort the array, compare the item[i].start and item[i-1].end
    
    Time	    O(nlogn)
    Space	    O(1)
    76 ms, faster than 39.42%
"""


class Solution(object):
    def canAttendMeetings(self, intervals):
        maxEnd = -sys.maxsize
        intervals.sort()
        for s, e in intervals:
            if s < maxEnd:
                return False
            maxEnd = e
        return True
