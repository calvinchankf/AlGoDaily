/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: iterative BST traversal
    - if the node doesnt exist, create one

    Time    O(logN)
    Space   O(1)
    104 ms, faster than 63.72%
*/
var insertIntoBST = function (root, val) {
	if (root == null) {
		return new TreeNode(val);
	}
	let cur = root;
	while (cur != null) {
		if (val < cur.val) {
			if (cur.left == null) {
				cur.left = new TreeNode(val);
				break;
			} else {
				cur = cur.left;
			}
		} else if (val > cur.val) {
			if (cur.right == null) {
				cur.right = new TreeNode(val);
				break;
			} else {
				cur = cur.right;
			}
		}
	}
	return root;
};
