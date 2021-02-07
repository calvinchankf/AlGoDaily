"""
    math: learned from others

    There are only 2 patterns, ABA and ABC, each of them has several opportunities to go

    ABA:
    BAB, CAC, BCB   <- 3
    CAB, BAC        <- 2

    ABC:
    CAC, BCB        <- 2
    CAB, BCA        <- 2

    Time    O(N)
    Space   O(1)
    60 ms, faster than 45.90%
"""


class Solution(object):
    def numOfWays(self, n):
        patternABA = 6
        patternABC = 6
        for i in range(2, n+1):
            temp = patternABA
            patternABA = 3 * patternABA + 2 * patternABC
            patternABC = 2 * temp + 2 * patternABC
        return (patternABA + patternABC) % (10**9 + 7)
