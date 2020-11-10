"""
    https://leetcode.com/discuss/interview-question/894401/Facebook-or-Phone-or-Find-a-local-minima-in-an-array

    Find the a local minima in a array.
    The input array may contain multiple dips, in that case return the index to any one of the dips is fine.

    - similar to lc162, 852
"""


class Solution:
    def findDipElement(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid-1] > nums[mid]:
                left = mid + 1
            else:
                right = mid
        if right-1 < 0:
            return 0
        return right - 1


s = Solution()

a = [1, 2, 3, 1]
print(s.findDipElement(a))  # 0 or 3

a = [2, 4, 1, 3, 5, 6, -1, 4]
print(s.findDipElement(a))  # 2 or 6

a = [0, 1, 0]
print(s.findDipElement(a))  # 0 or 2

a = [0, 2, 1, 0]
print(s.findDipElement(a))  # 0 or 3

a = [0, 10, 5, 2]
print(s.findDipElement(a))  # 0 or 3

a = [3, 4, 5, 1]
print(s.findDipElement(a))  # 0 or 3

a = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19, 20]  # 9
print(s.findDipElement(a))

a = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]  # 9
print(s.findDipElement(a))
