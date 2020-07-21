from collections import defaultdict, Counter

"""
    1st: recursive DFS + hashtable

    Time    O(N^2)
    Space   O(N)
    4348 ms, faster than 100.00%
"""


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        connections = defaultdict(list)
        for i in range(len(edges)):
            s, d = edges[i]
            connections[s].append(d)
            connections[d].append(s)
        res = n * [0]
        seen = set()
        self.dfs(0, labels[0], labels, connections, seen, res)
        return res

    def dfs(self, node, label, labels, connections, seen, res):
        if node in seen:
            return Counter()
        seen.add(node)
        counts = Counter()
        counts[label] = 1
        if node in connections:
            for c in connections[node]:
                counts += self.dfs(c, labels[c],
                                   labels, connections, seen, res)
        res[node] = counts[label]
        return counts
