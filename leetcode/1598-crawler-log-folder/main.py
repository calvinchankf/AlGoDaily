"""
    1st: stack

    Time    O(N)
    Space   O(N)
    32 ms, faster than 100.00%
"""
class Solution(object):
    def minOperations(self, logs):
        stack = []
        for log in logs:
            if log == '../':
                if len(stack) > 0:
                    stack.pop()
            elif log == './':
                continue
            else: 
                stack.append(log)
        return len(stack)