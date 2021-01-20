# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        1st approach: lower bound binary search

        Time    O(logn)
        Space   O(1)
        20 ms, faster than 60.60%
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
