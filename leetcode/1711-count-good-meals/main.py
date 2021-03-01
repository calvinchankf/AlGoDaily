
from collections import *

"""
    1st: hashtable
    - 2 sum
    - there are only 21 powerOfTwos, find the each of the remain in the hashtable, thats it

    Time    O(NlogK) N=len(deliciousness), K=deliciousness[i]
    Space   O(N + logK)
    1456 ms, faster than 100.00%
"""


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cands = [2**i for i in range(22)]
        counter = Counter()
        res = 0
        for i in range(len(deliciousness)):
            x = deliciousness[i]
            for c in cands:
                remain = c - x
                if remain in counter:
                    res += counter[remain]
                    res %= 10**9 + 7
            counter[x] += 1
        return res
