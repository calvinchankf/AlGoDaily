/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val === undefined ? 0 : val;
 *    this.children = children === undefined ? [] : children;
 * };
 */

/*
    1st: recursion
    - lc543, lc414, lc1522

    Time    O(N)
    Space   O(H)
    84 ms, faster than 100.00%
*/
const diameter = (root) => {
	let res = 0;

	const dfs = (node) => {
		if (node == null) {
			return 0;
		}
		let largest = 0;
		let secondLargest = 0;
		for (let child of node.children) {
			let depth = dfs(child);
			if (depth > largest) {
				secondLargest = largest;
				largest = depth;
			} else if (depth > secondLargest) {
				secondLargest = depth;
			}
		}
		let total = largest + secondLargest;
		res = Math.max(res, total);
		return largest + 1;
	};
	dfs(root);

	return res;
};
