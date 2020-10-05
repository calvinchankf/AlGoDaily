/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/*
    1st: recursion

    Time    O(N)
    Space   O(N)
    92 ms, faster than 83.72%
*/
var preorder = function (root) {
	const res = [];
	const dfs = (node) => {
		if (node == null) {
			return;
		}
		res.push(node.val);
		for (let child of node.children) {
			dfs(child);
		}
	};
	dfs(root);
	return res;
};
