"""
    1st: recursion
    - this is a subset problem, leetcode78

    Time    O(2^N)
    Space   O(2^N)
    64 ms, faster than 74.58% 
"""


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        self.dfs(nums, 0)
        return self.total

    def dfs(self, nums, xor):
        self.total += xor
        for i in range(len(nums)):
            self.dfs(nums[i+1:], xor ^ nums[i])
