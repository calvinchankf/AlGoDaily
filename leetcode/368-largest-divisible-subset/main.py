from typing import List

"""
    1st: dynamic programming, learned from others
    - in fact, if a%b = 0 and b%c = 0, then a%c = 0
    
    Consider [1,2,4,7,8]
    dp[1] = [1]
    dp[2] = [2]
    dp[4] = [4]
    dp[7] = [7]
    dp[8] = [8]

    at dp[2]: 
    since 2%1 == 0, dp[2] = dp[1] + [2] = [1,2] which the length is > dp[1], therefore...
    dp[2] = [1,2]

    at dp[4]:
    4%1 == 0, it means dp[4] can be [1,4]
    4%2 == 0, it means dp[4] can be [1,2,4]
    since the later one is longer, therefore...
    dp[4] = [1,2,4]

    at dp[7]:
    since ony 7%1 == 0
    dp[7] = [1,7]

    at dp[8]
    81 == 0, it means dp[4] can be [1,4]
    8%2 == 0, it means dp[4] can be [1,2,4]
    8%4 == 0, it means dp[4] can be [1,2,4]
    since the later one is longer, therefore...
    dp[8] = [1,2,4,8]

    finally,
    dp[1] = [1]
    dp[2] = [1,2]
    dp[4] = [1,2,4]
    dp[7] = [1,7]
    dp[8] = [1,2,4,8]

    ********
    Caution: during the process, we ignore if the intermediates are divisible amongst others in a set
    ********
    it is because
    8%2 = 0 <- a%c = 0
    8%4 = 0 <- a%b = 0
    it implies that
    4%2 = 0 <- b%c = 0

    ref:
    - https://www.youtube.com/watch?v=6WRuJzsw1TE

    Time    O(N^2)
    Space   O(N)
    560 ms, faster than 23.65%
"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        n = len(nums)
        nums.sort()
        dp = [[x] for x in nums]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
