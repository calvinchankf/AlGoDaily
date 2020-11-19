"""
    2nd approach: 2 pointers

    Time	O(n)
    Space	O(1)
    52 ms, faster than 44.85%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left+1, right+1]
        return []
