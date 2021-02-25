"""
    1st approach:
    - add a class for StackItem
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(n)
    Space   O(n)
"""


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(StackItem(x, x))
            return
        top = self.stack[-1]
        if x < top.minVal:
            self.stack.append(StackItem(x, x))
        else:
            self.stack.append(StackItem(x,  top.minVal))

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop().val

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1].val

    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1].minVal


# for interview, OOD > tuple
class StackItem(object):
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal


"""
    2nd approach:
    - just use tuple instead of StackItem
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(n)
    Space   O(n)
"""


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) > 0 and x >= self.stack[-1][1]:
            self.stack.append([x, self.stack[-1][1]])
        else:
            self.stack.append([x, x])

    def pop(self) -> None:
        x, _ = self.stack.pop()
        return x

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
