"""
    1st:recursive dfs + memorization
    - dfs to traverse the path from bottom
    - if we see a (idx, total) that we previously visited, 
    we can just use the previous result because the way come up with the remain would be the same
    
    Time    O(NNS)
    Space   O(n)
    456 ms, faster than 31.96%
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        return self.dfs(nums, S, {})

    def dfs(self, nums, S, ht):
        if len(nums) == 0:
            if S == 0:
                return 1
            return 0
        key = (len(nums), S)
        if key in ht:
            return ht[key]
        a = self.dfs(nums[1:], S - nums[0], ht)
        b = self.dfs(nums[1:], S + nums[0], ht)
        ht[key] = a + b
        return a + b


"""
    optimize 1st by iterating the nums instead slicing
    

    Time    O(NS)
    Space   O(n)
    380 ms, faster than 48.17%
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
