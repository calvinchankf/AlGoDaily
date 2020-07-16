# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

"""
    1st: recursive dfs + hashtable
    - put every node in a hashtable
    - when we clone a tree, use the nodes from hashtable

    Time    O(N)
    Space   O(N)
    276 ms, faster than 100.00%
"""


class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        self.ht = {}
        self.buildPool(root)
        return self.cloneTree(root)

    def buildPool(self, node):
        if node == None:
            return
        newNode = NodeCopy(node.val)
        self.ht[node] = newNode
        self.buildPool(node.left)
        self.buildPool(node.right)

    def cloneTree(self, node):
        if node == None:
            return None
        newNode = self.ht[node]
        if node.random != None:
            newNode.random = self.ht[node.random]
        newNode.left = self.cloneTree(node.left)
        newNode.right = self.cloneTree(node.right)
        return newNode
