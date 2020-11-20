"""
    1st approach: 2pointers
    - similar to lc42, 135, 487, 689, 915, 1493
    - calculate max from the front
    - calculate max from the end
    - the min(forward[i], backward[i]) - height[i] is the volumn of the trapping water on that cell

    Time    O(3n)
    Space   O(3n)
    48 ms, faster than 35.09%
"""


class Solution(object):
    def trap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftMax = 0
        forward = []
        for i in range(len(nums)):
            leftMax = max(leftMax, nums[i])
            forward.append(leftMax)
        backward = []
        rightMax = 0
        for i in range(len(nums)-1, -1, -1):
            rightMax = max(rightMax, nums[i])
            backward.append(rightMax)
        backward = backward[::-1]
        res = 0
        for i in range(len(nums)):
            res += min(forward[i], backward[i]) - nums[i]
        return res


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

print("--------------------")


"""
    2nd approach: optimize the 1st approach
    - calculate max from the front
    - calculate max from the end
    - the min(forward[i], backward[i]) - height[i] is the volumn of the trapping water on that cell

    ref:
    - https://www.youtube.com/watch?v=2LjNzbK2cmA

    Time    O(n)
    Space   O(1)
    40 ms, faster than 43.69%
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                right -= 1
        return res


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
