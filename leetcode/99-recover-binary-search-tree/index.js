/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: inorder+sort
	- actually the inorder traversal of a BST is suppoed to be a sorted list of a valid
	1. so we can just get the inorder list
	2. clone the list and sort it, then compare with the inorder list we get from the inroder traversal to get that 2 nodes
	3. traverse again the tree, coorect that 2 nodes

	Time	O(nlogn+2n)
	Space	O(n)
	160 ms, faster than 85.25%
*/
var recoverTree = function (root) {
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

	const sNums = [...nums].sort((a, b) => a - b);
	let a = null;
	let b = null;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] !== sNums[i]) {
			a = nums[i];
			b = sNums[i];
			break;
		}
	}

	const mutate = (node) => {
		if (node === null) {
			return;
		}
		if (node.val == a) {
			node.val = b;
		} else if (node.val == b) {
			node.val = a;
		}
		mutate(node.left);
		mutate(node.right);
	};
	mutate(root);
};
