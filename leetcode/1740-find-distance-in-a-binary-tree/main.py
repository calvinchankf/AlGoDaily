
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: LCA + DFS

    Time    O(N)
    Space   O(H)
    120 ms, faster than 100.00%
"""


class Solution(object):
    def findDistance(self, root, p, q):
        ancestor = self.lca(root, p, q)
        a = self.getDistance(ancestor, p)
        b = self.getDistance(ancestor, q)
        return a + b

    def lca(self, node, p, q):
        if node == None or node.val == p or node.val == q:
            return node
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right

    def getDistance(self, node, target):
        if node == None:
            return -1
        if node.val == target:
            return 0
        left = self.getDistance(node.left, target)
        right = self.getDistance(node.right, target)
        if left != -1:
            return left + 1
        if right != -1:
            return right + 1
        return -1


"""
    2nd: LCA + BFS

    Time    O(N)
    Space   O(H)
    84 ms, faster than 100.00%
"""


class Solution(object):
    def findDistance(self, root, p, q):
        ancestor = self.lca(root, p, q)
        a = self.getDistance(ancestor, p)
        b = self.getDistance(ancestor, q)
        return a + b

    def lca(self, node, p, q):
        if node == None or node.val == p or node.val == q:
            return node
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right

    def getDistance(self, root, target):
        q = [(root, 0)]
        while len(q) > 0:
            node, depth = q.pop(0)
            if node.val == target:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return -1
