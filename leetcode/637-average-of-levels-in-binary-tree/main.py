# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: bfs

    Time    O(N)
    Space   O(N)
    52 ms, faster than 74.26%
"""


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            n = len(q)
            total = 0
            for _ in range(n):
                node = q.pop(0)
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(total/n)
        return res
