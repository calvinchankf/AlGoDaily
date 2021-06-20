from collections import *

"""
    1st: hashtable + sort + line sweep
    - similar to lc732, l094, 1109, 1589, 1854
    - basically we can just use the prefix-sum concept to mark the start and the end of each interval

    Time of book()  O(NlogN)
    Space           O(N)
    2556 ms, faster than 6.58%
"""


class MyCalendarThree:

    def __init__(self):
        self.T = Counter()

    def book(self, start: int, end: int) -> int:
        self.T[start] += 1
        self.T[end] -= 1

        times = sorted([key for key in self.T])
        res = 0
        cur = 0
        for x in times:
            cur += self.T[x]
            res = max(res, cur)
        return res
