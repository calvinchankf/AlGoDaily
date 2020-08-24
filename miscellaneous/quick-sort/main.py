"""
    in-place version
    ref:
    - https://gist.github.com/imwally/58d6bb9bf9da098064054f73a19cdca1
    - https://www.youtube.com/watch?v=COk73cpQbFQ

    Worst Time		O(n^2): findHalf might need to iterate the rest of the array for each item
    Average	Time	O(nlogn)
    Space 				O(h)
"""


class Solution(object):
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums)-1)
        return nums

    # quick sort
    def quicksort(self, nums, start, end):
        if start < end:
            pIdx = self.partition(nums, start, end)
            self.quicksort(nums, start, pIdx-1)
            self.quicksort(nums, pIdx+1, end)

    def partition(self, nums, start, end):
        pivot = nums[end]
        pIdx = start
        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        # after the for loop, all numbers on the left-hand side of pIdx <= pivot
        # so now we can put the pivit at pIdx
        nums[end], nums[pIdx] = nums[pIdx], nums[end]
        return pIdx
