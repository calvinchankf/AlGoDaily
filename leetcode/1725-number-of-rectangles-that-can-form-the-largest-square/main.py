"""
    1st: array

    Time    O(N)
    Space   O(1)
    140 ms, faster than 66.67%
"""


class Solution(object):
    def countGoodRectangles(self, rectangles):
        maxLen = 0
        maxLenCount = 0
        for l, w in rectangles:
            temp = min(l, w)
            if temp > maxLen:
                maxLen = temp
                maxLenCount = 1
            elif temp == maxLen:
                maxLenCount += 1
        return maxLenCount
