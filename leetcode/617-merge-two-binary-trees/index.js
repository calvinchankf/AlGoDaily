/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: dfs, return the input nodes

    Time    O(N)
    Space   O(N)
    104 ms, faster than 94.15%
*/
var mergeTrees = function (t1, t2) {
	return buildTree(t1, t2);
};

const buildTree = (node1, node2) => {
	if (node1 === null && node2 === null) {
		return null;
	} else if (node1 == null) {
		return node2;
	} else if (node2 == null) {
		return node1;
	}
	const node = new TreeNode(node1.val + node2.val);
	node.left = buildTree(node1.left, node2.left);
	node.right = buildTree(node1.right, node2.right);
	return node;
};

/*
    2nd: dfs, return new nodes

    Time    O(N)
    Space   O(N)
    104 ms, faster than 94.15%
*/
var mergeTrees = function (t1, t2) {
	return buildTree(t1, t2);
};

const buildTree = (node1, node2) => {
	if (node1 === null && node2 === null) {
		return null;
	}
	let a = 0;
	let b = 0;
	if (node1) {
		a = node1.val;
	}
	if (node2) {
		b = node2.val;
	}
	const node = new TreeNode(a + b);
	node.left = buildTree(node1 ? node1.left : null, node2 ? node2.left : null);
	node.right = buildTree(
		node1 ? node1.right : null,
		node2 ? node2.right : null
	);
	return node;
};
