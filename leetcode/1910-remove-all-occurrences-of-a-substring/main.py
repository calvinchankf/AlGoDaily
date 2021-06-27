"""
    1st: stack
    - this is an extend version of the classic parentheses problem
    - put the characters onto the stack along the way, remove the tail if there is a match

    Time    O(N)
    Space   O(N)
     28 ms, faster than 71.43%
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= len(part) and stack[-1] == part[-1]:
                i = len(stack) - 1
                j = len(part) - 1
                while i >= 0 and j >= 0 and stack[i] == part[j]:
                    i -= 1
                    j -= 1
                if j == -1:
                    stack = stack[:i+1]
        return ''.join(stack)
