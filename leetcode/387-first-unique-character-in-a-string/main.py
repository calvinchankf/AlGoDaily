"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
	136ms beats 57.31%
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {}
        for c in s:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        for i in range(len(s)):
            if ht[s[i]] == 1:
                return i
        return -1
