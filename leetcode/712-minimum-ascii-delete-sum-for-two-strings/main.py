"""
    1st: dynamic programming, learnt from others
    - similar to lc1143, but this time we store the ascii-sum instead of the length of characters
    - and then, we subtract the dp[-1][-1] with the ascii-sum of s1, s2 to get the answer

    ref:
    - https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/108821/LCS-variation-solution-python-and-c%2B%2B

    Time    O(MN+M+N)
    Space   O(MN)
    440 ms, faster than 99.49%
"""


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i]) * 2
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        n1 = sum(ord(c) for c in s1)
        n2 = sum(ord(c) for c in s2)
        return n1 + n2 - dp[l1][l2]
