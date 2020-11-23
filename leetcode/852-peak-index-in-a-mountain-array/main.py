"""
    1st: linear search the largest element

    Time    O(N)
    Space   O(N)
    96 ms, faster than 21.10%
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))


"""
    2nd: upper boundy binary search
    - similar to lc162, 852

    Time    O(logN)
    Space   O(1)
    68 ms, faster than 93.13%
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right)//2
            if A[mid-1] < A[mid]:
                left = mid + 1
            else:
                right = mid
        if right-1 < 0:
            return 0
        return right - 1


"""
    3rd: lower bound binary search
    - similar to lc162, 852
    - when the next item is smaller, the peak is on the left hand side
    - actually same as 2nd, but the left & right are always within boundary

    Time    O(logN)
    Space   O(1)
    40 ms, faster than 87.66%
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return None
        # elif len(nums) == 1:
        #     return 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
