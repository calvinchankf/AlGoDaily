/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    Recursive dfs inorder

    Time    O(n)
    Space   O(h)
*/
var inorderTraversal = function (root) {
	const res = [];
	const inorder = (node) => {
		if (node == null) {
			return;
		}
		inorder(node.left);
		res.push(node.val);
		inorder(node.right);
	};
	inorder(root);
	return res;
};
