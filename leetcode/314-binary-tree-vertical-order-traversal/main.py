# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    2nd approach: bfs + hashtable + bucket sort
    - similar to lc987

    Time    O(NlogN)
    Space   O(H+N) the height of tree(recursion) + the result
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
        minCol, maxCol = 0, 0
        ht = defaultdict(list)  # {col: []}
        q = [(root, 0)]  # (node, col)
        while len(q) > 0:
            node, col = q.pop(0)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            ht[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        res = []
        for i in range(minCol, maxCol+1):
            if i in ht:
                res.append(ht[i])
        return res
