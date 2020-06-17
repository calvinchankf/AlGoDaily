"""
    2nd attempt: DP, learned from others
    - similar to lc377 but diff loop arrangement

	the idea is to divide the problem into subproblems:
	for each amount, calculate the number of different combinations using the result from smaller amount
	
	e.g.
	dp[amount] = dp[amount] + dp[amount-coin]
	dp[4] = 1 + dp[2]
	it means 4 can be came up with 1111 and the dp[2](the combination of 2), which is 11 and 2
	therefore
	dp[4] = 1 + 2 = 3
	see ./explanation.jpeg

    ref:
    - https://www.youtube.com/watch?v=jaNZ83Q3QGc

    Time    O(N * A)
    Space   O(N)
    192 ms, faster than 46.52%
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = (amount+1)*[0]
        dp[0] = 1  # it means if dp[amount - coin] = dp[0], there is one way
        for i in range(len(coins)):
            coin = coins[i]
            for j in range(1, amount+1):
                if j - coin >= 0:
                    dp[j] += dp[j-coin]
        return dp[amount]


s = Solution()

a = 5
b = [1, 2, 5]
print(s.change(a, b))

a = 10
b = [1, 2, 5, 7]
print(s.change(a, b))

print("----")

"""
    3rd: 2d array DP

    ref: 
    - https://www.youtube.com/watch?v=DJ4a7cmjZY0
    - https://leetcode.com/problems/coin-change-2/discuss/674977/100-Faster-or-Recursive-1-d-2-d-DP-or-Matrix-With-Example-or-Commented
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0

        dp = []
        for _ in range(len(coins)):
            dp.append((amount+1) * [0])

        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(len(coins)):
            coin = coins[i]
            for j in range(1, amount+1):
                remain = j - coin
                if remain >= 0:
                    dp[i][j] = (dp[i-1][j] if i-1 >= 0 else 0) + dp[i][remain]
                else:
                    dp[i][j] = (dp[i-1][j] if i-1 >= 0 else 0)
        return dp[-1][-1]


s = Solution()

a = 5
b = [1, 2, 5]
print(s.change(a, b))

a = 10
b = [1, 2, 5, 7]
print(s.change(a, b))
