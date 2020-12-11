"""
    1st: string
    - keep adding extending the 'word' until no match in sequence

    Time    O(N^2)
    Space   O(1)
    52 ms, faster than 33.33%
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        cur = word
        while cur in sequence:
            k += 1
            cur += word
        return k
