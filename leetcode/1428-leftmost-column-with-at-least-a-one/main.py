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
        R, C = binaryMatrix.dimensions()
        minVal = C
        for i in range(R):
            idx = self.lowerBsearch(binaryMatrix, i, C)
            minVal = min(minVal, idx)
        return minVal if 0 <= minVal < C else -1

    def lowerBsearch(self, binaryMatrix, R, C):
        left = 0
        right = C
        while left < right:
            mid = (left + right)//2
            if binaryMatrix.get(R, mid) == 1:
                right = mid
            else:
                left = mid + 1
        return left
