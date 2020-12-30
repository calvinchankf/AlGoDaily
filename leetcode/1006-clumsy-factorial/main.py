"""
    1st: brute force math
    - process the numbers 4 by 4
    e.g. 
    10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
    --------------   -------------   -----
    18              -4             -2      = 12


    Time    O(N)
    Space   O(1)
    60 ms, faster than 54.94%
"""


class Solution:
    def clumsy(self, N: int) -> int:
        res = None
        while N > 0:
            a = N
            b = max(N - 1, 1)
            c = max(N - 2, 1)
            d = max(N - 3, 0)
            if res == None:
                res = a * b // c + d
            else:
                res -= a * b // c - d
            N -= 4
        return res
