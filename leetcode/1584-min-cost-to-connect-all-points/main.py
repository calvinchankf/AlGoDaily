"""
    1st: kruskal
    1. generate all the edges
    2. sort the edges
    3. do union find

    Time    O(N^2 + NlogN)
    Space   O(N^2)
    9776 ms, faster than 100.00% ???
"""


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.roots = {}
        self.caps = {}
        for vertex in vertices:
            self.roots[vertex] = vertex
            self.caps[vertex] = 1

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
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.roots[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.roots[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


class Solution(object):
    def minCostConnectPoints(self, points):
        # generate all the edges
        edges = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append([dist, (x1, y1), (x2, y2)])
        # sort them by cost
        edges.sort(key=lambda x: x[0])
        # union find
        nodes = [(x, y) for x, y in points]
        uf = UnionFind(nodes)
        res = 0
        for cost, a, b in edges:
            rootA = uf.find(a)
            rootB = uf.find(b)
            if rootA != rootB:
                uf.union(a, b)
                res += cost
        # if the nodes are not in a same group
        if uf.count > 1:
            return []
        return res
