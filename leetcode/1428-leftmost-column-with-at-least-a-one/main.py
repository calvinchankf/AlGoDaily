"""
    binary search
    - similar to lc278

    Time    O(RlogC)
    Space   O(1)
    88 ms, faster than 100.00%
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """


class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        n, m = binaryMatrix.dimensions()
        minVal = m
        for i in range(n):
            idx = self.lowerBsearch(binaryMatrix, i, m)
            minVal = min(minVal, idx)
        return minVal if minVal < m else -1

    def lowerBsearch(self, binaryMatrix, n, m):
        left = 0
        right = m
        while left < right:
            mid = (left + right)//2
            if binaryMatrix.get(n, mid) == 1:
                right = mid
            else:
                left = mid + 1
        return left
