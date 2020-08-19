/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: inorder + build BST
    - convert the tree to a sorted array using an in-order traversal
    - construct a new balanced tree from the sorted array recursively

    Time    O(2N)
    Space   O(N)
    180 ms, faster than 63.46%
*/
var balanceBST = function (root) {
	const nums = [];
	const inorder = (node) => {
		if (node == null) {
			return;
		}
		inorder(node.left);
		nums.push(node.val);
		inorder(node.right);
	};
	inorder(root);

	return sortedArrayToBST(nums);
};

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
