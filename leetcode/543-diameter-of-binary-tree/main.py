# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: dfs in recursion
    - for each node, compare the depths of left and right subtree
    - and compare and assign the result
    - in each node, just return the max depth of either left or right subtree 

    Time  O(n)
    Space O(h)
    48 ms, faster than 40.03% 
"""


class Solution(object):

    def diameterOfBinaryTree(self, root):
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node == None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.result = max(self.result, left + right)
        return max(left, right) + 1
