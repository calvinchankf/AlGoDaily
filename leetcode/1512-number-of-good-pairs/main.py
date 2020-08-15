from collections import defaultdict

"""
    1st: hashtable + math

    Time    O(N)
    Space   O(N)
    40 ms, faster than 66.67%
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        ht = defaultdict(int)
        for x in nums:
            if x in ht:
                res += ht[x]
            ht[x] += 1
        return res
