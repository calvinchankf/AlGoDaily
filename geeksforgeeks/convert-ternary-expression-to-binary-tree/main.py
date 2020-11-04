class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convert_expression(expression):
    
    def dfs(q):
        if len(q) == 0:
            return None
        
        # the node
        cur = ''
        while len(q) > 0 and q[0] != '?' and q[0] != ':':
            cur += q.pop(0)
        
        node = TreeNode(cur)
        
        if len(q) == 0:
            return node
        
        # push to the left only if we see a ?
        sign = q.pop(0)
        if sign == '?':
            node.left = dfs(q)
            node.right = dfs(q)
        return node
    
    return dfs([c for c in expression])

def printTree(node, prefix = ''):
    if not node:
        return
    print(prefix + node.val)
    printTree(node.left, prefix+'-')
    printTree(node.right, prefix+'-')

a = 'a?b:c'
res = convert_expression(a)
printTree(res)

print('-----')

a = 'a?b?c:d:e'
res = convert_expression(a)
printTree(res)