"""
    1st: brute force
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


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.ht = {}
        return self.dfs(s1, 0, s2, 0, s3, "")

    def dfs(self, s1, i, s2, j, s3, cur):
        key = (i, j)
        print(i, j, cur)
        if i == len(s1) and j == len(s2):
            if cur == s3:
                return True
            else:
                return False
        if key in self.ht:
            # print(key, self.ht[key])
            return self.ht[key]
        result = False
        if i < len(s1):
            result = result or self.dfs(s1, i+1, s2, j, s3, cur + s1[i])
        if j < len(s2):
            result = result or self.dfs(s1, i, s2, j+1, s3, cur + s2[j])
        self.ht[key] = result
        return result


s = Solution()

a = "aabcc"
b = "dbbca"
c = "aadbbcbcac"
print(s.isInterleave(a, b, c))

# a = "aabcc"
# b = "dbbca"
# c = "aadbbbaccc"
# print(s.isInterleave(a, b, c))

# # LTE: 66 / 101 test cases passed.
# a = "cabbcaaacacbac"
# b = "acabaabacabcca"
# c = "cacabaabacaabccbabcaaacacbac"
# print(s.isInterleave(a, b, c))
