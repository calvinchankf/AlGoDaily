"""
    1st approach: stack
    - similar to parentheses problem
    - when the last item is equal to the current item, pop stack

    Time    O(N)
    Space   O(N)
    92 ms, faster than 41.55%
"""


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
