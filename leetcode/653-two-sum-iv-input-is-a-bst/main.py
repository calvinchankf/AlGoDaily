# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    2nd approach
	1. bfs all the nodes, and put the node.val into a set
	2. if k-node.val exists in the set, return true immediately
    
	Time		O(n)
	Space		O(n) hashtable
	96 ms, faster than 47.88%
"""


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root == None:
            return False
        hs = set()
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            if k - node.val in hs:
                return True
            hs.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
