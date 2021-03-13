
from sortedcontainers import SortedList

"""
    1st: SortedList/binary search
    - put left and right of every building into a list of events
    - iterate from left to right
    - maintain a fenwick tree(log(N) mutable maxheap) to record to 'silhouette' of the buildings
    
    2 cases to consider:
    - if there are more than one building have the same left, consider taller one first
    - if there are more than one building have the same right, consider shorter one first

    ref:
    - https://www.youtube.com/watch?v=8Kd-Tn_Rz7s&ab_channel=HuaHua

    Time    O(NlogN) -> O(N^2) sortedList uses insert(k, item) which is written in C, so it's faster
    Space   O(N)
    144 ms, faster than 44.39%
"""


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, height, 'left'))
            events.append((right, -height, 'right'))  # case2
        events.sort(key=lambda x: (x[0], x[2], -x[1]))  # case1
        sl = SortedList()
        sl.add(0)
        res = []
        for x, h, t in events:
            if t == 'left':
                if len(sl) == 0 or h > sl[-1]:
                    res.append((x, h))
                sl.add(h)
            else:
                sl.remove(-h)
                if -h > sl[-1]:
                    res.append((x, sl[-1]))
        return res
