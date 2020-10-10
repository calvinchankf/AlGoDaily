from typing import List

"""
    1st: brute force dp

    Time    O(N^2)
    Space   O(N)
    9800 ms, faster than 5.02%
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: x[0] * x[1])
        dp = n * [1]
        for i in range(1, n):
            w1, h1 = envelopes[i]
            for j in range(i):
                w2, h2 = envelopes[j]
                if w1 > w2 and h1 > h2:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()

# 4
a = [[5, 4], [8, 7], [8, 3], [6, 4], [8, 8], [6, 7], [
    2, 3], [1, 10], [3, 9], [10, 2], [10, 4], [10, 5]]
print(s.maxEnvelopes(a))
