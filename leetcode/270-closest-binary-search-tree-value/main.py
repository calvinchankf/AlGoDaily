# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st: do BST traversal twice
    - one for x <= target
    - one for x >= target

    Time    O(H)
    Space   O(1)
    44 ms, faster than 33.33% 
"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        a = self.smallerEqual(root, target)
        b = self.largerEqual(root, target)
        if abs(a - target) < abs(b - target):
            return a
        return b

    def smallerEqual(self, node, target):
        cur = node
        maxSmaller = -(2**32)
        while cur != None:
            if target < cur.val:
                maxSmaller = cur.val
                cur = cur.left
            elif target > cur.val:
                cur = cur.right
            else:
                return cur.val
        return maxSmaller

    def largerEqual(self, node, target):
        cur = node
        minLarger = 2**32
        while cur != None:
            if target < cur.val:
                cur = cur.left
            elif target > cur.val:
                minLarger = cur.val
                cur = cur.right
            else:
                return cur.val
        return minLarger


"""
    2nd: recursive BST search
	Time		O(H)
	Space	    O(H) recursion call stack
	beats 100%
	20jan2019
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.res = root.val
        self.helper(root, target)
        return self.res

    def helper(self, root, target):
        if root == None:
            return
        a = abs(root.val - target)
        b = abs(self.res - target)
        if a < b:
            self.res = root.val
        if target < root.val:
            self.helper(root.left, target)
        elif target > root.val:
            self.helper(root.right, target)


"""
    3rd approach: iterative BST search
    - set the root as intermediate result
    - bst traverse down to the nearest node and keep updating the result

    Time    O(H)
    Space   O(1)
    32 ms, faster than 81.41%
    24apr2019
"""


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = root.val
        cur = root
        while cur != None:
            if abs(cur.val - target) < abs(res - target):
                res = cur.val
            if target < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return res
