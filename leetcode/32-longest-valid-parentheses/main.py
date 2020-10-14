"""
    1st approach: brute force

    Time    O(n^3)
    Space   O(1)
    LTE
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if self.isValid(sub):
                    res = max(res, j-i+1)
        return res

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


a = "(()"
print(Solution().longestValidParentheses(a))

a = ")()())"
print(Solution().longestValidParentheses(a))

a = ")(()())"
print(Solution().longestValidParentheses(a))

a = ")(()()))"
print(Solution().longestValidParentheses(a))

a = ")(()()))))(()()())"
print(Solution().longestValidParentheses(a))

a = "()(()"
print(Solution().longestValidParentheses(a))

print("---------------")


"""
    2nd: stack
    - similar to lc20

    e.g. ")()(()))"

    01234567
    )()(()))()
     ^    ^
    the longest valid one


    1. just store the parentheses and corresponding indices into a stack [(parentheses, index), ...]
    2. then when we see a (, we can calculate the length of a valid parentheses by i - stack[-1][1]

    Time    O(N)
    Space   O(N)
    84 ms, faster than 79.21%
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append((c, i))
            elif c == ')':
                if len(stack) > 0 and stack[-1][0] == '(':
                    stack.pop()
                    diff = None
                    if len(stack) > 0:
                        diff = i - stack[-1][1]
                    else:
                        diff = i + 1
                    res = max(res, diff)
                else:
                    stack.append((c, i))
        return res


a = "(()"
print(Solution().longestValidParentheses(a))

a = ")()())"
print(Solution().longestValidParentheses(a))

a = ")(()())"
print(Solution().longestValidParentheses(a))

a = ")(()()))"
print(Solution().longestValidParentheses(a))

a = ")(()()))))(()()())"
print(Solution().longestValidParentheses(a))

a = "()(()"
print(Solution().longestValidParentheses(a))
