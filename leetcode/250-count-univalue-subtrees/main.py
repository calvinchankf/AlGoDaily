# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: bottom up recusrion
	- return the value of the node if it is a univalue subtree

    Time    O(N)
    Space   O(N)
    40 ms, faster than 24.46%
"""


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        self.countUni(root)
        return self.res

    def countUni(self, node):
        if node == None:
            return set()
        seen = set()
        seen.add(node.val)
        seen |= self.countUni(node.left)
        seen |= self.countUni(node.right)
        if len(seen) == 1:
            self.res += 1
        return seen
