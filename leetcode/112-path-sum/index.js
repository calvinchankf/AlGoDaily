/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/*
    1st: dfs
    Time    O(N)
    Spae    O(h) h: height of the tree
    80 ms, faster than 85.12%
*/
var hasPathSum = function (root, sum) {
	let res = 0;
	const dfs = (node, total) => {
		if (node == null) {
			return;
		}
		const newTotal = total + node.val;
		if (node.left == null && node.right == null && newTotal == sum) {
			res += 1;
		}
		dfs(node.left, newTotal);
		dfs(node.right, newTotal);
	};
	dfs(root, 0);
	return res > 0;
};
