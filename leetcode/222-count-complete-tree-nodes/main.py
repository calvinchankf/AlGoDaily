# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    2nd approach
	- actually we dont need to go though all the nodes
	- we can just search for the node which the left and right have different heights
        - if no diff, the subtree has 2^n-1 nodes
        - if has diff, go into its children and count the number of nodes again

    Time    O(logn * logn) because it is almost balenced
    Space   O(h)
    80 ms, faster than 80.30%
    24apr2019
"""


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = 1 + self.countLeftMost(root.left)
        right = 1 + self.countRightMost(root.right)
        if left == right:
            # if left == right, it means that this subtree is a perfect tree
            # therefore the number of nodes = 2^n-1
            return 2**left-1
        # if unfortunately left != right, we need to traverse down its children and count
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countLeftMost(self, node):
        if node == None:
            return 0
        count = 0
        cur = node
        while cur != None:
            count += 1
            cur = cur.left
        return count

    def countRightMost(self, node):
        if node == None:
            return 0
        count = 0
        cur = node
        while cur != None:
            count += 1
            cur = cur.right
        return count
