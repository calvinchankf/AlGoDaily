"""
    1st approach:
	- naive brute force

	Time		O(n^2)
	Space		O(1)
	368ms beats 34.48%
	18apr2019
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(height)):
            for j in range(i):
                h = min(height[i], height[j])
                w = i-j
                res = max(res, h*w)
        return res


a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(a))

print("--------------------")

"""
    2nd approach
	- 2 pointers: one from the front, one from the end
	- move inward by retaining the heightest amongst the arr[i] and arr[j]
	- https://leetcode.com/articles/container-with-most-water/
    
	Time		O(n)
	Space		O(1)
    120 ms, faster than 25.71%
    18apr2019
"""


class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            h = min(nums[left], nums[right])
            w = right - left
            res = max(res, h*w)
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return res


a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(a))

print("--------------------")
