# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: tree recursive dfs + kadan along each route

    on each node, 

    the max value should be amongst
    - current node val
    - left branch sum + current node val
    - right branch sum + current node val
    - left branch sum + current node val + right branch sum

    since we only count branches' sum but not the total nodes' sum from each sub tree
    , we should just return the max amongst
    - current node val
    - left branch sum + current node val
    - right branch sum + current node val

    Time    O(n)
    Space   O(h)
    92 ms, faster than 47.52%
"""


class Solution(object):

    def __init__(self):
        self.res = -sys.maxsize

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        mid = node.val
        midLeft = left + mid
        midRight = mid + right
        midLeftRight = left + mid + right

        # kadan's algorithm
        self.res = max(self.res, mid, midLeft, midRight, midLeftRight)

        return max(mid, midLeft, midRight)
