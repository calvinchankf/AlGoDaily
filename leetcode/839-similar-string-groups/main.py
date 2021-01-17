"""
    1st: swap check + Union Find

    1. first build the swappable pairs from all (i,j), i.e. tars, rats <- only the characters at index0 and index2 are different
    2. Union Find(with Weighted quick-union with path compression) to group all of them

    Time    O(N^2L + NlogM) L: length of the string, N: number of strings, M: number of unions, it can be as big as N at worst case
    Space   O(N)
    2560 ms, faster than 74.73% 
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
    def numSimilarGroups(self, A: List[str]) -> int:
        n = len(A)
        pairs = []
        for i in range(n):
            for j in range(i+1, n):
                if A[i] == A[j] or self.isSwapable(A[i], A[j]):
                    pairs.append((i, j))
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
        return uf.count

    def isSwapable(self, s, t):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count == 2


"""
    2nd: swap check + BFS

    Time    O(N^2L + N) L: length of the string, N: number of strings
    Space   O(N)
    2936 ms, faster than 42.19%
"""


class Solution(object):
    def numSimilarGroups(self, A):
        n = len(A)

        graph = {}
        for i in range(n):
            graph[i] = []

        for i in range(n):
            for j in range(i+1, n):
                if A[i] == A[j] or self.isSwapable(A[i], A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        res = 0
        seen = set()
        for i in graph:
            if i in seen:
                continue
            q = [i]
            while len(q) > 0:
                node = q.pop(0)
                if node in seen:
                    continue
                seen.add(node)
                for nb in graph[node]:
                    q.append(nb)
            res += 1
        return res

    def isSwapable(self, s, t):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count == 2
