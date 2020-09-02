/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/*
    2nd approach: inorder + suffix sum

    Time    O(n)
    Space   O(h)
    68 ms, faster than 93.57%
*/
var bstToGst = function (root) {
	const ht = {};
	const arr = [];
	let pfs = 0;
	const inorder = (node) => {
		if (node == null) {
			return;
		}
		inorder(node.left);
		arr.push(node.val);
		inorder(node.right);
	};
	inorder(root);

	let sfs = 0;
	for (let i = arr.length - 1; i >= 0; i--) {
		sfs += arr[i];
		ht[arr[i]] = sfs;
	}

	const q = [root];
	while (q.length > 0) {
		const node = q.shift();
		node.val = ht[node.val];
		if (node.left) {
			q.push(node.left);
		}
		if (node.right) {
			q.push(node.right);
		}
	}
	return root;
};
