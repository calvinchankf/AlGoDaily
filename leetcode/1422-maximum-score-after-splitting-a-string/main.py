"""
    1st: prefix sum

    Time    O(2N)
    Space   O(N)
    20 ms, faster than 97.00%
"""


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        zeroCountFromLeft = n * [0]
        oneCountFromRight = n * [0]
        curZeroCount = 0
        curOneCount = 0
        for i in range(n):
            if s[i] == '0':
                curZeroCount += 1
                zeroCountFromLeft[i] = curZeroCount
            if s[n-i-1] == '1':
                curOneCount += 1
                oneCountFromRight[n-i-1] = curOneCount
        res = 0
        for i in range(n-1):
            temp = zeroCountFromLeft[i] + oneCountFromRight[i+1]
            res = max(res, temp)
        return res
