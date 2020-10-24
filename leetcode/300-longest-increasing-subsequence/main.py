"""
    1st approach: dynamic programming
    - similar to lc198

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(n^2)
    Space   O(n)
    1068 ms, faster than 12.81%
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = n * [1]
        for i in range(1, n):
            maxCount = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxCount = max(maxCount, dp[j])
            dp[i] += maxCount
        return max(dp)


s = Solution()

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(s.lengthOfLIS(a))

"""
    follow up: print the subsequence
"""


class Solution(object):
    def printLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([nums[i]])
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # dp[i] = max(dp[j] + 1, dp[i])
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        res = []
        for x in dp:
            if len(x) > len(res):
                res = x
        return res


s = Solution()

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(s.printLIS(a))
