"""
    1st approach: dfs
	- recursively go through all the possibilities
	- avoid duplicate computing by using a set
    
	Time	O(2^n)
	Space	O(2^n)
	48 ms, faster than 70.01%
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.res = []
        self.dfs(S, 0, '')
        return self.res

    def dfs(self, s, i, cur):
        if i == len(s):
            self.res.append(cur)
            return
        c = s[i]
        if c.isdigit():
            self.dfs(s, i+1, cur+c)
        else:
            self.dfs(s, i+1, cur+c.lower())
            self.dfs(s, i+1, cur+c.upper())
