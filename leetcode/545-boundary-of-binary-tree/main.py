# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: preorder + inorder + postorder

    Time    O(3N)
    Space   O(N)
    36 ms, faster than 96.63%
"""


class Solution(object):

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                return
            boundary.append(node.val)
            if node.left:
                preorder(node.left)
            else:
                preorder(node.right)

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            if node != root and node.left == None and node.right == None:
                boundary.append(node.val)
            inorder(node.right)

        def postorder(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                return
            if node.right:
                postorder(node.right)
            else:
                postorder(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        preorder(root.left)
        inorder(root)
        postorder(root.right)
        return boundary


"""
    2nd: suboptimal but the way easier to explain in interviews

    Time    O(4N)
    Space   O(N)
    36 ms, faster than 99.00%
"""


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        if not root.left and not root.right:
            return [root.val]
        leftBoundary = []

        def getLeft(node):
            if node == None:
                return
            if not node.left and not node.right:
                return
            leftBoundary.append(node.val)
            if node.left:
                getLeft(node.left)
            else:
                getLeft(node.right)
        getLeft(root.left)

        rightBoundary = []

        def getRight(node):
            if node == None:
                return
            if not node.left and not node.right:
                return
            rightBoundary.append(node.val)
            if node.right:
                getRight(node.right)
            else:
                getRight(node.left)
        getRight(root.right)
        rightBoundary.reverse()

        leaves = []

        def getLeaves(node):
            if node == None:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            getLeaves(node.left)
            getLeaves(node.right)
        getLeaves(root)

        return [root.val] + leftBoundary + leaves + rightBoundary


"""
    3rd: iterative, queue + stack

    Time    O(3N)
    Space   O(N)
    44 ms, faster than 22.85%
"""


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        leftBoundary = []
        q = []
        if root.left:
            q.append(root.left)
        while len(q) > 0:
            node = q.pop(0)
            if not node.left and not node.right:
                continue
            leftBoundary.append(node.val)
            if node.left:
                q.append(node.left)
            elif node.right:
                q.append(node.right)

        rightBoundary = []
        q = []
        if root.right:
            q.append(root.right)
        while len(q) > 0:
            node = q.pop(0)
            if not node.left and not node.right:
                continue
            rightBoundary.append(node.val)
            if node.right:
                q.append(node.right)
            elif node.left:
                q.append(node.left)

        leaves = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return [root.val] + leftBoundary + leaves + rightBoundary[::-1]
