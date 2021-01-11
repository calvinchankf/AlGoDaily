"""
    brute force string

    Time    O(N)
    Space   O(N)
    32 ms, faster than 75.81%
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        chars = ''
        for c in number:
            if c.isdigit():
                chars += c
        res = []
        while len(chars) > 0:
            if len(chars) == 4:
                res.append(chars[:2])
                res.append(chars[2:4])
                chars = []
            else:
                res.append(chars[:3])
                chars = chars[3:]
        return '-'.join(res)
