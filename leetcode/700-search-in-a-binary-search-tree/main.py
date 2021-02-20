# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        1st approach: iterative bst traversal

        Time    O(height)
        Space   O(height)
        72 ms, faster than 56.73%
        """
        cur = root
        while cur != None:
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
            else:
                return cur
        return cur


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        2nd approach: recursive bst traversal

        Time    O(height)
        Space   O(height)
        72 ms, faster than 56.73%
        """
        if root == None:
            return None

        if root.val < val:
            right = self.searchBST(root.right, val)
            if right != None:
                return right
        elif root.val > val:
            left = self.searchBST(root.left, val)
            if left != None:
                return left
         elif root.val == val:
            return root
        return None
