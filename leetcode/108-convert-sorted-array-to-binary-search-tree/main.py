# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    recursion:
    0. to create a balence tree, u must sort the array first
    1. sort the array
    2. build the tree recursively in the way of binary search
"""


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nums = sorted(nums)
        return self.buildBST(nums, 0, len(nums)-1)

    def buildBST(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = self.buildBST(nums, left, mid - 1)
        node.right = self.buildBST(nums, mid + 1, right)
        return node


"""
    recursion: using slice, but keep in mind that slicing takes O(n)
    0. to create a balence tree, u must sort the array first
    1. sort the array
    2. build the tree recursively in the way of binary search

    1st approach: divide and conquer
	- the mid of a sorted array is the parent of a sub tree
	1, 2, 3, 4, 5, 6, 7
			 4
		2			6
	1	  3		5		7

	Time	O(n)
	Space	O(n)
"""


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildBST(nums)

    def buildBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildBST(nums[:mid])
        node.right = self.buildBST(nums[mid+1:])
        return node
