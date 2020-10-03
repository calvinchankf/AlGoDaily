"""
    1st approach: array

    Time    O(n) number of nums
    Space   O(1)
    16 ms, faster than 86.02%
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower > upper:
            return []
        nums = [lower-1] + nums + [upper+1]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                res.append(str(nums[i-1]+1))
            elif nums[i] - nums[i-1] > 2:
                res.append(str(nums[i-1]+1) + '->' + str(nums[i]-1))
        return res
