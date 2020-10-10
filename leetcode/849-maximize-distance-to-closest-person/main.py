"""
    1st: array
    - there are 3 only cases
        1. alex seats between two 1s
        2. alex seats at the first seat
        3. alex seats at the last seat

    Time    O(N)
    Space   O(1)
    100 ms, faster than 98.32%
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        n = len(seats)
        res = 0
        j = -sys.maxsize
        for i in range(n):
            if seats[i] == 1:
                if j == -sys.maxsize:
                    mid = i
                    diff = mid
                    res = max(res, diff)
                else:
                    mid = (i + j)//2
                    diff = mid - j
                    res = max(res, diff)
                j = i
        lastDiff = n - 1 - j
        res = max(res, lastDiff)
        return res