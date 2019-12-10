from collections import defaultdict


"""
    1st: brute-force BFS
    LTE
"""


class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        nodeSet = set()
        connections = defaultdict(list)
        for a, b in edges:
            nodeSet.add(a)
            nodeSet.add(b)
            connections[a].append(b)
            connections[b].append(a)
        res = 0
        for node in nodeSet:
            seen = set()
            q = [(node, 0)]
            while len(q) > 0:
                head, steps = q.pop(0)
                if head in seen:
                    continue
                seen.add(head)
                res = max(res, steps)
                for child in connections[head]:
                    q.append((child, steps + 1))
        return res


"""
    2nd: recursion
    - similar to lc543
    - there are 3 things we need to know to consider
        1. 0 <= edges[i][j] <= edges.length
        2. no cycle
        3. all nodes are connected
    - they mean that, for pair of nodes, e.g. from A to B, they are connected, there is only one way
    - so for every node, if we can find out the 2 deepest paths from its children, this will be a potential answer

    Time    O(N)
    Space   O(N) recursion tree call stack
    152 ms, faster than 95.83%
"""


class Solution(object):

    def __init__(self):
        self.res = 0
        self.connections = defaultdict(list)

    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        for a, b in edges:
            self.connections[a].append(b)
            self.connections[b].append(a)
        self.dfs(0, None)
        return self.res

    def dfs(self, node, prev):
        d1, d2 = 0, 0
        for child in self.connections[node]:
            if child == prev:
                continue
            d = self.dfs(child, node)
            if d > d1:
                d2 = d1
                d1 = d
            elif d > d2:
                d2 = d
        self.res = max(self.res, d1 + d2)
        return d1 + 1
