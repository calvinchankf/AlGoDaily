"""
    ref:
    - https://algs4.cs.princeton.edu/15uf/
"""


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.roots = {}
        self.caps = {}
        for vertex in vertices:
            self.roots[vertex] = vertex
            self.caps[vertex] = 1

    def getCount(self):
        return self.count

    def find(self, key):
        # loop to find to the ultimate root
        if key not in self.roots:
            return None
        cur = key
        while cur != self.roots[cur]:
            cur = self.roots[cur]
        return cur

    def union(self, p, q):
        if p not in self.roots or q not in self.roots:
            return
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

    def isConnect(self, p, q):
        if p not in self.roots or q not in self.roots:
            return None
        return self.find(p) == self.find(q)


nodes = ['a', 'b', 'c', 'd', 'e']
uf = UnionFind(nodes)

uf.union('a', 'b')
uf.union('c', 'd')
uf.union('d', 'e')

ht = {}
for node in nodes:
    root = uf.find(node)
    if root in ht:
        ht[root].append(node)
    else:
        ht[root] = [node]

print(ht)

largestGroup = []
for key in ht:
    if len(ht[key]) > len(largestGroup):
        largestGroup = ht[key]
print(largestGroup)
