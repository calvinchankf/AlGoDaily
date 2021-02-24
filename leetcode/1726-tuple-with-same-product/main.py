
from collections import *

"""
    1st: hashtable
    - count the number of pairs those have the same product
    - for every pair, there are 8 possibilities
    (a, b) => [(a, b), (b, a)] = 2
    (c, d) => [(c, d), (d, c)] = 2
    so (a, b) and (c, d) => [(a,b) and (c,d), (c,d) and (a,b)] = 2 * 2 * 2 = 8

    Time    O(N^2)
    Space   O(N^2)
    1044 ms, faster than 47.93%
"""


class Solution(object):
    def tupleSameProduct(self, nums):
        n = len(nums)
        ht = Counter()
        for i in range(n):
            for j in range(i+1, n):
                temp = nums[i] * nums[j]
                ht[temp] += 1
        res = 0
        for key in ht:
            c = ht[key]
            if c > 1:
                res += 8 * self.pairsCount(c)
        return res

    def pairsCount(self, n):
        return n * (n-1) // 2
