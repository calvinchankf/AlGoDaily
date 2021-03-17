"""
    1st: brute force

    Time of fetch()     O(N)
    Space               O(N)
    864 ms, faster than 100.00% 
"""


from sortedcontainers import SortedList


class MRUQueue:

    def __init__(self, n: int):
        self.q = [i + 1 for i in range(n)]

    def fetch(self, k: int) -> int:
        k -= 1
        target = self.q[k]
        self.q = self.q[:k] + self.q[k+1:] + [target]
        return target


"""
    2nd: sorted list

    Time of fetch()     O(logN)
    Space               O(N)
    276 ms, faster than 100.00%
"""


class MRUQueue(object):

    def __init__(self, n):
        self.sl = SortedList()
        self.size = n
        for d in range(1, n+1):
            self.sl.add((d, d))

    def fetch(self, k):
        idx, res = self.sl.pop(k-1)
        self.sl.add((self.size+1, res))
        self.size += 1
        return res
