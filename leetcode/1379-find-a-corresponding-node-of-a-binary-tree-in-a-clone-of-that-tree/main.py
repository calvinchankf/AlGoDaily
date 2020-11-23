# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: BFS
    - I was asked 3 years ago by fb
    - leetcode did really bad on rephasing the question, 
        - supposedly the numbers should not be unique
        - its about subviews on web, n-ary tree

    Time    O(N)
    Space   O(N)
    684 ms, faster than 22.01%
"""


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = [cloned]
        while len(q) > 0:
            node = q.pop(0)
            if node.val == target.val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


"""
    2nd: recursive DFS
    - a decent way

    Time    O(N)
    Space   O(N)
    684 ms, faster than 22.01%
"""


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == None or original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        right = self.getTargetCopy(original.right, cloned.right, target)
        if left != None:
            return left
        return right


"""
    original: n-ary tree
    - it is what I was asked to do back then
    - here is a python version from JS

    class TreeNode:
    def __init__(self, x):
        self.val = x
        self.subviews = []
"""


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        res = None
        for i in range(len(original.children)):
            a = original.children[i]
            b = cloned.children[i]
            res = res or self.getTargetCopy(a, b, target)
        return res
