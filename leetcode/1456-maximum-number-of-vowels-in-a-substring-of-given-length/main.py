"""
    1st: sliding window

    Time    O(N)
    Space   O(1)
    468 ms, faster than 100.00%
"""


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        resCount = 0
        curCount = 0
        for i in range(len(s)):

            if i >= k:
                lastChar = s[i-k]
                if lastChar in ['a', 'e', 'i', 'o', 'u']:
                    curCount -= 1

            char = s[i]
            if char in ['a', 'e', 'i', 'o', 'u']:
                curCount += 1
            resCount = max(resCount, curCount)
        return resCount
