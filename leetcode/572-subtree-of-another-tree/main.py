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
    64 ms, faster than 95.22%
    2may2019
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

        sStr = self.serialize(s)
        tStr = self.serialize(t)
        if tStr in sStr:
            return True
        return False

    # it converts a tree to e.g. (1(2(3)())4()())
    def serialize(self, node):
        if node == None:
            return '()'
        left = self.serialize(node.left)
        right = self.serialize(node.right)
        return '('+str(node.val) + left + right + ')'

    # followup: deserialize
    # there might be negative numbers, and the numbers can be > 9(multiple digits)
    def deserialize(self, s):
        if len(s) == 0:
            return None
        arr = []
        # execpt the open and end parentheses
        for i in range(1, len(s)-1):
            arr.append(s[i])
        return self.deserializeHelper(arr)

    def deserializeHelper(self, arr):
        if len(arr) == 0:
            return None

        # negative
        isNegative = False
        if arr[0] == "-":
            arr.pop(0)
            isNegative = True

        # multiple digits
        num = ""
        node = None
        while len(arr) > 0 and arr[0] != "(" and arr[0] != ")":
            num += arr.pop(0)

        # put negative
        if isNegative:
            if len(num) != 0:
                node = TreeNode(-int(num))
        else:
            if len(num) != 0:
                node = TreeNode(int(num))

        # left child
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.left = self.deserializeHelper(arr)

        # right child
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.right = self.deserializeHelper(arr)

        # end this scope
        if len(arr) > 0 and arr[0] == ")":
            arr.pop(0)
        return node

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
