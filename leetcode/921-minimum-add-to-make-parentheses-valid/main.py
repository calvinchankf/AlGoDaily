"""
    1st approach: stack
    - similar to lc1614
	1. for each add, push to stack
	2. for each close and no counterpart in stack, result++
	3. result = res + len(stack)

	Time	O(n)
	Space	O(n)
    20 ms, faster than 96.69%
"""


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S) == 0:
            return 0
        closeCount = 0
        openCount = 0
        for c in S:
            if c == '(':
                openCount += 1
            else:
                if openCount == 0:
                    closeCount += 1
                else:
                    openCount -= 1
        return openCount + closeCount


a = "())"
print(Solution().minAddToMakeValid(a))

a = "((("
print(Solution().minAddToMakeValid(a))

a = "()"
print(Solution().minAddToMakeValid(a))

a = "()))(("
print(Solution().minAddToMakeValid(a))

print("------------------------")

"""
    followup: we also include {} and []
    therefore 3 types:
    - (), {}, []
"""


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type S: str
        :rtype: int
        """
        if len(s) == 0:
            return True
        stack = []
        m = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        extraClose = 0
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif c in m:
                if len(stack) > 0 and stack[-1] == m[c]:
                    stack.pop()
                else:
                    extraClose += 1
        return len(stack) + extraClose


a = "())"
print(Solution().minAddToMakeValid(a))

a = "((("
print(Solution().minAddToMakeValid(a))

a = "()"
print(Solution().minAddToMakeValid(a))

a = "()))(("
print(Solution().minAddToMakeValid(a))

a = "()){}"
print(Solution().minAddToMakeValid(a))

a = "((({{}"
print(Solution().minAddToMakeValid(a))

a = "(){]"
print(Solution().minAddToMakeValid(a))

a = "()))(({]]}}"
print(Solution().minAddToMakeValid(a))
