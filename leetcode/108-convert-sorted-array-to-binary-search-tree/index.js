/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
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
    84 ms, faster than 76.81%
*/
var sortedArrayToBST = function (nums) {
	if (nums.length == 0) {
		return null;
	}
	const mid = Math.floor(nums.length / 2);
	const node = new TreeNode(nums[mid]);
	node.left = sortedArrayToBST(nums.slice(0, mid));
	node.right = sortedArrayToBST(nums.slice(mid + 1));
	return node;
};
