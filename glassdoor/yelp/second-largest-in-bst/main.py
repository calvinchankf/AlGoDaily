# leetcode doesn't support golang submission for this question

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def secondLargest(root):
    cur = root
    parent = None
    res = -(2**32)
    while cur != None:
        if cur.left != None:
            res = max(res, cur.left.val)
        if parent != None:
            res = max(res, parent.val)
        parent = cur
        cur = cur.right
    return res


#           10
#       5       15
#     1   7   12   17
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(1)
e = TreeNode(7)
f = TreeNode(12)
g = TreeNode(17)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print(secondLargest(a))

#           10
#       5       15
#     1   7   12
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(1)
e = TreeNode(7)
f = TreeNode(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
print(secondLargest(a))

#   10
# 5
a = TreeNode(10)
b = TreeNode(5)
a.left = b
print(secondLargest(a))


#       10
#   5
# 1
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(1)
a.left = b
b.left = c
print(secondLargest(a))
