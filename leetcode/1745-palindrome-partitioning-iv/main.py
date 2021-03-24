"""
    1st: brute force

    Time    O(N^3)
    LTE
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        forwards = []
        for i in range(n-2):
            if self.checkPalindrom(s, 0, i):
                forwards.append(i)
        backwards = []
        for i in range(n-1, 1, -1):
            if self.checkPalindrom(s, i, n-1):
                backwards.append(i)
        for i in forwards:
            for j in backwards:
                if i+1 < j:
                    if self.checkPalindrom(s, i+1, j-1):
                        return True
                else:
                    break
        return False

    def checkPalindrom(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


"""
    2nd: DP, learned from others
    - build a palindrom quick look-up table to tell us if s[i:j+1] is a palindrome in O(1)
    - if s[i] == s[j], we know if s[i:j+1] is a palindrom by looking at s[i+1,j-1]

    ref:
    - https://leetcode.com/problems/palindrome-partitioning-iv/discuss/1042910/Java-Detailed-Explanation-DP-O(N2)

    Time    O(N^2)
    Space   O(N^2)
    3508 ms, faster than 58.67%
"""


class Solution(object):
    def checkPartitioning(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i+1 <= j-1:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = True
        for i in range(1, n):
            for j in range(i, n-1):
                if dp[0][i-1] and dp[i][j] and dp[j+1][n-1]:
                    return True
        return False
