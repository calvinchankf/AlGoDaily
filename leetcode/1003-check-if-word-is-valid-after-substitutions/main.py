"""
    1st: stack
    - similar lc20

    Time    O(N)
    Space   O(N)
    48 ms, faster than 74.58%
"""


class Solution(object):
    def isValid(self, S):
        stack = []
        for c in S:
            if c == 'c':
                if len(stack) >= 2 and stack[-2] == 'a' and stack[-1] == 'b':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
