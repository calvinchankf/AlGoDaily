"""
    1st: array
    - similar to leetcode161
    - if it is not increasing, either remove the previous item or the current one and check again

    Time    O(N)
    Space   O(N)
    48 ms, faster than 80.00%
"""


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                a = nums[:i-1] + nums[i:]
                b = nums[:i] + nums[i+1:]
                return self.isStrictlyIncreasing(a) or self.isStrictlyIncreasing(b)
        return True

    def isStrictlyIncreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True
