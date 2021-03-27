"""
    1st: dyanmic programming

    Time    O(N^2)
    Space   O(N^2)
    TLE 58 / 62 test cases passed

    Actually this is correct, it works in JS
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        return self.dfs(nums, multipliers, 0, n-1, 0, {})

    def dfs(self, nums, multipliers, i, j, k, cache):
        if k == len(multipliers):
            return 0
        if i == j:
            return nums[i] * multipliers[k]
        key = (i, j)
        if key in cache:
            return cache[key]
        left = self.dfs(nums, multipliers, i+1, j, k+1,
                        cache) + nums[i] * multipliers[k]
        right = self.dfs(nums, multipliers, i, j-1, k+1,
                         cache) + nums[j] * multipliers[k]
        cache[key] = max(left, right)
        return cache[key]
