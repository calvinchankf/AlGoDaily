"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

"""
    1st approach: straight forward intuition
    - similar to lc114, 426, 430, 897
    - put the nodes in an array in ascending order
    - update the values of the nodes

    Time    O(2N)
    Space   O(N)
    32 ms, faster than 96.20%
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        nodes = []
        # inorder traversal of a BST is actually a sorted list

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)
        # dump node for referening
        dump = Node(0, None, nodes[0])
        # iterate the sorted list and update the left and right
        for i in range(len(nodes)):
            left = None
            right = None
            if i == 0:
                left = nodes[-1]
            else:
                left = nodes[i-1]
            if i+1 == len(nodes):
                right = nodes[0]
            else:
                right = nodes[i+1]
            nodes[i].left = left
            nodes[i].right = right

        return dump.right


"""
    2nd: recursive inorder
    - similar to lc114, 426, 430, 897
    - reassign the pointers during the inorder traversal process

    Time    O(N)
    Space   O(N)
    36 ms, faster than 56.19%
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        # declare a dumphead
        dumphead = Node(-1)
        self.prev = dumphead
        # do recursion to reassign the pointers
        self.inorder(root)
        # final work on the 1st and n-1the node
        head = dumphead.right
        head.left = self.prev  # first.left point to the last
        self.prev.right = head  # last.right point to the first
        return head

    def inorder(self, node):
        if node == None:
            return None
        self.inorder(node.left)

        # reassign the pointers
        # things are on the left, so the logic wont affect the future traversal on the right
        self.prev.right = node
        node.left = self.prev
        self.prev = node

        self.inorder(node.right)


"""
    3rd: iterative inorder
    - similar to lc114, 426, 430, 897
    - reassign the pointers during the inorder traversal process

    Time    O(N)
    Space   O(N)
    32 ms, faster than 94.92%
"""


class Solution(object):
    def treeToDoublyList(self, root):
        if root == None:
            return None
        dumphead = Node(-1)
        dumphead.right = root
        prev = dumphead
        cur = dumphead.right
        stack = []
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()

            prev.right = node
            node.left = prev
            prev = node

            cur = node.right

        prev.right = dumphead.right
        dumphead.right.left = prev

        return dumphead.right
