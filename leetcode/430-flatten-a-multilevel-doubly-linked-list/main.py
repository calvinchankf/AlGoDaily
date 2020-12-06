"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


"""
    1st approach: recursion but dont create new nodes
    - similar to lc114, 426, 430, 897
    - get all the nodes. if a node has child, go into the child linked list
    - construct the linked list with the nodes in order

    Time    O(2n)
    Space   O(n)
    1148 ms, faster than 82.96%
"""


class Solution(object):
    def flatten(self, head):
        if head == None:
            return None
        dumphead = Node()
        self.prev = dumphead
        self.preorder(head)
        dumphead.next.prev = None
        return dumphead.next

    def preorder(self, node):
        if node == None:
            return

        nodeNext = node.next

        node.prev = self.prev
        self.prev.child = None
        # due to this change, we need nodeNext, or we keep traversing the node over**2 again
        self.prev.next = node
        self.prev = node

        self.preorder(node.child)
        self.preorder(nodeNext)
