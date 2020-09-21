"""
    recursive dfs + memorization
    - dfs to traverse the path from bottom
    - if we see a (idx, total) that we previously visited, we can just use the previous result because the way come up with the remain would be the same

    Time    O(n^2)
    Space   O(n)
    440 ms, faster than 23.93%
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        return self.dfs(nums, 0, 0, S, {})

    def dfs(self, nums, idx, total, S, ht):
        if idx == len(nums):
            if total == S:
                return 1
            else:
                return 0
        key = (idx, total)
        if key in ht:
            return ht[key]
        left = self.dfs(nums, idx+1, total - nums[idx], S, ht)
        right = self.dfs(nums, idx+1, total + nums[idx], S, ht)
        ht[key] = left + right
        return ht[key]
