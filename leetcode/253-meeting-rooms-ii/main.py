import heapq

"""
    1st approach
    - sort the array
    - create an array to store the end time of the latest meeting in every room
    - each interval, compare the last meeting(since sorted) amongst the meeting in the meeting rooms
    - if there is no collision, put the meeting in that room, else create a new meeting room for the interval
    
    Time		O(NlogN)    sort
    Space 	    O(N)	    result array
    76 ms, faster than 52.42% 
"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        def cptr(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cptr)

        ends = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            found = False
            for j in range(len(ends)):
                if ends[j] <= s:
                    found = True
                    ends[j] = e
                    break
            if not found:
                ends.append(e)
        return len(ends)


"""
    2nd: sort + heap
    - sort the intervals by starting time
    - for each interval, compare the last meeting(since sorted) amongst the end times in the minheap
        - if there is no collision, put the meeting in that room
        - else create a new meeting room for the interval(by adding a new time in the minheap)

    Time    O(2NlogN)
    Space   O(N)
    64 ms, faster than 65.23%
"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        intervals = sorted(intervals, key=lambda x: x[0])

        pq = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if len(pq) > 0 and start >= pq[0]:
                heapq.heapreplace(pq, end)
            else:
                heapq.heappush(pq, end)
        return len(pq)
