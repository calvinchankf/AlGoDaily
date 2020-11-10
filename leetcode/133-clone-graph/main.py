"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
    1st: recursive DFS
    - use the return of each recursion

    Time    O(N)
    Space   O(N)
    76 ms, faster than 86.98%
"""


class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        ht = {}

        def dfs(node):
            if node == None:
                return None
            if node in ht:
                return ht[node]
            clone = Node(node.val)
            ht[node] = clone

            for child in node.neighbors:
                clone.neighbors.append(dfs(child))
            return clone

        return dfs(root)


"""
    2nd: BFS
    - assign the neighbors in the enqueue loop, because this is where parent and neighbors present

    Time    O(N)
    Space   O(N)
    36 ms, faster than 76.55%
"""


class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        ht = {}
        ht[root] = Node(root.val, [])
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            for nb in node.neighbors:
                if nb not in ht:
                    ht[nb] = Node(nb.val, [])
                    q.append(nb)
                ht[node].neighbors.append(ht[nb])
        return ht[root]
