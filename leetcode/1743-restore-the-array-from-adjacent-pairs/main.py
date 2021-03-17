
from collections import *

"""
    1st: brute force hashtable
    - given that all the numbers are unique, it means
        - there is at most one possibility to append a tail
        - if no more tail to append, do it on another end

    Time    O(N)
    Space   O(N)
    1604 ms, faster than 33.33%
"""


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 0:
            return []
        ht = defaultdict(set)
        for u, v in adjacentPairs:
            ht[u].add(v)
            ht[v].add(u)
        seen = set()
        start = adjacentPairs[0][0]
        forward = self.appendNext(start, ht)
        backward = self.appendNext(start, ht)
        backward.pop(0)
        return backward[::-1] + forward

    def appendNext(self, start, ht):
        arr = [start]
        while len(ht) > 0:
            tail = arr[-1]
            if tail in ht and len(ht[tail]) > 0:
                newTail = ht[tail].pop()
                arr.append(newTail)
                ht[newTail].remove(tail)
            else:
                break
        return arr
