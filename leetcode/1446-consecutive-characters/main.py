"""
    1st: array interation

    Time    O(N)
    Space   O(1)
    44 ms, faster than 25.00%
"""


from collections import Counter


class Solution:
    def maxPower(self, s: str) -> int:
        maxCount = 0
        curCount = 0
        lastChar = ''
        for c in s:
            if c == lastChar:
                curCount += 1
            else:
                lastChar = c
                curCount = 1
            maxCount = max(maxCount, curCount)
        return maxCount


"""
    2nd: array interation
    - same logic as 1st approach

    Time    O(N)
    Space   O(1)
    28 ms, faster than 81.69%
"""


class Solution:
    def maxPower(self, s: str) -> int:
        maxCount = 1
        curCount = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curCount += 1
            else:
                curCount = 1
            maxCount = max(maxCount, curCount)
        return maxCount


"""
    3rd: 2pointers + hashtable

    Time    O(N)
    Space   O(N)
    124 ms, faster than 5.63%
"""


class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = Counter()
        j = 0
        res = 0
        for i in range(len(s)):
            c = s[i]
            ht[c] += 1
            while len(ht) > 1:
                left = s[j]
                j += 1
                ht[left] -= 1
                if ht[left] == 0:
                    del ht[left]
            res = max(res, i-j+1)
        return res
