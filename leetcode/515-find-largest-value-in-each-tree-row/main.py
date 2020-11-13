# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: BFS, level order traversal

    Time    O(N)
    Space   O(N)
    48ms beats 65.52%
"""

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            n = len(q)
            maxNum = -(2**31)
            for _ in range(n):
                node = q.pop(0)
                maxNum = max(maxNum, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxNum)
        return res