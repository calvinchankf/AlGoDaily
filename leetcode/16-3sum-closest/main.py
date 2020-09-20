import sys

"""
    1st approach: binary search
	- for each pair, we look for the remain
	e.g. [1,2,3,4,5] 10
	for pair 1,2, search 7 within [3,4,5]
	for pair 1,3, search 6 within [4,5]

	Time		O(n^2logn)
	Space		O(1)
	1552 ms, faster than 5.01%
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = sys.maxsize
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                remain = target - nums[i] - nums[j]
                # search from j+1
                idx = self.bSearchNearest(nums, j+1, remain)
                # update res if necessary
                if idx >= j+1 and idx < len(nums):
                    total = nums[i] + nums[j] + nums[idx]
                    if abs(total-target) < abs(res-target):
                        res = total
        return res

    def bSearchNearest(self, nums, start, target):
        left = start
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # checking
        if right < start:
            return start
        if left > len(nums)-1:
            return len(nums)-1
        # compare
        if abs(target-nums[right]) < abs(target-nums[left]):
            return right
        return left


a = [0, 1, 2]
b = 3
print(Solution().threeSumClosest(a, b))

a = [-1, 2, 1, -4]
b = 1
print(Solution().threeSumClosest(a, b))

a = [-1, 2, 1, -4, 3]
b = 1
print(Solution().threeSumClosest(a, b))

print("---")

"""
    2nd approach: 2 pointers
	- e.g. [2,3,6,10], 10
	pair=0,3, sum = 12, diff=+2, right--
	pair=0,2, sum = 8, diff=-2, left++
	pair=1,2, sum = 9, diff=-1, cannot move any pointers
    ...
    
    reminder:
    - since closest means the result can be either smaller or bigger than the target,
        the 2 pointers loop ends only either: 
        - left==right
        - OR total == target

	Time		O(n^2)
	Space		O(1)
	132 ms, faster than 71.46%
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sys.maxsize
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if abs(cur - target) < abs(res - target):
                    res = cur
                if cur == target:
                    return cur
                elif cur < target:
                    left += 1
                else:
                    right -= 1
        return res
