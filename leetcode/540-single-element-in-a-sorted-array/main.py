"""
    1st: brute force
    Time    O(N)
    Space   O(1)
    60ms beats 49.91%
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i+1 < len(nums):
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return nums[i]