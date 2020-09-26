import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursion
    - in every recursion, return (count, minVal, maxVal)
    - in every parent recursion, check if the leftMax < currentNode < rightMin
    - if yes, update the result if the subtree size is larger

    Time    O(N)
    Space   O(H)
    36 ms, faster than 87.32%
"""


class Solution(object):
    def largestBSTSubtree(self, root):
        if root == None:
            return 0
        self.maxCount = 0
        self.dfs(root)
        return self.maxCount

    def dfs(self, node):
        if node == None:
            return (0, sys.maxsize, -sys.maxsize)

        leftCount, leftMin, leftMax = self.dfs(node.left)
        rightCount, rightMin, rightMax = self.dfs(node.right)

        if leftCount == -1:
            return (-1, sys.maxsize, -sys.maxsize)
        if rightCount == -1:
            return (-1, sys.maxsize, -sys.maxsize)

        count = 1 + leftCount + rightCount
        if leftMax < node.val < rightMin:
            if count > self.maxCount:
                self.maxCount = count
        else:
            count = -1

        if leftMin == sys.maxsize:
            leftMin = node.val
        if rightMax == -sys.maxsize:
            rightMax = node.val

        return (count, leftMin, rightMax)
