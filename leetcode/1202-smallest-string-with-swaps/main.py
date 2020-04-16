from typing import List
from collections import defaultdict

"""
    1st: union find + sort
    - basically, if pairs contains [0,3], [3,5], it means that all characters at index [0, 3, 5] are swappable
    - therefor we can first union find all the groups
    - for each group of indices, sort the associated characters
        e.g. s = udyyekxy, pairs = [[2,3],[4,5],[3,6],[2,7]]
        groups are 
        {
            3: [0, 1, 3, 4, 5], 
            2: [2, 6], 
            7: [7]
        }
    - and then in each group, we sort the associated characters
        for the 1st group in above example
        
        index               = 0, 1, 3, 4, 5
        original sequence   = u, d, y, e, k
        sorted sequence     = d, e, k, u, y 
    - finally put sorted sequences in the result

    Time    O(NlogN)
    Space   O(N)
    1364 ms, faster than 8.35%
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = {}
        self.caps = {}
        for vertex in range(n):
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        # union find
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
        # extract the groups from the union find instance
        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)
        # for each group of indices, sort the associated characters
        res = [c for c in s]
        for root in groups:
            group = groups[root]
            includeds = []
            for idx in group:
                includeds.append(s[idx])
            includeds.sort()
            for idx in group:
                res[idx] = includeds.pop(0)

        return "".join(res)


s = Solution()

a = "dcab"
b = [[0, 3], [1, 2]]
print(s.smallestStringWithSwaps(a, b))

a = "dcab"
b = [[0, 3], [1, 2], [0, 2]]
print(s.smallestStringWithSwaps(a, b))

a = "cba"
b = [[0, 1], [1, 2]]
print(s.smallestStringWithSwaps(a, b))

a = "udyyek"
b = [[3, 0], [5, 1], [3, 1], [3, 4], [3, 5]]
print(s.smallestStringWithSwaps(a, b))

a = "udyyekxy"
b = [[3, 0], [5, 1], [3, 1], [3, 4], [3, 5], [2, 6]]
print(s.smallestStringWithSwaps(a, b))
