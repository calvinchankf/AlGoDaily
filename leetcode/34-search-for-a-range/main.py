from typing import List

"""
    1st approach: binary search

    Time    O(2logn)
    Space   O(1)
    204 ms, faster than 5.22%
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.lowerBsearch(nums, target)
        right = self.upperBsearch(nums, target)

        if left >= right:
            return [-1, -1]

        return [left, right-1]

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
