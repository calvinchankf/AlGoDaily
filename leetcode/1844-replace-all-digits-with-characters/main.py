"""
    1st: string

    Time    O(N)
    Space   O(N)
    28 ms, faster than 100.00%
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            c = s[i]
            if s[i].isdigit():
                res += self.shift(s[i-1], int(c))
            else:
                res += c
        return res

    def shift(self, c, x):
        x %= 26
        asc = ord(c) + x
        return chr(asc)
