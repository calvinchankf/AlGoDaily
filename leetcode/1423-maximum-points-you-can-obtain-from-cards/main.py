"""
    1st: 2 arrays min max + sliding window?

    Time    O(N)
    Space   O(N)
    556 ms, faster than 25.90%
"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        forwards = n * [0]
        pfs = 0
        for i in range(n):
            pfs += cardPoints[i]
            forwards[i] = pfs

        backwards = n * [0]
        sfs = 0
        for i in range(n-1, -1, -1):
            sfs += cardPoints[i]
            backwards[i] = sfs

        res = max(forwards[k-1], backwards[n-k])
        for i in range(k-1):
            temp = forwards[i] + backwards[n-k+i+1]
            res = max(res, temp)
        return res
