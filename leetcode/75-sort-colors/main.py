"""
    1st approach:
	- move the zeros to the front
	- move the twos to the back
	- similar to lc26, 283 moving zeros
    
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
        j = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        j = n - 1
        for i in range(n-1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1


"""
    2nd approach: 3 pointers
    
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
        left = 0
        mid = 0
        right = n - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:
                mid += 1
