# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: recursive depth first search

    Time    O(N)
    Space   O(N)
    56 ms, faster than 67.57%
"""


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node: TreeNode, count: int):
        if node == None:
            return
        if count == 1:
            self.res.append(node.val)
        newCount = 0
        newCount += 1 if node.left != None else 0
        newCount += 1 if node.right != None else 0
        self.dfs(node.left, newCount)
        self.dfs(node.right, newCount)


"""
    2nd: iterative depth first search

    Time    O(N)
    Space   O(N)
    60 ms, faster than 44.26%
"""


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = []
        stack = [(root, 0)]
        while len(stack) > 0:
            node, count = stack.pop()
            if count == 1:
                res.append(node.val)
            newCount = 0
            newCount += 1 if node.left != None else 0
            newCount += 1 if node.right != None else 0
            if node.left:
                stack.append((node.left, newCount))
            if node.right:
                stack.append((node.right, newCount))
        return res


"""
    3rd iterative breath first search

    Time    O(N)
    Space   O(N)
    60 ms, faster than 44.26%
"""


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        res = []
        queue = [(root, 0)]
        while len(queue) > 0:
            node, count = queue.pop(0)
            if count == 1:
                res.append(node.val)
            newCount = 0
            newCount += 1 if node.left != None else 0
            newCount += 1 if node.right != None else 0
            if node.left:
                queue.append((node.left, newCount))
            if node.right:
                queue.append((node.right, newCount))
        return res
