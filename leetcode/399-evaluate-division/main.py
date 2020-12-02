from typing import List
from collections import *


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        1st: union find

        consider

        case 1, all in the same set:
        a/b=2, b/c=3
        we can compute any combinations of the a,b,c 

        case 2, different sets:
        a/b=2, c/d=3
        we can compute any combinations of the a,b and any combinations of the c/d

        case 3, they are in different sets initially, but they combine afterwards
        a/b=2, c/d=3, a/c=4
        first compute a,b, compute c,d
        then for the symbols in set(a,b), mutiply them to a correct scale as set(c,d)

        Time    O(E*N*logN) E: equations, N: nodes
        Space   O(2N) nodes in union find
        20 ms, faster than 70.51%
        """
        # init unionfind
        nodeSet = set()
        for i in range(len(equations)):
            a, b = equations[i]
            nodeSet.add(a)
            nodeSet.add(b)
        nodes = list(nodeSet)
        uf = UnionFind(nodes)
        # equations
        ht = {}
        for i in range(len(equations)):
            a, b = equations[i]

            # if they are seen and they are not in the same set
            # multiply all the values in A and values[i] so that set A and set B will be with a same ratio
            # e.g. a/b=2, c/d=4, b/c=3
            # a     b   c   d
            # 2     1   4   1
            # ---------------- then we see b/c=3, mutliply a, b with values[i]*ht[b] = 3 * 4 = 12
            # 24    12  4   1
            rootA = uf.find(a)
            rootB = uf.find(b)
            if a in ht and b in ht and rootA != rootB:
                for node in nodes:
                    if uf.find(node) == rootA:
                        ht[node] *= values[i]*ht[b]
            else:
                if a not in ht and b not in ht:
                    ht[a] = values[i]
                    ht[b] = 1.0
                elif a not in ht:
                    ht[a] = values[i] * ht[b]
                elif b not in ht:
                    ht[b] = ht[a] / values[i]
            uf.union(a, b)
        # compute result
        res = []
        for q in queries:
            a, b = q
            rootA = uf.find(a)
            rootB = uf.find(b)
            if rootA == rootB and rootA != None:
                res.append(ht[a]/ht[b])
            else:
                res.append(-1.0)
        return res


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        # loop to find to ultimate root
        if key not in self.ids:
            return None
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        if p not in self.ids or q not in self.ids:
            return

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


s = Solution()

# normal
a = [["a", "b"], ["b", "c"]]
b = [2.0, 3.0]
c = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(s.calcEquation(a, b, c))

# very important test case: combine sets after we saved
a = [["a", "b"], ["e", "f"], ["b", "e"]]
b = [3.4, 1.4, 2.3]
c = [["b", "a"], ["a", "f"], ["f", "f"], [
    "e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
print(s.calcEquation(a, b, c))

print("-----")


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            2nd: BFS

            e.g. a/b = 2, b/c = 3
            means
            a -> b = 2
            b -> c = 3
            so, a -> b -> c = 2 * 3 = 6
            therefore, 
            we can start BFS from 1.0,
            after BFS, ratio = 1.0 * graph[a][b] * graph[b][c] = 1 * 2 * 3 = 6

            Time    O(N^2)
            Space   O(N^2)
            32 ms, faster than 52.91% 
        """
        n = len(equations)
        graph = defaultdict(dict)
        for i in range(n):
            a, b = equations[i]
            ratio = values[i]
            graph[a][b] = ratio         # from A to B = ratio
            graph[b][a] = 1.0/ratio     # from B to A = 1/ratio

        def bfs(s, e):
            if s not in graph and e not in graph:
                return -1
            q = [(s, 1.0)]
            seen = set()
            while len(q) > 0:
                node, ratio = q.pop(0)
                if node == e:
                    return ratio
                if node in seen:
                    continue
                seen.add(node)
                for neighbor in graph[node]:
                    q.append((neighbor, ratio * graph[node][neighbor]))
            return -1

        res = []
        for s, e in queries:
            res.append(bfs(s, e))
        return res


s = Solution()

# normal
a = [["a", "b"], ["b", "c"]]
b = [2.0, 3.0]
c = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(s.calcEquation(a, b, c))

# very important test case: combine sets after we saved
a = [["a", "b"], ["e", "f"], ["b", "e"]]
b = [3.4, 1.4, 2.3]
c = [["b", "a"], ["a", "f"], ["f", "f"], [
    "e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
print(s.calcEquation(a, b, c))
