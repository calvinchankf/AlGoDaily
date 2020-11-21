# leetcode doesn't support golang
import sys

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    my intuitive solution:
    get the paths, compare the paths
    O(p+q+min(p,q)) = O(3k) = O(n) TLE
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pPath = self.dfs(root, p, [])
        qPath = self.dfs(root, q, [])

        longer = []
        shorter = []
        minLen = 0
        if len(pPath) > len(qPath):
            longer = pPath
            shorter = qPath
            minLen = len(qPath)
        else:
            longer = qPath
            shorter = pPath
            minLen = len(pPath)

        i = 0
        while i < minLen:
            if longer[i].val != shorter[i].val:
                break
            i = i+1

        return longer[i-1]

    def dfs(self, node, target, route):
        if node is None:
            return None
        x = list(route)
        x.append(node)
        if node.val == target.val:
            return x
        return self.dfs(node.left, target, x) or self.dfs(node.right, target, x)


"""
    suggested solution:
    - similar to lc235
    - recursion ./236.png

    potential followups:
    - if u r given the values instead of nodes reference?
    - it is possible that P or/and Q are not int the tree, lc1644

    Time    O(N)
    Space   O(N)
"""


class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None:
            return root
        return left if left != None else right


#     5
#   3   6
# 2  4
# 1
a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

print("ada")
ans = Solution1().lowestCommonAncestor(a, d, e)
print("ans=", ans.val)


"""
    followup1: if u r given the values instead of nodes reference?
"""


class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left == None:
            return right
        if right == None:
            return left
        return root
