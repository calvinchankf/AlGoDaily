class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: brute force checking
    - for each node, check it equals to target tree

    Time    O(n^2)
    Space   O(h)
    232ms beats 54.85%
    24jan2019
"""


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False

        if s.val == t.val:
            if self.isIdentical(s, t) == True:
                return True

        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return left or right

    def isIdentical(self, a, b):
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        mid = a.val == b.val
        left = self.isIdentical(a.left, b.left)
        right = self.isIdentical(a.right, b.right)
        return mid and left and right


"""
    2nd approach:
    - serialize both trees
    - check if the 2nd serialized representation is within the 1st serialized representation

    corner case: [12] and [2]
    - so we have to wrap the whole tree within a pair of parentheses

    Time    O(S+T)
    Space   O(h)
    68 ms, faster than 96.06%
"""


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        sStr = self.serialize(s)
        tStr = self.serialize(t)
        if tStr in sStr:
            return True
        return False

    def serialize(self, node):
        if node == None:
            return '()'
        left = self.serialize(node.left)
        right = self.serialize(node.right)
        return '('+str(node.val) + left + right + ')'

# helpers


def printTree(node):
    if node == None:
        return
    printTree(node.left)
    print(node.val)
    printTree(node.right)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
s = Solution().serialize(a)
print(s)
ds = Solution().deserialize(s)
printTree(ds)
