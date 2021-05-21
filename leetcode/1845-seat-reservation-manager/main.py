
from heapq import *

"""
    1st: heap

    Time of init()          O(N)
    Time of reserve()       O(NlogN)
    Time of unreserve()     O(NlogN)
    Space   O(N)
    544 ms, faster than 100.00%
"""


class SeatManager:

    def __init__(self, n: int):
        self.minheap = [i + 1 for i in range(n)]

    def reserve(self) -> int:
        minNum = heappop(self.minheap)
        return minNum

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.minheap, seatNumber)
