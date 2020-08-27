/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    Time    O(N)
    Space   O(H) H: height
    112 ms, faster than 30.93%
*/
var lowestCommonAncestor = function (root, p, q) {
	if (root == null || root == p || root == q) {
		return root;
	}
	const left = lowestCommonAncestor(root.left, p, q);
	const right = lowestCommonAncestor(root.right, p, q);
	if (left !== null && right !== null) {
		return root;
	}
	if (left !== null) {
		return left;
	}
	return right;
};

/*
1nd approach: iterative bst dfs

    idea: common anestor of 2 nodes must inclusively lies between left and right
    left <= anestor <= right
    e.g. 3 < 4 < 5

    Time    O(logn)
    Time    O(logn) height of the bst
    68 ms, faster than 99.7%
*/
var lowestCommonAncestor = function (root, p, q) {
	let cur = root;
	while (cur !== null) {
		if (cur.val > p.val && cur.val > q.val) {
			cur = cur.left;
		} else if (cur.val < p.val && cur.val < q.val) {
			cur = cur.right;
		} else {
			return cur;
		}
	}
	return cur;
};

/*
    2nd approach: recursive bst dfs

    idea: common anestor of 2 nodes must inclusively lies between left and right
    left <= anestor <= right
    e.g. 3 < 4 < 5

    Time    O(logn)
    Time    O(logn) height of the bst
    96 ms, faster than 66.37%
*/
var lowestCommonAncestor = function (root, p, q) {
	if (root == null || root == p || root == q) {
		return root;
	}

	if (root.val > p.val && root.val > q.val) {
		return lowestCommonAncestor(root.left, p, q);
	} else if (root.val < p.val && root.val < q.val) {
		return lowestCommonAncestor(root.right, p, q);
	}
	return root;
};
