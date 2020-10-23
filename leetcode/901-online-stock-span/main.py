"""
    1st approach: stack
    - similar to minstack
    
    e.g. [100, 80, 60, 70, 60, 75, 85]
    when next(100), stack = [100:1
    when next(80),  stack = [100:1, 80: 1
    when next(60),  stack = [100:1, 80: 1, 60: 1
    when next(70),  stack = [100:1, 80: 1, 70: 2
    when next(60),  stack = [100:1, 80: 1, 70: 2, 60: 1
    when next(75),  stack = [100:1, 80: 1, 75: 4
    when next(85),  stack = [100:1, 85: 6

    Time of next()      O(n) at worse but average O(1) because stock prices flutuate
    Space               O(n)
    440 ms, faster than 98.45%
"""


class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        count = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            x, c = self.stack.pop()
            count += c
        self.stack.append((price, count))
        return count


"""
    2nd: same approach but using a wrapper class instead of a tuple
"""


class StackItem:
    def __init__(self, val, count=1):
        self.val = val
        self.count = count


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while len(self.stack) > 0 and self.stack[-1].val <= price:
            si = self.stack.pop()
            count += si.count
        self.stack.append(StackItem(price, count))
        return count
