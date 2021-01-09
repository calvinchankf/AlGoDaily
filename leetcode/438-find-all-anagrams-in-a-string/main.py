"""
    1st approach: sliding window
    - check if each substring is an anagram but dont use slice in every iteration

    Time    O(26S)
    Space   O(52)
    204 ms, faster than 32.10%
"""


from collections import *


class Solution(object):
    def findAnagrams(self, s, p):
        target = 26 * [0]
        for c in p:
            i = ord(c) - ord('a')
            target[i] += 1
        res = []
        cur = 26 * [0]
        j = 0
        for i in range(len(s)):
            c = s[i]
            idx = ord(c) - ord('a')
            cur[idx] += 1
            if i >= len(p):
                left = s[j]
                _idx = ord(left) - ord('a')
                cur[_idx] -= 1
                j += 1
            if self.isMatched(target, cur):
                res.append(j)
        return res

    def isMatched(self, a, b):
        for i in range(26):
            if a[i] != b[i]:
                return False
        return True


print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))


"""
    follow-up: all ascii characters

    Time    O(S+P)
    Space   O(S+P)
    1080ms beats 16.86%
"""


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter()
        for c in p:
            target[c] += 1
        res = []
        cur = Counter()
        j = 0
        for i in range(len(s)):
            c = s[i]
            cur[c] += 1
            if i >= len(p):
                left = s[j]
                cur[left] -= 1
                if cur[left] == 0:
                    del cur[left]
                j += 1
            if self.isMatched(target, cur):
                res.append(j)
        return res

    def isMatched(self, htA, htB):
        remain = Counter()
        for c in htA:
            remain[c] = htA[c]
        for c in htB:
            if c not in remain:
                return False
            remain[c] -= htB[c]
            if remain[c] == 0:
                del remain[c]
        return len(remain) == 0
