"""
    1st approach: reuse leetcode 198
	- circular means that we cannot rob houses[0] and houses[n-1] at the same time, so the result is either:
        - from houses[1] to houses[n-2]
        - Or from houses[2] to houses[n-1]

	Time		O(2n)
	Space		O(1)
	8 ms, faster than 99.45%
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        a = self.simpleRob(nums[:-1])
        b = self.simpleRob(nums[1:])
        return max(a, b)

    def simpleRob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        included = nums[0]
        excluded = 0
        for i in range(1, len(nums)):
            temp = included
            included = max(excluded+nums[i], included)
            excluded = temp
        # return included
        return max(included, excluded)
