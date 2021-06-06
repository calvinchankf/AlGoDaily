"""
    1st: sort + binary search + max heap
    - this is slow becos we put a poped element back in the maxheap and compute again

    Time    O(N + DlogD + NNlogD)
    Space   O(N)
    LTE
"""
from heapq import *


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        clone = nums[:]
        clone = list(set(clone))
        clone.sort()
        maxheap = []
        for i in range(len(nums)):
            x = nums[i]
            heappush(maxheap, (-x, i))
        res = 0
        while len(maxheap) > 0:
            _x, i = heappop(maxheap)
            x = -_x
            j = self.bsearch(clone, x) - 1
            if j < 0:
                continue
            res += 1
            nextLargest = clone[j]
            heappush(maxheap, (-nextLargest, i))
        return res

    def bsearch(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1


"""
    2nd: sort + binary search + math

    Time    O(N + DlogD + NlogD) N: len(nums), D: len(distinct)
    Space   O(N)
    4140 ms, faster than 33.33%
"""


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        clone = nums[:]
        clone = list(set(clone))
        clone.sort()
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            j = self.bsearch(clone, x)
            res += j
        return res

    def bsearch(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1
