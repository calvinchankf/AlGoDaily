"""
    1st: brute force

    Time    O(NlogN) binary transformation takes O(logN) time
    Space   O(N)
    1448 ms, faster than 62.18% 
"""


class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        s = ''
        while x < n:
            x += 1
            s += str(bin(x))[2:]
        return int(s, 2) % (10**9 + 7)
