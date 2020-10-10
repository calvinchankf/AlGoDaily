import sys

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach
    - compare the node.val with min & max in each recursion
    
    Time 	O(n)
    Space	O(h)
    52ms beats 19.48%
    23apr2019
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -sys.maxsize, sys.maxsize)

    def helper(self, node, left, right):
        if node == None:
            return True
        if node.val <= left or node.val >= right:
            return False
        a = self.helper(node.left, left, node.val)
        b = self.helper(node.right, node.val, right)
        return a and b


"""
    2nd approach: stack based dfs
    - compare the node.val with min & max in each iteration

    Time 	O(n)
    Space	O(h)
    44 ms, faster than 30.58%
    3july2019
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        stack = []
        stack.append((root, -sys.maxsize, sys.maxsize))
        while len(stack) > 0:
            node, left, right = stack.pop()
            if node.val <= left or node.val >= right:
                return False
            if node.left != None:
                stack.append((node.left, left, node.val))
            if node.right != None:
                stack.append((node.right, node.val, right))
        return True


"""
    followup: find out the incorrect node
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -sys.maxsize, sys.maxsize)

    def helper(self, node, left, right):
        if node == None:
            return None
        if node.val <= left or node.val >= right:
            return node
        a = self.helper(node.left, left, node.val)
        b = self.helper(node.right, node.val, right)
        # we should return a node if there is one
        return a or b