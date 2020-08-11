// This is an input class. Do not edit.
class BST {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

/*
    - similar to lc98
    - BUT here the range of a node value: left < node.value <= right
*/

function validateBst(tree) {
	// Write your code here.
	return dfs(tree, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
}

const dfs = (node, left, right) => {
	if (node == null) {
		return true;
	}
	if (node.value < left || node.value >= right) {
		return false;
	}
	return (
		dfs(node.left, left, node.value) && dfs(node.right, node.value, right)
	);
};

// Do not edit the line below.
exports.BST = BST;
exports.validateBst = validateBst;
