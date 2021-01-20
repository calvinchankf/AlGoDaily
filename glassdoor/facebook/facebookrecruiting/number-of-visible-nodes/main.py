"""
    There is a binary tree with N nodes. 
    You are viewing the tree from its left side and can see only the leftmost nodes at each level. 
    Return the number of visible nodes.
    
    Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. 
    The leftmost node at a level could be a right node.

    see ./q.png
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def visible_nodes(root):
    if root == None:
        return 0
    res = 0
    q = [(root, 1)]
    while len(q) > 0:
        node, depth = q.pop(0)
        res = max(res, depth)
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return res
