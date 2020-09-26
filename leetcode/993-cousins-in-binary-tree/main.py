# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: BFS + hashtable
    - BFS the tree level by level
    - use a hashtable to store [parent, currentnode]
    - after we have done the iterating one level, check if the x, y are on the same level and have diff parents

    Time    O(n)
    Space   O(n)
    12ms beats 100%
"""


class Solution(object):
    def isCousins(self, root, x, y):
        if root == None:
            return False
        xParent = -1
        xDepth = -1
        yParent = -1
        yDepth = -1
        q = [(root, None, 0)]
        while len(q) > 0:
            node, parent, depth = q.pop(0)
            if node.val == x:
                xParent = parent
                xDepth = depth
            if node.val == y:
                yParent = parent
                yDepth = depth
            if node.left:
                q.append([node.left, node, depth + 1])
            if node.right:
                q.append([node.right, node, depth + 1])
        return xDepth == yDepth and xParent != yParent
