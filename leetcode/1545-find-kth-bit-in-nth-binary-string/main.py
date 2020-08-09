"""
    1st: brute force

    Time    O(2^N)
    Space   O(2^N)
    1284 ms, faster than 12.50%
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = '0'
        i = 1
        while i < n:
            S = S + '1' + self.reverseInvert(S)
            i += 1
        return S[k-1]

    def reverseInvert(self, S):
        res = ''
        for i in range(len(S)-1, -1, -1):
            if S[i] == '0':
                res += '1'
            else:
                res += '0'
        return res
