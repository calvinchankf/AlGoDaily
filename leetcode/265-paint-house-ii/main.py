import sys
from typing import List

"""
    1st: similar to lc256
    - but this time we can optimize the speed by precompute 2 smallest values from the previous row result

    Time    O(NK)
    Space   O(K)
    104 ms, faster than 95.10%
"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        R = len(costs)
        C = len(costs[0])
        dp = costs[0][:]
        for i in range(1, R):
            min1, min2 = sys.maxsize, sys.maxsize
            min1Idx, min2Idx = -1, -1
            for j in range(C):
                if dp[j] < min1:
                    min2, min2Idx = min1, min1Idx
                    min1, min1Idx = dp[j], j
                elif dp[j] < min2:
                    min2, min2Idx = dp[j], j
            temp = C * [0]
            for j in range(C):
                if j != min1Idx:
                    temp[j] = costs[i][j] + min1
                else:
                    temp[j] = costs[i][j] + min2
            dp = temp
        return min(dp)
