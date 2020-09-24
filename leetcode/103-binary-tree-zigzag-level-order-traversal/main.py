# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        q = [root]
        level = 0
        while len(q) > 0:
            n = len(q)
            row = []
            for i in range(n):
                node = q.pop(0)
                row.append(node.val)
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
            if level % 2 == 0:
                res.append(row)
            else:
                res.append(row[::-1])
            level += 1
        return res
