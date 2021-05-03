"""
    1st: math

    Time    O(1)
    Space   O(1)
    32 ms, faster than 77.24%
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        m = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        x, y = coordinates
        x, y = m[x], int(y)
        return (x + y) % 2 == 1
