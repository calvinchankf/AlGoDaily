"""
    naive approach:
    generate all the substrings and check

    Time    O(n^3)
    Space   O(1)
"""

"""
    1st approach: expand from center like lc5

    Time    O(n^2)
    Space   O(1)
    164 ms, faster than 64.96%
"""


class Solution(object):
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            res += self.expand(s, i-1, i)
            res += self.expand(s, i, i)
        return res

    def expand(self, s, left, right):
        i = left
        j = right
        if i < 0:
            return 0
        if s[i] != s[j]:
            return 0
        res = 1
        while i-1 >= 0 and j+1 < len(s) and s[i-1] == s[j+1]:
            res += 1
            i -= 1
            j += 1
        return res
