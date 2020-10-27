/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    2nd approach: recursive dfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 99.45%
*/
var isSymmetric = function (root) {
	return check(root, root);
};

const check = (node1, node2) => {
	if (node1 === null && node2 === null) {
		return true;
	}
	if (node1 === null || node2 === null) {
		return false;
	}
	if (node1.val !== node2.val) {
		return false;
	}
	const a = check(node1.left, node2.right);
	const b = check(node1.right, node2.left);
	return a && b;
};

/*
    2nd approach: recursive dfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 99.45%
*/
var isSymmetric = function(root) {
    return check(root, root)
};

const check = (node1, node2) => {
    if (node1 == null && node2 == null) {
        return true
    }
    if (node1 == null || node2 == null) {
        return false
    }
    if (node1.val != node2.val) {
        return false
    }
    if (check(node1.left, node2.right) === false) {
        return false
    }
    if (check(node1.right, node2.left) === false) {
        return false
    }
    return true
}