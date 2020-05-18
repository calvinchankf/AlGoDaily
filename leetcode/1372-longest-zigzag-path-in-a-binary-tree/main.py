"""
    1st: recursion
    - keep track of the zigzag path(left, right) along the way when we traverse the tree
    - update our global resuslt if necessary

    Time    O(N)
    Space   O(N+H)
    548 ms, faster than 24.62%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, '')
        return self.res

    def dfs(self, node: TreeNode, path: str):
        if node == None:
            return
        if len(path) > self.res:
            self.res = len(path)

        if len(path) > 0 and path[-1] == 'l':
            self.dfs(node.left, 'l')
        else:
            self.dfs(node.left, path + 'l')

        if len(path) > 0 and path[-1] == 'r':
            self.dfs(node.right, 'r')
        else:
            self.dfs(node.right, path + 'r')


"""
    2nd: stack
    - keep track of the zigzag path(left, right) along the way when we traverse the tree
    - update our global resuslt if necessary

    Time    O(N)
    Space   O(N+H)
    516 ms, faster than 27.48%
"""


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, '')]
        while len(stack) > 0:
            node, path = stack.pop()
            if node == None:
                continue
            if len(path) > res:
                res = len(path)

            if len(path) > 0 and path[-1] == 'l':
                stack.append((node.left, 'l'))
            else:
                stack.append((node.left, path + 'l'))

            if len(path) > 0 and path[-1] == 'r':
                stack.append((node.right, 'r'))
            else:
                stack.append((node.right, path + 'r'))
        return res
