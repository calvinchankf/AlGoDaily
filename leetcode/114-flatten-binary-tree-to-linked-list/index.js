/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/*
    1st approach: 
    - store the nodes' values
    - add the values back to the linked list

    Time    O(2n)
    Space   O(n)
    84 ms, faster than 66.78%
*/
var flatten = function (root) {
	if (root == null) {
		return;
	}

	const arr = [];
	const preorder = (node) => {
		if (node == null) {
			return;
		}
		arr.push(node);
		preorder(node.left);
		preorder(node.right);
	};
	preorder(root);

	let prev = root;
	for (let i = 1; i < arr.length; i++) {
		const x = arr[i];
		prev.left = null;
		prev.right = x;
		prev = x;
	}
	prev.left = null;
	prev.right;
};
