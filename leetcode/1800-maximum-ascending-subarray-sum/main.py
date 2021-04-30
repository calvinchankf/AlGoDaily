"""
    1st: array

    Time    O(N)
    Space   O(1)
    36 ms, faster than 100.00%
"""
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        n = len(nums)
        for i in range(n):
            if i == 0 or (i > 0 and nums[i] > nums[i-1]):
                cur += nums[i]
            else:
                cur = nums[i]
            res = max(res, cur)
        return res