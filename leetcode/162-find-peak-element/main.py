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

"""
    2nd: upper bound binary search
    - compare with the previous item, if prev < cur, then search on the right handside

    e.g.1 [1,2,1,3,5,6,4]
                 ^          mid
                     ^      mid
                        ^   mid
    
    e.g.2 [1,6,5,4,3,2,1]
                 ^          mid
             ^              mid
               ^            mid

    Time    O(logN)
    Space   O(1)
    96 ms, faster than 15.38%
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        if left <= 0:
            return 0
        return left - 1