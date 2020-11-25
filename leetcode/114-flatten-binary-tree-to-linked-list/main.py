# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
    1st approach: 
    - similar to lc114, 426, 430
    - store the nodes' values
    - add the values back to the linked list

    Time    O(2N)
    Space   O(N)
    28 ms, faster than 71.08%
"""


class Solution(object):
    def flatten(self, root):
        arr = []

        def preOrder(node):
            if node == None:
                return
            arr.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        cur = root
        for i in range(len(arr)):
            x = arr[i]
            cur.val = x
            cur.left = None
            if i+1 < len(arr):
                cur.right = TreeNode(-1)
            cur = cur.right


"""
    2nd approach: recursion
    - similar to lc114, 426, 430
    - store the nodes' values
    - add the values back to the linked list

    Time    O(N)
    Space   O(N)
    36 ms, faster than 73.33%
"""


class Solution:
    def flatten(self, root: TreeNode) -> None:
        dumphead = TreeNode(root)
        self.prev = dumphead
        self.preorder(root)
        return dumphead.right

    def preorder(self, node):
        if not node:
            return
        left = node.left
        right = node.right
        self.prev.left = None
        self.prev.right = node
        self.prev = node
        self.preorder(left)
        self.preorder(right)


"""
    3rd approach: stack
    - similar to lc114, 426, 430
    - store the nodes' values
    - add the values back to the linked list

    Time    O(N)
    Space   O(N)
    32 ms, faster than 20.53%
"""


class Solution(object):
    def flatten(self, root):
        if not root:
            return None
        dumphead = TreeNode()
        prev = dumphead
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            prev.left = None
            prev.right = node
            prev = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return dumphead.right
