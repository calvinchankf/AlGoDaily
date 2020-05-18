"""
    1st approach: bit op
    - same as lc476
    - if the current bit is 0, add 1 << count the result
    - increment the count and N//2 when we iterating through the binary representation of the number

    Time    O(logn)
    Space   O(1)
    12 ms, faster than 98.08%
"""


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        res = 0
        i = 0
        while N > 0:
            if N & 1 == 0:
                res += 1 << i
            i += 1
            N >>= 1
        return res
