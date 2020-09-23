# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: dfs all the nodes, and sum sup the values within the ranges

    Time    O(n)
    Space   O(h)
    296 ms, faster than 59.63%
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root, L, R):
        self.dfs(root, L, R)
        return self.res

    def dfs(self, node, L, R):
        if node == None:
            return
        if L <= node.val and node.val <= R:
            self.res += node.val
        self.dfs(node.left, L, R)
        self.dfs(node.right, L, R)


#       10
#    5      15
#  3  7        18
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(3)
e = TreeNode(7)
f = TreeNode(18)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(Solution().rangeSumBST(a, 7, 15))

#       10
#    5      15
#  3  7  13   18
# 1  6
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(3)
e = TreeNode(7)
f = TreeNode(13)
g = TreeNode(18)
h = TreeNode(1)
i = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
d.right = i
print(Solution().rangeSumBST(a, 6, 10))
