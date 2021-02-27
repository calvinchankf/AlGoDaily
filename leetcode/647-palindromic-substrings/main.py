"""
    naive approach:
    generate all the substrings and check

    Time    O(n^3)
    Space   O(1)
"""

"""
    1st approach: expand from center like lc5

    Time    O(N^2)
    Space   O(1)
    164 ms, faster than 64.96%
"""


class Solution(object):
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            a = self.explore(s, i, i)
            b = self.explore(s, i, i+1)
            res += a + b
        return res

    def explore(self, s, left, right):
        if right == len(s) or s[left] != s[right]:
            return 0
        count = 1
        while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
            count += 1
            left -= 1
            right += 1
        return count
