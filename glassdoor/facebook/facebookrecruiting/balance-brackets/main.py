"""
    lc20
"""


def isBalanced(s):
    m = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif len(stack) > 0 and stack[-1] == m[c]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
