from collections import Counter

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: iterative dfs

    Time    O(N)
    Space   O(N^2)
    1084 ms, faster than 100.00%
"""


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        stack = [(root, [])]
        while len(stack) > 0:
            node, arr = stack.pop()
            arr2 = arr + [node.val]
            if node.left == None and node.right == None:
                if self.isPalindromic(arr2):
                    res += 1
            if node.left != None:
                stack.append((node.left, arr2))
            if node.right != None:
                stack.append((node.right, arr2))
        return res

    def isPalindromic(self, s):
        counter = Counter(s)
        seenOdd = False
        for key in counter:
            if counter[key] % 2 == 1:
                if seenOdd:
                    return False
                seenOdd = True
        return True


"""
    1st: recursive dfs

    Time    O(N)
    Space   O(N^2)
    1076 ms, faster than 100.00%
"""


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, [])
        return self.res

    def dfs(self, node, arr):
        if node == None:
            return
        arr2 = arr + [node.val]
        if node.left == None and node.right == None:
            if self.isPalindromic(arr2):
                self.res += 1
        self.dfs(node.left, arr2)
        self.dfs(node.right, arr2)

    def isPalindromic(self, s):
        counter = Counter(s)
        seenOdd = False
        for key in counter:
            if counter[key] % 2 == 1:
                if seenOdd:
                    return False
                seenOdd = True
        return True
