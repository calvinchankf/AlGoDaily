"""
    1st: sort

    Time    O(NlogN)
    Space   O(1)
    168 ms, faster than 14.29%
"""


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
