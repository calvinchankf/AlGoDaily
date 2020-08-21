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
    3rd: tarjan, learn from others
    - an edge is a critical connection, if and only if it is not in a cycle
    - so we are discard the nodes that are not in the cycles
    - the remaining edges are our result

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
        lowlinks = n * [-1]
        res = []
        self.helper(0, -1, 0, lowlinks, connections, res)
        return res

    def helper(self, cur, parent, level, lowlinks, connections, res):

        lowlinks[cur] = level

        for child in connections[cur]:
            if child == parent:
                continue
            if lowlinks[child] == -1:
                min_step = self.helper(
                    child, cur, level+1, lowlinks, connections, res
                )
                lowlinks[cur] = min(lowlinks[cur], min_step)
            else:
                lowlinks[cur] = min(lowlinks[child], lowlinks[cur])

        if lowlinks[cur] == level and cur != 0:
            res.append([parent, cur])

        return lowlinks[cur]


"""
    4th: tarjan
    - similar to 3rd but without using recursion results

    ref:
    - https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me
    
    Time    O(N+E)
    Space   O(N)
    2108 ms, faster than 95.21%
"""


class Solution:
    def criticalConnections(self, n, connections):
        # vertex i ==> [its neighbors]
        graph = [[] for _ in range(n)]
        # here lowestSteps[i] represents the lowest order of vertex that can reach this vertex i
        lowestSteps = [i for i in range(n)]
        # common DFS/BFS method to mark whether this node is seen before
        visited = [False for _ in range(n)]

        # build graph:
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        res = []
        # we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestSteps, 0, -1, 0, visited)
        return res

    def _dfs(self, res, graph, lowestSteps, currentSteps, prevVertex, currentVertex, visited):

        visited[currentVertex] = True
        lowestSteps[currentVertex] = currentSteps

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                # do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.
                continue

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestSteps, currentSteps +
                          1, currentVertex, nextVertex, visited)
                # We avoid visiting visited nodes here instead of doing it at the beginning of DFS -
                # the reason is, even that nextVertex may be visited before, we still need to update my lowestSteps using the visited vertex's information.

            lowestSteps[currentVertex] = min(
                lowestSteps[currentVertex], lowestSteps[nextVertex])
            # take the min of the current vertex's and next vertex's ranking
            # if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
            if lowestSteps[nextVertex] >= currentSteps + 1:
                res.append([currentVertex, nextVertex])
