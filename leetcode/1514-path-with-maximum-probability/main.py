from typing import List
import heapq

"""
    1st: dijkstra

    Time    O(E + VlogV) E=number of edges. V=number of nodes
    Space   O(E+V)
    928 ms, faster than 20.00%
"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        connections = {}
        for i in range(n):
            connections[i] = []
        for i in range(len(edges)):
            src, dest = edges[i]
            prob = succProb[i]
            connections[src].append((dest, -prob))
            connections[dest].append((src, -prob))
        heap = [(1, start)]
        best = {}
        while len(heap) > 0:
            # always take in edge with the max probability
            rawProb, node = heapq.heappop(heap)
            prob = abs(rawProb)
            if node in best and prob <= best[node]:
                continue
            best[node] = prob
            if node in connections:
                candidates = connections[node]
                for _node, _prob in candidates:
                    newProb = -abs(prob*_prob)
                    heapq.heappush(heap, (newProb, _node))
        # in case the end cannot be reached
        if end in best:
            return best[end]
        return 0


s = Solution()

a = 3
b = [[0, 1], [1, 2], [0, 2]]
c = [0.5, 0.5, 0.2]
d = 0
e = 2
print(s.maxProbability(a, b, c, d, e))

a = 3
b = [[0, 1]]
c = [0.5]
d = 0
e = 2
print(s.maxProbability(a, b, c, d, e))
