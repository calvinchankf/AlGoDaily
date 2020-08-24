from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    Classic recursion problem
    - related lc96

    ref:
    - https://www.youtube.com/watch?v=hQn61BjdA7M

    56 ms, faster than 89.45%

    Time    O(Catalan Number)
    Space   O(Catalan Number)
    56 ms, faster than 89.45%
"""


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, s, e):
        res = []
        if s > e:
            res.append(None)
            return res
        for i in range(s, e+1):
            left = self.dfs(s, i-1)
            right = self.dfs(i+1, e)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res
