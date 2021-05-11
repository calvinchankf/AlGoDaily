"""
    1st: binary search
    - count local inversion by simple iteration
    - count global inversion by upper-bound binary search

    Time    O(NlogN) -> O(N^2) binary search takes O(logN) but array.inser() takes O(N)
    Space   O(N)
    792 ms, faster than 5.18%
"""


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        localCount = 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                localCount += 1

        globalCount = 0
        nums = []
        for i in range(len(A)):
            j = self.upperBsearch(nums, A[i])
            globalCount += len(nums) - j
            nums.insert(j, A[i])

        return localCount == globalCount

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
