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
        maxDepth = 0
        maxDepthNodes = []
        q = [(root, 0)]
        while len(q) > 0:
            node, d = q.pop(0)

            if d > maxDepth:
                maxDepth = d
                maxDepthNodes = [node]
            elif d == maxDepth:
                maxDepthNodes.append(node)

            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))

        if len(maxDepthNodes) == 1:
            return maxDepthNodes[0]
        return self.lca(root, maxDepthNodes[0], maxDepthNodes[-1])

    def lca(self, node, a, b):
        if node == None or node == a or node == b:
            return node
        left = self.lca(node.left, a, b)
        right = self.lca(node.right, a, b)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right
