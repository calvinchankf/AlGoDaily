import sys

"""
    1st: dp, learned from others
    - actually it is similar to coin change, we can do it with a bottom up approach
    - be careful that:
        1. for non-present days, extand the previous day cost
        2. ticket(s) might be more expensive than 1/7 day(s) ticket e.g. days = [1, 4, 6, 7, 8, 20], costs = [7, 2, 15]

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

            # extand the cost from previous day if there is no such day in the list
            if i not in daySet:
                dp[i] = dp[i-1]
                continue

            temp = sys.maxsize
            # day - 1 or just buy ticket[0]
            # keep in mind that i starts from 1, i-1 < 0 would never be reached
            temp = min(temp, dp[i-1]+costs[0])
            # day - 7 or just buy ticket[1]
            if i - 7 >= 0:
                temp = min(temp, dp[i-7]+costs[1])
            else:
                # corner case: [1, 4, 6, 7, 8, 20], costs = [7, 2, 15]
                # on day 1, buying 7 days ticket is cheaper than buying 1 day
                temp = min(temp, costs[1])
            # day - 30 or just buy ticket[2]
            if i - 30 >= 0:
                temp = min(temp, dp[i-30]+costs[2])
            else:
                # corner case: [1, 4, 6, 7, 8, 20], costs = [7, 2, 1]
                # on day 1, buying 30 days ticket is cheaper than buying 1 day and 7 days
                temp = min(temp, costs[2])
            # update dp[i]
            dp[i] = temp

        return dp[lastDay]


a = [1, 4, 6, 7, 8, 20]
b = [2, 7, 15]
print(Solution().mincostTickets(a, b))

print("-----")

"""
    2nd : dp, learned from others, more concise
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

            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2]
            )

        return dp[lastDay]


a = [1, 4, 6, 7, 8, 20]
b = [2, 7, 15]
print(Solution().mincostTickets(a, b))
