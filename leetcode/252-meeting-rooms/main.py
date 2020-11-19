"""
    1st approach
    - sort the array, compare the item[i].start and item[i-1].end
    
    Time	    O(NlogN)
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


"""
    2nd: activity selection
    similar to lc646

    Time    O(NlogN)
    Space   O(1)
    60 ms, faster than 50.71% 
"""


class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[1])
        curEnd = -sys.maxsize
        for s, e in intervals:
            if s >= curEnd:
                curEnd = e
            else:
                return False
        return True
