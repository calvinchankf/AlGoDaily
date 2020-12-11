"""
    1st: 2 arrays

    Time of every function   O(1)
    Space                    O(N)
    68 ms, faster than 76.19%
"""


class FrontMiddleBackQueue(object):

    def __init__(self):
        self.front = []
        self.back = []

    def pushFront(self, val):
        self.front.insert(0, val)
        self._balance()

    def pushMiddle(self, val):
        if len(self.front) > len(self.back):
            self._frontToBack()
        self.front.append(val)

    def pushBack(self, val):
        self.back.append(val)
        self._balance()

    def popFront(self):
        if len(self.front) == 0:
            return -1
        res = self.front.pop(0)
        self._balance()
        return res

    def popMiddle(self):
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        if len(self.front) == 1 and len(self.back) == 0:
            return self.front.pop()
        res = self.front.pop()
        self._balance()
        return res

    def popBack(self):
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        if len(self.front) == 1 and len(self.back) == 0:
            return self.front.pop()
        res = self.back.pop()
        self._balance()
        return res

    # xxx xxx OR xxxx xxx i.e. len(front) == len(back) OR len(front) == len(back) + 1
    def _balance(self):
        if len(self.front) > len(self.back) + 1:
            self._frontToBack()
        elif len(self.front) < len(self.back):
            self._backToFront()

    def _frontToBack(self):
        frontRight = self.front.pop()
        self.back.insert(0, frontRight)

    def _backToFront(self):
        backLeft = self.back.pop(0)
        self.front.append(backLeft)

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
