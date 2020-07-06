from collections import defaultdict
"""
    1st: bfs
    Time    O(N^M)?
    Space   O(E)
    LTE
"""


class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        connections = []
        indegrees = []
        for _ in range(n):
            indegrees.append(0)
            connections.append([])

        for preq, cur in prerequisites:
            indegrees[cur] += 1
            connections[preq].append(cur)

        q = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append((i, []))

        ht = defaultdict(list)
        while len(q) > 0:
            node, path = q.pop(0)
            ht[node] += path
            for child in connections[node]:
                q.append((child, path + [node]))

        ht2 = {}
        for key in ht:
            ht2[key] = set(ht[key])

        res = []
        for a, b in queries:
            res.append(a in ht2[b])
        return res


"""
    2nd: Floyd-Warshall
    - FW is designed to find shortest path between all nodes
    - similar to lc1334

    ref:
    - https://leetcode.com/problems/course-schedule-iv/discuss/660509/JavaPython-FloydWarshall-Algorithm-Clean-code-O(n3)

    Time    O(N^3)
    Space   O(N^2)
    2220 ms, faster than 100.00%
"""


class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        connected = [[False] * n for i in range(n)]

        for a, b in prerequisites:
            connected[a][b] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # see if middle node k can connect node i and node j
                    connected[i][j] = connected[i][j] or (
                        connected[i][k] and connected[k][j])

        res = []
        for a, b in queries:
            res.append(connected[a][b])
        return res
