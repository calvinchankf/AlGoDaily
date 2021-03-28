from collections import *

"""
    1st: 2 pointers
    - similar to lc3

    Time    O(N)
    Space   O(1)
    752 ms, faster than 100.00%
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        j = 0
        counter = Counter()
        for i in range(len(s)):
            c = s[i]
            counter[c] += 1
            while len(counter) > 1:
                left = s[j]
                j += 1
                counter[left] -= 1
                if counter[left] == 0:
                    del counter[left]
            res += i - j + 1
            res %= (10**9 + 7)
        return res
