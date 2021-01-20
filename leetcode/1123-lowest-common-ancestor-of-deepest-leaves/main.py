# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: bfs + lowest common ancestor
    - bfs to record the nodes with maxDepth
    - find the LCA of the leftmost leaf and the rightmost leaf

    Time    O(2N)
    Space   O(N)
    44 ms, faster than 91.95%
"""


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        maxDepth = 0
        maxDepthLeaves = []
        q = [(root, 0)]
        while len(q) > 0:
            node, d = q.pop(0)
            if d > maxDepth:
                maxDepth = d
                maxDepthLeaves = [node]
            elif d == maxDepth:
                maxDepthLeaves.append(node)
            if node.left:
                q.append((node.left, d + 1))
            if node.right:
                q.append((node.right, d + 1))
        first, last = maxDepthLeaves[0], maxDepthLeaves[-1]
        return self.lca(root, first, last)

    def lca(self, node, p, q):
        if node == None or node == p or node == q:
            return node
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right
