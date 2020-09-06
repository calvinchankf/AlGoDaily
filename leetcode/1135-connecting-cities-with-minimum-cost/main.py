import heapq
from collections import defaultdict
"""
    1st: minimum spanning tree (kruskal: union find + sort)

    Time		O(E log E) + O(V log V) <= sort the edges + union find
	Space		O(V) edges in union find
  	E: number of edges, V: number of vertices

    660 ms, faster than 42.53%
"""


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(N)
        connections = sorted(connections, key=lambda x: x[2])
        res = 0
        for a, b, c in connections:
            rootA = uf.find(a)
            rootB = uf.find(b)
            if rootA != rootB:
                uf.union(a, b)
                res += c
        if uf.count > 1:
            return -1
        return res


class UnionFind(object):
    def __init__(self, N):
        self.count = N
        self.roots = {}
        self.caps = {}
        for i in range(1, N+1):
            self.roots[i] = i
            self.caps[i] = 1

    def getCount(self):
        return self.count

    def find(self, key):
        # loop to find to ultimate root
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


"""
    2nd: minimum spanning tree (prim)

    ref:
	- https://www.youtube.com/watch?v=YyLaRffCdk4

	Time	O(E log V) E: number of edges, V: number of vertices
	Space	O(E + V) hashtable + heap
    744 ms, faster than 60.81%
"""


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        G = defaultdict(list)
        for a, b, cost in connections:
            G[a].append((cost, b))
            G[b].append((cost, a))

        queue = [(0, N)]  # [1] Arbitrary starting point: (cost, point)
        visited = set()
        total = 0
        # [3] Exit if all cities are visited.
        while len(queue) > 0 and len(visited) < N:
            # cost is always least cost connection in queue.
            cost, node = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                total += cost  # [2] Grow tree by one edge.
                for edge_cost, next_node in G[node]:
                    heapq.heappush(queue, (edge_cost, next_node))
        return total if len(visited) == N else -1
