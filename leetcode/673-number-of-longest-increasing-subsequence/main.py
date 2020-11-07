"""
    1st approach: dynamic programming

    very similar to lc300

    the basic idea is, instead of storing a list of counts [1,1,1,1,1]
    we store a list of [count, possibilites]
    [
        [1:1],
        [1:1],
        [1:1],
        [1:1],
        [1:1],
    ]

    e.g.
    1,   3,   5,   4,   7,   7,   7,   8
    [1,1]<1,1><1,1><1,1><1,1><1,1><1,1><1,1>
         [2,1]<2,1><2,1><2,1><2,1><2,1><2,1>
              [3,1][3,1]<3,1><3,1><3,1><3,1>
                        <4,1><4,1><4,1><4,1>
                        [4,2][4,2][4,2]<4,2>
                                       <5,2>
                                       <5,4>
                                       [5,6]
    Time    O(n^2)
    Space   O(n)
    804 ms, faster than 25.62%
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = n * [1]
        counts = n * [1]
        maxLen = 1
        for i in range(n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                curLen = dp[j] + 1
                if curLen > dp[i]:
                    dp[i] = curLen
                    counts[i] = counts[j]
                elif curLen == dp[i]:
                    counts[i] += counts[j]
            maxLen = max(maxLen, dp[i])
        res = 0
        for i in range(n):
            if dp[i] == maxLen:
                res += counts[i]
        return res
