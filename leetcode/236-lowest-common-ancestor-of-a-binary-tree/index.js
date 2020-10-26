/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    2nd: recursion

    Time    O(N)
    Space   O(N)
    88 ms, faster than 91.45%
*/
var lowestCommonAncestor = function (root, p, q) {
	if (!root) {
		return null;
	}
	return dfs(root, p, q);
};

const dfs = (node, p, q) => {
	if (node == null || node == p || node == q) {
		return node;
	}
	let left = dfs(node.left, p, q);
	let right = dfs(node.right, p, q);
	if (left != null && right != null) {
		return node;
	}
	if (left != null) {
		return left;
	}
	if (right != null) {
		return right;
	}
	return null;
};
