"""
    1st: easy dp
    - keep the peak when we traverse the list from the ocean
    - put the index of a higher building along the way
    - similar to lc121

    Time    O(N)
    Space   O(N)
    608 ms, faster than 100.00%
"""


class Solution(object):
    def findBuildings(self, heights):
        maxH = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            if h > maxH:
                maxH = h
                res.append(i)
        return res[::-1]
