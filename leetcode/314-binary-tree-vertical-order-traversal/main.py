# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach
    1. find the width of the binary tree by dfs
    2. bfs the tree with a corresponding 'diff'
    3. put the node.val into a right subarray of result corresponding to the 'diff'

    Time    O(n)
    Space   O(h+n) the height of tree(recursion) + the result
    24ms beats 100%
"""


class Solution(object):

    def __init__(self):
        self.max = 0
        self.min = 0

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.findWidth(root, 0)
        n = self.max-self.min+1

        res = []
        for i in range(n):
            res.append([])

        q = [(root, 0)]
        while len(q) > 0:
            node, col = q.pop(0)
            res[col-self.min].append(node.val)
            if node.left != None:
                q.append((node.left, col-1))
            if node.right != None:
                q.append((node.right, col+1))

        return res

    def findWidth(self, node, at):
        if node == None:
            return
        self.min = min(self.min, at)
        self.max = max(self.max, at)
        self.findWidth(node.left, at-1)
        self.findWidth(node.right, at+1)


#      1
#    2   3
#  5  6    7
#      8
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
a.left = b
a.right = c
b.left = e
b.right = f
c.right = g
f.right = h
print(Solution().verticalOrder(a))

print(Solution().verticalOrder(None))

"""
    2nd approach: dfs + hashtable
    - dfs through the tree with incrementing row and incrementing/decrementing col
    - put the node to the corresponding col in a hashtable
    - iterating the hastable to get the nodes in vertical traversal order
    - and sort the nodes by row count

    Time    O(N + C RlogR) N: number of nodes, R: row, C: column
    Space   O(h+n) the height of tree(recursion) + the result
    24ms beats 100%
"""


class Solution(object):
    def __init__(self):
        self.minCol = 0
        self.maxCol = 0
        self.m = defaultdict(list)

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.dfs(root, 0, 0)
        res = []
        for i in range(self.minCol, self.maxCol+1):
            temp = self.m[i]
            temp = sorted(temp, key=lambda x: x[1])
            arr = [x[0] for x in temp]
            res.append(arr)
        return res

    def dfs(self, node, row, col):
        if node == None:
            return
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)
        self.m[col].append((node.val, row))
        self.dfs(node.left, row+1, col-1)
        self.dfs(node.right, row+1, col+1)


"""
    2nd approach: bfs + hashtable + sort
    - similar to lc987

    Time    O(NlogN)
    Space   O(h+n) the height of tree(recursion) + the result
    20ms beats 78.65%
"""


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ht = defaultdict(list)

        q = [(root, 0)]  # (node, col)
        while len(q) > 0:
            node, col = q.pop(0)
            ht[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        rawRes = []
        for c in ht:
            rawRes.append((c, ht[c]))

        res = []
        for c, arr in sorted(rawRes):
            res.append(arr)
        return res
