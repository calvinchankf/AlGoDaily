"""
    classic approach: Next lexicographical permutation algorithm

    - similar to lc3, 556, 1053

	e.g. 43143221
	- find the non-increasing suffix, e.g. 431<43221>
	- once it encounters a smaller number from the end, this is the target we want
		e.g. 43 <1> 43221
	- i need to swap the target with the value in the stack which is just larger then it
		e.g. 43 <1> 43221
                       ^
         => 43 <2> 43211
                      ^
	- reverse the right half and put it back to the number
		e.g. 43 <2> 43211 => 43 <2> 11234
	- combine them together and form the result
		e.g. 43 <2> 11234 => 43211234

	ref:
	- https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

	Time	O(n)
	Space	O(n)
	28 ms, faster than 69.06%
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # find the monotonic increasing suffix
        i = n - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            self.reverse(nums, 0, n-1)
            return
        # pivot is the num next to the suffix
        pivot = i - 1

        # find the successor
        j = n - 1
        while j - 1 >= 0 and nums[j] <= nums[pivot]:
            j -= 1

        # swap the numbers at pivot and the successor
        nums[pivot], nums[j] = nums[j], nums[pivot]

        # reverse the suffix
        self.reverse(nums, i, n-1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
