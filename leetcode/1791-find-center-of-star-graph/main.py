from collections import *
"""
    1st: graph
    - calculate the number of neighbours for every node(indegree/outdegree)

    Time    O(N)
    Space   O(N)
    892 ms, faster than 100.00%
"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        res = 1
        for key in neighbours:
            if len(neighbours[key]) > len(neighbours[res]):
                res = key
        return res
