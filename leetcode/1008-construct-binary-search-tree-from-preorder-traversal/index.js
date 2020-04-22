/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    1st: recursion
    - reuse lc701: Insert into a Binary Search Tree
    - for each element in the array
    - do lc701

    Time    from O(N) to O(NlogN), because the number of nodes of result tree < N during the construction of it
    Space   O(N)
    60 ms, faster than 56.65% 
*/

/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function (preorder) {
	let root = null;
	for (let x of preorder) {
		root = buildTree(root, x);
	}
	return root;
};

const buildTree = (node, val) => {
	if (node == null) {
		return new TreeNode(val);
	}
	if (val < node.val) {
		node.left = buildTree(node.left, val);
	} else {
		node.right = buildTree(node.right, val);
	}
	return node;
};

/*
    2nd: same concept but with iteration
    - reuse lc701: Insert into a Binary Search Tree
    - for each element in the array
    - do lc701

    Time    from O(N) to O(NlogN), because the number of nodes of result tree < N during the construction of it
    Space   O(N)
    52 ms, faster than 91.91%
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function (preorder) {
	let root = null;
	for (let x of preorder) {
		root = buildTree(root, x);
	}
	return root;
};

const buildTree = (node, val) => {
	if (node == null) {
		return new TreeNode(val);
	}
	let cur = node;
	while (cur != null) {
		if (val < cur.val) {
			if (cur.left == null) {
				cur.left = new TreeNode(val);
				break;
			} else {
				cur = cur.left;
			}
		} else {
			if (cur.right == null) {
				cur.right = new TreeNode(val);
				break;
			} else {
				cur = cur.right;
			}
		}
	}
	return node;
};
