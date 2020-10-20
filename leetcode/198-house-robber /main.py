"""
    0th: suboptimal dynamic programming
    - similar to lc300, 746

    Time    O(N^2)
    Space   O(N)
    36 ms, faster than 45.56%
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = n * [0]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            maxFromLeft = 0
            for j in range(i-1):
                maxFromLeft = max(maxFromLeft, dp[j])
            dp[i] = maxFromLeft + nums[i]
        return max(dp[-1], dp[-2])


"""
    1st approach: dynamic programming
    
    Time    O(N)
    Space   O(N)
    16 ms, faster than 89.83%
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        included = [0] * len(nums)
        excluded = [0] * len(nums)
        for i in range(len(nums)):
            included[i] = max(
                excluded[i-1] + nums[i],
                included[i-1]
            )
            excluded[i] = included[i-1]
        return included[-1]
        # return max(included[-1], excluded[-1])


"""
    2nd approach: dynamic programming
    
    Time    O(N)
    Space   O(N)
    12 ms, faster than 98.42% 
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        notRob = 0
        for x in nums:
            temp = rob
            rob = max(rob, notRob + x)
            notRob = temp
        return max(rob, notRob)


"""
    followup: what if there are negative numbers? lets say the thieves might lose money by visiting a house
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        included = nums[0]
        excluded = 0
        for i in range(1, len(nums)):
            temp = included
            # the crux is: the filth must be >= 0
            included = max(excluded + max(nums[i], 0), included)
            excluded = temp
        return included
