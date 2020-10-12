class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.roots = {}
        self.caps = {}
        for vertex in vertices:
            self.roots[vertex] = vertex
            self.caps[vertex] = 1

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
            return False
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.roots[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.roots[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1
        return True


"""
    1st: union find
    - sort the edges so that we can consider the bidirectional edges first
    - union each of the edges, if an edges was established, it is an useless edge that can be removed

    Time    O(ElogE + ElogV)
    Space   O(E)
    3468 ms, faster than 100.00%
"""


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        edges.sort(reverse=True)

        nodes = [x+1 for x in range(n)]
        uf1 = UnionFind(nodes)
        uf2 = UnionFind(nodes)

        useful = 0
        for t, u, v in edges:
            if t == 1:
                a = uf1.union(u, v)
                if a:
                    useful += 1
            elif t == 2:
                b = uf2.union(u, v)
                if b:
                    useful += 1
            elif t == 3:
                a = uf1.union(u, v)
                b = uf2.union(u, v)
                if a or b:
                    useful += 1

        if uf1.count == 1 and uf2.count == 1:
            return len(edges) - useful
        return -1


s = Solution()

a = 4
b = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
print(s.maxNumEdgesToRemove(a, b))

a = 4
b = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
print(s.maxNumEdgesToRemove(a, b))

a = 4
b = [[3, 2, 3], [1, 1, 2], [2, 3, 4]]
print(s.maxNumEdgesToRemove(a, b))

a = 2
b = [[1, 1, 2], [2, 1, 2], [3, 1, 2]]
print(s.maxNumEdgesToRemove(a, b))
