"""
    1st: greedy

    Time    O(1)
    Space   O(1)
    20 ms, faster than 100.00%
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        timeArr = [c for c in time]
        a = timeArr[0]
        b = timeArr[1]
        c = timeArr[3]
        d = timeArr[4]
        if a == '?':
            if timeArr[1] == '?' or int(timeArr[1]) < 4:
                timeArr[0] = '2'
            else:
                timeArr[0] = '1'
        if b == '?':
            if timeArr[0] == '2':
                timeArr[1] = '3'
            else:
                timeArr[1] = '9'
        if c == '?':
            timeArr[3] = '5'
        if d == '?':
            timeArr[4] = '9'
        return ''.join(timeArr)
