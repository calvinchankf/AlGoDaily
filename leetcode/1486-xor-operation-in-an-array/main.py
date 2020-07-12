"""
    1st: array

    Time    O(N)
    Space   O(1)
    16 ms, faster than 93.00%
"""


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = 0
        for i in range(n):
            res ^= start + 2*i
        return res
