"""
    1st: sort

    Time    O(NlogN)
    Space   O(1)
    1200 ms, faster than 25.00%
"""


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            res = max(res, nums[left] + nums[right])
            left += 1
            right -= 1
        return res
