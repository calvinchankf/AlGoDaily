from collections import *

"""
    https://leetcode.com/discuss/interview-question/537301/Facebook-or-Phone-or-Split-profiles-into-two-groups

    There is a set of social profiles. Some of them are connected.
    Is it possible to split the set into two groups, such that there are no direct connections inside a group?
    
    input 
    [[A, B], [B, C]] 
    A-B, B-C
    output true
    because we can split them in 2 groups [A, C] and [B]

    input
    [[A, B], [B, C], [A, C]]
    A-B, B-C, A-C
    output false
"""


class Solution:
    def possibleBipartition(self, edges):
        nodes = set()
        for a, b in edges:
            nodes.add(a)
            nodes.add(b)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        cache = {}
        for node in nodes:
            if node not in cache:
                if self.bfs(graph, node, cache) == False:
                    return False
        return True

    def bfs(self, graph, start, cache):
        q = [(start, 1)]
        while len(q) > 0:
            node, color = q.pop(0)
            if node in cache:
                if cache[node] != color:
                    return False
                continue
            cache[node] = color
            for nb in graph[node]:
                q.append((nb, -color))
        return True


s = Solution()

a = [['A', 'B'], ['B', 'C']]
print(s.possibleBipartition(a))

a = [['A', 'B'], ['B', 'C'], ['A', 'C']]
print(s.possibleBipartition(a))
