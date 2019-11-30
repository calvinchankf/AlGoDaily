import threading
import collections

"""
    in python3
    
    learned from others
    https://leetcode.com/problems/design-bounded-blocking-queue/discuss/380926/Python-beats-100-easy-to-understand/369575
"""


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = collections.deque()
        self.add_cap = threading.Semaphore(capacity)
        self.pop_cap = threading.Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.add_cap.acquire()  # insertion/adding capacity decreases as a new element is inserted
        self.pop_cap.release()  # popping capacity increases by one
        self.q.append(element)

    def dequeue(self) -> int:
        self.pop_cap.acquire()  # pop capacity decreases
        self.add_cap.release()  # adding capacity increases
        return self.q.popleft()

    def size(self) -> int:
        return len(self.q)
