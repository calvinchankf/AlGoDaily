import sys
"""
    questions to ask:
    - upper case == lower case? yes
    - if there is a tie, return the first one? yes
"""

"""
    1st approach: hashtable
    Time    O(L+WK)
    Space   O(K)
    76 ms, faster than 55.30%
"""


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        targetHt = self.getStructure(licensePlate)
        res = 'aaaaaaaaaaaaaaaaaaaaaaaaa'
        for w in words:
            curHt = self.getStructure(w)
            if self.ifContain(curHt, targetHt):
                if len(w) < len(res):
                    res = w
        return res

    def getStructure(self, s):
        s = s.lower()
        ht = 26 * [0]
        for c in s:
            i = ord(c) - ord('a')
            if 0 <= i < 26:
                ht[i] += 1
        return ht

    def ifContain(self, curHt, targetHt):
        for i in range(26):
            if curHt[i] < targetHt[i]:
                return False
        return True
