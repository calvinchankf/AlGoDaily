"""
    1st: bianry search + 2 pointers
    - learned from others
    - lower-bound binary search to find the smallest
    - the way to calculate the count the subarray sum less than a target is a good technique

    ref:
    - https://leetcode.com/problems/kth-smallest-subarray-sum/discuss/1309749/Binary-Search-%2B-Sliding-Window

    Time    O(log(N^2))
    Space   O(1)
    1584 ms, faster than 97.01%
"""


class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            count = self.countLessThanOrEqual(nums, mid)
            if k <= count:
                right = mid
            else:
                left = mid + 1
        return left

    def countLessThanOrEqual(self, nums, target):
        j = 0
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            while total > target:
                total -= nums[j]
                j += 1
            count += i - j + 1
        return count
