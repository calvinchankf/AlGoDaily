class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        m = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif c in m:
                if len(stack) > 0 and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


"""
    simplified version: only '('
"""


class Solution(object):
    def isValid(self, s):
        if len(s) == 0:
            return True
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            else:
                if openCount == 0:
                    return False
                else:
                    openCount -= 1
        return openCount == 0


print(Solution().isValid("(())"))
print(Solution().isValid("(()"))
print(Solution().isValid("(())()"))

print("-----")

"""
    2nd: brute force
    - remove all parentheses () [] {} from the string until the point we cannot remove anymore

    Time    O(N^2)
    Space   O(1)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
        return len(s) == 0


print(Solution().isValid("(())"))
print(Solution().isValid("(()"))
print(Solution().isValid("(())()"))
