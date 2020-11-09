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
        res = C
        for i in range(R):
            left = 0
            right = C
            while left < right:
                mid = (left + right) // 2
                if binaryMatrix.get(i, mid) == 1:
                    right = mid
                else:
                    left = mid + 1
            res = min(res, left)
        if res == C:
            return -1
        return res
