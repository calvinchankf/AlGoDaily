class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# in


def inOrderRecursive(root):
    res = []

    def inOrder(node):
        if node == None:
            return
        inOrder(node.left)
        res.append(node.val)
        inOrder(node.right)
    inOrder(root)
    return res


def inOrderIterative(root):
    res = []
    stack = []
    cur = root
    while cur != None or len(stack) > 0:
        while cur != None:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.val)
        cur = node.right
    return res

# pre


def preOrderRecursive(root):
    res = []

    def preOrder(node):
        if node == None:
            return
        res.append(node.val)
        preOrder(node.left)
        preOrder(node.right)
    preOrder(root)
    return res


def preOrderIterative(root):
    res = []
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        res.append(node.val)
        if node.right:  # stack is last-in-first-out
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

# post


def postOrderRecursive(root):
    res = []

    def postOrder(node):
        if node == None:
            return
        postOrder(node.left)
        postOrder(node.right)
        res.append(node.val)
    postOrder(root)
    return res


def postOrderIterative(root):
    res = []
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(2)
e = TreeNode(7)
f = TreeNode(12)
g = TreeNode(17)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(inOrderRecursive(a))
print(inOrderIterative(a))

print(preOrderRecursive(a))
print(preOrderIterative(a))

print(postOrderRecursive(a))
print(postOrderIterative(a))
