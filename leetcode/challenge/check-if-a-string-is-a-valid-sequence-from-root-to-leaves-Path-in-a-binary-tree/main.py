# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: DFS

    Time    O(N) at most
    Space   O(logN -> N) height of the tree
    140 ms
"""


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        y = ',' + ','.join([str(x) for x in arr])
        return self.dfs(root, '', y)

    def dfs(self, node: TreeNode, x: str, y: str):
        if node == None:
            return False
        x_ = x + ',' + str(node.val)
        if node.left == None and node.right == None:
            return x_ == y
        return self.dfs(node.left, x_, y) or self.dfs(node.right, x_, y)
