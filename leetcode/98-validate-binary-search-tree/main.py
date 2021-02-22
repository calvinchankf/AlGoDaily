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
    
    Time 	O(N)
    Space	O(N)
    32 ms, faster than 99.46%
"""


class Solution(object):
    def isValidBST(self, root):
        return self.isValid(root, -sys.maxsize, sys.maxsize)

    def isValid(self, node, lower, upper):
        if node == None:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        if self.isValid(node.left, lower, node.val) == False:
            return False
        return self.isValid(node.right, node.val, upper)


"""
    2nd approach: stack based dfs
    - compare the node.val with min & max in each iteration

    Time 	O(n)
    Space	O(h)
     44 ms, faster than 67.43%
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
