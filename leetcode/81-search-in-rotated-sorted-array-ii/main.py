"""
    classic approach: binary search with conditions
	- when we look for a the number lerger than the mid, we do bearch when either
		1. the pivot point is in the right hand side(which means maximum is in the right)
		2. normally when no pivot but target is <= nums[right]
	- similar logic for the left-handed side
	- However for duplicates numbers on both ends,
	we should not consider the left most number(or right most) until there are no duplicate numbers on both ends

	Time	O(logn) if no duplicates, O(n) if duplicates present on both ends
	Space	O(1)
	40 ms, faster than 46.93%
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :rtype: bool
        :type target: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:

            # this is the trickiest part, if both ends have the same number
            # e.g. [5,1,1,1,1,2,3,4]
            # dont consider the next number when it is the same as the current one
            while left + 1 < right and nums[left] == nums[left+1]:
                left += 1

            mid = (left + right)/2
            if target < nums[mid]:
                if target >= nums[left] or nums[left] > nums[mid]:
                    # search left when the pivot is here OR normally nums[left] < nums[mid] and target >= nums[left]
                    right = mid - 1
                else:
                    # otherwise search in another half
                    left = mid + 1
            elif target > nums[mid]:
                if target <= nums[right] or nums[mid] > nums[right]:
                    # search right when the pivot is here OR normally nums[mid] < nums[right] and target <= nums[right]
                    left = mid + 1
                else:
                    # otherwise search in another half
                    right = mid - 1
            else:
                return True
        return False


a = [4, 5, 6, 7, 0, 1, 2]
b = 0
print(Solution().search(a, b))

a = [4, 5, 6, 7, 0, 1, 2]
b = 3
print(Solution().search(a, b))

a = [4, 5, 6, 7, 0, 0, 1, 2]
b = 0
print(Solution().search(a, b))

a = [4, 5, 6, 7, 7, 0, 1, 1, 2]
b = 3
print(Solution().search(a, b))
