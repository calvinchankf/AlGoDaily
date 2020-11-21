# leetcode doesnt support golang submissions


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1nd approach: iterative bst dfs

    idea: common anestor of 2 nodes must inclusively lies between left and right
    left <= anestor <= right
    e.g. 3 < 4 < 5

    Time    O(logn)
    Time    O(logn) height of the bst
    68 ms, faster than 99.7%
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = root
        while cur != None:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        return cur


"""
    2nd approach: recursive bst dfs
    - similar to lc236, 1644

    idea: common anestor of 2 nodes must inclusively lies between left and right
    left <= anestor <= right
    e.g. 3 < 4 < 5

    Time    O(logn)
    Time    O(logn) height of the bst
    72 ms, faster than 68.62%
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
