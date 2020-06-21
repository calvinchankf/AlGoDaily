"""
    1st: dp
    - similar to lc518 but diff loop arrangement

    Time    O(NA)
    Space   O(N)
    52 ms, faster than 28.01%
"""


class Solution:
    def combinationSum4(self, coins, amount):
        dp = (amount+1)*[0]
        dp[0] = 1
        for i in range(1, amount+1):
            for j in range(len(coins)):
                remain = i - coins[j]
                if remain >= 0:
                    dp[i] += dp[remain]
            print(dp)
        return dp[amount]


s = Solution()

a = [1, 2, 5]
b = 5
print(s.combinationSum4(a, b))
