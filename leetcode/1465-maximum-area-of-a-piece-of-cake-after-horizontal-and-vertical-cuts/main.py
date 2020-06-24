"""
    1st: array min-max
    - sort the cuts
    - find the max intervals of width and height
    - the result is the product of maxWidth and maxHeight

    Time    O(NlogN + MlogM)
    Space   O(N+M)
    492 ms, faster than 100.00%
"""


class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        hcs = [0] + horizontalCuts + [h]
        vcs = [0] + verticalCuts + [w]
        hcs.sort()
        vcs.sort()
        maxWidth = 0
        for i in range(1, len(hcs)):
            maxWidth = max(maxWidth, hcs[i]-hcs[i-1])
        maxHeight = 0
        for i in range(1, len(vcs)):
            maxHeight = max(maxHeight, vcs[i]-vcs[i-1])
        return (maxWidth * maxHeight) % (10**9+7)
