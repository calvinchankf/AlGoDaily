/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/*
    1st approach: dfs in recursion
    - for each node, compare the depths of left and right subtree
    - and compare and assign the result
    - in each node, just return the max depth of either left or right subtree 

    Time  O(n)
    Space O(h)
    60ms beats 85.65%
*/
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function (root) {
	let res = 0;

	const dfs = (node) => {
		if (node == null) {
			return 0;
		}
		const left = dfs(node.left);
		const right = dfs(node.right);
		const total = left + right;
		res = Math.max(res, total);
		return Math.max(left, right) + 1;
	};

	dfs(root);
	return res;
};
