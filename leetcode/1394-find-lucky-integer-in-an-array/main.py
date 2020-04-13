from collections import Counter

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    52 ms, faster than 100.00%
"""


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ht = Counter(arr)
        res = -1
        for key in ht:
            if key == ht[key]:
                res = max(res, key)
        return res
