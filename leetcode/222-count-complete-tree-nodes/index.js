/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    2nd approach
	- actually we dont need to go though all the nodes
	- we can just search for the node which the left and right have different heights
        - if no diff, the subtree has 2^n-1 nodes
        - if has diff, go into its children and count the number of nodes again

    Time    O(logn * logn) because it is almost balenced
    Space   O(h)
    108 ms, faster than 81.40%
*/
var countNodes = function (root) {
	if (root == null) {
		return 0;
	}
	const left = countLeftMost(root.left) + 1;
	const right = countRightMost(root.right) + 1;
	if (left == right) {
		return 2 ** left - 1;
	}
	return countNodes(root.left) + countNodes(root.right) + 1;
};

const countLeftMost = (node) => {
	if (node == null) {
		return 0;
	}
	let count = 0;
	let cur = node;
	while (cur != null) {
		count += 1;
		cur = cur.left;
	}
	return count;
};

const countRightMost = (node) => {
	if (node == null) {
		return 0;
	}
	let count = 0;
	let cur = node;
	while (cur != null) {
		count += 1;
		cur = cur.right;
	}
	return count;
};
