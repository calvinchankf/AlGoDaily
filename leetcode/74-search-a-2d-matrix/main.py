"""
    2nd approach:
	- upper bound binary search to look for the target range
	- binary search to look for the item within that range
    
	Time 	O(logR + logC)
	Space   O(1)
	48 ms, faster than 49.53%
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        idx = self.upperBsearch(matrix, target) - 1
        if idx < 0:
            return False
        b = self.bsearch(matrix[idx], target)
        return b > -1
    
    def upperBsearch(self, matrix, target):
        left = 0
        right = len(matrix)
        while left < right:
            mid = (left+right)//2
            if target >= matrix[mid][0]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1