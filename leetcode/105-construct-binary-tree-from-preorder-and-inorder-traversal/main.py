"""
    1st: recursion

    e.g.
    pre = [3,9,10,20,15,7]
    ino = [9,10,3,15,20,7]

    pre = [3,9,10,20,15,7]
           ^
    ino =[9,10,3,15,20,7]
              ^
    - the root of every subtree appears first in preorder
    - inorder:
        - the left hand side of 3 [9,10] must be the left subtree of 3
        - the right hand side of 3 [15,20,7] must be the right subtree of 3
    - prorder:
        - since len(preorder) == len(inorder), [9, 10] should be the preorder in the left subtree
        - so, [20,15,7] should be the reorder in the right subtree
    - so we can build the tree by recursion
    

    Time    O(N^2)
    Space   O(N)
    192 ms, faster than 41.97%
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.dfs(preorder, inorder)

    def dfs(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        head = preorder[0]
        root = TreeNode(head)
        mid = inorder.index(head)
        root.left = self.dfs(preorder[1:mid+1], inorder[:mid])
        root.right = self.dfs(preorder[mid+1:], inorder[mid+1:])
        return root


"""
    2nd: recursion + hashtable
    - same logic as 1st
    - but use a hashtable to record the index of every node
    - so we pass indices in recursion
    - since the head in every recursion must be the root, we can dequeue it in each recursion

    Time    O(N)
    Space   O(N)
    92 ms, faster than 68.84%
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        ht = {}
        for i in range(n):
            ht[inorder[i]] = i
        return self.dfs(preorder, inorder, ht, 0, n-1)

    def dfs(self, preorder, inorder, ht, iLeft, iRight):
        if iLeft > iRight:
            return None
        head = preorder.pop(0)
        root = TreeNode(head)
        mid = ht[head]
        root.left = self.dfs(preorder, inorder, ht, iLeft, mid-1)
        root.right = self.dfs(preorder, inorder, ht, mid+1, iRight)
        return root
