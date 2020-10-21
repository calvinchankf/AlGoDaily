"""
    1st: recursion

    Time    O(N^N)
    Space   O(N^N)
    984 ms, faster than 100.00%
"""


class Solution(object):
    def maxUniqueSplit(self, s):
        self.res = 1
        hs = set()
        self.dfs(s, hs)
        return self.res

    def dfs(self, s, hs):
        if len(s) == 0:
            self.res = max(self.res, len(hs))
            return
        for i in range(1, len(s) + 1):
            clone = hs.copy()
            clone.add(s[:i])
            self.dfs(s[i:], clone)


s = Solution()

a = 'ababccc'
print(s.maxUniqueSplit(a))

a = 'abc'
print(s.maxUniqueSplit(a))

a = "aba"
print(s.maxUniqueSplit(a))

a = "aa"
print(s.maxUniqueSplit(a))
