# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st: recursion
    - reuse lc701: Insert into a Binary Search Tree
    - for each element in the array
    - do lc701

    Time    from O(N) to O(NlogN), because the number of nodes of result tree < N during the construction of it
    Space   O(N)
    12 ms, faster than 99.45%
"""


class Solution(object):
    def bstFromPreorder(self, preorder):
        res = None
        for x in preorder:
            res = self.insertIntoBST(res, x)
        return res

    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


"""
    2nd: same concept but with iteration
    - reuse lc701: Insert into a Binary Search Tree
    - for each element in the array
    - do lc701

    Time    from O(N) to O(NlogN), because the number of nodes of result tree < N during the construction of it
    Space   O(N)
    20 ms, faster than 84.85%
"""


class Solution(object):
    def bstFromPreorder(self, preorder):
        res = None
        for x in preorder:
            res = self.insertIntoBST(res, x)
        return res

    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val)
        cur = root
        while True:
            if cur.val < val:
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
            else:
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
        return root
