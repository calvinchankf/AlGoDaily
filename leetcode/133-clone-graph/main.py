"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
    1st: DFS
    - use the return of each recursion

    Time    O(N)
    Space   O(N)
    76 ms, faster than 86.98%
"""


class Solution(object):
    def __init__(self):
        self.ht = {}

    def cloneGraph(self, node):
        if not node:
            return node
        if node in self.ht:
            return self.ht[node]
        clone = Node(node.val)
        self.ht[node] = clone

        for nb in node.neighbors:
            temp = self.cloneGraph(nb)
            clone.neighbors.append(temp)

        return clone
