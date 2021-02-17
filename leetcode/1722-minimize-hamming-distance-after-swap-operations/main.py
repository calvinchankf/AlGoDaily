
from collections import *

"""
    1st: union find
    - consider 'ABCD', if [0,1],[1,2] can be swapped, it means [0,2] can be swapped too
    - therefore we can just put all the swap-able indices in a same group
    - then compare (the values in source) and (the valus in target) for every group

    Time    O(NlogN) -> O(N) UnionFind with compression takes O(logN) to find a root on average
    Space   O(N)
    1612 ms, faster than 73.12%
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.roots = {}
        self.caps = {}
        for i in range(n):
            self.roots[i] = i
            self.caps[i] = 1

    def find(self, key):
        cur = key
        while cur != self.roots[cur]:
            cur = self.roots[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.caps[pId] < self.caps[qId]:
            self.roots[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.roots[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        # union find
        uf = UnionFind(n)
        for i, j in allowedSwaps:
            uf.union(i, j)
        # group the indices
        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)
        # calculate the diff for every group
        res = 0
        for root in groups:
            indices = groups[root]
            A = Counter()
            for i in indices:
                a = source[i]
                A[a] += 1
            for i in indices:
                b = target[i]
                A[b] -= 1
            diff = 0
            for key in A:
                diff += abs(A[key])
            res += diff // 2
        return res
