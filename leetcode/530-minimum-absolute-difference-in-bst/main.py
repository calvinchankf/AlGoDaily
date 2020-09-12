# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    3rd: dfs with ranges

    Time    O(N)
    Space   O(H)
     84 ms, faster than 27.50%
"""


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = sys.maxsize
        self.dfs(root, -sys.maxsize, sys.maxsize)
        return self.res

    def dfs(self, node, minVal, maxVal):
        if node == None:
            return
        self.res = min(self.res, abs(node.val - minVal),
                       abs(node.val - maxVal))
        self.dfs(node.left, minVal, node.val)
        self.dfs(node.right, node.val, maxVal)
