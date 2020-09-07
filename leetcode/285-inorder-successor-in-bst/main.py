# leetcode doesn't support go for this question, i did it in python first

import sys
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    3rd: decent recursive approach:

    Time    O(logn)
    Space   O(h)
    64 ms, faster than 85.19% 
    21feb2019
"""


class Solution(object):
    def inorderSuccessor(self, root, p):
        if root == None:
            return None
        if p.val < root.val:
            """
            the below line equals to
            ------
            while node.left != None:
                node = node.left
            """
            left = self.inorderSuccessor(root.left, p)
            if left != None:
                return left
            return root
        else:
            return self.inorderSuccessor(root.right, p)


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# try to search every number
ans = Solution().inorderSuccessor(a, e)
print("ans=", ans)
if ans != None:
    print("ans.val=", ans.val)

"""
    3rd: very similar to upper bound binary search BUT
    - here is BSTsearch, only record the sucessor when we go left
    - then the sucessor is either your parent OR your left most leaf in right subtree

    see ./idea.jpeg

    Time    O(logn)
    Space   O(h)
    68 ms, faster than 61.86%
    24apr2019
"""


class Solution(object):
    def inorderSuccessor(self, root, p):
        res = None
        cur = root
        while cur != None:
            if p.val < cur.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# try to search every number
ans = Solution().inorderSuccessor(a, e)
print("ans=", ans)
if ans != None:
    print("ans.val=", ans.val)

"""
    followup: inorder predecessor

    very similar to lower bound binary search BUT
    - exclude the lower bound
    - here is BSTsearch, only record the sucessor when we go right
    - then the sucessor is either your parent OR your right most leaf in left subtree
"""


class Solution(object):

    def inorderPredecessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        pred = None
        while node != None:
            if p.val <= node.val:
                node = node.left
            else:
                pred = node
                node = node.right
        return pred
