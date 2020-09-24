/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: preorder + inorder + postorder

    Time    O(3n)
    Space   O(n)
    92 ms, faster than 50.71%
*/
var boundaryOfBinaryTree = function (root) {
	if (root == null) {
		return [];
	}

	const leftBoundary = (node) => {
		if (node == null) {
			return;
		}
		if (node.left == null && node.right == null) {
			return;
		}
		res.push(node.val);
		if (node.left) {
			leftBoundary(node.left);
		} else {
			leftBoundary(node.right);
		}
	};
	const rightBoundary = (node) => {
		if (node == null) {
			return;
		}
		if (node.left == null && node.right == null) {
			return;
		}
		if (node.right) {
			rightBoundary(node.right);
		} else {
			rightBoundary(node.left);
		}
		res.push(node.val);
	};
	const leaves = (node) => {
		if (node == null) {
			return;
		}
		leaves(node.left);
		if (node !== root && node.left == null && node.right == null) {
			res.push(node.val);
		}
		leaves(node.right);
	};

	const res = [root.val];
	leftBoundary(root.left);
	leaves(root);
	rightBoundary(root.right);
	return res;
};
