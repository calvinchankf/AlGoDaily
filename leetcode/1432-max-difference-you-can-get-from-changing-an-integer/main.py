"""
    1st: string
    - replace characters to 0 or 1 to get the lowerBound
    - replace characters to 9 to get the upperBound

    Time    O(N + N^2) 
    Space   O(N)
    48 ms, faster than 33.33%
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        lowerBound = 10**8
        upperBound = 0
        s = str(num)
        for i in range(len(s)):
            replacement = '0'
            if i == 0 or s[0] == s[i]:
                replacement = '1'
            temp = s.replace(s[i], replacement)
            lowerBound = min(lowerBound, int(temp))
        for i in range(len(s)):
            temp = s.replace(s[i], '9')
            upperBound = max(upperBound, int(temp))
        return upperBound - lowerBound
