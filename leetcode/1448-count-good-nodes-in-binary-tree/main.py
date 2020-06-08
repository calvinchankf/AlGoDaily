# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: recursive DFS
    - retain a maximum value along the way when we do DFS

    Time    O(N)
    Space   O(H) the height the of tree
    392 ms, faster than 33.33%
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, -sys.maxsize)
        return self.res

    def dfs(self, node, maxVal):
        if node == None:
            return
        maxVal_ = max(maxVal, node.val)
        if node.val == maxVal_:
            self.res += 1
        self.dfs(node.left, maxVal_)
        self.dfs(node.right, maxVal_)


"""
    2nd: iterative DFS
    - retain a maximum value along the way when we do DFS

    Time    O(N)
    Space   O(H) the height the of tree
    392 ms, faster than 33.33%
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, -sys.maxsize)]
        while len(stack) > 0:
            node, maxVal = stack.pop()
            maxVal_ = max(maxVal, node.val)
            if node.val == maxVal_:
                res += 1
            if node.left != None:
                stack.append((node.left, maxVal_))
            if node.right != None:
                stack.append((node.right, maxVal_))
        return res
