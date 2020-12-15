# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recusion
    - similar to lc236, 1644, 1650, 1676

    Time    O(NK) N: size of the tree, K: nummber of 'nodes'
    Space   O(N)
    284 ms, faster than 100.00%
"""


class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        if root == None:
            return None
        res = nodes[0]
        for i in range(1, len(nodes)):
            res = self.lca(root, res, nodes[i])
        return res

    def lca(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left != None and right != None:
            return root
        return left if left != None else right
