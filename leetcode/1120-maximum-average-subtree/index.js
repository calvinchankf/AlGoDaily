/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: recursion

    Time    O(n)
    Space   O(h)
    76 ms, faster than 94.55%
*/
var maximumAverageSubtree = function (root) {
	let res = 0;

	const f = (node) => {
		if (node === null) {
			return [0, 0];
		}
		const [leftSum, leftCount] = f(node.left);
		const [rightSum, rightCount] = f(node.right);
		const total = leftSum + node.val + rightSum;
		const count = leftCount + 1 + rightCount;
		const avg = total / count;
		res = Math.max(res, avg);
		return [total, count];
	};
	f(root);

	return res;
};
