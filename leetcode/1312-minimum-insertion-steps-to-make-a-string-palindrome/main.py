"""
    dynamic programming: longest common subsequence
    - similar to lc516, 1143, 1312
    - revert the string, find the LCS, the offest is the result

    Time    O(N^2)
    Space   O(N)
    1108 ms, faster than 52.33%
"""


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        t = s[::-1]
        dp = []
        for i in range(n+1):
            dp.append((n+1)*[0])
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return n - dp[-1][-1]
