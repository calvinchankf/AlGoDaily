"""
    1st approach: dynamic programming
    
    Time    O(n)
    Space   O(n)
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
    
    Time    O(n)
    Space   O(1)
    16 ms, faster than 89.83%
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
