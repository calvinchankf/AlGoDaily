"""
    1st: same logic as Quick Sort
    similar to lc283

    Time    O(N)
    Space   O(1)
"""


class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j
