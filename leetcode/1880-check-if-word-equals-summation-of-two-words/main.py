"""
    1st: string

    Time    O(N)
    Space   O(1)
    32 ms, faster than 40.00%
"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = self.convert2Num(firstWord)
        b = self.convert2Num(secondWord)
        c = self.convert2Num(targetWord)
        return a + b == c

    def convert2Num(self, s):
        res = 0
        for c in s:
            x = ord(c) - ord('a')
            res = res * 10 + x
        return res
