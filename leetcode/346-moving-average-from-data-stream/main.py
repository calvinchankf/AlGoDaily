"""
    1st approach: sliding window

    Time    O(1) next()
    Space   O(k) k: size since we need to store the sliding window
    68 ms, faster than 73.33%
"""


class MovingAverage(object):

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.total = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.total += val
        if len(self.window) > self.size:
            left = self.window.pop(0)
            self.total -= left
        return self.total / len(self.window)
