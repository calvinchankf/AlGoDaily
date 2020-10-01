# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: recursion

    pre     = [1,2,4,5,3,6,7]
    post    = [4,5,2,6,7,3,1]

    pre     = [1,2,4,5,3,6,7]
               ^ *     |
    post    = [4,5,2,6,7,3,1]
                   *     | ^

    * is the left subtree root
    we can get how many numbers in the left subtree by searching it in postorder
    then separate | the left subtree and right subtree


    Time    O(N^2)
    Space   O(N)
    64 ms, faster than 30.12%
"""


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        val = pre[0]
        root = TreeNode(val)
        if len(pre) == 1:
            return root
        i = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:i+1], post[:i])
        root.right = self.constructFromPrePost(pre[i+1:], post[i:-1])
        return root
