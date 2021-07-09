"""
    1st: array
    - just do what has been told
    
    Time    O(N)
    Space   O(N)
    124 ms, faster than 33.33%
"""


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = n * [0]
        for i in range(n):
            res[i] = nums[nums[i]]
        return res
