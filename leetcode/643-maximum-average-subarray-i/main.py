"""
    1st approach: sliding window

	Time	O(N)
	Space	O(1)
    880 ms, faster than 18.74%
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxSum = -2**32
        curSum = 0
        for i in range(n):
            curSum += nums[i]
            if i >= k:
                curSum -= nums[i-k]
            if i >= k - 1:
                maxSum = max(maxSum, curSum)
        return maxSum/k
