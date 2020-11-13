# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: recursion
    - in each recursive function
        1. return the min and max node.val from the subtree
        2. compare the current node.val with the min and max which are from the return of subtrees

    Time    O(n)
    Space   O(h) h: height of the binary tree, worst case is O(n)
    36 ms, faster than 58.02%
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, None)
        return self.res

    def dfs(self, node, parentVal):
        if node == None:
            return (parentVal, parentVal)

        leftMin, leftMax = self.dfs(node.left, node.val)
        rightMin, rightMax = self.dfs(node.right, node.val)
        curMin = min(leftMin, rightMin)
        curMax = max(leftMax, rightMax)
        a = abs(curMin - node.val)
        b = abs(curMax - node.val)
        self.res = max(self.res, a, b)
        return min(node.val, curMin), max(node.val, curMax)
