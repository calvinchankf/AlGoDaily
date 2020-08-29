"""
    1st approach: sort
    - sort it, and then split them and put the numbers back to the array

    e.g. even
    [3,5,2,1,6,4] => [1,2,3,4,5,6]
    split => [1,2,3], [4,5,6]
    result will be [1,4,2,5,3,6]

    e.g. odd
    [3,5,2,1,6] => [1,2,3,5,6]
    split => [1,2,4], [5,6]
    result will be [1,5,2,6,4]

    e.g. duplicate
    [3,5,2,1,3] => [1,2,3,3,5]
    split => [1,2,3], [3,5]
    result will be [1,3,2,5,3]

    Time    O(nlogn)
    Space   O(n)
    92 ms, faster than 26.94%
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        clone = sorted(nums)
        halfIdx = (len(nums)+1)/2
        a = clone[:halfIdx]
        b = clone[halfIdx:]
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = a.pop(0)
            else:
                nums[i] = b.pop(0)

    def checkIfWiggle(self, nums):
        """
        followup: check if an array is wiggle-sorted
        """
        for i in range(1, len(nums)):
            if i % 2 == 0:
                if nums[i-1] < nums[i]:
                    return False
            else:
                if nums[i-1] > nums[i]:
                    return False
        return True


a = [3, 5, 2, 1, 6, 4]
Solution().wiggleSort(a)
print(Solution().checkIfWiggle(a))

"""
    2nd approach: swapping
    - this is quite similar to wiggle sort checking

    Time    O(n)
    Space   O(1)
    80 ms, faster than 48.94%
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i % 2 == 0:
                if nums[i-1] < nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
