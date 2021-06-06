"""
    1st: array

    Time    O(N)
    Space   (1)
    28 ms, faster than 100.00%
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longestOnes = 0
        longestZeros = 0
        ones = 0
        zeros = 0
        for i in range(len(s)):

            longestZeros = max(longestZeros, zeros)
            longestOnes = max(longestOnes, ones)

            c = s[i]
            if c == '0':
                zeros += 1
                ones = 0
            else:
                ones += 1
                zeros = 0

        longestZeros = max(longestZeros, zeros)
        longestOnes = max(longestOnes, ones)
        return longestOnes > longestZeros
