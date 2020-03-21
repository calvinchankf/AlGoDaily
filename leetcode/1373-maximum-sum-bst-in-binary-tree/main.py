# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursion
    - lc98 + sum of a binary tree

    444 ms, faster than 52.88%
"""


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        if root == None:
            return True
        self.dfs(root)
        return self.res

    def dfs(self, node: TreeNode) -> (bool, int, int, int):
        if node == None:
            return True, -sys.maxsize, sys.maxsize, 0

        isLeftBST, left_lower, left_upper, left_total = True, node.val, -sys.maxsize, 0
        isRightBST, right_lower, right_upper, right_total = True, sys.maxsize, node.val, 0

        if node.left:
            isLeftBST, left_lower, left_upper, left_total = self.dfs(node.left)
        if node.right:
            isRightBST, right_lower, right_upper, right_total = self.dfs(
                node.right)

        if isLeftBST == False or isRightBST == False:
            return False, -sys.maxsize, sys.maxsize, 0

        if left_upper < node.val < right_lower:
            total = node.val + left_total + right_total
            self.res = max(self.res, total)
            return True, left_lower, right_upper, total

        return False, -sys.maxsize, sys.maxsize, 0
