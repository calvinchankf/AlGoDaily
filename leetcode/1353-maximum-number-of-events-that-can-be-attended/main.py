import heapq

"""
    2nd: learned from others
    1. loop over 10^5 days
    2. on each day
        - pop the events that end before today
        - push the events that start from today
        - then greedily attend the event that ends soonest, res += 1

    ref:
    - https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue
    - https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510262/Detailed-analysisLet-me-lead-you-to-the-solution-step-by-step

    Time    O(10^5 x logN)
    Space   O(N)
    1900 ms, faster than 45.54%
"""


class Solution(object):
    def maxEvents(self, events):
        pq = []
        events.sort(key=lambda x: x[0])
        idx = 0
        res = 0
        n = len(events)
        for day in xrange(1, 100001):
            while len(pq) > 0 and pq[0] < day:
                heapq.heappop(pq)
            while idx < n and events[idx][0] == day:
                heapq.heappush(pq, events[idx][1])
                idx += 1
            if len(pq) > 0:
                heapq.heappop(pq)
                res += 1
        return res
