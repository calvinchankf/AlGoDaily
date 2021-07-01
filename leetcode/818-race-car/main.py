# from heapq import *
from collections import deque

"""
    1st: optimized BFS + hashtable
    - instead of using an array, we use a deque. So the time complexity of dequeue() takes O(1)

    Time    O(2^N)
    Space   O(N)
    4468 ms, faster than 5.55%
"""


class Solution(object):
    def racecar(self, target):
        cache = set()
        q = deque()
        q.append((0, 1, 0))  # (position, speed, steps)
        while len(q) > 0:
            position, speed, steps = q.popleft()
            if position == target:
                return steps

            key = (position, speed)
            if key in cache:
                continue
            cache.add(key)

            q.append((position+speed, speed*2, steps + 1))
            if speed > 0:
                q.append((position, -1, steps + 1))
            else:
                q.append((position, 1, steps + 1))
        return -1
