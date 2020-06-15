"""
    1st: array interation

    Time    O(N)
    Space   O(1)
    44 ms, faster than 25.00%
"""


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
    44 ms, faster than 25.00%
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
