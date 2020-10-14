"""
    0th: brute force
    Time    O(2^(M+N))
    LTE:
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.dfs(s1, 0, s2, 0, s3, "")

    def dfs(self, s1, i, s2, j, s3, cur):
        if i == len(s1) and j == len(s2):
            if cur == s3:
                return True
            else:
                return False
        result = False
        if i < len(s1):
            result = result or self.dfs(s1, i+1, s2, j, s3, cur + s1[i])
        if j < len(s2):
            result = result or self.dfs(s1, i, s2, j+1, s3, cur + s2[j])
        return result


s = Solution()

a = "aabcc"
b = "dbbca"
c = "aadbbcbcac"
print(s.isInterleave(a, b, c))

a = "aabcc"
b = "dbbca"
c = "aadbbbaccc"
print(s.isInterleave(a, b, c))

# LTE: 66 / 101 test cases passed.
a = "cabbcaaacacbac"
b = "acabaabacabcca"
c = "cacabaabacaabccbabcaaacacbac"
# print(s.isInterleave(a, b, c))

print("-----")

"""
    1st: dynamic programming, recursive dfs + hashtable
    - recursively check the suffix, to see if we can form s3 from the end

    e.g.
    s1 = abc
    s2 = def
    s3 = abdecf

    At the bottom of the recursion:
    s2[2:] = s3[5:], f = f so we return true

    then we see that:
    s1[2] == s3[4] and s2[2:] = s3[5:](the result from recursion), so we return true

    ....do the steps over and over again we will get the result

    Time    O(MN)
    Space   O(M+N)
    36 ms, faster than 62.76%
"""


class Solution:
    def isInterleave(self, s1, s2, s3) -> bool:
        ht = {}
        return self.dfs(s1, 0, s2, 0, s3, 0, ht)

    def dfs(self, s1, i, s2, j, s3, k, ht):
        if i == len(s1):
            return s2[j:] == s3[k:]
        if j == len(s2):
            return s1[i:] == s3[k:]

        key = (i, j)
        if key in ht:
            return ht[key]

        res = False
        if s3[k] == s1[i] and self.dfs(s1, i + 1, s2, j, s3, k + 1, ht) or\
           s3[k] == s2[j] and self.dfs(s1, i, s2, j + 1, s3, k + 1, ht):
            res = True
        ht[key] = res
        return res


s = Solution()

a = "aabcc"
b = "dbbca"
c = "aadbbcbcac"
print(s.isInterleave(a, b, c))

a = "aabcc"
b = "dbbca"
c = "aadbbbaccc"
print(s.isInterleave(a, b, c))

a = "cabbcaaacacbac"
b = "acabaabacabcca"
c = "cacabaabacaabccbabcaaacacbac"
print(s.isInterleave(a, b, c))

print("-----")


"""
    2nd: dynamic programming, recursive dfs + hashtable
    - recursively check the suffix, to see if we can form s3 from the end

    e.g.
    s1 = abc
    s2 = def
    s3 = abdecf

    At the bottom of the recursion:
    s2[2:] = s3[5:], f = f so we return true

    then we see that:
    s1[2] == s3[4] and s2[2:] = s3[5:](the result from recursion), so we return true

    ....do the steps over and over again we will get the result

    Time    O(MN)
    Space   O(M+N)
    24 ms, faster than 79.12% 
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dfs(s1, s2, s3, {})

    def dfs(self, s1, s2, s3, ht):
        if len(s1) == 0 and len(s2) == 0:
            if len(s3) == 0:
                return True
            return False
        key = (len(s1), len(s2), len(s3))
        if key in ht:
            return ht[key]
        b = False
        if len(s1) > 0 and s1[0] == s3[0]:
            b |= self.dfs(s1[1:], s2, s3[1:], ht)
        if len(s2) > 0 and s2[0] == s3[0]:
            b |= self.dfs(s1, s2[1:], s3[1:], ht)
        ht[key] = b
        return b


"""
    3rd: dynamic programming, 2d array bottom up
    - see ./idea.jpg


    ref:
    - https://leetcode.com/articles/interleaving-strings/
    - https://www.youtube.com/watch?v=ih2OZ9-M3OM

    40 ms, faster than 22.44%
"""


class Solution:
    def isInterleave(self, s1, s2, s3) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        r, c = len(s1), len(s2)
        dp = [[False for _ in range(c+1)] for _ in range(r+1)]
        for i in range(r+1):
            for j in range(c+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = s2[j-1] == s3[i+j-1] and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = s1[i-1] == s3[i+j-1] and dp[i-1][j]
                else:
                    dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) \
                        or s2[j-1] == s3[i+j-1] and dp[i][j-1]
        return dp[-1][-1]
