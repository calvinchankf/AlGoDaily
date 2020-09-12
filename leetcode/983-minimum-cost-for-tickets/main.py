import sys

"""
    1st : dp, learned from others, more concise
    - actually it is similar to coin change, we can do it with a bottom up approach
    - be careful that:
        1. for non-present days, extand the previous day cost
        2. since 7days, 30 days passes might cheaper than the 1day and 7days, we need to consider the cost if i-1/7/30 < 0

    e.g. days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]
    cost
    dp[0]                           = 0
    dp[1] = dp[1]+2                 = 2
    dp[2] = dp[1]                   = 2 <= no such date extand from previous
    dp[3] = dp[2]                   = 2 <= no such date extand from previous
    dp[4] = dp[3]+2                 = 4
    dp[5] = dp[4]                   = 4 <= no such date extand from previous
    dp[6] = dp[5]+2                 = 6
    dp[7] = min(dp[6]+2, dp[0]+7)   = 7
    dp[8] = min(dp[7]+2, dp[1]+7)   = 9
    dp[9] = dp[8]                   = 9 <= no such date extand from previous
    ...

    Time    O(n)
    Space   O(n)
    28 ms, faster than 80.10%
"""


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        daySet = set(days)
        lastDay = days[-1]
        dp = (lastDay + 1) * [0]
        for i in range(1, lastDay+1):
            if i not in daySet:
                dp[i] = dp[i-1]
                continue
            a = dp[max(i - 1, 0)] + costs[0]
            b = dp[max(i - 7, 0)] + costs[1]
            c = dp[max(i - 30, 0)] + costs[2]
            dp[i] = min(a, b, c)
        return dp[lastDay]


a = [1, 4, 6, 7, 8, 20]
b = [2, 7, 15]
print(Solution().mincostTickets(a, b))
