"""
    1st: dp
    - related to lc516, 1143
    - rephrase: see if the length of longest common subsequence >= n - k

    Time    O(N^2)
    Space   O(N^2)
    776 ms, faster than 28.95%
"""
class Solution(object):
    def isValidPalindrome(self, s, k):
        n = len(s)
        t = s[::-1]
        maxPalindromeLen = self.longestCommonSubsequence(s, t)
        if maxPalindromeLen >= n - k:
            return True
        return False
    
    def longestCommonSubsequence(self, text1, text2):
        R, C = len(text1), len(text2)
        dp = [C * [0] for _ in range(R)]
        
        for i in range(R):
            if text1[i] == text2[0] or (i > 0 and dp[i-1][0] == 1):
                dp[i][0] = 1
        
        for j in range(1, C):
            if text1[0] == text2[j] or (j > 0 and dp[0][j-1] == 1):
                dp[0][j] = 1
        
        res = 0
        for i in range(R):
            for j in range(C):
                if i > 0 and j > 0:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                res = max(res, dp[i][j])
        
        return res