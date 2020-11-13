# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive dfs

    Time    O(n)
    Space   O(h)
    52 ms, faster than 73.41%
"""


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0
        cur = node.val
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res += abs(left - right)
        return cur + left + right
