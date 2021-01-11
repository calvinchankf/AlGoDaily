# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: inorder traversal + merge 2 lists

    Time    O(M+N)
    Space   O(M+N)
    388 ms, faster than 39.18%
"""


class Solution(object):
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        A = self.getSortedList(root1)
        B = self.getSortedList(root2)
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        if i < len(A):
            res += A[i:]
        if j < len(B):
            res += B[j:]
        return res

    def getSortedList(self, root):
        res = []

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res


"""
    2nd: ONE PASS iterative inorder traversal + merge 2 lists

    Time    O(M+N)
    Space   O(M+N)
    456 ms, faster than 23.77%
"""


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        cur1, cur2 = root1, root2
        res = []
        while cur1 or cur2 or len(stack1) > 0 or len(stack2) > 0:
            while cur1 != None:
                stack1.append(cur1)
                cur1 = cur1.left
            while cur2 != None:
                stack2.append(cur2)
                cur2 = cur2.left

            if len(stack2) == 0 or (len(stack1) > 0 and stack1[-1].val < stack2[-1].val):
                node = stack1.pop()
                res.append(node.val)
                cur1 = node.right
            else:
                node = stack2.pop()
                res.append(node.val)
                cur2 = node.right
        return res
