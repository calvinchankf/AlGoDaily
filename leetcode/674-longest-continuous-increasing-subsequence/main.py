"""
    1st: sliding window

    Time    O(n)
    Space   O(1)
    68 ms, faster than 95.02% 
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        res = 0
        cur = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)
        return res


"""
    2nd approach: same logic + followup: print the result array

    Time    O(n)
    Space   O(n)
    60 ms, faster than 57.69%
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = []
        cur = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > cur[-1]:
                cur.append(nums[i])
            else:
                cur = [nums[i]]
            if len(cur) > len(res):
                res = cur
        return res


"""
    3rd: dynamic programming
    - Longest increasing subsequence

    Time    O(N)
    Space   O(N)
    72ms beats 80.69%
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = n * [1]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] += dp[i-1]
        return max(dp)
