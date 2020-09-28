"""
    1st approach: recursion
    - the logic is similar to lc227 but we also do recursion when we see an open parenthesis

    Time    O(n^2) because we have to find the corresponding closing parenthesis for recursion
    Space   O(n)
    204 ms, faster than 7.41%
"""


class Solution(object):
    def calculate(self, s):
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)

            if c == '(':
                # find the corresponding ")"
                pCnt = 0
                end = 0
                clone = s[i:]
                while end < len(clone):
                    if clone[end] == '(':
                        pCnt += 1
                    elif clone[end] == ')':
                        pCnt -= 1
                        if pCnt == 0:
                            break
                    end += 1
                # do recursion to calculate the sum within the next (...)
                num = self.calculate(s[i+1:i+end])
                i += end

            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
            i += 1

        return sum(stack)


# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
print(Solution().calculate("1 + 1"))
print(Solution().calculate(" 6-4 / 2 "))
print(Solution().calculate("1-(2+3)"))
print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))
print(Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))

print("-----")


"""
    2nd approach: better recursion
    - transform input array into an array so that we can use pop()
    - the logic is similar to the 1st approach but we dont need to find the closing parenthesis before go into a (...)

    Time    O(n)
    Space   O(n)
    80 ms, faster than 22.22%
"""


class Solution:
    def calculate(self, s: str) -> int:
        q = [c for c in s]
        return self.helper(q)

    def helper(self, q):
        stack = []
        sign = '+'
        num = 0
        while len(q) > 0:
            c = q.pop(0)
            if c.isdigit():
                num = num*10 + int(c)
            # regard '(...)' as a number
            if c == '(':
                num = self.helper(q)
            if len(q) == 0 or c == '+' or c == '-' or c == '*' or c == '/' or c == ')':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                # finish and return
                if c == ')':
                    return sum(stack)
                sign = c
                num = 0
        return sum(stack)


# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
print(Solution().calculate("1 + 1"))
print(Solution().calculate(" 6-4 / 2 "))
print(Solution().calculate("1-(2+3)"))
print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))
print(Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
