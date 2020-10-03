import sys

"""
	2nd approach: bottom-up DP, learned from others https://zhuanlan.zhihu.com/p/32980698
	e.g. [10,15,20,30,4]
	dp[0] = 10
	dp[1] = 15 to get here, we must step on this stair, therefore it is not min(10, 15) = 10
	dp[2] = 20 + min(dp[0], dp[1]) = 20 + 10 = 30
	dp[3] = 30 + min(dp[1], dp[2]) = 20 + 15 = 35
	dp[4] = 4  + min(dp[2], dp[3]) = 4  + 30 = 34
    dp[5] = 0  + min(dp[3], dp[4]) = 34

	Time 	O(n)
	Space	O(n) the dp array
	44 ms, faster than 78.81%
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = (n+1) * [0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n+1):
            curCost = 0
            if i < len(cost):
                curCost = cost[i]
            dp[i] = min(dp[i-1], dp[i-2]) + curCost
        return dp[n]


print(Solution().minCostClimbingStairs([10, 15, 20, 30, 4]))

print("-----")

"""
	3rd approach: bottom-up DP, learned from others https://zhuanlan.zhihu.com/p/32980698
	e.g. [10,15,20,30]
	dp[0] = 10
	dp[1] = 15 to get here, we must step on this stair, therefore it is not min(10, 15) = 10
	dp[2] = 20 + min(dp[0], dp[1]) = 20 + 10 = 30
	dp[3] = 30 + min(dp[1], dp[2]) = 20 + 15 = 35
    dp[4] = 4  + min(dp[2], dp[3]) = 4  + 30 = 34
    result = min(dp[3], dp[4]) = 34

	Time 	O(n)
	Space	O(n) the dp array
	40 ms, faster than 89.69%
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = n * [sys.maxsize]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])


print(Solution().minCostClimbingStairs([10, 15, 20, 30, 4]))
