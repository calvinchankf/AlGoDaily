from sortedcontainers import SortedDict

"""
    2nd: BST
    - build a BST
    - return the max depth
    - it seems like creating a node takes so long, this approach results in LTE
"""


class Solution:
    def maxDepthBST(self, nums: List[int]) -> int:
        root = None
        res = 0
        for x in nums:
            root, d = self.insertIntoBST(root, x)
            res = max(res, d)
        return res + 1

    def insertIntoBST(self, root, val):
        if root == None:
            return (TreeNode(val), 0)
        L, R = 0, 0
        if val < root.val:
            root.left, L = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right, R = self.insertIntoBST(root.right, val)
        return root, max(L, R) + 1


"""
    1st: treemap / sortedDict
    - learned from others

    ref:
    - https://leetcode.com/problems/depth-of-bst-given-insertion-order/discuss/1280067/Interval-Array

    Time    O(NlogN) -> O(N^2)
    Space   O(N)
    8048 ms, faster than 100.00%
"""


class Solution(object):
    def maxDepthBST(self, order):
        depths = SortedDict()
        depths[0] = 0
        depths[10**5+1] = 0
        for x in order:
            i = depths.bisect_left(x)
            vals = depths.values()
            left = vals[i-1]
            right = vals[i]
            depths[x] = max(left, right) + 1
        return max(depths.values())
