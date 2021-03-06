"""
    1st approach: 2 pointers

    Time    O(n)
    Space   O(1)
    144 ms, faster than 74.03%
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        p1 = 0
        for c in t:
            if p1 < len(s) and c == s[p1]:
                p1 += 1
        return p1 == len(s)


"""
    2nd approach: same as 1st but break earlier
    
    Time    O(n)
    Space   O(1)
    148 ms, faster than 73.82%
"""


class Solution(object):
    def isSubsequence(self, word, S):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        i = 0
        for c in S:
            if c == word[i]:
                i += 1
            if i == len(word):
                return True
        return False
