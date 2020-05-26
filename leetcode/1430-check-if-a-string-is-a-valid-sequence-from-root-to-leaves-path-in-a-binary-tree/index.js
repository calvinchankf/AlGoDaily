/*
    1st: DFS

    Time    O(N) at most
    Space   O(logN -> N) height of the tree
    88 ms, faster than 100.00%
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[]} arr
 * @return {boolean}
 */
var isValidSequence = function (root, arr) {
	const y = `,${arr.join(",")}`;
	return dfs(root, "", y);
};

const dfs = (node, x, y) => {
	if (node == null) {
		return false;
	}
	const _x = `${x},${node.val}`;
	if (node.left == null && node.right == null) {
		return _x == y;
	}
	return dfs(node.left, _x, y) || dfs(node.right, _x, y);
};
