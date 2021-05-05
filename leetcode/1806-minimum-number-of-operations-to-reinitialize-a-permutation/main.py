"""
    1st: brute force mutation

    Time    O(N^2)
    Space   O(2N)
    588 ms, faster than 57.19%
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        res = 0
        _perm = perm[:]
        while True:
            cur = n * [0]
            for i in range(n):
                if i % 2 == 0:
                    cur[i] = _perm[i//2]
                else:
                    cur[i] = _perm[n//2 + (i - 1)//2]
            res += 1
            if tuple(cur) == tuple(perm):
                return res
            _perm = cur
