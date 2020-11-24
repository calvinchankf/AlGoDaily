"""
    https://leetcode.com/discuss/interview-question/894401/Facebook-or-Phone-or-Find-a-local-minima-in-an-array

    Find the a local minima in a array.
    The input array may contain multiple dips, in that case return the index to any one of the dips is fine.

    - similar to lc162, 852
    - when the next item is larger than the current item,
        the dip is on the left hand side (including the current item)
"""


class Solution:
    def findDipElement(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()

a = []
print(s.findDipElement(a))  # none

a = [1]
print(s.findDipElement(a))  # 0

a = [1, 2, 3, 1]
print(s.findDipElement(a))  # 0 or 3

a = [2, 4, 1, 3, 5, 6, -1, 4]
print(s.findDipElement(a))  # 2 or 6

a = [0, 1, 0]
print(s.findDipElement(a))  # 0 or 2

print("-----")

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
