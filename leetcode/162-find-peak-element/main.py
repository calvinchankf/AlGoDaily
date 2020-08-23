"""
    1st: linear search

    Time    O(N)
    Space   O(1)
    76 ms, faster than 7.05%
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-sys.maxsize] + nums + [-sys.maxsize]
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i-1
        return -1
