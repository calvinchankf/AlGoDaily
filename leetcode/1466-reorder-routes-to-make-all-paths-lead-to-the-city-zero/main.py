from collections import defaultdict

"""
    1st: bfs
    - create an undirect graph
    - from a graph G from node 0 with bfs
    - see if the routes in G are in the original connections

    Time    O(E+V)
    Space   O(2E)
    1992 ms, faster than 100.00%
"""


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        hs = set()
        graph = defaultdict(list)
        for a, b in connections:
            hs.add((a, b))
            graph[a].append(b)
            graph[b].append(a)

        q = []
        for dest in graph[0]:
            q.append((0, dest))

        seen = set([0])
        pathsToZero = set()

        while len(q) > 0:
            source, dest = q.pop(0)
            if dest in seen:
                continue
            seen.add(dest)
            pathsToZero.add((dest, source))
            for child in graph[dest]:
                q.append((dest, child))

        res = 0
        for src, dest in pathsToZero:
            if (src, dest) not in hs:
                res += 1
        return res
