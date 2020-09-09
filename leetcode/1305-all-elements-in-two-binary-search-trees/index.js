/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: inorder traversal + merge 2 lists

    Time    O(M+N)
    Space   O(M+N)
    184 ms, faster than 92.02%
*/
var getAllElements = function (root1, root2) {
	const A = getList(root1);
	const B = getList(root2);
	let i = 0;
	let j = 0;
	let res = [];
	while (i < A.length && j < B.length) {
		if (A[i] < B[j]) {
			res.push(A[i]);
			i += 1;
		} else {
			res.push(B[j]);
			j += 1;
		}
	}
	if (i < A.length) {
		res = res.concat(A.slice(i));
	}
	if (j < B.length) {
		res = res.concat(B.slice(j));
	}
	return res;
};

const getList = (root) => {
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
