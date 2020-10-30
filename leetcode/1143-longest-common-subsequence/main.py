"""
    class dynamic programming problem
    - longest common substring
    - similar to lc712
    - see miscellaneous/longest-common-subsequence/idea.png

    ref:
    - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    Time    O(AB)
    Space   O(AB)
    360 ms, faster than 59.82%
"""


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) == 0 or len(B) == 0:
            return 0
        dp = []
        for i in range(len(A)+1):
            dp.append((len(B)+1)*[0])
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return res


s = Solution()

a = 'BATD'
b = 'ABACD'
print(s.findLength(a, b))

a = 'XMJYAUZ'
b = 'MZJAWXU'
print(s.findLength(a, b))

a = 'XMJYAUZMJ'
b = 'MZJAWXUM'
print(s.findLength(a, b))

a = 'ABCDEFGHIJKLM'
b = 'CFKABEFJMABC'
print(s.findLength(a, b))

a = 'BSBININM'
b = 'JMJKBKJKV'
print(s.findLength(a, b))

print("-----")

"""
    2nd: same with 1st but
    - more similar to longest common substring
    - easier to explain
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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

s = Solution()

a = 'BATD'
b = 'ABACD'
print(s.findLength(a, b))

a = 'XMJYAUZ'
b = 'MZJAWXU'
print(s.findLength(a, b))

a = 'XMJYAUZMJ'
b = 'MZJAWXUM'
print(s.findLength(a, b))

a = 'ABCDEFGHIJKLM'
b = 'CFKABEFJMABC'
print(s.findLength(a, b))

a = 'BSBININM'
b = 'JMJKBKJKV'
print(s.findLength(a, b))