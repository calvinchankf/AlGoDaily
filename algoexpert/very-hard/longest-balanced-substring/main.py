"""
    - lc32

    Time    O(N)
    Space   O(N)
"""


def longestBalancedSubstring(s):
    stack = []
      res = 0
       for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append((c, i))
            else:
                if len(stack) > 0 and stack[-1][0] == '(':
                    stack.pop()
                    diff = 0
                    if len(stack) > 0:
                        diff = i - stack[-1][1]
                    else:
                        diff = i + 1
                    res = max(res, diff)
                else:
                    stack.append((c, i))
        return res
