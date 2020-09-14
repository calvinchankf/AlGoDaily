"""
    questions to ask:
    - any malformed expression? no
    - any other characters? only digit and +-*/ and space
    - no negative numbers? yes
    - all numbers are single digited? no, u might be given 12+34+5/6
"""

"""
    1st approach:
    - use 1 queue
    - for every number or + / -, put it into the queue
    - but for * and /, multiply or divide the next item with the last item in the queue

    Time    O(2n)
    Space   O(n) the queue
    4152 ms, faster than 5.09%
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = []
        i = 0
        shouldMultiply = False
        shouldDivide = False
        while i < len(s):
            if s[i].isdigit():
                temp = int(s[i])
                j = i+1
                while j < len(s) and s[j].isdigit():
                    temp = temp*10 + int(s[j])
                    j += 1
                if shouldMultiply:
                    queue[-1] = temp * queue[-1]
                    shouldMultiply = False
                elif shouldDivide:
                    queue[-1] = queue[-1] / temp
                    shouldDivide = False
                else:
                    queue.append(temp)
                i = j
            else:
                if s[i] == "*":
                    shouldMultiply = True
                elif s[i] == "/":
                    shouldDivide = True
                elif s[i] == "+" or s[i] == "-":
                    queue.append(s[i])
                i += 1
        shouldAdd = False
        shouldMinus = False
        result = 0
        while len(queue) > 0:
            pop = queue.pop(0)
            if isinstance(pop, int):
                if shouldAdd:
                    result += pop
                    shouldAdd = False
                elif shouldMinus:
                    result -= pop
                    shouldMinus = False
                else:
                    result += pop
            elif pop == "+":
                shouldAdd = True
            elif pop == "-":
                shouldMinus = True
        return result


# string = '0'
# print(string.isdigit())

# a = "da"
# print(isinstance(a, int))

# a = 5
# print(isinstance(a, int))

# 47
print(Solution().calculate("3+22*2"))
# 1
print(Solution().calculate(" 3/2 "))
# -1
print(Solution().calculate(" 0-3/2 "))
# 5
print(Solution().calculate(" 3+5 / 2"))
# 12
print(Solution().calculate("14-3/2"))
# 7
print(Solution().calculate("3+5/2*2"))
# 6
print(Solution().calculate("1+2 *5/3+6/4*2 "))
# 45
print(Solution().calculate("100-1-2-3-4-5-6-7-8-9-10"))
# -5
print(Solution().calculate("0-5"))
# -2147483647
print(Solution().calculate("0-2147483647"))

print("-----")

"""
    2nd approach:

    The basic idea is to use a stack.
    when we encounter, we do operation with the last item in the stack with the last operator and the current number
    e.g. + 1 + 2 * 3 + ...
    lastOp = *
    cur = 3
    stack = [1, 2]
    when it reaches to the last +, we pop the 2, multipy with the current number and put it back to the stack => [1, 6]


    1. use 1 stack
    2. 1 buffer for number(cos it might have more than one digit)
    3. 1 buffer for operator
    4. if the current character is an operator
        1. operate the current number with the previous operator
        2. and put the result into the stack
        3. set the current character as the next operator
    5. sum up all the numbers in the stack to get the result

    Time    O(2n)
    Space   O(n) the stack
    152 ms, faster than 51.65%
"""


class Solution(object):
    def calculate(self, s):
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)
            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                sign = c
                num = 0
        return sum(stack)


# python2 integer division floors to smaller integer, but we circumvent it by doing float division
# https://www.quora.com/What-does-floor-division-in-Python-do
a = -3
b = 2
print(a/b)
print(int(a/float(b)))

print('---')

# 47
print(Solution().calculate("3+22*2"))
# 1
print(Solution().calculate(" 3/2 "))
# -1
print(Solution().calculate(" 0-3/2 "))
# 5
print(Solution().calculate(" 3+5 / 2"))
# 12
print(Solution().calculate("14-3/2"))
# 7
print(Solution().calculate("3+5/2*2"))
# 6
print(Solution().calculate("1+2 *5/3+6/4*2 "))
# 45
print(Solution().calculate("100-1-2-3-4-5-6-7-8-9-10"))
# -5
print(Solution().calculate("0-5"))
# -2147483647
print(Solution().calculate("0-2147483647"))
