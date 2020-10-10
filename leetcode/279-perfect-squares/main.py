import sys
import math

"""
    2nd approach: bottom up dp

    similar to lc322: coin change
    e.g. coins = [1,2,5], amount = 7
    f(0) = 0  so if f(100-100), it output 0+1=1
    f(1) = min(f0)) + 1
    f(2) = min(f(1)+f(0)) + 1
    f(3) = min(f(2)+f(1)) + 1
    f(4) = min(f(3)+f(2)) + 1
    f(5) = min(f(4)+f(3)+f(0)) + 1
    f(6) = min(f(5)+f(4)+f(1)) + 1
    f(7) = min(f(6)+f(5)+f(2)) + 1

    Time    O(nk) k: square of n
    Space   O(n)
    3492 ms, faster than 42.63%
"""


class Solution(object):
    def numSquares(self, n):
        cands = []
        for i in range(1, int(math.sqrt(n))+1):
            cands.append(i**2)

        dp = (n + 1) * [0]
        for i in range(1, n+1):
            minCount = sys.maxsize
            for cand in cands:
                if i - cand >= 0:
                    minCount = min(minCount, dp[i-cand] + 1)
                else:
                    break
            dp[i] = minCount
        return dp[-1]


print(Solution().numSquares(7691))
