import sys
import heapq
from collections import defaultdict

"""
    1st: Dijkstra
    - for each node, find the least cost to every one of its neighbors
    - compare the count and return the result

    Time    O(E + N^2logN) -> O(E + N^3) E: initial calculation for connects. NlogN -> N^2: dijkstra
    Space   O(N^2) 2D array: for each node, the shortest distance to all other nodes
    1816 ms, faster than 7.75%
"""


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # adjacent list
        connections = defaultdict(list)
        # edge with cost { from: (to, cost), ... }
        for a, b, cost in edges:
            # undirected: a -> b, b -> a
            connections[a].append((b, cost))
            connections[b].append((a, cost))

        res = 0
        gCount = sys.maxsize
        for i in range(n):
            count = self.dijkstra(i, connections, distanceThreshold)
            if count <= gCount:
                gCount = count
                res = i
        return res

    def dijkstra(self, start, connections, distanceThreshold):
        # put (cost, node) into the heap
        heap = [(0, start)]
        best = {}
        while len(heap) > 0:
            # pop the edge with min cost
            cost, node = heapq.heappop(heap)
            # if the cost < calculated cost of the node, update the node
            if node in best and cost >= best[node]:
                continue
            best[node] = cost
            # add the adjacent nodes to the pq for processing
            if node in connections:
                candidates = connections[node]
                for can in candidates:
                    heapq.heappush(heap, (cost+can[1], can[0]))

        # count distance that < threshold
        count = 0
        for key in best:
            if best[key] <= distanceThreshold:
                count += 1
        return count


"""
    2nd: Floyd Warshall algorithm
    - similar to lc1462

    ref:
    - https://www.youtube.com/watch?v=4OQeCuLYj-4
    - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/490312/JavaC%2B%2BPython-Easy-Floyd-Algorithm
    - http://alrightchiu.github.io/SecondRound/all-pairs-shortest-pathfloyd-warshall-algorithm.html

    Time    O(N^3)
    Space   O(N^2)
    744 ms, faster than 55.72%
"""


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # construct the 2D matrix
        dis = [n * [sys.maxsize] for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        # see if node middle(k) can connect node i and node j
        # and update the cost if its smaller
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        # find the result
        res = 0
        gCount = sys.maxsize
        for i in range(n):
            count = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    count += 1
            if count <= gCount:
                gCount = count
                res = i
        return res
