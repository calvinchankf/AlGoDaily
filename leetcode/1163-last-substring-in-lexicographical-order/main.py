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


"""
    2nd: 3 pointers
    - learned from others
    
    idea:
    i: start of left subtring
    j: start of right substring
    k: the shared length of substrings

    e.g.1: when both string equal to each other, keep increasing k
        i        j
        zzzab....zzzab...
    k=      ^        ^

    e.g.2: when left substring is smaller, let left substring = right substring, so zzzaa becomes zzzab
        i        j
        zzzaa....zzzab...
    k=      ^        ^
                 ^new i

    e.g.3: when right substring is smaller, start the right substring from j+k+1. Just like we start new right substring
        i        j
        zzzab....zzzaa...
    k=      ^        ^
                      ^new j

    Time    O(N)
    Space   O(1)
    264 ms, faster than 64.49%
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 0
        j = i + 1
        k = 0
        while j + k < len(s):
            if s[i+k] == s[j+k]:
                k += 1
            else:
                if s[i+k] < s[j+k]:
                    i = j
                    j = i + 1
                else:
                    j = j + k + 1
                k = 0
        return s[i:]
