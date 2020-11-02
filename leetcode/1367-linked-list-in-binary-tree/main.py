# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: DFS
    - get all the paths
    - see if each path has substring of linked list

    Time    O(L+T)
    Space   O(L+T)
    92 ms, faster than 92.28%
"""


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        ll = ''
        cur = head
        while cur != None:
            ll += str(cur.val) + ','
            cur = cur.next

        self.arr = []
        self.dfs(root, '')

        for s in self.arr:
            if ll in s:
                return True
        return False

    def dfs(self, node, s):
        if node == None:
            return
        s += str(node.val) + ','
        if node.left == None and node.right == None:
            self.arr.append(s)
        if node.left != None:
            self.dfs(node.left, s)
        if node.right != None:
            self.dfs(node.right, s)


"""
    1st: brute force DFS
    - not a very readable way...

    ref:
    - https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N)-Time

    Time    O(T^2)
    Space   O(T height)
    232 ms, faster than 7.41%
"""


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(head, root):
            if head == None:
                return True
            if root == None:
                return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))

        if head == None:
            return True
        if root == None:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
