/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/*
    1st: recursion

    Time    O(N)
    Space   O(N)
    88 ms, faster than 95.59% 
*/
var postorder = function (root) {
	const res = [];
	const dfs = (node) => {
		if (node == null) {
			return;
		}
		for (let child of node.children) {
			dfs(child);
		}
		res.push(node.val);
	};
	dfs(root);
	return res;
};
