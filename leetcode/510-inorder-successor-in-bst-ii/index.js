/**
 * // Definition for a Node.
 * function Node(val) {
 *    this.val = val;
 *    this.left = null;
 *    this.right = null;
 *    this.parent = null;
 * };
 */

/*
    1st: bst traversal
    1. find the root
    2. lc285

    Time    (N + logN)
    Space   O(1)
    92 ms, faster than 61.54%
*/
var inorderSuccessor = function (node) {
	let root = null;
	let cur = node;
	while (cur !== null) {
		root = cur;
		cur = cur.parent;
	}

	let target = node.val;
	let successor = null;
	cur = root;
	while (cur !== null) {
		if (target < cur.val) {
			successor = cur;
			cur = cur.left;
		} else {
			cur = cur.right;
		}
	}
	return successor;
};
