"""
    In short, just transform the tree into a graph and do bfs or dfs.

    e.g.
    {
        val1 : [parent1, left1, right1],
        val2 : [parent2, left2, right2],
        ....
    }

    Time    O(N)
    Space   O(N)
    24 ms, faster than 97.55%
"""


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        connections = {}

        def dfs(node, parent):
            if node == None:
                return
            neighbours = [parent, -1, -1]
            if node.left != None:
                neighbours[1] = node.left.val
            if node.right != None:
                neighbours[2] = node.right.val
            dfs(node.left, node.val)
            dfs(node.right, node.val)
            connections[node.val] = neighbours
        dfs(root, -1)

        q = [(target.val, 0)]
        seen = set()
        res = []
        while len(q) > 0:
            node, steps = q.pop(0)
            if node in seen:
                continue
            seen.add(node)
            if node == -1:
                continue
            if steps == K:
                res.append(node)
                continue
            neighbours = connections[node]
            for nb in neighbours:
                q.append((nb, steps + 1))
        return res
