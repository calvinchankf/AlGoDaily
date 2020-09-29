"""
    1st: stack

    Time    O(N)
    Space   O(N)
    48 ms, faster than 98.82%
"""
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    if (a < 0 and b < 0) or (a >= 0 and b > 0):
                        stack.append(a // b)
                    elif a < 0:
                        stack.append(-(abs(a) // b))
                    elif b < 0:
                        stack.append(-(a // abs(b)))
            else:
                stack.append(int(t))
        return stack[0]