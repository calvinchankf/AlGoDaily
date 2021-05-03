"""
    1st: array

    Time    O(N)
    Space   O(N)
    24 ms, faster than 96.67%
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        firstK = words[:k]
        return ' '.join(firstK)
