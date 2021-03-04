from collections import *

"""
    1st: hashtable count

    Time    O(N)
    Space   O(N)
    36 ms, faster than 100.00%
"""


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for key in counter:
            if counter[key] == 1:
                res += key
        return res
