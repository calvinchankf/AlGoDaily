"""
    2nd approach:
	- move the zeros to the front
	- move the twos to the back
	- see leetcode 283) moving zeros
    
    Time    O(N)
    Space   O(N)
    12 ms, faster than 99.25%
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nonZeroIdx = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[nonZeroIdx] = nums[nonZeroIdx], nums[i]
                nonZeroIdx += 1
        nonTwoIdx = n - 1
        for i in range(n-1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[nonTwoIdx] = nums[nonTwoIdx], nums[i]
                nonTwoIdx -= 1
