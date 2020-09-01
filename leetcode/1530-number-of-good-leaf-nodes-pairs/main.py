# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: DFS + BFS
    - transform the tree to a graph
    - BFS from each node to find out the distance between nodes

    Time    O(N^2)
    Space   O(N)
    548 ms, faster than 28.71%
"""


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root == None:
            return 0
        connections = {}
        leaves = []

        def dfs(node, parent):
            arr = [parent, None, None]
            if node.left != None:
                arr[1] = node.left
                dfs(node.left, node)
            if node.right != None:
                arr[2] = node.right
                dfs(node.right, node)
            if node.left == None and node.right == None:
                leaves.append(node)
            connections[node] = arr
        dfs(root, None)

        res = 0
        for cand in leaves:
            seen = set()
            q = [(cand, 0)]
            while len(q) > 0:
                node, steps = q.pop(0)
                if node == None:
                    continue
                if node in seen:
                    continue
                seen.add(node)
                if steps > 0 and connections[node][1] == None and connections[node][2] == None:
                    res += 1
                if steps == distance:
                    continue
                for child in connections[node]:
                    q.append((child, steps + 1))

        return res//2
