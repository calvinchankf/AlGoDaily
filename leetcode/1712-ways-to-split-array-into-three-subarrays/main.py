
import bisect

"""
    1st: prefix sum + binary search
    - calculate prefix sum
    - binary search the left and right for second boundary

    e.g.
    [1, 1, 2, 1, 1, 2, 5, 0]
     1  2  4  5  6  8  13
        ^
           L     R
    when we are at idx1(^), find the L and R using binary search

    Time    O(NlogN)
    Space   O(N)
    2156 ms, faster than 27.56%
"""


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        # prefix sum
        total = 0
        pfs = 0
        pfss = []
        for x in nums:
            total += x
            pfs += x
            pfss.append(pfs)
        # binary search the left and right for second boundary
        res = 0
        for i in range(n-2):
            remain = total - pfss[i]
            if remain < 2 * pfss[i]:  # catch1: the right must be >= middle
                break
            left = self.lowerBsearch(pfss, 2 * pfss[i], i+1)
            right = self.upperBsearch(pfss, pfss[i] + remain//2, i+1) - 1
            res += max(right - left + 1, 0)
            res %= 10**9 + 7
        return res

    def lowerBsearch(self, nums, target, i):
        left = i
        # catch2: we at least need one element on the right
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBsearch(self, nums, target, i):
        left = i
        # catch2: we at least need one element on the right
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
