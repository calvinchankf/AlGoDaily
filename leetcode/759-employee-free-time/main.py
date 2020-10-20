import heapq

"""
    1st approach: heap + merge intervals
    1. put all the intervals into a heap
    2. merge the intervals
    3. the result is exactly the time between the merged intervals

    Time    O(nlogn) n: number of intervals
    Space   O(n)
    204 ms, faster than 17.74% 
"""


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution(object):
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intvs = []
        for arr in schedule:
            for x in arr:
                intvs.append([x.start, x.end])
        if len(intvs) == 0:
            return []
        intvs.sort()
        merged = [intvs[0]]
        for i in range(1, len(intvs)):
            s, e = intvs[i]
            if s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])
        res = []
        for i in range(1, len(merged)):
            s = merged[i-1][1]
            e = merged[i][0]
            res.append(Interval(s, e))
        return res


a = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
print(Solution().employeeFreeTime(a))

a = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
print(Solution().employeeFreeTime(a))
