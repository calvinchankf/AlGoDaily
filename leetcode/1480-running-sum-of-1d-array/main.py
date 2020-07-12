"""
    1st: prefix sum
    
    Time    O(N)
    Space   O(N)
    76 ms, faster than 33.33%
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        pfs = 0
        for x in nums:
            pfs += x
            res.append(pfs)
        return res
