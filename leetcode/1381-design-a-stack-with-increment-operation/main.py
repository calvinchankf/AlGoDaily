"""
    1st: array
    - straight-forward approach

    Time    O(k) per increment()
    Space   O(maxSize)
    124 ms, faster than 45.15%
"""


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr) == self.maxSize:
            return
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        start = max(len(self.arr) - k, 0)
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

"""
    2nd: similar logic as min stack
    - similar to lc155

    e.g.
    stack = [1,2,3,4,5], maxSize = 5

    increment(2, 100) => stack = [1, 2,   3, 4, 5]
                        incres = [0, 0, 100, 0, 5]
    increment(9, 100) => stack = [1, 2,   3, 4,   5]
                        incres = [0, 0, 100, 0, 105]

    when we pop(), we add the increment to the stack[-1]
    pop() returns 5 + 100 = 105
    the stack becomes    stack = [1, 2,   3,   4]
                        incres = [0, 0, 100, 100]

    when we pop() again, do the same thing
    pop() returns 4 + 100 = 104
    the stack becomes    stack = [1, 2,   3]
                        incres = [0, 0, 200]
    
    when we pop() again, do the same thing
    pop() returns 3 + 200 = 203
    the stack becomes    stack = [1,   2]
                        incres = [0, 200]

    ref:
    https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/542205/Python-Prefix-sum-with-1-array

    Time    O(1)
    Space   O(1)
    132 ms, faster than 59.04%
"""


class CustomStack(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append([x, 0])

    def pop(self):
        if not self.stack:
            return -1

        res, inc = self.stack.pop()
        res += inc

        if self.stack:
            self.stack[-1][1] += inc

        return res

    def increment(self, k, val):
        if self.stack:
            self.stack[min(k, len(self.stack)) - 1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
