"""
    class dynamic programming problem
    - similar to longest common substring
    - see ./idea.png

    ref:
    - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    Time    O(AB)
    Space   O(AB)
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

print('-----')

"""
    class dynamic programming problem
    - similar to longest common substring
    - see ./idea.png

    ref:
    - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    Time    O(AB)
    Space   O(AB)
"""


class Solution(object):
    def findLongestCommonSubsequence(self, A, B):
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
        # resCount = 0
        res = ''
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    # res = max(res, dp[i+1][j+1])
                    if dp[i+1][j+1] > len(res):
                        res += A[i]  # or res += B[i]
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
