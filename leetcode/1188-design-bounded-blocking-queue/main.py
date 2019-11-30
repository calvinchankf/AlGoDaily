from threading import Semaphore
from collections import deque

""" 
    learned from others
    https://leetcode.com/problems/design-bounded-blocking-queue/discuss/380926/Python-beats-100-easy-to-understand/369575
    40 ms, faster than 27.61%
"""


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.q = deque()
        self.enSem = Semaphore(capacity)
        self.deSem = Semaphore(0)

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        # when capacity of self.enSem == 0, the function pauses here until capacity of self.enSem > 0
        self.enSem.acquire()  # adding capacity decreases as a new element is inserted
        self.q.append(element)
        self.deSem.release()  # popping capacity increases by one

    def dequeue(self):
        """
        :rtype: int
        """
        # when capacity of self.deSem == 0, the function pauses here until capacity of self.deSem > 0
        self.deSem.acquire()  # popping capacity decrease by 1
        x = self.q.popleft()
        self.enSem.release()  # adding capacity increase by 1
        return x

    def size(self):
        """
        :rtype: int
        """
        return len(self.q)
