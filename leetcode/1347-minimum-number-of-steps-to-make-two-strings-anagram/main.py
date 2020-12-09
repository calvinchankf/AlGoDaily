"""
    1st: hashtable
    - count the number fo each character
    - subtract the source from target, to get the diff

    Time    O(S+T)
    Space   O(52)
    332 ms, faster than 16.01%
"""


from collections import *


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ht_t = 26 * [0]
        ht_s = 26 * [0]
        for c in t:
            idx = ord(c) - ord('a')
            ht_t[idx] += 1
        for c in s:
            idx = ord(c) - ord('a')
            ht_s[idx] += 1
        diff = 0
        for i in range(26):
            diff += abs(ht_s[i] - ht_t[i])
        return diff//2


"""
    followup: if not only lowercase letters
"""


class Solution(object):
    def minSteps(self, s, t):
        ht_s = Counter()
        ht_t = Counter()
        seen = set()
        for c in s:
            ht_s[c] += 1
            seen.add(c)
        for c in t:
            ht_t[c] += 1
            seen.add(c)
        diff = 0
        for c in seen:
            if c in ht_s and c in ht_t:
                diff += abs(ht_s[c] - ht_t[c])
            elif c in ht_s:
                diff += ht_s[c]
            elif c in ht_t:
                diff += ht_t[c]
        return diff//2
