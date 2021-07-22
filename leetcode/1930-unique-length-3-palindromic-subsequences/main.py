"""
    1st: hashtable
    - compare the forwardLetterCounts[i] and backwradLetterCounts[i]
    
    Time    O(26N)
    Space   O(26+26)
    8784 ms, faster than 25.00%
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        total = 26 * [0]
        for c in s:
            total[ord(c) - ord('a')] += 1
        forwards = 26 * [0]
        res = set()
        for c in s:
            backwards = self.getBackwardCounts(total, forwards)

            # remember to substract the current character from the backwradLetterCounts
            cIdx = ord(c) - ord('a')
            backwards[cIdx] -= 1

            # for every char from forward, if there is a counterpart on the other side(backward), we can form a palindromic
            for i in range(26):
                if forwards[i] > 0 and backwards[i] > 0:
                    res.add((i, cIdx, i))
            forwards[cIdx] += 1
        return len(res)

    def getBackwardCounts(self, total, forwards):
        backwards = 26 * [0]
        for i in range(26):
            backwards[i] = total[i] - forwards[i]
        return backwards
