"""
    1st approach:
    - count the number of redundant of open and close parentheses
    - generate all possibilities and aggregate the valid results

    Time    O(2^n)
    Space   O(2^n)
    LTE
"""


class Solution(object):
    def __init__(self):
        self.res = set()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        # count the redundant open and close
        closeCount = 0
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            elif c == ')':
                if openCount == 0:
                    closeCount += 1
                else:
                    openCount -= 1
        # call recursion
        self.dfs(s, openCount, closeCount)
        return list(self.res)

    def dfs(self, s, remainOpen, remainClose):
        if remainOpen == 0 and remainClose == 0:
            if self.isValid(s):
                # self.res.append(s)
                self.res.add(s)
        else:
            for i in range(len(s)):
                if s[i] == '(' and remainOpen > 0:
                    self.dfs(s[:i]+s[i+1:], remainOpen-1, remainClose)
                if s[i] == ')' and remainClose > 0:
                    self.dfs(s[:i]+s[i+1:], remainOpen, remainClose-1)

    def isValid(self, s):
        if len(s) == 0:
            return True
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            elif c == ')':
                if openCount == 0:
                    return False
                else:
                    openCount -= 1
        return openCount == 0


"""
    2nd approach: same as approach 1 but optimize a bit
    - count the number of redundant of open and close parentheses
    - generate all possibilities and aggregate the valid results
    - only strip out the last ( or ) if see a sequence of them

    Time    O(2^n)
    Space   O(2^n)
    48 ms, faster than 86.49%
"""


class Solution(object):

    def __init__(self):
        self.res = set()
        # self.res = []

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        # count the redundant open and close
        closeCount = 0
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            elif c == ')':
                if openCount == 0:
                    closeCount += 1
                else:
                    openCount -= 1
        # call recursion
        self.dfs(s, openCount, closeCount, 0)
        return list(self.res)
        # return self.res

    def dfs(self, s, remainOpen, remainClose, startFrom):
        if remainOpen == 0 and remainClose == 0:
            if self.isValid(s):
                self.res.add(s)
                # self.res.append(s)
        else:
            for i in range(startFrom, len(s)):
                if i != startFrom and s[i] == s[i-1]:
                    continue
                if s[i] == '(' and remainOpen > 0:
                    self.dfs(s[:i]+s[i+1:], remainOpen -
                             1, remainClose, i)
                if s[i] == ')' and remainClose > 0:
                    self.dfs(s[:i]+s[i+1:], remainOpen,
                             remainClose-1, i)

    def isValid(self, s):
        if len(s) == 0:
            return True
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            elif c == ')':
                if openCount == 0:
                    return False
                else:
                    openCount -= 1
        return openCount == 0


a = "()())()"
print(Solution().removeInvalidParentheses(a))

a = "(a)())()"
print(Solution().removeInvalidParentheses(a))

a = ")("
print(Solution().removeInvalidParentheses(a))

a = "((()((s((((()"
print(Solution().removeInvalidParentheses(a))

a = ")k)))())()())))())"
print(Solution().removeInvalidParentheses(a))

a = ")()m)(((()((()(((("
print(Solution().removeInvalidParentheses(a))
