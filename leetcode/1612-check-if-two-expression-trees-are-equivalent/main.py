from collections import Counter
# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    1st: recursive traversal + hashtable

    Time    O(A+B)
    Space   O(A+B)
    608 ms, faster than 100.00%
"""
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        ht1 = self.getNodeValsCount(root1)
        ht2 = self.getNodeValsCount(root2)
        for k in ht1:
            if k not in ht2 or ht2[k] != ht1[k]:
                return False
        for k in ht2:
            if k not in ht1 or ht1[k] != ht2[k]:
                return False
        return True
    
    def getNodeValsCount(self, root):
        ht = Counter()
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            ht[node.val] += 1
            inorder(node.right)
        inorder(root)
        return ht

"""
    2nd: iterative traversal + hashtable

    Time    O(A+B)
    Space   O(A+B)
    624 ms, faster than 100.00%
"""
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        ht1 = self.getNodeValsCount(root1)
        ht2 = self.getNodeValsCount(root2)
        for k in ht1:
            if k not in ht2 or ht2[k] != ht1[k]:
                return False
        for k in ht2:
            if k not in ht1 or ht1[k] != ht2[k]:
                return False
        return True
    
    def getNodeValsCount(self, root):
        ht = Counter()
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            ht[node.val] += 1
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return ht