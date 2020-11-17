""" 
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=270278&extra=&page=1
    also, know as baseball game
    - https://yidongzhang.gitbooks.io/-oa/content/chapter1.html
    - https://leetcode.com/problems/baseball-game

    - we need to have a stack to store the previous block that we seen along the way
    - when we see an integer, pile up the stack and the score
    - when we see a Z, we need to pop the stack
    - when we see a X, we peak the top item in the stack and add item*2 to the stack
    - when we see a +, we comput the score by adding the prevously 2 items from the stack
        here, i am not sure if the stack size will be legit along the iteration, so i just add one item if len(stack) < 2
    - the result is the sum of the stack items

    Time    O(N)
    Space   O(N)
"""


def baseballScore(scores):
    stack = []
    for i in range(len(scores)):
        score = scores[i].upper()
        if len(stack) > 0 and score == 'Z':
            pop = stack.pop()
        elif len(stack) > 0 and score == 'X':
            x = stack[-1] * 2
            stack.append(x)
        elif score == '+':
            n = len(stack)
            val = 0
            if n >= 2:
                val = stack[-2] + stack[-1]
            elif n == 1:
                val = stack[-1]
            stack.append(val)
        else:
            try:
                x = int(score)
                stack.append(x)
            except ValueError:
                continue
    return sum(stack)


# 27
print(baseballScore(["5", "-2", "4", "Z", "X", "9", "+", "+"]))
# 3
print(baseballScore(["1", "2", "+", "Z"]))
# 3
print(baseballScore(["1", "2", "+", "A", "Z"]))
