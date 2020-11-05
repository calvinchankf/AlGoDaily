# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursion
    - similar to lc235, 236
    1. use LCA
    2. check if both p and q are in the result LCA

    Time    O(3N)
    Space   O(N)
    360 ms, faster than 100.00%
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        temp = self.lca(root, p, q)
        left = self.hasNode(temp, p)
        right = self.hasNode(temp, q)
        if left and right:
            return temp
        return None

    def lca(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left != None and right != None:
            return root
        if left != None:
            return left
        return right

    def hasNode(self, root, target):
        if root == None:
            return False
        if root == target:
            return True
        return self.hasNode(root.left, target) or self.hasNode(root.right, target)
