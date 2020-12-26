"""
    math

    Time    O(logN)
    Space   O(N)
"""


class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            match = n//2
            count += match
            n -= match
        return count
