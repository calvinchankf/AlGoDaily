import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: bfs
	1. bfs all the nodes
    2. compare with the minVal and 2nd minVal

	Time		O(n)
	Space		O(1)
	48 ms, faster than 19.47%
"""


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        min1 = sys.maxsize
        min2 = sys.maxsize

        q = [root]
        while len(q) > 0:
            node = q.pop(0)

            if node.val < min1:
                min2 = min1
                min1 = node.val
            elif node.val > min1 and node.val < min2:
                min2 = node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if min2 == sys.maxsize:
            return -1
        return min2
