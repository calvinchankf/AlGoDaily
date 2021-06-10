"""
    1st: sliding window

    Time    O(N)
    Space   O(4)
    32 ms, faster than 60.00%
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ht = {}
        res = 0
        for i in range(len(s)):
            c = s[i]
            if c not in ht:
                ht[c] = 0
            ht[c] += 1
            if i >= 3:
                left = s[i-3]
                ht[left] -= 1
                if ht[left] == 0:
                    del ht[left]
            if len(ht) == 3:
                res += 1
        return res
