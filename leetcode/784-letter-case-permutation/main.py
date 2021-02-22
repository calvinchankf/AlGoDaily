"""
    1st approach: dfs
	- recursively go through all the possibilities
	- avoid duplicate computing by using a set
    
	Time	O(2^n)
	Space	O(2^n)
	48 ms, faster than 70.01%
"""


class Solution(object):
    def letterCasePermutation(self, S):
        self.res = []
        self.dfs(S, '')
        return self.res

    def dfs(self, S, cur):
        if len(S) == 0:
            self.res.append(cur)
            return
        c = S[0]
        remain = S[1:]
        if c in '0123456789':
            self.dfs(remain, cur + c)
        else:
            self.dfs(remain, cur + c.upper())
            self.dfs(remain, cur + c.lower())
