"""
    1st approach: DP
    - same approach can solve another classic problem: K-Palindrome
    - clone and revert the input string
    - do longest common subsequence against the input string

    Time    O(n^2)
    Space   O(n^2)
    2484 ms, faster than 6.40%
"""


class Solution(object):
    def longestPalindromeSubseq(self, A):
        """
        :type s: str
        :rtype: int
        """
        if len(A) == 0:
            return 0
        B = A[::-1]
        dp = []
        for i in range(len(A)+1):
            dp.append((len(A)+1)*[0])
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
