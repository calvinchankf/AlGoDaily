"""
    1st: greedy, string
    - iterate from the back, if a character is odd, return the prefix

    Time    O(N)
    Space   O(1)
    52 ms, faster than 40.00%
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            c = int(num[i])
            if c % 2 == 1:
                return num[:i+1]
        return ""
