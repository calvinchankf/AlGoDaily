from collections import defaultdict

"""
    1st: brute force + union find
    - for every edege, union find all the remaining edges to see if nodes are all connected

    Time    O(EElogN)
    Space   O(N)
    TLE
    8 / 12 test cases passed.
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = {}
        self.caps = {}
        for i in range(n):
            self.ids[i] = i
            self.caps[i] = 1

    def getCount(self):
        return self.count

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


class Solution(object):
    def criticalConnections(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        res = []
        for i in range(len(edges)):
            uf = UnionFind(n)
            for j in range(len(edges)):
                if i == j:
                    continue
                uf.union(edges[j][0], edges[j][1])
            if uf.count > 1:
                res.append(edges[i])
        return res


"""
    2nd: brute force + BFS
    - for every edege, BFS all the remaining edges to see if nodes are all connected

    Time    O(EN)
    Space   O(N)
    TLE
    8 / 12 test cases passed.
"""


class Solution(object):
    def criticalConnections(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        res = []
        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]
            hs = set()
            q = [0]
            while len(q) > 0:
                node = q.pop(0)
                if node in hs:
                    continue
                hs.add(node)
                for neighbor in connections[node]:
                    if (node == a and neighbor == b) or (neighbor == a and node == b):
                        continue
                    q.append(neighbor)
            if len(hs) < n:
                res.append([a, b])
        return res


"""
    3rd: DFS, learn from others
    - an edge is a critical connection, if and only if it is not in a cycle
    - so we are gonna find all in cycles, the remaining edges must be critical

    ref:
    - https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/No-TarjanDFS-detailed-explanation-O(orEor)-solution-(I-like-this-question)
    - https://www.youtube.com/watch?v=mKUsbABiwBI

    Time    O(N+E)
    Space   O(N)
    2240 ms, faster than 51.02%
"""


class Solution(object):
    def criticalConnections(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        steps = n * [-1]
        res = []
        self.helper(0, -1, 0, steps, connections, res)
        return res

    def helper(self, cur, parent, level, steps, connections, res):

        steps[cur] = level

        for child in connections[cur]:
            if child == parent:
                continue
            if steps[child] == -1:
                min_step = self.helper(
                    child, cur, level+1, steps, connections, res)
                steps[cur] = min(steps[cur], min_step)
            else:
                steps[cur] = min(steps[child], steps[cur])

        if steps[cur] == level and cur != 0:
            res.append([parent, cur])

        return steps[cur]
