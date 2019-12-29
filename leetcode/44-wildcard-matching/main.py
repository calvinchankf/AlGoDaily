"""
    1st: recursion + hashtable
    LTE 1807 / 1809 test cases passed.
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.ht = {}
        return self.dfs(s, p)

    def dfs(self, s, p):
        if s == p:
            return True

        if len(p) == 0 and len(s) > 0:
            return False

        if (s, p) in self.ht:
            return self.ht[(s, p)]

        if p[0] == '?':
            if len(s) == 0:
                self.ht[(s, p)] = False
                return False
            b = self.dfs(s[1:], p[1:])
            if b:
                self.ht[(s, p)] = True
                return True
        elif p[0] == '*':
            for i in range(-1, len(s)):
                b = self.dfs(s[i+1:], p[1:])
                if b:
                    self.ht[(s, p)] = True
                    return True
        elif len(s) > 0 and s[0] == p[0]:
            b = self.dfs(s[1:], p[1:])
            if b:
                self.ht[(s, p)] = True
                return True
        self.ht[(s, p)] = False
        return False


s = Solution()

# False
a = 'aa'
b = 'a'
print(s.isMatch(a, b))

# True
a = 'aa'
b = '*'
print(s.isMatch(a, b))

# False
a = 'cb'
b = '?a'
print(s.isMatch(a, b))

# True
a = 'adceb'
b = '*a*b'
print(s.isMatch(a, b))

# False
a = 'acdcb'
b = 'a*c?b'
print(s.isMatch(a, b))

# False
a = ''
b = '?'
print(s.isMatch(a, b))

# True
a = ''
b = '*'
print(s.isMatch(a, b))

# True
a = ''
b = '**'
print(s.isMatch(a, b))

a = "ababbbbbbaabbbbabaaabbaaaabaaababbbaababbaaabbaaaabbabaabbabbbbbabbaabbbaabbbbababbaabaaaabbabaaaabababbaababbbbaababbabaababbabbbbbaaaaababaabaaabaabbabaaaaabbaaaaabaaababbbbbbabbabbbbbababbaabaaaabbbbaa"
b = "*ba*a*b*****a*ba*a*****aa***bba**a**aab**aa*a****a*a*bb*aabb*bbb*aa*aba*bbbb**aba***a*ba**bba*****a**abb"
print(s.isMatch(a, b))

print("-----")

"""
    2nd: bottom-up dynamic programming, learnd from others
    - similar to lc72, 583, 712

    ref:
    - https://www.youtube.com/watch?v=3ZDZ-N0EPV0
    - https://leetcode.com/articles/wildcard-matching/

    Time    O(SP)
    Space   O(SP)
    736 ms, faster than 65.31%
"""


class Solution(object):

    def removeDummyStars(self, p):
        if p == '':
            return p
        p1 = [p[0]]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

    def isMatch(self, s, p):
        p = self.removeDummyStars(p)
        dp = [(len(p) + 1) * [False] for _ in range(len(s) + 1)]
        dp[0][0] = True
        if len(p) > 0 and p[0] == '*':
            dp[0][1] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[len(s)][len(p)]


s = Solution()

# False
a = 'aa'
b = 'a'
print(s.isMatch(a, b))

# True
a = 'aa'
b = '*'
print(s.isMatch(a, b))

# False
a = 'cb'
b = '?a'
print(s.isMatch(a, b))

# True
a = 'adceb'
b = '*a*b'
print(s.isMatch(a, b))

# False
a = 'acdcb'
b = 'a*c?b'
print(s.isMatch(a, b))

# False
a = ''
b = '?'
print(s.isMatch(a, b))

# True
a = ''
b = '*'
print(s.isMatch(a, b))

# True
a = ''
b = '**'
print(s.isMatch(a, b))

a = "ababbbbbbaabbbbabaaabbaaaabaaababbbaababbaaabbaaaabbabaabbabbbbbabbaabbbaabbbbababbaabaaaabbabaaaabababbaababbbbaababbabaababbabbbbbaaaaababaabaaabaabbabaaaaabbaaaaabaaababbbbbbabbabbbbbababbaabaaaabbbbaa"
b = "*ba*a*b*****a*ba*a*****aa***bba**a**aab**aa*a****a*a*bb*aabb*bbb*aa*aba*bbbb**aba***a*ba**bba*****a**abb"
print(s.isMatch(a, b))
