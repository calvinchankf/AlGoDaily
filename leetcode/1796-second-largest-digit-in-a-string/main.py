"""
    1st: array

    Time    O(N)
    Space   O(1)
    40 ms, faster than 100.00%
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        largest2 = -1
        for c in s:
            if c in '0123456789':
                d = int(c)

                if d == largest or d == largest2:
                    continue

                if d > largest:
                    largest2 = largest
                    largest = d
                elif d > largest2:
                    largest2 = d
        return largest2
