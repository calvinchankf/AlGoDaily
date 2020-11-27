# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    1st: recursion

    Time    O(N)
    Space   O(N)
"""


class Solution:

    def __init__(self):
        self.hs = set()

    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        self.hs.add(root)
        if root.right:
            if root.right in self.hs:
                return None
        root.right = self.correctBinaryTree(root.right)
        root.left = self.correctBinaryTree(root.left)
        return root
