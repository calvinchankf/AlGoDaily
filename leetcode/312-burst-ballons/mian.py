import sys

"""
    0th: brute force recursion

    Time    O(N!)
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dfs(nums)

    def dfs(self, nums):
        if len(nums) == 1:
            return nums[0]
        res = 0
        for i in range(len(nums)):
            left = 1
            if i > 0:
                left = nums[i-1]
            right = 1
            if i+1 < len(nums):
                right = nums[i+1]
            temp = self.dfs(nums[:i]+nums[i+1:]) + left * nums[i] * right
            res = max(res, temp)
        return res


s = Solution()

a = [3, 1, 5, 8]
print(s.maxCoins(a))
"""
    1st: recursion + hashtable

    Time    x < O(N!)
    LTE
    34 / 70 test cases passed
"""

print("-----")


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dfs(nums, {})

    def dfs(self, nums, ht):
        if len(nums) == 1:
            return nums[0]
        # key = tuple(nums)
        # if key in ht:
        #     return ht[key]
        res = 0
        for i in range(len(nums)):
            left = 1
            if i > 0:
                left = nums[i-1]
            right = 1
            if i+1 < len(nums):
                right = nums[i+1]
            temp = self.dfs(nums[:i], ht) \
                + left * nums[i] * right \
                + self.dfs(nums[i+1:], ht)
            res = max(res, temp)
        # ht[key] = res
        return res


s = Solution()

a = [3, 1, 5, 8]
print(s.maxCoins(a))

a = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2]
# print(s.maxCoins(a))

a = [8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]
# print(s.maxCoins(a))

print("-----")

"""
    3rd: recursion + hashtable
    - the problem of 2nd is the keys are too diversed, not efficient
    
    So how about working backwards?
    - dont burst, but add
    
    e.g. [3, 1, 5, 8]
    start = [1,1]
    add 8 = [1,8,1]
    add 3 = [1,3,8,1]
    add 5 = [1,3,5,8,1]
    add 1 = [1,3,1,5,8,1]

    reference of the details:
    - https://leetcode.com/articles/burst-balloons/

    Time    O(N^3)
    Space   O(N^2)
    936 ms, faster than 5.07%
"""


class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        self.ht = {}
        return self.dp(nums, 0, len(nums)-1)

    def dp(self, nums, left, right):
        # no more balloons can be added
        if left + 1 == right:
            return 0
        key = (left, right)
        if key in self.ht:
            return self.ht[key]
        # add each balloon on the interval and return the maximum score
        res = 0
        for i in range(left+1, right):
            temp = nums[left] * nums[i] * nums[right] \
                + self.dp(nums, left, i) + self.dp(nums, i, right)
            res = max(res, temp)
        self.ht[key] = res
        return res


s = Solution()

a = [3, 1, 5, 8]
print(s.maxCoins(a))

a = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2]
print(s.maxCoins(a))

a = [8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]
print(s.maxCoins(a))
