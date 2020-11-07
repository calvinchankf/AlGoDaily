class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def maxPathSum(root):
    res = -2**31
    
    def dfs(node):
        nonlocal res
        if node == None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if node.left != None and node.right != None:
            total = node.data + left + right
            res = max(res, total)
            return max(node.data + left, node.data + right)
        if node.left == None:
            return node.data + right
        return node.data + left
    
    dfs(root)
    return res

a = Node(6)
b = Node(-9)
c = Node(-10)
a.left = b
a.right = c

print(maxPathSum(a))