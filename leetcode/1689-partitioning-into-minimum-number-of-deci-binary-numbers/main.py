"""
    math ???
    - the result is actually the largest digit in the input string

    Time    O(N) N: number of digits in input string
    Space   O(1)
    468 ms, faster than 33.33%
"""


class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        maxNum = 0
        for c in n:
            maxNum = max(maxNum, int(c))
        return maxNum
