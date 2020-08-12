"""
    1st approach: combinations, dfs in recursion
	1. for 13,a->d, a->e, a->f...so on
	2. quite similar to permutation problem

	Time	O(3^n -> 4^m)
	Space	O(3^n -> 4^m)
	n: number of 3 characters digits like 1->abc
	m: number of 4 characters digits like 9->wxyz
    20 ms, faster than 75.92%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ht = {}
        ht['2'] = 'abc'
        ht['3'] = 'def'
        ht['4'] = 'ghi'
        ht['5'] = 'jkl'
        ht['6'] = 'mno'
        ht['7'] = 'pqrs'
        ht['8'] = 'tuv'
        ht['9'] = 'wxyz'
        self.dfs("", digits, ht)
        return self.res

    def dfs(self, prefix, remain, ht):
        if len(remain) == 0 and len(prefix) > 0:
            self.res.append(prefix)
        elif len(remain) > 0:
            first = remain[0]
            if first not in ht:
                self.dfs(prefix, remain[1:], ht)
                return
            cands = ht[first]
            for cand in cands:
                self.dfs(prefix+cand, remain[1:], ht)


print(Solution().letterCombinations(""))
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("13"))
print(Solution().letterCombinations("13#4"))
print("-----")

"""
    1st approach: combinations, dfs in recursion
	1. for 13,a->d, a->e, a->f...so on
	2. quite similar to permutation problem

	Time	O(3^n -> 4^m)
	Space	O(3^n -> 4^m)
	n: number of 3 characters digits like 1->abc
	m: number of 4 characters digits like 9->wxyz
    20 ms, faster than 80.31%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ht = {}
        ht['2'] = 'abc'
        ht['3'] = 'def'
        ht['4'] = 'ghi'
        ht['5'] = 'jkl'
        ht['6'] = 'mno'
        ht['7'] = 'pqrs'
        ht['8'] = 'tuv'
        ht['9'] = 'wxyz'
        self.dfs(digits, "", ht)
        return self.res

    def dfs(self, remain, prefix, ht):
        if len(remain) == 0:
            if len(prefix) > 0:
                self.res.append(prefix)
            return
        numStr = remain[0]
        if numStr in ht:
            cands = ht[numStr]
            for cand in cands:
                self.dfs(remain[1:], prefix+cand, ht)
        else:
            self.dfs(remain[1:], prefix, ht)


print(Solution().letterCombinations(""))
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("13"))
print(Solution().letterCombinations("13#4"))
