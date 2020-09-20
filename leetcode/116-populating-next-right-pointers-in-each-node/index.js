/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/*
    1st approach: bfs

    Time    O(n)
    Space   O(2w)
    92 ms, faster than 92.86%
*/
var connect = function (root) {
	if (root === null) {
		return null;
	}
	const q = [root];
	while (q.length > 0) {
		const n = q.length;
		const row = [];
		for (let i = 0; i < n; i++) {
			const node = q.shift();
			row.push(node);
			if (node.left) {
				q.push(node.left);
			}
			if (node.right) {
				q.push(node.right);
			}
		}
		for (let i = 0; i < row.length - 1; i++) {
			row[i].next = row[i + 1];
		}
	}
	return root;
};
