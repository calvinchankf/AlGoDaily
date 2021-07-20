"""
    1st: hashtable

    Time    O(N^2)
    Space   O(N)
    208 ms, faster than 100.00%
"""


class Solution:
    def countTriples(self, n: int) -> int:
        hs = set()
        for i in range(1, n+1):
            hs.add(i*i)
        res = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i*i + j*j in hs:
                    res += 1
        return res
