# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: BFS

    Time    O(N)
    Space   O(N)
    372 ms, faster than 100.00%
"""

class Solution(object):
    def findNeartestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        q = [root]
        while len(q) > 0:
            n = len(q)
            nodes = []
            j = -1
            for i in range(n):
                head = q.pop(0)
                if head == u:
                    j = i
                nodes.append(head)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            if j > -1:
                if j+1 < len(nodes):
                    return nodes[j+1]
                else:
                    return None
        return None
        