"""
    1st: bfs?
    - check the indgree of each node

    Time    O(N)
    Space   O(N)
    228 ms, faster than 100.00%
"""


class Solution:
    def findRoot(self, nodes: List['Node']) -> 'Node':
        ht = {}
        for node in nodes:
            if node not in ht:
                ht[node] = 0
            for child in node.children:
                if child in ht:
                    ht[child] += 1
                else:
                    ht[child] = 1

        for key in ht:
            if ht[key] == 0:
                return key
        return None
