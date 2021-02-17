# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: bfs + math
    - do math to calculate the position of a node in the full binary tree
        left = position*2 + 0
        right = position*2 + 1
    - use bfs to traverse the btree level by level such that we can get the leftmost and the rightmost nodes' position
        diff = right pos - left pos + 1
    - if diff > res, override the result

    Time    O(n)
    Space   O(h)
    28 ms, faster than 79.22%
"""


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = 0
        # node, position
        q = [(root, 0)]
        while len(q) > 0:
            left, right = 0, 0
            n = len(q)
            for i in range(n):
                node, position = q.pop(0)

                if i == 0:
                    left = position
                if i+1 == n:
                    right = position

                if node.left != None:
                    q.append((node.left, position*2))
                if node.right != None:
                    q.append((node.right, position*2+1))
            diff = right - left + 1
            res = max(res, diff)
        return res
