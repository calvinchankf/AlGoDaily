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
    def countComponents(self, n, edges):
        uf = UnionFind([i for i in range(n)])
        for a, b in edges:
            uf.union(a, b)
        return uf.count
