from heapq import *

"""
    1st: heap
    - use a maxheap to deal with the memory stacks

    Time    less than O(NlogN)
    Space   O(2)
    940 ms, faster than 10.60%
"""


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        maxheap = [
            (-memory1, 1),
            (-memory2, 2)
        ]
        heapify(maxheap)
        inc = 1
        while len(maxheap) > 0:
            available = -maxheap[0][0]
            if available < inc:
                break
            available -= inc
            _, stackIdx = heappop(maxheap)
            heappush(maxheap, (-available, stackIdx))
            inc += 1

        maxheap.sort(key=lambda x: x[1])
        return [inc, -maxheap[0][0], -maxheap[1][0]]


"""
    2nd: array

    Time    less than O(N)
    Space   O(2)
    436 ms, faster than 25.00%
"""


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        inc = 1
        while max(memory1, memory2) >= inc:
            if memory1 >= memory2:
                memory1 -= inc
            else:
                memory2 -= inc
            inc += 1
        return [inc, memory1, memory2]
