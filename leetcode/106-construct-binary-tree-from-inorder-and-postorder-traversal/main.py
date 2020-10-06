# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: recursion
    - similar to lc105
    - but this time the root of every subtree is the tail of postorder

    e.g.
    post    [9,10,15,7,20,3]
    in      [9,10,3,15,20,7]

    post    [9,10,15,7,20,3]
                          ^
    in      [9,10,3,15,20,7]
                  ^
    - the root of every subtree appears last in postorder
    - inorder:
        - the left hand side of 3 [9,10] must be the left subtree of 3
        - the right hand side of 3 [15,20,7] must be the right subtree of 3
    - prorder:
        - since len(postorder) == len(inorder), [9, 10] should be the postorder in the left subtree
        - so, [15,7,20] should be the reorder in the right subtree
    - so we can build the tree by recursion
    

    Time    O(N^2)
    Space   O(N)
    192 ms, faster than 41.97%
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(postorder, inorder)

    def dfs(self, postorder, inorder):
        if len(postorder) == 0:
            return None
        head = postorder[-1]
        root = TreeNode(head)
        mid = inorder.index(head)
        root.left = self.dfs(postorder[:mid], inorder[:mid])
        root.right = self.dfs(postorder[mid:-1], inorder[mid+1:])
        return root


"""
    2nd: recursion + hashtable
    - same logic as 1st
    - but use a hashtable to record the index of every node
    - so we pass indices in recursion
    - since the head in every recursion must be the root, we can dequeue it in each recursion

    *** be careful: build the right subtree first ***
    - since we pop the postorder from the end, the sequence of postorder is L->R->P, we should handle R before we handle L

    e.g. 
    post    [9,10,15,7,20,3]
    in      [9,10,3,15,20,7]

    post    [9,10,15,7,20,3]
                          ^
    in      [9,10,3,15,20,7]
                  ^
    
    after the first split, look at postorder, the segments should be
    
    ---L-- ----R---
    [9,10 | 15,7,20]
                  ^
                in the next recursion, we will pop this, and this value is the root of right subtree, 
                so thats why we need to build the right subtree first

    Time    O(N)
    Space   O(N)
    92 ms, faster than 68.84%
"""


class Solution(object):
    def buildTree(self, inorder, postorder):
        n = len(inorder)
        ht = {}
        for i in range(n):
            ht[inorder[i]] = i
        return self.dfs(postorder, inorder, ht, 0, n-1)

    def dfs(self, postorder, inorder, ht, iLeft, iRight):
        if iLeft > iRight:
            return None
        head = postorder.pop()
        root = TreeNode(head)
        mid = ht[head]
        root.right = self.dfs(postorder, inorder, ht, mid+1, iRight)  # ***
        root.left = self.dfs(postorder, inorder, ht, iLeft, mid-1)
        return root
