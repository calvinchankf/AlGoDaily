from collections import Counter
"""
    1st: hashtable

    Time    O(S+T)
    Space   O(S+T)
    40 ms, faster than 35.80%
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        htS = 26 * [0]
        htT = 26 * [0]
        for c in s:
            key = ord(c) - ord('a')
            htS[key] += 1
        for c in t:
            key = ord(c) - ord('a')
            htT[key] += 1
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            if htS[i] != htT[i]:
                return alphabets[i]
        return ''


"""
    2nd: hashtable

    Time    O(S+T)
    Space   O(S+T)
    40 ms, faster than 35.80%
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        htS = Counter()
        htT = Counter()
        for c in s:
            htS[c] += 1
        for c in t:
            htT[c] += 1
        for c in t:
            if c not in htS:
                return c
            if htS[c] < htT[c]:
                return c
        return ''
