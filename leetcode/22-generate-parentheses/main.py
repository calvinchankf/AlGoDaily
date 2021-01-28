class Solution(object):

    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        148ms beats 2.52%
        """
        if n <= 0:
            return []
        self.permuate("", 0, 2*n)
        return self.res

    def permuate(self, s, i, k):
        if i == k:
            if self.isValid(s):
                self.res.append(s)
            return
        self.permuate(s + "(", i+1, k)
        self.permuate(s + ")", i+1, k)

    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack = stack[:-1]
                else:
                    return False
        return len(stack) == 0


print(Solution().generateParenthesis(-1))
print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))

"""
    2nd approach:
    - there are total 2^2n permutation we when appedn ( and ) from top to down
    - however, some resulting parentheses strings are not balenced
    - to make it balence, we should set a constraint that no. of close <= no. of open

    Time    < O(2^2n) the total number of nodes in the recursion tree
    Space   < O(2^2n)
    24 ms, faster than 100.00%
"""


class Solution(object):
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        self.res = []
        self.dfs(n, '', 0, 0)
        return self.res

    def dfs(self, n, s, openCount, closeCount):
        if openCount == n and closeCount == n:
            self.res.append(s)
        if openCount < n:
            self.dfs(n, s + '(', openCount+1, closeCount)
        if closeCount < openCount:
            self.dfs(n, s + ')', openCount, closeCount+1)


print(Solution().generateParenthesis(-1))
print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
