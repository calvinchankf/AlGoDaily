# leetcode doesn't support golang submission for this question

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# my first intuitive attempt


class BSTIterator1(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = []
        self.unfold(root)

    def unfold(self, node):
        if node is not None:
            self.unfold(node.left)
            self.arr.append(node)
            self.unfold(node.right)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.arr) > 0

    def next(self):
        """
        :rtype: int
        """
        result = None
        if len(self.arr) > 0:
            result = self.arr[0]
            self.arr = self.arr[1:]
        return result.val


"""
    suggested solution: Iterative Inorder Traversal of BST

    Time    O(N)
    Space   O(N)
    64 ms, faster than 97.38%
"""


class BSTIterator:
    def __init__(self, root):
        self.cur = root
        self.stack = []

    def hasNext(self):
        return len(self.stack) > 0 or self.cur != None

    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        node = self.stack.pop()
        self.cur = node.right
        return node.val

#       5
#    3      6
#  2  4
# 1
# a = TreeNode(5)
# b = TreeNode(3)
# c = TreeNode(6)
# d = TreeNode(2)
# e = TreeNode(4)
# f = TreeNode(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# d.left = f


#   2
# 1
a = TreeNode(2)
b = TreeNode(1)
a.left = b

#   1
#     2
#       3
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.right = c

i, v = BSTIterator(a), []
while i.hasNext():
    v.append(i.next())

print(v)
