"""
    1st: brute force with suffix string

    Time    O(N^2) string comparison & string concat take O(N)
    Space   O(N)

    Python 2: LTE 22 / 24 test cases passed
    Python 3: 3576 ms, faster than 10.08%
"""


class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        sfs = ''
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            sfs = c + sfs
            if sfs > res:
                res = sfs
        return res
