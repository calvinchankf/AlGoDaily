"""
    1st: string

    Time    O(N)
    Space   O(1)
    52 ms, faster than 25.00%
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        A = s[:mid]
        B = s[mid:]
        vowelCount = 0
        for c in A:
            if c in 'aeiouAEIOU':
                vowelCount += 1
        for c in B:
            if c in 'aeiouAEIOU':
                vowelCount -= 1
        return vowelCount == 0
