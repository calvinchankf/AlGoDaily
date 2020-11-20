# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: bfs + lowest common ancestor
    - bfs to record the nodes with maxDepth
    - find the LCA of the leftmost leaf and the rightmost leaf

    Time    O(2N)
    Space   O(N)
    36 ms, faster than 59.33%
"""


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        maxDepth = 0
        maxDepthNodes = []
        q = [(root, 0)]
        while len(q) > 0:
            node, d = q.pop(0)

            if d > maxDepth:
                maxDepth = d
                maxDepthNodes = [node]
            elif d == maxDepth:
                maxDepthNodes.append(node)

            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))

        if len(maxDepthNodes) == 1:
            return maxDepthNodes[0]
        return self.lca(root, maxDepthNodes[0], maxDepthNodes[-1])

    def lca(self, node, a, b):
        if node == None or node == a or node == b:
            return node
        left = self.lca(node.left, a, b)
        right = self.lca(node.right, a, b)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right


"""
    2nd approach: recursion
    - if the depth of left child == depth of right child, it means that current node is the result
    - if the depth of left < depth of right, the node return from the right is the result
    - if the depth of left > depth of right, the node return from the left is the result
    
    Time    O(n)
    Space   O(n)
    16 ms, faster than 95.53%
"""


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root)[1]

    def dfs(self, node):
        if node == None:
            return 0, None
        left_depth, left_res = self.dfs(node.left)
        right_depth, right_res = self.dfs(node.right)
        if left_depth == right_depth:
            return left_depth+1, node
        elif left_depth < right_depth:
            return right_depth+1, right_res
        else:
            return left_depth+1, left_res
