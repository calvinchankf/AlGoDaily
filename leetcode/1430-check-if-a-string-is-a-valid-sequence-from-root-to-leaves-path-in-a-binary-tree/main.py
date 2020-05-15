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
    148 ms, faster than 100.00% 
"""


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        y = ',' + ','.join([str(x) for x in arr])
        return self.dfs(root, '', y)

    def dfs(self, node: TreeNode, x: str, y: str):
        if node == None:
            return False
        _x = x + ',' + str(node.val)
        if node.left == None and node.right == None:
            return _x == y
        return self.dfs(node.left, _x, y) or self.dfs(node.right, _x, y)
