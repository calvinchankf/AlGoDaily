# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        
        c = str(t.val)
        if len(left) == 0 and len(right) == 0:
            return c
        
        l = ''
        if len(left) > 0:
            l = '(' + left + ')'
        else:
            l = '()'
        
        r = ''
        if len(right) > 0:
            r = '(' + right + ')'
        
        return c + l + r